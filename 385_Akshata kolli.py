print("====================================Program-1==========================")

print("====================================Palindrome using for loop==========================")
string_input=input("enter the string:")
lst=[]
for i in string_input[::-1]:
    lst.append(i)
print("".join(lst))

print("-------------using generator mechanism--------------")
def palindrom(str):
    lst=[]
    for i in string_input[::-1]:
        yield(lst.append(i))
str=input("enter a string:")
res=palindrom(str)
print("this is generator object:",res)
print("final output-")
list=[]
for i in lst:
    list.append(i)
print("".join(list))


print("---------------PROGRAM-2--------------------")
def sum_of_digit(n1,n2):
    return int(n1)+int(n2)
n1=list(str(int(input("enter first number:"))))
n2=list(str(int(input("enter second number:"))))
res=list(map(sum_of_digit,n1,n2))
temp=0
for i in res:
    temp=temp+i
print("final output:",temp)


print("-----------------------PROGRAM-3---------------------------")
def reverse_string(st):
    return''.join(reverse_word(word)for word in st.split())
def reverse_word(st):
    stack = []
    for el in st:
        if el.isalpha():
            stack.append(el)
    result=""
    for el in st:
        if el.isalpha():
            result+=stack.pop()
        else:
            result += el
    return result
instr='fe@#dc!ba'
print(reverse_string(instr))


print("--------------------------PROGRAM-4--------------------------")
from collections import Counter
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
counts = dict(Counter(some_list))
duplicates = {key:value for key, value in counts.items() if value > 1}
print(duplicates)


print(" ----------------------PROGRAM-5--------------------------------")
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
lis1 = []
lis2 = []
for t in t1:
    if isinstance(t, int):
        for i in t2:
            if i not in lis2 and isinstance(i, int):
                lis2.append(i)
                lis1.append((t + i))
                break
    else:
        for i in t2:
            if i not in lis2 and isinstance(i, str):
                lis2.append(i)
                lis1.append((t + i))
                break

print(lis1)


print("-------------------PROGRAM-6-----------------------------------")
def ip(ip_add):
  new_ip = ".".join([str(int(i)) for i in ip_add.split(".")])
  return new_ip


print("--------------------------PROGRAM-7--------------------------------")
a = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
print(list(map(lambda x:int(x),str(a).replace('[','').replace(']','').split(', '))))



print('-------------------PROGRAM-8--------------------------')
'''1.No of lines in file '''

with open(r"/Users/naresh/Desktop/FLASK (1).txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)

'''2.No of words in each line '''

file = open("/Users/naresh/Desktop/FLASK (1).txt", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))

'''3. No of chars in each line '''

file = open("/Users/naresh/Desktop/FLASK (1).txt", "r")
data = file.read()
#get the length of the data
number_of_characters = len(data)

print('Number of characters in text file :', number_of_characters)

''' 4. No of vowels and consonants'''

fileName = input("Enter the file to check: ").strip()
infile = open(fileName, "r")
vowels = set("A E I O U a e i o u")
cons = set("b c d f g h j k l m n p q r s t v w x y z B C D F G H J K L M N P Q R S T V W X Y Z")
text = infile.read().split()
countV = 0
for V in text:
    if V in vowels:
        countV += 1
countC = 0
for C in text:
    if C in cons:
        countC += 1
print("The number of Vowels is: ",countV,"\nThe number of consonants is: ",countC)



def abc():
    print("hello python")
abc()


