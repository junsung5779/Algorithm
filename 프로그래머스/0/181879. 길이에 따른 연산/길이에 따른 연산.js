function solution(num_list) {
    let answer = 1;
    if (num_list.length >= 11) {
        for (const num of num_list){
            answer += num;
        }
        answer -= 1;
    } else {
        for (const num of num_list){
            answer *= num;
        }
    }
    return answer;
}