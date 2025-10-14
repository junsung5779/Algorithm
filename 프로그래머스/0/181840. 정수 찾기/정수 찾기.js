function solution(num_list, n) {
    let answer = 0;
    for (const i of num_list) {
        if (i===n) {
            return 1;
        }
    }
    return answer;
}