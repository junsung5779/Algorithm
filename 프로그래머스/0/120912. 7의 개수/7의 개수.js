function solution(array) {
    let answer = 0;
    for(const num of array) {
       for (const i of String(num)) {
           if (i === "7") {
               answer += 1;
           }
       }
    }
    return answer;
}