function solution(arr) {
  const answer = [...arr];

  if (answer.length === 1) {
    return answer;
  }

  for (let i = 1; i <= 1024; i *= 2) {
    if (answer.length === i) {
      return answer;
    }
    if (arr.length < i) { // arr.length 고정값 사용 = 안전
      for (let j = 0; j < i - arr.length; j++) {
        answer.push(0);
      }
      return answer;
    }
  }
  return answer;
}