function solution(n) {
    let answer = 0;
    for(const number of String(n)){
        answer += Number(number)
    }
    return answer;
}