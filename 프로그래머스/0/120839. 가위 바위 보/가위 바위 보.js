function solution(rsp) {
    let answer = '';
    for(let i=0; i<rsp.length; i++){
        answer += calculator(rsp[i]);
    }
    return answer;
}

const calculator = (str) => {
    if (str === "2") {
        return "0";
    }
    if (str === "0") {
        return "5";
    }
    if (str === "5") {
        return "2";
    }
}