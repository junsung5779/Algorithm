function solution(price) {
    var answer = 0;
    if(price < 100000) {
        answer = price;
    } else if(100000<=price && price<300000){
        answer = Math.floor(price*0.95);
    } else if(300000<=price && price<500000){
        answer = Math.floor(price*0.9);
    } else {
        answer = Math.floor(price*0.8);
    }
    return answer;
}