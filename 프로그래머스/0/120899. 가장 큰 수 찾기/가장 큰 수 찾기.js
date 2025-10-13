function solution(array) {
    let highest_number = 0;
    let index = 0;
    
    for(let i=0; i<array.length; i++) {
        if(array[i] > highest_number) {
            highest_number = array[i];
            index = i;
        }
    }
    return [highest_number, index];
}