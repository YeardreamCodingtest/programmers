def solution(phone_book):
    phone_book = sorted(phone_book) # 11, 12, 119 -> 11, 119, 12 순으로 정렬 (string)
    for i in range(1, len(phone_book)): 
        if phone_book[i-1] in phone_book[i]: 
            return False
    return True
