# 01.

from setuptools import setup


def do_setup(args_dict):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          url=args_dict['url'],
          license=args_dict['license'],
          packages=args_dict['packages'],
         )
		 
		
# 02.

from setuptools import setup


def do_setup(args_dict, requires):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires,
         )
		 
		 
# 03.

from setuptools import setup


def do_setup(args_dict, requires, entry_points):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires,
          entry_points=entry_points,
          )
		  
		  
# 04.

def is_integer(s: str) -> bool:
    s = s.strip()
    if len(s) == 0:
        return False
    if s[0] in ('-', '+'):
        s = s[1:]
    return True if s.isdigit() else False
	
	
# 05.

def capital_text(s: str) -> str:
    lst = s.split()
    for i in range(len(lst)):
        if i == 0 or lst[i - 1][-1] in '.!?':
            lst[i] = lst[i][0].upper() + lst[i][1:]
    return ' '.join(lst)
	
	
# 06.

def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse:
        riddle = riddle[::-1]
    pos = riddle.find(start_letter, 0, len(riddle) - word_length)
    return '' if pos == -1 else riddle[pos:pos+word_length]
	
	
# 07.

def data_preparation(list_data):
    result = []
    for sub_lst in list_data:
        if len(sub_lst) > 2:
            sub_lst.remove(min(sub_lst))
            sub_lst.remove(max(sub_lst))
        result.extend(sub_lst)
    return sorted(result, reverse=True)
	
	
# 08.

import re

def token_parser(s):
    return re.findall(r'\d+|[\(\)+\-*/]', s)
	
	
# 09.

def all_sub_lists(data):
    result = [[]]
    for n in range(len(data)):
        for i in range(len(data) - n):
            result.append(data[i:i+n+1])
    return result
	
	
# 10.

def make_request(keys, values):
    if len(keys) != len(values):
        return {}
    return dict(zip(keys, values))
	
	
# 11.

def sequence_buttons(string):
    BUT_SYM = [' ', '.,?!:', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    TRANS = {}
    for i in range(10):
        for j in range(len(BUT_SYM[i])):
            TRANS[ord(BUT_SYM[i][j])] = str(i) * (j + 1)
    return string.upper().translate(TRANS)
	
	
# 12.

def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as fh:
        fh.write(additional_info)
    with open(path, 'r') as fh:
        fh.seek(start_pos)
        result = fh.read(count_chars)
    return result
	
	
# 13.

def get_employees_by_profession(path, profession):
    with open(path, 'r') as fh:
        workers = fh.readlines()
    result = []
    for worker in workers:
        man = worker.strip().split()
        if man[1] == profession:
            result.append(man[0])
    return ' '.join(result)
	
	
# 14.

def to_indexed(start_file, end_file):
    with open(start_file, 'r') as sf, open(end_file, 'w') as ef:
        counter = 0
        for line in sf:
            ef.write(str(counter) + ': ' + line)
            counter += 1
			
			
# 15.

def flatten(data):
    result = []
    for elem in data:      
        if type(elem) == list:
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result
	
	
# 16.

def decode(data):
    if len(data) == 0:
        return []
    elif len(data) == 1:
        return [data[0]]
    elif len(data) == 2:
        return [data[0]] * data[1]
    else:
        return [data[0]] * data[1] + decode(data[2:])
		
		
# 17.

def encode(data):
    result = []
    if len(data) == 0:
        return result
    last, counter = data[0], 0
    for i in range(len(data)):
        if data[i] == last:
            counter += 1
        else:
            result.extend([last, counter])
            result.extend(encode(data[i:]))
            break
    else:
        result.extend([last, counter])
    return result