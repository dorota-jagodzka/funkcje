def check_if_palindrome(word):
    word_from_backwords = word[::-1]
    decision=True
    if(word != word_from_backwords):
        decision=False
    return decision