function solution(num_list) {
    let answer = 0;
    const oddAndEven = [0,0];
    for(let i=0; i<num_list.length; i++) {
        if (i%2 === 1) {
            oddAndEven[0] += num_list[i];
        } else {
            oddAndEven[1] += num_list[i];
        }
    }
    if (oddAndEven[0] < oddAndEven[1]) {
        answer = oddAndEven[1];
    } else {
        answer = oddAndEven[0];
    }
    return answer;
}