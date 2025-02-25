task1:
name = "Abdulaziz"
print(len(name))

task2:
str1 = "google.com"
letter_count = {}
for letter in str1:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count) 

task3:
str1 = 'w3resource' 
print(str1[0:2] + str1[-2:])
str2 = 'w3'
print(str2 + str2)
str3 = ' w'
if len(str3) < 2:
  print(' ') 

task4:
word = "restart"
count = 0
new_word = ""
for r in word:
    if r == "r":
        count += 1
        if count == 2:
            new_word += "$"
    new_word += r
print(new_word)

task5:
letters = [ 'abc', 'xyz']
letters.reverse()
print(letters)

task6:
a = "abc"
a1 = a + "ing"
print(a1)

b = "string" 
b1 = b + "ly"
print(b1)

task7:
string = 'The lyrics is not that poor!'
new_string = string.replace("not that poor", "good")
print(new_string)

task8:
sentence = "I love Exercises in Python"
words = sentence.split()
longest_word = max(words, key=len) 
count_letters = len(longest_word)
print("The longest word is:", longest_word, "letter count: ", count_letters)

task9:
def swap_first_last(word):
    if len(word) > 1:
        return word[-1] + word[1:-1] + word[0]
    else:
        return word

word = "karl"
result = swap_first_last(word)
print("Original word:", word)
print("Word after swapping:", result)

task10:
from collections import Counter
w = "I am from Uzbekistan and I am 20 years old"
w_count = Counter(w.split()) 
print(w_count) 

task11:
q = input("your message: ") 
if q.lower():
    print(q.upper()) 

w = input("your message: ")
if w.upper():
    print(w.lower())

task12:
w = ["red, white, black, red, green, black"]
w.sort() 
print(w)

task13:
def wrap_word_with_html_tag(sentence, word, tag):
    wrapped_word = f"<{tag}>{word}</{tag}>"
    return sentence.replace(word, wrapped_word)
sentence = "Python, Python Tutorial"
word_to_wrap = "Python"
html_tag = "b" 
result = wrap_word_with_html_tag(sentence, word_to_wrap, html_tag)
print(result)

task14:
def insert_string_between (str1, str2, str_to_insert):
    return str1 + str_to_insert + str2
str1 = "karl"
str2 = "Abu"
string_to_insert = " Abdulaziz "
result = insert_string_between(str1, str2, string_to_insert)
print(result)

task15:
w = "Python"
two_letters = w[-2:]
print((two_letters) * 4) 

q = "Exercises"
two_letter = q[-2:]
print((two_letter)* 4) 

task16:
w = "Python"
three_letters = w[:3]
print(three_letters)

task17:
def reverse_string(w):
    if len(w) % 4 ==0:
        print(w[::-1]) 
    else:
        print(w) 
string = "karl"
result = reverse_string(string)
print(result)

task18:
def upper_case(w):
    if 1 in w[:4] is upper_case:
        return w.upper()
string = "PyThon"
res = upper_case(string)
print(res)

task19:
def sorted_word(w):
    return sorted(w) 
string = "fjsifjfiojsifj"
result = sorted_word(string)
print(result) 

task20:
w = "Abdulaziz Karl\n"
print(w.rstrip())

task1: 
w = 1
while w <= 10:
    print(w)
    if w == 10:
        break
w += 1
