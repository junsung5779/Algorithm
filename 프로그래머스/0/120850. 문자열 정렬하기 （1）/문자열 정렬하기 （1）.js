function solution(my_string) {
    let answer = [];
    for(const i of my_string) {
        if(!isNaN(Number(i))) {
            answer.push(Number(i))
        }
    }
    answer = quickSort(answer)
    return answer;
}

const quickSort = (array) => {
    if(array.length <= 1) {
        return array;
    }
    const pivot = array[array.length-1];
    const left = [];
    const right = [];
    
    //피벗 포함하면 무한재귀되기때문에 array.length-1
    for(let i = 0; i<array.length-1; i++) {
        if(array[i] < pivot) {
            left.push(array[i]);
        } else {
            right.push(array[i]);
        }
    }
    return [...quickSort(left), pivot, ...quickSort(right)];
}