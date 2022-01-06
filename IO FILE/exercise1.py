with open('exercise1.txt','r') as rf:
    with open('exercise1_part.txt','a') as wf:
        for line in rf.readlines():
            name,salay=line.split(',')
            wf.write(f"{name}'s salary{salay}")
