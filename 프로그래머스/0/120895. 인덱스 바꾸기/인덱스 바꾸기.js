function solution(my_string, num1, num2) {
    const answer = [];
    for(let i=0; i<my_string.length; i++) {
        if (i===num1) {
            answer.push(my_string[num2]);
        } else if (i===num2) {
            answer.push(my_string[num1]);
        } else {
            answer.push(my_string[i])
        }
    }
    return answer.join('');
}