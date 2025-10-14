function solution(myString) {
    const answer = [];
    for (const i of myString) {
        if (i<"l") {
            answer.push("l");
        } else {
            answer.push(i);
        }
    }
    return answer.join("");
}