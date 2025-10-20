function solution(my_string) {
    const arr = [];
    // 모든 접두사 answer에 담기
    for(let i=0; i<my_string.length; i++) {
        arr.push(my_string.slice(i,my_string.length+1));
    }
    return(arr.sort());
}
    
