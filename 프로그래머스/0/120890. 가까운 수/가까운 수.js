function solution(array, n) {
    let answer = 9999;
    let gap = 9999;
    for (let i=0; i<array.length; i++) {
        const diff = Math.abs(array[i] - n);
        if (diff <= gap) {
            if (diff === gap) {
                if (array[i] < answer) {
                    answer = array[i];
                }
            } else {
                gap = diff;
                answer = array[i];
            }
        }
    }
    return answer;
}