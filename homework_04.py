# 01.

def amount_payment(payment):
    sum = 0
    for pay in payment:
      if pay > 0:
        sum += pay
    return sum
	
	
# 02.

def prepare_data(data):
    data.remove(min(data))
    data.remove(max(data))
    return sorted(data)
	
	
# 03.

def format_ingredients(items):
    if len(items) == 0:
        return ''
    if len(items) == 1:
        return items[0]
    return ', '.join(items[:-1]) + ' и ' + items[-1]
	
	
# 04.

def get_grade(key):
    grades = {'F': 1, 'FX': 2, 'E': 3, 'D': 3, 'C': 4, 'B': 5, 'A': 5}    
    return grades.get(key, None)    

def get_description(key):
    descriptions = {'F': 'неудовлетворительно', 'FX': 'неудовлетворительно', 'E': 'достаточно', 'D': 'удовлетворительно', 'C': 'хорошо', 'B': 'очень хорошо', 'A': 'отлично'}
    return descriptions.get(key, None)	
	
	
# 05.

def lookup_key(data, value):
    result = []
    for key in data:
        if data[key] == value:
            result.append(key)
    return result
	
	
# 06.

def split_list(grade):
    if not len(grade):
        return ([], [])
    grade1, grade2 = [], []
    average = sum(grade) / len(grade)
    for gr in grade:
        if gr > average:
            grade2.append(gr)
        else:
            grade1.append(gr)
    return (grade1, grade2)
	
	
# 07.

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    if len(coordinates) < 2:
        return 0
    distance = 0
    for i in range(len(coordinates) - 1):
        if coordinates[i] > coordinates[i + 1]:
            distance += points[(coordinates[i + 1], coordinates[i])]
        else:
            distance += points[(coordinates[i], coordinates[i + 1])]
    return distance
	
	
# 08.

def game(terra, power):  
    for lst in terra:
        for pwr in lst:
            if power >= pwr:
                power += pwr
            else:
                break
    return power
	
	
# 09.

def is_valid_pin_codes(pin_codes):
    if len(pin_codes) > len(set(pin_codes)) or len(pin_codes) == 0:
        return False
    for code in pin_codes:
        if type(code) != str:
            return False
        if len(code) != 4:
            return False
        if not code.isdigit():        
            return False
    return True 
	
	
# 10.

from random import randint


def get_random_password():
    result = ''
    for _ in range(8):
        result += chr(randint(40, 126))
    return result
	
	
# 11.

def is_valid_password(password):
    if len(password) != 8:
        return False
    valid = [False, False, False]
    for ch in password:
        if 'A' <= ch <= 'Z':
            valid[0] = True
        if 'a' <= ch <= 'z':
            valid[1] = True
        if '0' <= ch <= '9':
            valid[2] = True
    if sum(valid) == 3:
        return True
    else:
        return False
		
		
# 12.

from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():
    for _ in range(100):
        password = get_random_password()
        if is_valid_password(password):
            return password
    return None
	
	
# 13.

def parse_folder(path):
    files = []
    folders = []
    for el in path.iterdir():
        if el.is_file():
            files.append(el.name)
        elif el.is_dir():
            folders.append(el.name)
    return files, folders
	
	
# 14.

import sys


def parse_args():
    return ' '.join(sys.argv[1:])