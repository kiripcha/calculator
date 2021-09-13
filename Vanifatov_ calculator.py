#!/usr/bin/env python
# coding: utf-8

# In[52]:


#Ванифатов Кирилл ПИ20-5 
#Задание по практикуму. Калькулятор строчных выражений
from collections import deque
import math
numbers = {'один':1,'два':2,'три':3,'четыре':4,'пять':5,'шесть':6,'семь':7,'восемь':8,'девять':9,'десять':10,
       'одиннадцать':11,'двенадцать':12,'тринадцать':13,'четырнадцать':14,'пятнадцать':15,'шетьнадцать':16,
       'семьнадцать':17,'восемьнадцать':18,'девятнадцать':19,'двадцать':20,'тридцать':30,'сорок':40,
       'пятьдесят':50,'шестьдесят':60,'семьдесят':70,'восемьдесят':80,'девяносто':90,'сто':100,'двести':200,
       'триста':300,'четыреста':400,'пятьсот':500,'шестьсот':600,'семьсот':700,'восемьсот':800,'девятьсот':900,
       'тысяча':1000,'две тысячи':2000,'три тысячи':3000,'четыре тысячи':4000,'пять тысяч':5000,'шесть тысяч':6000,
       'семь тысяч':7000,'восемь тысяч':8000,'девять тысяч':9000}
priority = {'минус':1,'плюс':1,'умножить':2,'делить':2,'целочисленное':2,'остаток':2,'степень':3,
            'скобка_открывается':-1,'скобка_закрывается':0}
OPERATIONS = {'плюс':lambda x,y: x + y, 'минус':lambda x,y: x - y, 'умножить':lambda x,y: x * y, 'делить':lambda x,y: x / y,
             'степень':lambda x,y: x ** y}

#input
string = input().lower().split()
for i in range(len(string)-1): #складываем одно число по частям. 'двадцать','два','плюс','пять'  =>  22,'плюс',5
    if string[i] in numbers.keys():
        string[i] = numbers.get(string[i])
        if i < (len(string)-1):
            if string[i+1] in numbers.keys():
                string[i] = string[i] + numbers.get(string[i+1])
                del string[i+1]
    elif string[i] in priority.keys():
        continue
    else:
        print('введены неправильные данные') #проверка на корректность данных, если они есть в словаре, то пропускаем
        
if string[-1] in numbers.keys(): #проверяем последний элемент в строчке
    string[-1] = numbers.get(string[-1])

#minus
step = 0       
for i in string: #проверяем элемент и идущий следом, если оба в словаре операций, а второй минус, то домножаем следующую цифру на -1 
    if string[step] in priority.keys() and (string[step+1] == 'минус'):
        string[step+2] *= -1 
        del string[step+1]
    elif step == 0 and string[step] == 'минус': #если первый элемент минус
        string[step+1] *= -1 
        del string[step]
    step += 1
            
#work algorithm
def perfom_operation(): #задаем функцию, выполняющую операцию, если ее приоритетность выше, чем у предыдущей операции в стеке
    second = numbers_stack.pop() #она запоминает операцию и выполняет ее с последними двумя числами в стеке, преобразуя их в одно
    first = numbers_stack.pop()
    operation = operation_stack.pop()
    final = OPERATIONS[operation](first,second)
    numbers_stack.append(final)
operation_stack = deque()
numbers_stack = deque()
    
for i in string:
    if type(i) is int: #определям число или операция
        numbers_stack.append(i) #добавляем цифры в стек с числами 
    else:
        if i == 'скобка_закрывается': #если находится скобка_закрвыается, то выполняем операции до скобка_открвается
            while operation_stack[-1] != 'скобка_открывается':
                perfom_operation()
            del operation_stack[-1]
            continue
        elif i == 'скобка_открывается':
            operation_stack.append(i) #если находит скобка_открвыается, то заносит ее в стек операций
            continue
        while len(operation_stack) and priority[i] < priority[operation_stack[-1]] > 0: #сравниваем приоритетность операций
            perfom_operation() #если приоритет позволяет, то выполняем операцию
        operation_stack.append(i)
while len(operation_stack) > 0:    
    perfom_operation()
           
result = int(numbers_stack[0]) #берем первый элемент списка и дополнительно делаем его типа инт
output = []

#output
if result < 0:
    result *= -1
    output.append('минус')
if result >= 1000: #сравниваем значение результата и прикрепляем к строке соответсвующий значению ключ
    output.append(list(numbers.keys())[list(numbers.values()).index(((result // 1000)*1000))])
    result = result % 1000
if result >= 100:
    output.append((list(numbers.keys())[list(numbers.values()).index(((result // 100)*100))]))
    result = result % 100
if result >=20:
    output.append((list(numbers.keys())[list(numbers.values()).index(((result // 10)*10))]))
    result = result % 10
elif result >= 10 and result <= 19:
    output.append((list(numbers.keys())[list(numbers.values()).index(result)]))
    result = -1
if result > 0 and len(output)>0:
    output.append((list(numbers.keys())[list(numbers.values()).index(result)]))
    result = 0
elif result >= 0 and len(output) == 0:
    output.append('ноль')

print(output)

# один плюс два минус три умножить двадцать пять делить пять степень два
# два умножить три минус скобка_открывается пять плюс шесть скобка_закрывается умножить один
# минус один минус два

# сложность(8) + основная часть(3)
# 3 произвольное количество операций 3 балла
# 4 приоритетность и добавление скобок 3 балла
# 5 отрицательные числа 1 балл
# 8 добавил операцию возведения в степень 1 балл

