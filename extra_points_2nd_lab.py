info = input()

def code(x):
    
    if (int(x[0]) + int(x[2]) + int(x[4]) + int(x[6])) % 2 == 0 and \
       (int(x[1]) + int(x[2]) + int(x[5]) + int(x[6])) % 2 == 0 and \
       (int(x[3]) + int(x[4]) + int(x[5]) + int(x[6])) % 2 == 0:
        return x[2] + x[4] + x[5] + x[6]
  
    else:
        if (int(x[0]) + int(x[2]) + int(x[4]) + int(x[6])) % 2 != 0 and \
           (int(x[1]) + int(x[2]) + int(x[5]) + int(x[6])) % 2 == 0 and \
           (int(x[3]) + int(x[4]) + int(x[5]) + int(x[6])) % 2 == 0:
            if x[0] == '0':
                x = '1' + x[1:]
            else:
                x = '0' + x[1:]
            return x[2] + x[4] + x[5] + x[6], 'Ошибочный бит: 1'
        
        if (int(x[0]) + int(x[2]) + int(x[4]) + int(x[6])) % 2 == 0 and \
           (int(x[1]) + int(x[2]) + int(x[5]) + int(x[6])) % 2 != 0 and \
           (int(x[3]) + int(x[4]) + int(x[5]) + int(x[6])) % 2 == 0:
            if x[1] == '0':
                x = x[0] + '1' + x[2:]
            else:
                x = x[0] + '0' + x[2:]
            return x[2] + x[4] + x[5] + x[6], 'Ошибочный бит: 2'

        if (int(x[0]) + int(x[2]) + int(x[4]) + int(x[6])) % 2 == 0 and \
           (int(x[1]) + int(x[2]) + int(x[5]) + int(x[6])) % 2 == 0 and \
           (int(x[3]) + int(x[4]) + int(x[5]) + int(x[6])) % 2 != 0:
            if x[3] == '1':
                x = x[0:3] + '0' + x[4:]
            else:
                x = x[0:3] + '1' + x[4:]
            return x[2] + x[4] + x[5] + x[6], 'Ошибочный бит: 4'

        if (int(x[0]) + int(x[2]) + int(x[4]) + int(x[6])) % 2 != 0 and \
           (int(x[1]) + int(x[2]) + int(x[5]) + int(x[6])) % 2 != 0 and \
           (int(x[3]) + int(x[4]) + int(x[5]) + int(x[6])) % 2 == 0:
            if x[2] == '1':
                x = x[0:2] + '0' + x[3:]
            else:
                x = x[0:2] + '1' + x[3:]
            return x[2] + x[4] + x[5] + x[6], 'Ошибочный бит: 3'

        if (int(x[0]) + int(x[2]) + int(x[4]) + int(x[6])) % 2 == 0 and \
           (int(x[1]) + int(x[2]) + int(x[5]) + int(x[6])) % 2 != 0 and \
           (int(x[3]) + int(x[4]) + int(x[5]) + int(x[6])) % 2 != 0:
            if x[5] == '1':
                x = x[0:5] + '0' + x[6]
            else:
                x = x[0:5] + '1' + x[6]
            return x[2] + x[4] + x[5] + x[6], 'Ошибочный бит: 6'

        if (int(x[0]) + int(x[2]) + int(x[4]) + int(x[6])) % 2 != 0 and \
           (int(x[1]) + int(x[2]) + int(x[5]) + int(x[6])) % 2 == 0 and \
           (int(x[3]) + int(x[4]) + int(x[5]) + int(x[6])) % 2 != 0:
            if x[4] == '1':
                x = x[0:4] + '0' + x[5:]
            else:
                x = x[0:4] + '1' + x[5:]
            return x[2] + x[4] + x[5] + x[6], 'Ошибочный бит: 5'

        if (int(x[0]) + int(x[2]) + int(x[4]) + int(x[6])) % 2 != 0 and \
           (int(x[1]) + int(x[2]) + int(x[5]) + int(x[6])) % 2 != 0 and \
           (int(x[3]) + int(x[4]) + int(x[5]) + int(x[6])) % 2 != 0:
            if x[6] == '1':
                x = x[0:6] + '0'
            else:
                x = x[0:6] + '1'
            return x[2] + x[4] + x[5] + x[6], 'Ошибочный бит: 7'

print(*code(info))


