# 1.

def greeting():
    print('Hello world!')

greeting()


# 2.

def invite_to_event(username):
    return f'Уважаемый(ая) {username}, имеем честь пригласить вас на наше мероприятие'
	
	
# 3.

base_rate = 40
price_per_km = 10
total_trip = 0

def trip_price(path):
    global total_trip 
    total_trip += 1
    return base_rate + price_per_km * path 
	
	
# 4.

def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price * (1 - discount)
        return

    apply_discount()
    return price
	
	
# 5.

def get_fullname(first_name, last_name, middle_name=''):
    if middle_name:
        return f'{first_name} {middle_name} {last_name}'
    else:
        return f'{first_name} {last_name}'
		
		
# 6.

def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        return ' ' * ((length - len(string)) // 2) + string  
		
		
# 7.

def first(size, *args):
    return size + len(args)

def second(size, **kwargs):
    return size + len(kwargs)
	
	
# 8.

def cost_delivery(quantity, *_, discount=0):
    return (5 + (quantity - 1) * 2) * (1 - discount) 
	
	
# 9.

def cost_delivery(quantity, *_, discount=0):
    '''    
    Функция возвращает общую сумму доставки.

    Первый параметр quantity; количество товаров в заказе.
    Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0.
    '''
    
    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result
	
	
# 10.

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)    
        
def number_of_groups(n, k):
    return factorial(n) // (factorial(n-k) * factorial(k))
	
	
# 11.

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)