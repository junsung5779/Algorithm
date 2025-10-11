function solution(my_string) {
    const answer = [];
    for(const i of my_string){
        if(isUpperCase(i)) {
            answer.push(String.fromCharCode(i.charCodeAt()+32))
        } else {
            answer.push(String.fromCharCode(i.charCodeAt()-32))
        }
    }
    return answer.join('');
}

const isUpperCase = (str) => {
    if(97 <= str.charCodeAt()) {
        return false;
    }
    return true
}