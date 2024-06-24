word=input('''Hi you can get meaning of the following words here :
      1. Kam
      2. Dam
      3. Suru
      4. Khatam
      Give your response in 1,2,3 or 4 :''')

word=int(word)

hindi_dic={
    1:"Work",
    2:"Price",
    3:"Start",
    4:"End"
}

print(hindi_dic[word])
