function solution(order) {
    let answer = 0;
    for(const num of String(order)) {
        if(num%3 === 0 && num>0) {
            answer += 1;
        }
    }
    return answer;
}