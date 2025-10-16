function solution(myString) {
    const answer = [];
    let tmpNum = 0;
    for (let i=0; i<myString.length; i++){
        if(myString[i]==="x") {
            answer.push(tmpNum);
            tmpNum=0;
        } else{
            tmpNum += 1;
        }
        if(i === myString.length-1) {
            answer.push(tmpNum);
        }
    }
    return answer;
}