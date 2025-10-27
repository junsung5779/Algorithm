function solution(strArr) {
    const answer = [];
    let max = 0;
    for(let i=0; i<30; i++) {
        answer.push(0)
    }
    
    for (const str of strArr) {
        answer[str.length-1] += 1;
    }
    
    for (const num of answer) {
        if(num > max) {
            max = num;
        }
    }
    return max;
}