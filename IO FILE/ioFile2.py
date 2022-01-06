## w mode is used for write data in file  and w is deleted given data.
## a mode is used for append data in file.
## r+ mode is used for read and write data in file  and it overwrite the given 
# data in file in char or we can add data in end of first data.


with open('ioFile2.txt','w') as w:
    w.write('Hello ever one ')
with open('ioFile2.txt','a') as a:
    a.write('\nPlease do it\n Haider Ali Jutt ')
with open('ioFile2.txt','r+') as r:
    r.seek(len(r.read()))
    r.write('\nPlease do it ')
input()