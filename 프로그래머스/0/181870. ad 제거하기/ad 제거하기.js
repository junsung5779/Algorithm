function solution(strArr) {
    const answer = [];
    for (const str of strArr) {
        if (str.length === 1) {
            answer.push(str);
        } else {
            for (let i=0; i<str.length-1; i++) {
                if (str[i]+str[i+1] === "ad") {
                    break;
                }
                if (i === str.length-2) {
                    answer.push(str);
                }
            }
        }
        
    }
    return answer;
}