def my_split(s):
    word=""
    words=[]
    for i in s:
        if i !=' ':
            word=word+i
        elif i==' ' and word!='':
            words.append(word)
            word=""
    if word!=' ':
        words.append(word)
    return words
l=my_split("Height    is awesome")
print(l)
