with open('star_s.txt','a') as a:
    row=int(input('Enter a number of row :'))
    a.write('Your style is added in file \n')
    end=''
    for i in range(row):
        end+='*'
        a.write(f"{end}\n")