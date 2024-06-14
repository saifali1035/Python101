letter = '''Dear <Name>,
            You are Selected!
            <Date>'''

name = input("Enter Your Name: ")
date = input("Enter a date: ")

print(letter.replace("<Name>", name).replace("<Date>",date))