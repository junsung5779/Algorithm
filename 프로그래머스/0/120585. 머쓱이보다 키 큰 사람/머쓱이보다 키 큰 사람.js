function solution(array, height) {
    let answer = 0;
    for (const person of array) {
        if (person > height) {
            answer += 1;
        }
    }
    return answer;
}