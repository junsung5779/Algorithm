function solution(s1, s2) {
    let answer = 0;
    for(const i of s2){
        for(const j of s1){
            if (i === j) {
                answer += 1;
                break;
            }
        }
    }
    return answer;
}