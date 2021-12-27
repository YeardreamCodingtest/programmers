def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        len_x = len(phone_book[i])
        len_y = len(phone_book[i+1])
        if phone_book[i] == phone_book[i+1][:len_x] and len_x != len_y:
            return False

    return True
