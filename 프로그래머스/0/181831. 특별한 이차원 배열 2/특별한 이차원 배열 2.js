function solution(arr) {
    const answer = 1;
    for(let i=0; i<Math.ceil(arr.length/2); i++) {
        for(let j=0; j<arr[i].length; j++) {
            if (arr[i][j] === arr[j][i]) {
                continue;
            } else {
                return 0;
            }
        }
    }
    return answer;
}