function solution(str_list, ex) {
    let answer = '';
    for (const i of str_list) {
        // 문자열 ex가 i에 포함되면 다음 i진행
        if (isIn(i,ex)) {
            continue;
        } else {
            // 문자열 ex가 i에 포함되지 않으면 정답에 추가
            answer += i;
        }
        
        
    }
    return answer;
}

const isIn = (str, ex) => {
    for (let i=0; i<str.length; i++) {
        for (let j=0; j<ex.length; j++) {
            if (str[i+j] === ex[j]) {
                if(j === ex.length-1) {
                    return true;
                }
                continue;
            } else {
                break;
            }
        }
    }
}