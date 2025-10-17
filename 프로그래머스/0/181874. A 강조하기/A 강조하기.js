function solution(myString) {
    const arr = [];
    for (const str of myString) {
        if (str === "a") {
            arr.push("A");
        } else {
            if (str.charCodeAt() >= 66 && str.charCodeAt() <= 90) {
                arr.push(String.fromCharCode(str.charCodeAt()+32));
            } else {
                arr.push(str);
            }
        }
    }
    return arr.join("");
}