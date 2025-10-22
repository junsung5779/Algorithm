function solution(n) {
    let people = n;
    while(people % 6 !== 0) {
        people += n;
    }
    return people/6;
}