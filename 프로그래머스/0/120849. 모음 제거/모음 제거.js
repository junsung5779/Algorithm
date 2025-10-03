function solution(my_string) {
    var answer = '';
    for(const i of my_string) {
        if(i ==='a' || i === 'e' || i === 'i' || i === 'o' || i === 'u') {
            continue;
        } else {
            answer += i;
        }
    }
    return answer;
}