
function solution(array) {
    // 1. 오름차순으로 정렬을 할 수 있어야 함. .. 아... sort 직접구현하기 싫다... 피곤하니까.. 한잔해..
  const sortedArray = quickSort(array);
    // 2. 가운데 수를 구해야 함. -> 가운데 수란? -> 정렬했을 때 가운데 인덱스에 있는 수
    // 배열 길이가 홀수일떄 -> 중앙값: 배열[(배열 길이/2)+1]
    // 배열 길이가 짝수일때 -> 배열[(배열 길이/2)-1] 와 배열[(배열 길이/2)] 값 중에 중앙값을 찾아야 함.
    // 이 경우에 중앙값은 뭐지? -> 정답보니깐 둘 다 더한다음 2로 나눈값이 중앙값이 나오도록 해야 하네
    // 이 케이스에 대한 명확한 설명없이 문제를 낸듯.
  const mid = Math.floor(sortedArray.length / 2);

  let answer = 0;
  if (sortedArray.length % 2 === 0) {
    answer = (sortedArray[mid - 1] + sortedArray[mid]) / 2;
  } else {
    answer = sortedArray[mid];
  }

  return answer;
}

const quickSort = (array) => {
    if(array.length <= 1) {
        return array;
    }
    
    const pivot = array[array.length-1]
    const left = [];
    const right = [];
    
    for(let i=0; i<array.length-1; i++) {
        if(array[i] < pivot) {
            left.push(array[i]);
        } else {
            right.push(array[i]);
        }
    }
    return [...quickSort(left), pivot, ...quickSort(right)];
}