function solution(strArr) {
    const answer = [];
    for (let i=0; i<strArr.length; i++) {
        const tmpArr = [];
        for (let j=0; j<strArr[i].length; j++) {
            // 홀수번째 인덱스의 모든 문자를 대문자로
            if(i%2 === 1) {
                if (isUpperCase(strArr[i][j])) {
                    tmpArr.push(strArr[i][j]);
                } else {
                    tmpArr.push(makeUpperCase(strArr[i][j]));
                }
            } else {
                // 짝수번째 인덱스의 모든 문자를 소문자로
                if (isUpperCase(strArr[i][j])) {
                    tmpArr.push(makeLowerCase(strArr[i][j]));
                } else {
                    tmpArr.push(strArr[i][j]);
                }
            }
        }
        answer.push(tmpArr.join(""))
    }
    return answer;
}

const isUpperCase = (str) => {
    if (str.charCodeAt() >= 65 && str.charCodeAt() <= 90) {
        return true;
    } else {
        return false;
    }
}

const makeUpperCase = (str) => {
    return String.fromCharCode(str.charCodeAt()-32);
}

const makeLowerCase = (str) => {
    return String.fromCharCode(str.charCodeAt()+32);
}