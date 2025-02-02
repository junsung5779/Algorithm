function solution(numbers) {
    // var answer = [];
    
    // 1. 만들 수 있는 모든 숫자 조합 구하기
    // 1-1. 서로 다른 인덱스, 두 개의 수, 덧셈
    const allArr = []
    for (let i = 0; i < numbers.length; i++) {
        for (let j = 0; j < i; j++) {
            allArr.push(numbers[i]+ numbers[j]);
        }
    }
    // 2. 중복 제거
    const uniqueArr = [...new Set(allArr)]
    // 3. 오름차순 정렬
    const answer = uniqueArr.sort((a,b)=>a-b);
    return answer;
}