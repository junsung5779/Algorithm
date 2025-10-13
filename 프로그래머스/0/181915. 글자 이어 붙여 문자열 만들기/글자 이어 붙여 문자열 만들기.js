function solution(my_string, index_list) {
    const answer = [];
    for (const i of index_list) {
        answer.push(my_string[i]);
    }
    return answer.join("");
}