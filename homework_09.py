# 01.

def get_student_grade(option):
    if option == 'grade':
        return get_grade
    elif option == 'description':
        return get_description
		
		
# 02.

DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    def new_discount():
        if 'discount' not in customer:
            customer['discount'] = DEFAULT_DISCOUNT
        return (1 - customer['discount']) * price
    return new_discount()
	
	
# 03.

def caching_fibonacci():
    cache = {0: 0, 1: 1}
    def fibonacci(n):
        if n in cache:
            result = cache[n]
        else:
            result = cache.get(n - 1, fibonacci(n - 1)) + cache.get(n - 2, fibonacci(n - 2))
            cache[n] = result
        return result

    return fibonacci
	
	
# 04.

def discount_price(discount):
    def price_calculation(price):
        return (1 - discount) * price
        
    return price_calculation  
	
	
# 05.

def format_phone_number(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if len(result) == 12:
            return '+' + result
        else:
            return '+38' + result
        
    return wrapper


@format_phone_number
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
	
	
# 06.

import re


def generator_numbers(string=""):
    str_to_lst = re.split(r'\W+', string)
    for word in str_to_lst:
        if word.isdigit():
            yield int(word)


def sum_profit(string):
    result = 0
    for num in generator_numbers(string):
        result += num
    return result
	
	
# 07.

def normal_name(list_name):
    return list(map(str.title, list_name))
	
	
# 08.

def get_emails(list_contacts):
    return list(map(lambda contact: contact['email'], list_contacts))
	
	
# 09.

def positive_values(list_payment):
    return list(filter(lambda sum: sum >0, list_payment))
	
	
# 10.

