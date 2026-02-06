def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book: # 번호를 하나씩 꺼내서
        hash_map[phone_number] = 1 # 딕셔너리 만들고 {"119": 1, "97674223": 1, "1195524421":1}
    for phone_number in phone_book: # 번호를 하나씩 꺼내서
        temp = "" # 변수 생성 및 초기화, 문자열
        for number in phone_number: # 딕셔너리에서 키값 번호 하나씩 꺼내서
            temp += number # 번호 하나씩 넣고
            if temp in hash_map and temp != phone_number: # 변수가 접두어이고(들어가있고) 키값으로 있고 벼수가 키값이 아니면
                answer = False
    return answer