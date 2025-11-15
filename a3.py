str1 = input("Enter a sentence:")
num = 1

for i in range(len(str1)):
    if(str1[i] ==' '):
        num+=1

print("The total number of words=",num)