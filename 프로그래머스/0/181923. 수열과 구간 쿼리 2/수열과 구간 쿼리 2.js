function solution(arr, queries) {
    var answer = [];
    
    for(const [s, e, k] of queries) {
        // 쿼리 인덱스의 범위 내에 있는 숫자들을 오름차순으로 정렬 후 배열로 만듦
        const sortedArray = arr.slice(s, e+1).sort((a,b)=>a-b);
        
        let isTargetNumberFound = false;    // 특정 쿼리의 답의 존재유무
        
        for(const number of sortedArray) {
            // 정렬된 배열의 요소를 낮은 숫자부터 비교하며 k보다 큰 숫자를 발견하는 경우
            if(k < number) {
                // 해당 숫자를 answer에 push
                answer.push(number);
                isTargetNumberFound = true  // 해당 쿼리에서는 답이 있음.
                break;
            }
        }
        // 답이 없으면 -1을 answer에 push
        if (!isTargetNumberFound) {
            answer.push(-1);
        }
    }
    return answer;
}