def check_if_palindrome(word):
    word_spelled_backwards = word[::-1]
    decision = True
    if word != word_spelled_backwards:
        decision = False
    return decision

word = "potop"
result = check_if_palindrome(word)
if result :
    print("To słowo jest palindromem")
else:
    print("To słowo nie jest palindromem")