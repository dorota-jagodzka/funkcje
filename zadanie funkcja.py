def check_if_palindrome(word):
    word_from_backwords = word[::-1]
    decision=True
    if(word != word_from_backwords):
        decision=False
    return decision

word = "potop"
result= check_if_palindrome(word)
if(result):
    print("To słowo jest palindromem")
else:
    print("To słowo nie jest palindromem")