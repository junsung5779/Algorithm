function solution(board, k) {
    const answer = [0];
    for (let i=0; i<board.length; i++) {
        for (let j=0; j<board[i].length; j++) {
            if(i+j <= k) {
                answer[0] += board[i][j];
            }
        }
    }
    return answer[0];
}