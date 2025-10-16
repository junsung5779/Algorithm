function solution(arr1, arr2) {
    let answer = 0;
    if (checkArrayLength(arr1, arr2) === 0) {
         // 두 배열의 길이가 같은 경우
        for(let i=0; i<arr1.length; i++){
            arr2[i] = arr2[i]-arr1[i];
        }
        for (const j of arr2) {
            answer += j;
        }
        return checkPositive(answer);
    } else {
        return checkArrayLength(arr1, arr2)
    }
}

const checkArrayLength = (arr1, arr2) => {
    if (arr1.length < arr2.length) {
        // arr1의 길이가 arr2보다 작은 경우
        return -1;
    } else if (arr1.length > arr2.length) {
        // arr1의 길이가 arr2보다 긴 경우
        return 1;
    } else {
        return 0;
    }
}

const checkPositive = (num) => {
    if (num > 0) {
        // arr2의 모든 요소의 합이 더 큰 경우
        return -1;
    } else if (num < 0) {
        // arr1의 모든 요소의 합이 더 큰 경우
        return 1;
    } else {
        // 두 배열의 모든 요소의 합이 같은 경우
        return 0;
    }
}