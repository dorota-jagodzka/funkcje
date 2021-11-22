def check_if_palindrome(word):
    return word == word[::1]

word = "potop"
result = check_if_palindrome(word)
if result:
    print("To słowo jest palindromem")
else:
    print("To słowo nie jest palindromem")