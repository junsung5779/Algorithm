function solution(myString, pat) {
    const answer = [0];
    
    for (let i=0; i<myString.length; i++) {
        if(myString[i] === pat[0]){
            for (let j=0; j<pat.length; j++) {
                if (myString[i+j] === pat[j]) {
                    if (j === pat.length-1) {
                        answer[0] += 1;
                    }
                } else {
                    break;
                }
            }
        }
    }
    return answer[0];
}