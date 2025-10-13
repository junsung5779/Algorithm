function solution(my_string, is_prefix) {
    // 접두사보다 문자열이 짧으면 바로 0
    if (my_string.length < is_prefix.length) {
        return 0;
    }

    // 접두사 길이만큼 비교
    for (let i = 0; i < is_prefix.length; i++) {
        if (my_string[i] !== is_prefix[i]) {
            return 0;
        }
    }

    return 1;
}