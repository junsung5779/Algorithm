function solution(numbers, n) {
    let answer = 0;
    for(const num of numbers) {
        if (answer + num > n) {
            return answer + num;
        } else {
            answer += num;
        }
    }
    return answer;
}