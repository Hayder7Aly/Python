name=input('Enter a string :\n')
char=input('which word or alphabet you locate :')
if char in name:
    print('This',char,' word are present in string :')
else:
    print('this',char,'word are not present in string :')
    input()