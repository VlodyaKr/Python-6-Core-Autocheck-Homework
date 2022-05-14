# 01.

from datetime import datetime


def get_days_from_today(date):
    return (datetime.now() - datetime.strptime(date, '%Y-%m-%d')).days
	
	
# 02.

from datetime import date


def get_days_in_month(month, year):
    day1 = date(year=year, month=month, day=1)
    day2 = date(year=year + 1, month=1, day=1) if month == 12 else date(year=year, month=month + 1, day=1)
    return (day2 - day1).days
	
	
# 03.

from datetime import datetime


def get_str_date(date: str):
    ddate = datetime.strptime(date[:-1], '%Y-%m-%d %H:%M:%S.%f')
    return ddate.strftime('%A %d %B %Y')
	
	
# 04.

from random import randrange


def get_numbers_ticket(min, max, quantity):
    if not (min < quantity < max) or (min < 1 or max > 1000) or (quantity > max - min):
        return []
    result = []
    while len(result) < quantity:
        bowl = randrange(min, max + 1)
        if bowl in result:
            continue
        result.append(bowl)
    return sorted(result)
	
	
# 05.

import random


def get_random_winners(quantity, participants):
    if quantity > len(participants):
        return []
    members = [i for i in participants.keys()]
    random.shuffle(members)
    return random.sample(members, k=quantity)
	
	
# 06.

from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    decimal_list = [Decimal(i) for i in number_list]
    return sum(decimal_list) / len(decimal_list)
	
	
# 07.

import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    if not cats:
        return []
    if type(cats[0]) == Cat:
        return [{'nickname': cat.nickname, 'age': cat.age, 'owner': cat.owner} for cat in cats]
    else:
        return [Cat(cat['nickname'], cat['age'], cat['owner']) for cat in cats]
		
		
# 08.

from collections import Counter


def get_count_visits_from_ip(ips):
    return Counter(ips)

def get_frequent_visit_from_ip(ips):
    return Counter(ips).most_common(1)[0]
	
	
# 09.

from collections import deque

MAX_LEN = 10

lifo = deque(maxlen=MAX_LEN)


def push(element):
    lifo.appendleft(element)

def pop():
    return lifo.popleft()
	
	
# 10.


from collections import deque

MAX_LEN = 10

fifo = deque(maxlen=MAX_LEN)


def push(element):
    fifo.append(element)

def pop():
    return fifo.popleft()