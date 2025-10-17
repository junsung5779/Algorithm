function solution(rny_string) {
    let answer = '';
    for(const str of rny_string) {
        if (str === "m"){
            answer += "rn"
        } else {
            answer += str;
        }
    }
    return answer;
}