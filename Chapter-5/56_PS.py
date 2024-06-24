fav_lang={}

for i in range(4):
    name=input("What is your name:")
    lang=input("What is your favourite language:")
    fav_lang.update({name:lang})

print(fav_lang)