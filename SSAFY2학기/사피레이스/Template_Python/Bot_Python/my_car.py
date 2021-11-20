from DrivingInterface.drive_controller import DrivingController
import math

class DrivingClient(DrivingController):
    def __init__(self):
        # ============================================     =============== #
        #  Area for member variables =============================== #
        # =========================================================== #
        # Editing area starts from here
        #

        self.is_debug = False

        # api or keyboard
        self.enable_api_control = True # True(Controlled by code) /False(Controlled by keyboard)
        super().set_enable_api_control(self.enable_api_control)

        #
        # Editing area ends
        # ==========================================================#
        super().__init__()

    def control_driving(self, car_controls, info):

        # =========================================================== #
        # Area for writing code about driving rule ================= #
        # =========================================================== #
        # Editing area starts from here
        
        # TODO: 계속 조작해야 하는 값.
        angle_num = int(info.speed / 45)
        # track_forward_angles : 전방에 있는 도로의 커브 값. 도로와 평행한 정도이며 20개의 값이 주어짐
        # 잔디를 달릴 때에는 패널티로 인해 45키로 이하로 주행하므로 항상 angle_num의 값이 가장 가까운 트랙 앵글로 정해진다.
        ref_angle = info.track_forward_angles[angle_num]

        steering = (ref_angle - info.moving_angle)
        throttle_factor = 0.6 / (abs(ref_angle) + 0.1)
        if throttle_factor > 0.11: throttle_factor = 0.11

        half_val = self.half_road_limit
        print(half_val)

        steer_factor = info.speed * 1.5
        if info.speed > 70: steer_factor = info.speed * 0.85
        if info.speed > 100: steer_factor = info.speed * 0.7

        steering += (steer_factor + 0.001)

        middle_add = (info.to_middle / 80) * -1
        steering += middle_add

        way_points = []
        y = math.sqrt(math.pow(info.distance_to_way_points[0],2)-math.pow(info.to_middle,2))
        way_points.append({'x':0, 'y':y})
        for i in range(9):
            x = way_points[i]['x'] + (10 * math.sin(math.radians(info.track_forward_angles[i])))
            x = way_points[i]['y'] + (10 * math.cos(math.radians(info.track_forward_angles[i])))
            way_points.append({'x':x, 'y':y})

        ## 전방에 있는 몇 번재 좌표를 이동 목표로 정할 것인가?
        ref_idx = max(1, min(9, int(info.speed / 25)))
        target_x = way_points[ref_idx]['x']
        target_y = way_points[ref_idx]['y']

        # tmp target_y
        if target_y == 0:
            target_y = 0.1
            # target_x = 0.5

        steering = (math.atan((target_x - info.to_middle) / target_y) - math.radians(info.moving_angle)) * 0.4

        # 장애물 회피를 위한 아이디어 1
        forward_obstacles = []
        ## 장애물 리스트 처리
        for obstacle in info.track_forward_obstacles:
            ## 0m ~ (자동차 속도 x 0.5)m 사이의 장애물만 고려
            if obstacle['dist'] > 0 and obstacle['dist'] < (info.speed*0.5) and abs(obstacle['to_middle']) <= (self.half_load_width + 1.0):
                forward_obstacles.append(obstacle)

        if len(forward_obstacles) > 0:
            ref_idx = max(1, min(9, int(int(forward_obstacles[0]['dist'] / 10))))
            target_x = way_points[ref_idx]['x'] + (forward_obstacles[0]['to_middle']-2)
            target_y = forward_obstacles[0]['dist']

            steering = (math.atan((target_x - info.to_middle) / target_y) - math.radians(info.moving_angle)) * 0.8

        # 충돌 후 극복을 위한 아이디어
        accident_step = 0
        recovery_count = 0
        accident_count = 0

        ## 1. 10km/h 이상의 속도로 달리는 경우 정상적인 상황으로 간주
        if info.speed > 10:
            accident_step = 0
            recovery_count = 0
            accident_count = 0

        ## 2. 레이싱 시작 후 Speed 1km/h 이하가 된 경우 상황 체크
        if info.lap_progress > 0.5 and accident_step == 0 and abs(info.speed) < 1.0:
            accident_count += 1

        ## 3. Speed 1km/h 이하인 상태가 지속된 경우 충돌로 인해 멈춘 것으로 간주
        if accident_count > 8:
            accident_step = 1

        ## 4. 충돌로 멈춘 경우 후진 시작
        if accident_step == 1:
            recovery_count += 1
            steering *= -1
            throttle = -1
            brake = 0

        ## 5. 어느 정도 후진이 되었을 때 정지
        if recovery_count > 12:
            accident_step = 2
            recovery_count = 0
            accident_count = 0

        ## 6. 충돌을 회피 했다고 간주 후 정상 주행 상태로 돌림
        if accident_step == 2:
            steeing = 0.0
            throttle = 1
            brake = 1
            if info.speed > -1:
                accident_step = 0
                throttle = 1
                brake = 0

        ## 기본 throttle, brake
        throttle = 1
        brake = 0

        ## 일단 170km/h로 속도 제한
        if info.speed > 170: throttle = 0; brake = 0.5

        ## 거의 직선 주로라고 판단된다면 Full Throttle
        sum_fwd_angles = sum(info.track_forward_angles)
        checking_angle = abs(sum_fwd_angles)

        if checking_angle <= 100: throttle = 1; brake = 0

        ## 급격한 커브인지 판단
        sharp_curve = False
        for fwd_angle in info.track_forward_angles:
            if fwd_angle >= 80: sharp_curve = True

        if info.speed > 140:
            if checking_angle > 300: throttle -= 0.2; brake = 0.2
            if checking_angle > 500: throttle -= 0.2; steering *= 1.2; brake += 0.1
            if checking_angle > 600: throttle -= 0.3; steering *= 1.2; brake += 0.2
            if checking_angle > 700: throttle -= 0.4; steering *= 1.2; brake += 0.3
            if checking_angle > 900: throttle = -1.0; steering *= 1.2; brake = 1.0

        ## 급격한커브인 경우 급정거
        if sharp_curve:
            if info.speed > 160:
                throttle = -1; brake = 1

        if self.is_debug:
            print("=========================================================")
            print("[MyCar] to middle: {}".format(info.to_middle))

            print("[MyCar] collided: {}".format(info.collided))
            print("[MyCar] car speed: {} km/h".format(info.speed))

            print("[MyCar] is moving forward: {}".format(info.moving_forward))
            print("[MyCar] moving angle: {}".format(info.moving_angle))
            print("[MyCar] lap_progress: {}".format(info.lap_progress))

            print("[MyCar] track_forward_angles: {}".format(info.track_forward_angles))
            print("[MyCar] track_forward_obstacles: {}".format(info.track_forward_obstacles))
            print("[MyCar] opponent_cars_info: {}".format(info.opponent_cars_info))
            print("[MyCar] distance_to_way_points: {}".format(info.distance_to_way_points))
            print("=========================================================")

        ###########################################################################

        # Moving straight forward
        car_controls.steering = steering
        car_controls.throttle = throttle
        car_controls.brake = brake

        if self.is_debug:
            print("[MyCar] steering:{}, throttle:{}, brake:{}"\
                  .format(car_controls.steering, car_controls.throttle, car_controls.brake))

        #
        # Editing area ends
        # ==========================================================#
        return car_controls


    # ============================
    # If you have NOT changed the <settings.json> file
    # ===> player_name = ""
    #
    # If you changed the <settings.json> file
    # ===> player_name = "My car name" (specified in the json file)  ex) Car1
    # ============================
    def set_player_name(self):
        player_name = "Car1"
        return player_name


if __name__ == '__main__':
    print("[MyCar] Start Bot! (PYTHON)")

    client = DrivingClient()
    return_code = client.run()
    print("[MyCar] End Bot! (PYTHON)")

    exit(return_code)
