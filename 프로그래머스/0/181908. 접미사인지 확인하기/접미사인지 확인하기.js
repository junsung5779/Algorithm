function solution(my_string, is_suffix) {
    if(my_string.length < is_suffix.length) {
        return 0;
    }
    
    const arr = [];
    for (let i=my_string.length-is_suffix.length; i<my_string.length; i++) {
        arr.push(my_string[i]);
    }
    
    return arr.join("") === is_suffix ? 1:0;
}