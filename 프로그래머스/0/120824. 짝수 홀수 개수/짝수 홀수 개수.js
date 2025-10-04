function solution(num_list) {
    let answer = [0,0];
    for(const i of num_list) {
        if (i%2 === 0) {
            answer[0] += 1;
        } else {
            answer[1] += 1;
        }
    }
    return answer;
}