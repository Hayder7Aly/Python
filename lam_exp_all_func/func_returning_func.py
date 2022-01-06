def outer_func():
    def inner_func():
        print('Inner func is :')
    return inner_func
var =outer_func()
var()
def outer_func2(msg):
    def inner_func2():
        print(f"your message is ",msg)
    return inner_func2
var=outer_func2('Hi! there awsome.')
var()