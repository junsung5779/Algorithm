function solution(i, j, k) {
    let answer = 0;
    for (let start=i; start<=j; start++) {
        let num = start;
        while (num >= 1) {
            if(num%10 === Math.floor(k)) {
                answer += 1;
            }
            num = Math.floor(num/10);
        }
    }
    
    
    return answer;
}