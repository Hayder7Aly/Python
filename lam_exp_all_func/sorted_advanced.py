fruits={'apple','grapes','oranges'}
print(sorted(fruits))
guitars_model=[
    {'model':'yamah 33','price':10000},
    {'model':'fleia 44','price':30000},
    {'model':'gelia 465','price':453200}
]
print(sorted(guitars_model,key= lambda d:d['price'],reverse=True))
input()