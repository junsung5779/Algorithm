function solution(my_string) {
    const answer = [];
    for(const str of my_string) {
        if(answer.length === 0) {
            answer.push(str);
        }
        for (let i=0; i<answer.length; i++) {
            if(str === answer[i]) {
                break;
            }
            if(i === answer.length-1) {
                answer.push(str);
            }
        }
    }
    return answer.join("");
}