function solution(arr) {
    const answer = [];
    const seArr = [];
    for (let i=0; i<arr.length; i++) {
        if(arr[i] === 2) {
            seArr.push(i);
            break;
        }
    }
    
    for (let j=arr.length-1; j>=0; j--) {
        if(arr[j] === 2) {
            seArr.push(j)
            break;
        }
    }
    
    for (let k=seArr[0]; k<=seArr[1]; k++) {
        answer.push(arr[k]);
    }
    return answer.length === 0 ? [-1] : answer;
}