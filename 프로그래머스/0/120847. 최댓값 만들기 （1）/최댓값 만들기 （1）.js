function solution(numbers) {
    let answer = 0;
    const lastIndex = numbers.length;
    // 정렬하고 n
    const sortedNumbers = numbers.sort((a,b)=>(a-b));
    // 마지막 2개 원소 곱함(양의 정수니깐)
    answer = sortedNumbers[lastIndex-1] * sortedNumbers[lastIndex-2];
    return answer;
}