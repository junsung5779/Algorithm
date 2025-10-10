function solution(my_string) {
    let answer = 0;
    for (const i of my_string) {
        if (!isNaN(Number(i))) {
            answer += Number(i);
        }
    }
    return answer;
}