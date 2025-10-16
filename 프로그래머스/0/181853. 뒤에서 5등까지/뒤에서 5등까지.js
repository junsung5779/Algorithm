function solution(num_list) {
    const sorted_list = quickSort(num_list);
    const answer = sorted_list.slice(0,5);
    return answer;
}

const quickSort = (arr) => {
    if (arr.length <= 1) {
        return arr;
    }
    const pivotIndex = Math.floor(arr.length/2);
    const pivot = arr[pivotIndex];
    const left = [];
    const right = [];
    
    for (let i=0; i<arr.length; i++) {
        if(i === pivotIndex) {
            continue;
        }
        if (arr[i] <= pivot) {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }
    return [...quickSort(left), pivot, ...quickSort(right)];
}