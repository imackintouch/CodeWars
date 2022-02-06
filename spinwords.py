def spin_words(sentence):
    word_list = sentence.split(" ")
    spin=''
    for word in word_list:
        if len(word) >= 5:
            spin += word[-1::-1]+' '
        else:
            spin += word+' '

    return spin[:-1]

    #return (''.join([word[-1::-1]+' ' if len(word) >= 5 else word+' ' for word in word_list]))[:-1]


print(spin_words('ot')+'.')
print(spin_words('yeH wollef sroirraw')+'.')
print(spin_words('Make it so Number One')+'.')
print(spin_words('The clock is another demon that devours our time in Eden')+'.')
print(spin_words('Stop')+'.')
print(spin_words('')+'.')
