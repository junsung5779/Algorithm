function solution(x1, x2, x3, x4) {
    const answer = [];
    if (x1 === true || x2 === true) {
        answer.push(true);
    } else {
        answer.push(false);
    }
    
    if (x3 === true || x4 === true) {
        answer.push(true);
    } else {
        answer.push(false);
    }
    
    if (answer[0] === false || answer[1] === false) {
        return false;
    }
    return true;
}