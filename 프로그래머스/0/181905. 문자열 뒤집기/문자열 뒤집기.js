function solution(my_string, s, e) {
    const answer = [];
    for (let i=0; i<s; i++) {
        answer.push(my_string[i]);
    }
    
    for (let j=e; j>=s; j--) {
        answer.push(my_string[j]);
    }
    
    for (let k=e+1; k<my_string.length; k++) {
        answer.push(my_string[k])
    }
    
    return answer.join("");
}