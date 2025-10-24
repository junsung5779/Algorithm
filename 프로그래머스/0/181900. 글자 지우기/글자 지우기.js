function solution(my_string, indices) {
    const arr = [];
    const answer = [];

    const sorted_indices = indices.sort((a,b)=> {
        return a-b;
    });

    for(let i=my_string.length-1; i>=0; i--) {
        if(i === sorted_indices[sorted_indices.length-1]) {
            sorted_indices.pop()
        } else {
            arr.push(my_string[i]);
        }
    }
    
    for(let j=arr.length-1; j>=0; j--) {
        answer.push(arr[j]);
    }
    return answer.join("");
}