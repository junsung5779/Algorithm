function solution(myString, pat) {
    if (myString.length < pat.length) {
        return 0;
    }
    
    const myLowerString = myString.split("").map((a)=> {
        return a.toLowerCase();
    }).join("");
    
    const lowerPat = pat.toLowerCase();
    
    for (let i=0; i<myLowerString.length-lowerPat.length+1; i++) {
        for (j=0; j<lowerPat.length; j++) {
            if(myLowerString[i+j] !== lowerPat[j]) {
                break;
            }
            if(j === lowerPat.length-1) {
                return 1;
            }
        }
    }
    
    
    return 0;
}