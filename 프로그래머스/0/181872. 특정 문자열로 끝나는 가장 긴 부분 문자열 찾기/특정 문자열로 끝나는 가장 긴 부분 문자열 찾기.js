function solution(myString, pat) {
    const answer = [];
    for(let i=myString.length-1; i>=0; i--) {
        if (myString[i] === pat[0]) {
            for (let j=0; j<pat.length; j++) {
                if (myString[i+j] === pat[j]) {
                    if(j === pat.length-1) {
                        for(let k=0; k<=i+j; k++) {
                            answer.push(myString[k]);
                        }
                        return answer.join("");
                    } else {
                        continue;
                    }
                }
            }
        }
    }
    return answer;
}