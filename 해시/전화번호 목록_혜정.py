def solution(phone_book):
    phones = sorted(phone_book)
    answer = True
    for i in range(len(phones)-1):
        j = len(phones[i])
        if phones[i] == phones[i+1][:j]:
            answer = False
            break
    return answer
