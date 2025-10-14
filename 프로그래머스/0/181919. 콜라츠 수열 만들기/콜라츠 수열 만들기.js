function solution(n) {
    const answer = [];
    let number = n;
    while(number !== 1) {
        answer.push(number);
        if(number % 2 === 0) {
            number = number/2;
        } else {
            number = number*3 + 1;
        }
    }
    answer.push(1);
    return answer;
}