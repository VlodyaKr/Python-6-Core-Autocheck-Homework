# 1.

is_next = None
num = int(input("Введите количество баллов: "))
if num >= 83:
    is_next = True
else:
    is_next = False
	

# 2.

is_active = bool(input("Пользователь активен? "))
is_admin = bool(input("Пользователь администратор? "))
is_permission = bool(input("Пользователь имеет доступ? "))

access = is_admin or is_active and is_permission


# 3.

work_experience = int(input("Введите свой стаж полных лет: "))

if work_experience <= 1:
    developer_type = "Junior"
elif work_experience <= 5:
    developer_type = "Middle"
else:
    developer_type = "Senior"
	
	
# 4.

num = int(input("Введите число: "))

if num > 0:
    if num % 2:
        result = "Положительное нечетное число"
    else:
        result = "Положительное четное число"
elif num < 0:
    result = "Отрицательное число"
else:
    result = "Это ноль"
	
	
# 5.

import math

a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
c = int(input("Введите коэффициент c: "))

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
elif D == 0:
    x1 = -b / (2 * a)
else:
    print('Рівняння не має коренів!')
	
	
# 6.

num = int(input("Введите целое число: "))

is_even = False if num % 2 else True


# 7.

num = int(input("Введите целое число (0 до 100): "))
sum = 0

while num > 0:
    sum += num
    num -= 1
print(sum)


# 8.

message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for ch in message:
    if ch == search:
        result += 1  
		
		
# 9.

first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))

nod = first if first < second else second
while first % nod or second % nod:
    nod -= 1 
	
	
# 10.

num = int(input("Введите целое число (0 для выхода): "))
sum = 0
while num > 0:
    for i in range(num + 1):
        sum += i
    num = int(input("Введите целое число (0 для выхода): "))
	
	
# 11.

sum = 0
while True:
    num = int(input("Введите целое число (0 для выхода): "))
    if num == 0:
        break
    for i in range(num + 1):
        sum = sum + i
		
		
# 12.

sum = 0
while True:
    num = int(input("Введите целое число (0 для выхода): "))
    if num == 0:
        break
    for i in range(num + 1):
        if not i % 2:            
            sum = sum + i
			
			
# 13.

message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""

for ch in message:
    if ord('A') <= ord(ch) <= ord('Z'):
        encoded_message += chr(ord('A') + (ord(ch) - ord('A') + offset) % 26)
    elif ord('a') <= ord(ch) <= ord('z'):
        encoded_message += chr(ord('a') + (ord(ch) - ord('a') + offset) % 26)
    else:
        encoded_message += ch

print(encoded_message)   


# 14.

pool = 1000
quantity = int(input("Введите количество рассылок: "))
try:
    chunk = pool // quantity
except ZeroDivisionError:
    print('Выполнено деление на ноль!')
	
	
# 15.

result = None
operand = None
operator = True
wait_for_number = True

while True:
    if wait_for_number:
        operand = input('Введіть операнд: ')
        try:
            operand = float(operand)
        except ValueError:
            print('Ви ввели не число! Повторіть введення операнду: ')
            continue
        else:
            if result == None:
                result = operand
            else:
                if operator == '+':
                    result += operand
                elif operator == '-':
                    result -= operand
                elif operator == '*':
                    result *= operand
                elif operator == '/':
                    try:
                        result /= operand
                    except ZeroDivisionError:
                        print('Ділити на 0 не можна. Повторіть введення операнду: ')
                        continue
            wait_for_number = False
    else:
        operator = input('Введіть оператор: ')
        if not operator in '+-*/=':
            print('Ви ввели не знак! Повторіть введення оператора: ')
            continue
        if operator == '=':
            print('Результат:', result)
            break
        wait_for_number = True