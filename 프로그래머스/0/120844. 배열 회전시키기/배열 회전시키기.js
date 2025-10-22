function solution(numbers, direction) {
    const arr = new Array(numbers.length).fill(0);
    if (direction === "right") {
        for(let i=0; i<arr.length; i++) {
            if (i === arr.length-1) {
                arr[0] = numbers[i]
            } else {
                arr[i+1] = numbers[i]
            }
        }
    } else {
        for (let i=0; i<arr.length; i++) {
            if (i === 0) {
                arr[arr.length-1] = numbers[i];
            } else {
                arr[i-1] = numbers[i];
            }
        }
    }
    return arr;
}