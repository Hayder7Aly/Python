# In this programme t is variable
# Open is function which is used to open the file such as which user want !
# Read is method which is used for read the following words in file .
# Tell is used for find the position of word .
# Seek is used for print data in two times more.
# Readline is used for print lines wise.
# Name is Used for find the name of file .
# Closed is used for check whether the programme is close or not !


t=open('text.txt')
print(t.readline(),end='')
print(t.readline(),end='')
print(f'Cursor Position is :{t.tell()}')
print('Before Seek Method !')
t.seek(0)
print('After Seek Method !')
print(f'Cursor Position is : {t.tell()}')
print(t.read())
print(t.name)
for i in t.readlines()[:2]:
    print(i,end='')

t.close()
print(t.closed)
input()