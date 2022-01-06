def common(s,s2):
    return{i for i in s if i in s2}
def union_1(s_1,s_2):
    return s_1|s_2
user=int(input('How many number enter in set_1 :'))
print('Enter',user,'Numbers :')
total={0}
for i in range(1,user+1):
    num=int(input())
    total.add(num)
total.remove(0)
print(total)
user_1=int(input('How many number enter in set_2 :'))
print('Enter',user_1,'Numbers :')
total_1={0}
for i in range(1,user_1+1):
    num_1=int(input())
    total_1.add(num_1)
total_1.remove(0)
print(total_1)
print('SET INTERSECTION IS :\n',common(total,total_1))
print('SET UNION IS : \n',union_1(total,total_1) )
input()