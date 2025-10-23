function solution(n) {
    if (n < 4) {
        return 0;
    }
    const answer = [0];
    for (let i=4; i<=n; i++){

        for (let j=2; j<=i; j++) {
            if (j !== i && i%j === 0) {
                answer[0] += 1;
                break;
            }
        }
    }
    return answer[0];
}