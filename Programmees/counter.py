 def word_count(s):
    count={}
    for i in s:
        count[i]=s.count(i)
    return count
name=input('Enter your name :')
print(word_count(name))
input()