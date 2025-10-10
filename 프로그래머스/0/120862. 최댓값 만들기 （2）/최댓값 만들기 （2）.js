function solution(numbers) {
    var answer = 0;
    if (numbers.length === 2) {
        return numbers[0] * numbers[1];
    }
    const sorted_array = numbers.sort((a,b)=>{
        return a-b;
    })
    console.log(sorted_array)
    if (sorted_array[0]*sorted_array[1] < sorted_array[sorted_array.length-2] * sorted_array[sorted_array.length-1]) {
        answer = sorted_array[sorted_array.length-2] * sorted_array[sorted_array.length-1]
    } else {
        answer = sorted_array[0]*sorted_array[1]
    }
    return answer;
}