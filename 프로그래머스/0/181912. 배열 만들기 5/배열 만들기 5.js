function solution(intStrs, k, s, l) {
    const answer = [];
    for(const str of intStrs) {
        const tmpStr = [];
        for (let i=s; i<s+l; i++) {
            tmpStr.push(str[i]);
        }
        if(Number(tmpStr.join("")) > k) {
            answer.push(Number(tmpStr.join("")));
        }   
    }
    return answer;
}