function solution(num_list, n) {
    const answer = [];
    for (let i=0; i<num_list.length; i+=n) {
        const arr = [];
        for (let j=0; j<n; j++) {
            arr.push(num_list[i+j]);
        }
        answer.push([...arr]);
    }
    return answer;
}