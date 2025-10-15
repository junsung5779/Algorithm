function solution(arr, delete_list) {
    const answer = [];
    for (const i of arr) {
        for (let j=0; j<delete_list.length; j++) {
            // delete_list의 요소중 하나라도 일치하면 다음 i로 진행
            if(i === delete_list[j]) {
                break;
            }
            // 마지막 요소까지 검사했을 때 delete_list의 요소중 하나도 일치하지 않았다면 answer에 추가
            if(j === delete_list.length-1) {
                answer.push(i);
            }
        }
    }
    return answer;
}