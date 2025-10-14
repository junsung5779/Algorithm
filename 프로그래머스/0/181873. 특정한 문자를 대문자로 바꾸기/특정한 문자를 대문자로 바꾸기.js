function solution(my_string, alp) {
    const answer = [];
    for (let i=0; i<my_string.length; i++) {
        if(my_string[i] === alp) {
            answer.push(String.fromCharCode(alp.charCodeAt()-32));
        } else {
            answer.push(my_string[i]);
        }
    }
    return answer.join("");
}