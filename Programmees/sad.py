for i in range(5):
    keyboard_input=input('Enter a character from keyboard :')
    if keyboard_input>='a' and keyboard_input<='z':
        print('You enter' ,keyboard_input,'small alphbet letter :')
    elif keyboard_input>='A' and keyboard_input<='Z':
        print('You enter ',keyboard_input,'capital alphabet letter :')
    elif keyboard_input>='0' and keyboard_input<='9':
        print('You enter ',keyboard_input,'number digit :')
    else:
        print('you enter',keyboard_input,'symbol character :')
input()