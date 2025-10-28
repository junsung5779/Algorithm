function solution(my_string) {
    let answer = 0;
    const arr = [];
    for (let i=0; i<my_string.length; i++) {
        
        if (isNum(my_string[i])) {
            if (i === 0) {
                arr.push(Number(my_string[i]));
            } else {
                if (isNum(my_string[i-1])) {
                    arr[arr.length-1] *= 10;
                    arr[arr.length-1] += Number(my_string[i]);
                } else {
                    arr.push(Number(my_string[i]));
                }
            }
        }
        
    }
    for (const num of arr) {
        answer += num;
    }
    return answer;
}

const isNum = (str) => {
    if (48 <= str.charCodeAt() && str.charCodeAt() <= 57) {
        return true;
    } else {
        return false;
    }
}