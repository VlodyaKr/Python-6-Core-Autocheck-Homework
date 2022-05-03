# 01.

def total_salary(path):
    file = open(path, 'r', encoding='utf-8')
    result = 0.0
    while True:
        line = file.readline()
        if not line:
            break  
        result += float(line.split(',')[1])
    file.close()    
    return result
	
	
# 02.

def write_employees_to_file(employee_list, path):
    file = open(path, 'w')
    for department in employee_list:
        for worker in department:
            file.write(worker + '\n')
    file.close()
	
	
# 03.

def read_employees_from_file(path):
    file = open(path, 'r', encoding='utf-8')
    result = []
    while True:
        line = file.readline().strip()
        if not line:
            break  
        result.append(line)
    file.close()    
    return result    
	
	
# 04.

def add_employee_to_file(record, path):
    file = open(path, 'a')
    file.write(record + '\n')
    file.close()
	
	
# 05.

def get_cats_info(path):
    with open(path, 'r', encoding='utf-8') as file:
        result = []
        for line in file:
            result.append(dict(zip(['id', 'name', 'age'], line.strip().split(','))))
    return result
	
	
# 06.

def get_recipe(path, search_id):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            lst = line.strip().split(',')
            if search_id == lst[0]:
                return {'id' : lst[0],
                       'name': lst[1],
                       'ingredients': lst[2:]}
    return None
	
	
# 07.

import re

def sanitize_file(source, output):
    with open(source, 'r', encoding='utf-8') as sf, open(output, 'w') as of:
        of.write(re.sub(r'[\d]', '', sf.read()))
		
		
# 08.

def save_applicant_data(source, output):
    with open(output, 'w') as file:
        result = []
        for student in source:
            result.append(f'{student["name"]},{student["specialty"]},{student["math"]},{student["lang"]},{student["eng"]}\n')
        file.writelines(result)
		
		
# 09.

def is_equal_string(utf8_string, utf16_string):
    return utf8_string.decode() == utf16_string.decode('utf16')
	
	
# 10.

def save_credentials_users(path, users_info):
    with open(path, 'wb') as bfile:
        for key, value in users_info.items():
            bfile.write(f'{key}:{value}\n'.encode())
			
			
# 11.

def get_credentials_users(path):
    with open(path, 'rb') as bfile:
        return bfile.read().decode().split()
		
		
# 12.

import base64


def encode_data_to_base64(data):
    result = []    
    for pair in data:
        result.append(base64.b64encode(pair.encode("utf-8")).decode("utf-8"))
    return result


# 13.

import shutil


def create_backup(path, file_name, employee_residence):    
    with open(path + '/' + file_name, 'wb', encoding='utf-8') as bfile:
        for key, value in employee_residence.items():
            bfile.write(f'{key} {value}\n'.encode())
    return shutil.make_archive('backup_folder', 'zip', path)
	
	
# 14.

import shutil


def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(archive_path, path_to_unpack)