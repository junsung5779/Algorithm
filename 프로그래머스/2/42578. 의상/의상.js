function solution(clothes) {
    const noWearCase = 1;
    let answer = 1;
    const combination = new Map();
    const type = new Map();
    for (let i=0; i<clothes.length; i++) {
        if (combination.has(clothes[i][1])) {
            type.set(clothes[i][1], type.get(clothes[i][1])+1)
        } else {
            combination.set(clothes[i][1], clothes[i][0]);
            type.set(clothes[i][1], 1);
        }
    }
    for(const j of type) {
        answer *= j[1]+1;
    }
    return answer-noWearCase;
}