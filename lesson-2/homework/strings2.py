task1:
name = input("your name: ")
age = input("your age: ")
shablon = "Hello {}. you are {} y.o." .format(name, age) 
print(shablon)

task2:
txt = 'LMaasleitbtui'
target_word = "Malibu, Lasetti"
matched_word = (txt, target_word)
print(matched_word) 

task3:
txt = 'MsaatmiazD'
target_word = "Matiz, Damas"
matched_word = (txt, target_word)
print(matched_word)

task4:
txt = "I'am John. I am from London"
residence = txt.split()
sixth_word = residence[5]
print(sixth_word) 

task1: 
str1 = 'James'
res = str1[0]
l = len(str1)
mi = int(l / 2)
res = res + str1[mi]
res = res + str1[l - 1]
print(res)

task2:
str1 = "JhonDipPeta"
print(str1[4:7])

str2 = "JaSonAy"
print(str2[2:5])

task3:
s1 = "Ault"
s2 = "Kelly" 
q = int(len(s1) / 2) 
w = s1[:q:]
e = w + s2
e = e + s1
print(e)

task4:
s1 = "America"
s2 = "Japan" 
q = int(len(s1) / 2)
w = s1[:q:]
e = w + s2
e = e +s1
print(e)

task5:
str1 = "PyNaTive"
lower = []
upper = []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted_str = ''.join(lower + upper)
print('', sorted_str)

task6:
str1 = "P@#yn26at^&i5ve"
char_count = 0
digit_count = 0
symbol_count = 0
for char in str1:
    if char.isalpha():
        char_count += 1
    elif char.isdigit(): 
        digit_count += 1
    else: symbol_count += 1
print("chars = ", char_count, "digits = ", digit_count, "symbols = ", symbol_count)

task7:
def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag
s1 = "Yn"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print(flag)

s1 = "Ynf"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print(flag)

task8:
str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"
lower = str1.lower()
count = lower.count(sub_string.lower())
print(count)

task9:
str1 = "PYnative29@#8496"
total = 0 
count = 0
for char in str1:
    char.isdigit()
    total += int(char)
    count += 1
avg = total / count
print("total is: ", total, "average is: ", avg)

task10:
str1 = "Apple"

a = str1.count('A')
p = str1.count('p')
l = str1.count('l')
e = str1.count('e')

print(f"'A':{a},'p':{p}, 'l':{l}, 'e': {e}")

task11: 
str1 = "PYnative"

a = str1[::-1]
print(a)

task12:
str1 = "Emma is a data scientist who knows Python. Emma works at google."
index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", index)

task13:
str1 = "Emma-is-a-data-scientist"
q = "Emma\nis\na\ndata\nscientist"
print(q) 

task14:
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
new_str_list = list(filter(None, str_list))
print(new_str_list)

task15:
str1 = "/*Jon is @developer & musician" 
print("John is developer and musician")

task16:
str1 = 'I am 25 years and 10 months old'
print("2510")
