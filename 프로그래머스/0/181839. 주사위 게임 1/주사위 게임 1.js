function solution(a, b) {
    var answer = 0;
    if ((a*b)%2 === 1) {
        return a**2 + b**2
    }
    if ((a%2 === 1 && b%2 === 0) || (a%2 === 0 && b%2 === 1)) {
        return 2*(a+b);
    }
    if (a%2 === 0 && b%2 === 0) {
        if(a-b < 0) {
            return b-a;
        } else {
            return a-b;
        }
    }
    return answer;
}