from collections import Counter
from math import log
f = open("C:/Users/hp/PycharmProjects/pythonProject2/venv/input.txt" , "r")
my_str = f.read()
counter = Counter(my_str)
print(counter)
num_of_chars = len(my_str)
num_of_bits=num_of_chars*8
print("1.Number of bits used to encode the paragraph if ASCII code is used:",num_of_bits)

keys_dict = {}

ind = 0
inc = 1
while True:
    if not (len(my_str) >= ind+inc):
        break
    sub_str = my_str[ind:ind + inc]
   # print sub_str,ind,inc
    if sub_str in keys_dict:
        inc += 1
    else:
        keys_dict[sub_str] = 0
        ind += inc
        inc = 1
        # print 'Adding %s' %sub_str

list_a=list(keys_dict)
#print(list_a)
number_of_elements = len(list_a)
print("Number of codewords resulted by Limpel-Ziv:",number_of_elements)
bits = number_of_elements.bit_length()
print("Number of bits needed to represnt the Head:",bits)
Lempel_Ziv= (bits+8)*number_of_elements
print("2.The number of bits used to encode the paragraph if the Lempel-Ziv code is used:",Lempel_Ziv)

counter = Counter(my_str)
#print(counter)
List_b=[]
for s in counter.values():
    List_b.append(s / num_of_chars)
List_c=[]
for i in List_b:
    List_c.append(i*bits)

sum=0
for i in List_c:
    sum = sum + i
print("3.The average number of bits/symbol of the encoded paragraph:",sum)

ent=[]
for i in List_b:
    ent.append(-i * log(i, 2))

sum1=0
for i in ent:
    sum1 = sum1 + i
print("4.The entropy of the source alphabet:",sum1)
Efficiency= (Lempel_Ziv/num_of_bits)*100
print("5.The percentage of compression accomplished by using the Lempel-Ziv encoding as compared to ASCII code:",Efficiency,"%")
