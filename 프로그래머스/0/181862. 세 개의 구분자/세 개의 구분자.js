function solution(myStr) {
    const answer = [];
    let tmpStr = ''
    for (let i=0; i<myStr.length; i++) {
        if(myStr[i] === 'a' || myStr[i] === 'b' || myStr[i] === 'c') {
            if (tmpStr.length > 0) {
                answer.push(tmpStr);
                tmpStr = '';
            }
        } else {
            tmpStr += myStr[i];
        }
        if(i === myStr.length-1 && tmpStr.length > 0) {
            answer.push(tmpStr);
        }
    }
    if (answer.length === 0) {
        return ['EMPTY'];
    }
    return answer;
}