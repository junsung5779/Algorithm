function solution(arr, intervals) {
    const answer = [];
    for (const range of intervals) {
        for(let i=range[0]; i<=range[1]; i++) {
            answer.push(arr[i]);
        }
    }
    return answer;
}