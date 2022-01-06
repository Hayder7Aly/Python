letter=input('Enter a vowel or other letter :')
letter_1=letter.upper()
if letter_1=='A'or letter_1=='E'or letter_1=='I'or letter_1=='O'or letter_1=='U':
    print('You entered vowel alphabet :')
elif letter_1>='A'and letter_1<='Z':
    print('You do not enter vowel :')
else:
    print('Invalid choice :')
input()