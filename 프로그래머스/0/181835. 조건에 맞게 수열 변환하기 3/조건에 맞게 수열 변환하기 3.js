function solution(arr, k) {
    const answer = arr.map((element, index)=> {
        if (k % 2 === 0) {
            return element+k;
        } else {
            return element*k;
        }
    })
    return answer;
}