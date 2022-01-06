faherienheit=int(input('Enter the faherienhiet scale :'))
print('Faherienheit\tcelcius')
for i in range(1,11):
    celcius=((faherienheit-32)*5/9).__round__(2)
    print(faherienheit,'\t       ',celcius,'C')
    faherienheit+=5
input()
