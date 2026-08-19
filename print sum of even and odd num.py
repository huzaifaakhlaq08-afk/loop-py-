
num1 = int(input("Enter a number: "))

even = 0
odd = 0

for i in range(1, num1+1):
        if i %2 == 0:
                even += i

        else:
                odd += i
print(f"your even or odd sum are {even} & {odd}")                        
        