function solution(before, after) {
    const arr = [];
    for(let i=0; i<26; i++) {
        arr.push([0,0])
    }
    for (const i of before) {
        arr[i.charCodeAt()-97][0] += 1;
    }
    for (const i of after) {
        arr[i.charCodeAt()-97][1] += 1;
    }
    
    for (let j=0; j<26; j++) {
        if (arr[j][0] === arr[j][1]) {
            if (j===25) {
                return 1;
            }
            continue;
        } else {
            return 0
        }
    }
}

