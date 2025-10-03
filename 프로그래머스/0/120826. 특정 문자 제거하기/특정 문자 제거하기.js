function solution(my_string, letter) {
    var answer = '';
    for(const i of my_string) {
        if(i !== letter) {
        answer += i;
        } 
    }
    return answer;
}