

def word_count(s):
    words = s.lower().split()
    words_counted = dict()
    bad_chars = ['"', ':', ';', ',', '.', '-', '+', '=', '/',  '\\',
                 '|', '[', ']', '{', '}',  '(', ')', '*', '^', '&', ]

    # remove bad chars
    for word in words:
        stripped_word = ''.join(i for i in word if not i in bad_chars)
        if len(stripped_word) > 0:
            if stripped_word in words_counted:
                words_counted[stripped_word] = words_counted[stripped_word] + 1
            else:
                words_counted[stripped_word] = 1

    return words_counted


print(word_count('":;,.-+=/\\|[]{}()*^&'))
if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
