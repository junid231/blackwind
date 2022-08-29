def encrypt(msg):
    k = ''
    c = ''
    while len(k) < len(msg):
        k += key
    print(k)
    for i in range(len(msg)):
        if msg[i] == ' ':
            c += ' '
        if ord(msg[i]) >= 65 and ord(msg[i]) <= 90:
            new_C = ord(k[i].upper())-65+ord(msg[i])
            if new_C > 90:
                new_C -= 26
            c += chr(new_C)
        if ord(msg[i]) >= 97 and ord(msg[i]) <= 122:
            new_c = ord(k[i])-97+ord(msg[i])
            if new_c > 122:
                new_c -= 26
            c += chr(new_c)
    return c
        
def decrypt(msg):
    k = ''
    c = ''
    while len(k) < len(msg):
        k += key
    for i in range(len(msg)):
        #print(msg[i], k[i])
        if msg[i] == ' ':
            c += ' '
        if ord(msg[i]) >= 65 and ord(msg[i]) <= 90:
            new_C = ord(msg[i]) - ord(k[i].upper())+65
            if new_C < 65:
                new_C += 26
            c += chr(new_C)
        if ord(msg[i]) >= 97 and ord(msg[i]) <= 122:
            new_c = ord(msg[i])-ord(k[i])+97
            if new_c < 97:
                new_c += 26
            c += chr(new_c)
    return c

while True:
    key = 'lemon'
    mode = input('choose\n1. encrypt\n2. decrypt\n3. end\n')
    if mode == '1':
        msg = input('M: ')
        print('C:'+encrypt(msg))
    elif mode == '2':
        msg = input('M: ')
        print('C:'+ decrypt(msg))
    else:
        break