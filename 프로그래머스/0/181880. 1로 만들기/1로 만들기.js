function solution(num_list) {
    const answer = [0];
    const numList = [...num_list];
    for (let i=0; i<numList.length; i++) {
        if(numList[i] === 1) {
            continue;
        } else {
            if (numList[i]%2 !== 0) {
                numList[i] -= 1;
            }
            while(numList[i] >= 2) {
                numList[i] = numList[i]/2;
                answer[0] += 1;
            }
        }
        
    }
    return answer[0];
}