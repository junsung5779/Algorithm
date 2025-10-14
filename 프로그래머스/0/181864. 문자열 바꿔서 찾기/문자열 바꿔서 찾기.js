function solution(myString, pat) {
    let answer = 0;
    if (myString.length < pat.length) {
        return 0;
    }
    const reversed_pat = reverse(pat);
    for (let i=0; i<myString.length - reversed_pat.length + 1; i++) {
        for (let j=0; j<reversed_pat.length; j++) {
            if(myString[i+j] === reversed_pat[j]) {
                if(j===reversed_pat.length-1) {
                    answer = 1;
                } 
            } else {
                break;
            }
        }
    }
   
    return answer;
}

const reverse = (pat) => {
    let reversed_pat = '';
     for (const i of pat) {
        if(i === "A") {
            reversed_pat += "B";
        } else {
            reversed_pat += "A";
        }
    }
    return reversed_pat;
}