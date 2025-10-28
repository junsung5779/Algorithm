function solution(s) {
    const answer = [];
    const arr = [];
    
    for (let i=0; i<26; i++) {
        arr.push(0);
    }
    
    for (const str of s) {
        arr[str.charCodeAt()-97] += 1;
    }
    
    for (let num=0; num<arr.length; num++) {
        if(arr[num] === 1) {
            answer.push(String.fromCharCode(num+97));
        }
    }
    return answer.join("");
}