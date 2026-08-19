n = int(input("which num fact you want: "))

sum = 0
for i in range(1, n):
    if n %i == 0:
        sum += i
        
print(sum)
if sum == n:
    print(f"{n} is a perfect")

else:
    print(f"{n} is not a perfect")    
