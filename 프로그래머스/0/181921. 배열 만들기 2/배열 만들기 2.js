function solution(start, end) {
    let answer = [];
    for (let i=start; i<=end; i++) {
        let isTarget = true; 
        for(const j of String(i)){
            if(j !== "0" && j !== "5") {
                isTarget = false;
            }
        }
        if(isTarget) {
            answer.push(i);
        }
    }
    return answer.length > 1 ? answer : [-1];
}