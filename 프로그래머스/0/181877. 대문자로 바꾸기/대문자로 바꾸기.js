function solution(myString) {
    // toUpperCase 쓰면 너무 쉬우니..
    // toUpperCase 내부로직 직접 구현하는식으로 학습해보자.
    // charCodeAt 내부로직은 C++로 구현되어 있기 때문에 이 이상 가지말고 이걸로 구현하자.
    var answer = '';
    for(const i of myString) {
        if(97 <= i.charCodeAt(0) && i.charCodeAt(0) <= 122) {
            answer += String.fromCharCode(i.charCodeAt(0)-32);
        } else {
            answer += i;
        }
    }
    return answer;
}