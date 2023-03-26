class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 규칙1: 두 개의 문자의 위치를 서로 바꿀 수 있다.
        # 규칙2: 하나가 바뀌면 그에 대응하는 다른 문자도 동일하게 바뀐다.
        # 조건1: word1과 word2의 문자열의 길이가 맞아야 한다.
        # 조건2: a-z까지 개수를 파악하는 배열을 하나 만들어서 그 갯수를 배열에 입력 후
        # 정렬해줬을 때 word1에 대한 배열과 word2에 대한 배열이 동일하면 true 반환

        # 조건1 로직
        if len(word1) != len(word2):
            return False
        # 아스키코드로 배열 인덱스 결정
        arr_word1 = [0]*26
        arr_word2 = [0]*26
        # 조건2 로직
        for i in word1:
            arr_word1[ord(i)-97] += 1
        for j in word2:
            arr_word2[ord(j)-97] += 1
        # 배열 정렬
        arr_word1 = arr_word1.sort()
        arr_word2 = arr_word2.sort()
        # 정렬한 두 배열 비교
        if arr_word1 == arr_word2:
            return True
        else:
            return False