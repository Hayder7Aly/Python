with open('write_read.txt','r') as rf:
    with open('write_read2.txt','w') as wf:
        wf.write(rf.read())
input()