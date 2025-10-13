function solution(my_string) {
    let answer = [];
    answer = goLowerCase(my_string).sort();
    
    return answer.join("");
}

const goLowerCase = (string) => {
    const answer = [];
    for (let i=0; i<string.length; i++) {
        if(65 <= string[i].charCodeAt() && string[i].charCodeAt() <= 90) {
            answer.push(String.fromCharCode(string[i].charCodeAt()+32))
        }
        if(97 <= string[i].charCodeAt() && string[i].charCodeAt() <= 122) {
            answer.push(string[i]);
        }
    }
    return answer;
}

