
function solution(answers) {
    // 해설을 보고 푼 문제입니다.
    // 수포자들의 정답 패턴
    const patterns = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    // 수포자들의 점수를 저장할 배열
    const scores = [0,0,0]
    
    /**
    * 각 수포자들의 패턴과 정답이 얼마나 일치하는지 확인
    * entries() 는 배열 내 데이터를 인덱스와 값으로 묶어서 순회할 수 있는 Iterator 객체를 반환함.
    * Iterator 객체를 of 연산자를 이용하면 처음부터 끝까지 순회하는 것이 가능함.
    * 정답 패턴의 길이가 수포자의 답안 길이보다 긴 경우 정답 패턴의 처음 데이터와 다시 비교할 수 있도록 나머지 연산자 사용.
    */ 
    
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