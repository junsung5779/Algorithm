function solution(my_string, m, c) {
    const answer = [];
    for (let i=0; i<my_string.length; i+=m) {
        for(j=i; j<i+m; j++) {
            if(j%m === c-1) {
                answer.push(my_string[j]);
            }
        }
        
    }
    return answer.join("");
}