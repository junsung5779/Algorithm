function solution(str1, str2) {
    var answer = 0;
    for (let i=0; i<str2.length-str1.length+1; i++) {
        for (let j=0; j<str1.length; j++) {
            if(str2[i+j] === str1[j]) {
                if(j === str1.length-1){
                    answer = 1;
                }
                continue;
            } else {
                break;
            }
        }
    }
    return answer;
}