def outer_func(msg):
    def inner_func():
        print('Your message is :\n\t',msg)
    return inner_func
message=input('Type the message !')
var=outer_func(message)
var()
input()