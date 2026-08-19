for i in range(21):
    print(i)


for i in range(21, 0, -1):
    print(i)    


num = int(input("which table do u want: "))
for i in range(num, num*10+1, num):
    print(i)  


a = 'huzaifa akhlaq is the Hafiz'
for i in a:
    print(i)
print(a)


for i in range(1, 21):
    if i == 7:
        break
    print(i)


for i in range(1, 21):
    if i == 7:
        continue
    print(i)
