function solution(n, numlist) {
    let answer = [];
    for(const number of numlist) {
        if(number % n === 0) {
            answer.push(number);
        }
    }
    return answer;
}