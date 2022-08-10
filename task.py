
menu = '♘ ♞ ♘ ♞ ♘ ♞\n___МЕНЮ___\n1)ввести данные\n2)выход'
chessboard = '8▓░▓░▓░▓░\n\
7░▓░▓░▓░▓\n\
6▓░▓░▓░▓░\n\
5░▓░▓░▓░▓\n\
4▓░▓░▓░▓░\n\
3░▓░▓░▓░▓\n\
2▓░▓░▓░▓░\n\
1░▓░▓░▓░▓\n\
 abcdefgh'

i1 = 0
A = []
for i in range(64):
    A.append(i1)
    i1 += 1
B = []
num ='12345678'
letters ='abcdefgh'
for i in range(8):
    for i1 in range(8):
        B.append(f'{letters[i]}{num[i1]}')

C = dict(zip(B, A))
print(C)
print(63+1 == 65 - 1)





while True:
    print(menu)
    a = input()
    if a == '1':
        print(chessboard)
        print('Введите начальные координаты коня(в формате "a1")')
        start = input()
        print('Введите конечные координаты коня(в формате "a1")')
        finish = input()
        different = C[start] - C[finish]
        if different == 17 or different == 15 or different == 10 or different == 6 or \
                different == -6 or different == -10 or different == -15 or different == -17:
            print(True)
        else:
            print(False)
    if a == '2':
        print('До скорой встречи!')
        break