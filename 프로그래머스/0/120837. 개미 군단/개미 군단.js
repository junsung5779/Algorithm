function solution(hp) {
    let answer = 0;
    let leftHP = hp;
    answer += Math.floor(leftHP/5);
    leftHP = leftHP%5;
    if (leftHP === 0) {
        return answer;
    } else if(3 <= leftHP) {
        answer += Math.floor(leftHP/3) + ((leftHP-3)%3);
    } else {
        answer += leftHP;
    }
    
    
    
    return answer;
}