function solution(arr, n) {
    let answer = [];
    if (arr.length%2 === 1) {
        answer = arr.map((e,i)=>{
            if(i%2===0) {
                return e+n;
            } else {
                return e;
            }
        })
    } else {
        answer = arr.map((e,i)=>{
             if(i%2===1) {
                return e+n;
            } else {
                return e;
            }
        })
    }
    return answer;
}