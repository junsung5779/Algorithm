function solution(money) {
    let answer = [];
    const americanoPrice = 5500;
    answer.push(Math.floor(money/americanoPrice));
    answer.push(money%americanoPrice);
    return answer;
}