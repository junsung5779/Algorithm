function solution(box, n) {
    let answer = 0;
    // 가로, 세로, 높이 별로 최대 몇 개 들어갈 수 있는지 계산해서 전부 다 곱하기.
    const row = Math.floor(box[0]/n);
    const col = Math.floor(box[1]/n);
    const height = Math.floor(box[2]/n);
    answer = row * col * height;
    return answer;
}