# 01.

def real_len(text):
    return len(text.translate({ord('\n'): '', ord('\f'): '', ord('\r'): '', ord('\t'): '', ord('\v'): ''}))
	
	
# 02.

articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    result = []
    for blog in articles_dict:
        if blog['title'].count(key) + blog['author'].count(key):
            result.append(blog)
        elif blog['title'].upper().count(key.upper()) + blog['author'].upper().count(key.upper()) and not letter_case:
            result.append(blog)
    return result
	
	
# 03.

def sanitize_phone_number(phone):
    return phone.translate({ord(' '): '', ord('('): '', ord('-'): '', ord(')'): '', ord('+'): ''})
	
	
# 04.

def is_check_name(fullname, first_name):
    return fullname.startswith(first_name)
	
	
# 05.

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    result = {'UA': [], 'JP': [], 'TW': [], 'SG': []}
    for phone in list_phones:
        phone = sanitize_phone_number(phone)
        if phone.startswith('380'):
            result['UA'].append(phone)
        elif phone.startswith('81'):
            result['JP'].append(phone)
        elif phone.startswith('886'):
            result['TW'].append(phone)
        elif phone.startswith('65'):
            result['SG'].append(phone)
        else:
            result['UA'].append(phone)
    return result
	
	
# 06.

def is_spam_words(text, spam_words, space_around=False):
    for spam in spam_words:
        if spam.lower() in text.lower().strip(' .').split():
            return True
        if spam.lower() in text and not space_around:
            return True
    return False
	
	
# 07.

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def translate(name):
    return name.translate(TRANS)
	
	
# 08.

grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    format_string = '{:>4}|{:<10}|{:^5}|{:^5}'
    counter, result = 0, []
    for stud in students:
        counter += 1
        result.append(format_string.format(counter, stud, students[stud], grades[students[stud]]))
    return result
	
	
# 09.

def formatted_numbers():
    text = ['|{:^10}|{:^10}|{:^10}|'.format('decimal', 'hex', 'binary')]
    format_string = '|{:<10}|{:^10}|{:>10}|'
    for el in range(16):
        text.append(format_string.format(el, hex(el).removeprefix('0x'), bin(el).removeprefix('0b')))
    return text
	
	
# 10.

import re


def find_word(text, word):
    result = re.search(word, text)
    print(result)
    if result:
        return {'result': True, 'first_index': result.start(0), 'last_index': result.end(0),
                'search_string': word, 'string': text}
    else:
        return {'result': False, 'first_index': None, 'last_index': None,
                'search_string': word, 'string': text}
				
				
# 11.

import re


def find_all_words(text, word):
    return re.findall(word, text, re.I)
	
	
# 12.

import re


def replace_spam_words(text, spam_words):
    for spam in spam_words:
        text = re.sub(spam, '*' * len(spam), text, 0, re.I)
    return text
	
	
# 13.

import re


def find_all_emails(text):
    result = re.findall(r'[a-zA-Z][\w\.]+@[a-zA-Z]+\.[a-zA-Z]{2,}', text)
    return result
	
	
# 14.

import re


def find_all_phones(text):
    result = re.findall(r'\+380\(\d{2}\)\d{3}-\d(?:\d-|-\d)\d{2}', text)
    return result
	
	
# 15.

import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r'https?://(?:(?:\w)+\.)+(?:\w)+', text)
    for match in iterator:
        result.append(match.group())
    return result