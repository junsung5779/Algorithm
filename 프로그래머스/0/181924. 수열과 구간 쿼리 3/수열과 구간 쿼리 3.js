function solution(arr, queries) {
    let answer = arr;
    let tmp = 0;
    // arr의 원소끼리 교체해줌
    for(const query of queries) {
        tmp = arr[query[0]]
        arr[query[0]] = arr[query[1]]
        arr[query[1]] = tmp
    }
    return answer;
}