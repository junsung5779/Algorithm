function solution(age) {
    const answer = [];
    for (const i of String(age)) {
        answer.push(String.fromCharCode(i.charCodeAt()+49));
    }
    return answer.join("");
}