#
# See https://www.codewars.com/kata/5848565e273af816fb000449?utm_source=newsletter&utm_medium=email&utm_campaign=weekly_coding_challenges&utm_term=2020-06-07
#

def encrypt_this(words):
    word_list = words.split()
    encrypted_words_list = []
    for word in word_list:
        encrypted_word = str(ord(word[0]))
        if len(word) > 1:
            encrypted_word = str(ord(word[0])) + word[len(word) - 1] \
                         + (word[2:len(word) - 1] + word[1] if len(word) > 2 else "")
        encrypted_words_list.append(encrypted_word)

    return " ".join(encrypted_words_list)


print(encrypt_this("A wise old owl lived in an oak"))
print(":"+encrypt_this("Hello")+":")
print(":"+encrypt_this("hello world")+":")
print(":"+encrypt_this("A bird in hand")+":")
print(":"+encrypt_this("")+":")
# encrypt_this("Hello")
# encrypt_this("hello world")