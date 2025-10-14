function solution(num, k) {
    let answer = -1;
    for (let i=0; i<String(num).length; i++) {
        if (String(num)[i] === String(k)) {
            answer = i+1;
            break;
        }
    }
    return answer;
}