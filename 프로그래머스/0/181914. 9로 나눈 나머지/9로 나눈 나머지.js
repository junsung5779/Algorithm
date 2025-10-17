function solution(number) {
    const answer = [0];
    for(const num of number) {
        answer[0] += Number(num);
    }
    return answer[0]%9;
}