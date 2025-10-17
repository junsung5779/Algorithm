function solution(my_string) {
    const answer = [];
    let tmpStr = '';
    for(let i=0; i<my_string.length; i++) {
        // 공백이 아니면
        if (my_string[i] !== " ") {
            // 임시문자열에 추가
            tmpStr += my_string[i];
        }
        // 공백이면
        if (my_string[i] === " ") {
            // 임시 문자열이 없다면 계속 진행
            if (tmpStr.length === 0) {
                continue;
            } else {
                // 임시 문자열이 있다면 answer에 추가
                answer.push(tmpStr);
                tmpStr = '';
            }
        }
        // 마지막 문자열까지 순회했을 때 임사 문자열이 있다면 answer에 추가
        if (i === my_string.length-1 && tmpStr.length !== 0) {
            answer.push(tmpStr);
        }
    }
    return answer;
}