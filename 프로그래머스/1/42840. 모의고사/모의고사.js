function solution(answers) {
    // 수포자들의 정답 패턴
    const patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    // 수포자들의 점수를 저장할 배열
    const scores = [0,0,0]
    
    // 각 수포자들의 패턴과 정답이 얼마나 일치하는지 확인
    for (const [i, answer] of answers.entries()) {
        for (const [j, pattern] of patterns.entries()) {
            if (answer === pattern[i % pattern.length]) {
                scores[j] += 1;
            }
        }
    }
    
    // 가장 높은 점수 저장
    const maxScore = Math.max(...scores);
    
    // 가장 높은 점수를 받은 수포자들의 번호를 찾아서 배열에 담음(이 단계에서 이미 오름차순으로 배열에 집어넣음으로, 최고득점자가 여러명인 경우에도 정렬할 필요가 없음.)
    const highScoreUsers = [];
    for (let i = 0; i < scores.length; i++) {
        if (scores[i] === maxScore) {
            highScoreUsers.push(i + 1);
        }
    }
    
    
    return highScoreUsers;
}