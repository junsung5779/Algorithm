function solution(n, control) {
    var answer = n;
    for(let i of control) {
        switch(i) {
            case "w":
                answer++;
                break
            case "s":
                answer--;
                break
            case "d":
                answer += 10;
                break
            case "a":
                answer -= 10;
                break;
        }
    }
    return answer;
}