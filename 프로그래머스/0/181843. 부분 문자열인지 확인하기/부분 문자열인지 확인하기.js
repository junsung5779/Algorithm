function solution(my_string, target) {
    let answer = 0;
    if (my_string.length < target.length) {
        return 0;
    }
    
    return my_string.includes(target) ? 1:0;
}