function solution(letter) {
    const answer = [];
    const morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    console.log(morse['.-']);
    let tmpStr = '';
    for(const str of letter) {
        if (str === ' ') {
            answer.push(morse[tmpStr]);
            tmpStr = ''
            continue;
        } else {
            tmpStr += str;
            continue;
        }
    }
    if (tmpStr) {
        answer.push(morse[tmpStr]);
    }
    return answer.join("");
}