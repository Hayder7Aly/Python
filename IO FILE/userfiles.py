with open('userfiles.txt','a') as a:
    name=input('Enter your name :')
    age=int(input('Enter your age :'))
    a.write(f"Hello {name}\nYour age is {age}\n")
input()