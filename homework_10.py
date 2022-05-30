# 01.

class Animal:    
    pass
  
  
animal = Animal()


# 02.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


animal = Animal('dog', 10)


# 03.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight    


animal = Animal("Simon", 10)
animal.change_weight(12)


# 04.

class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        Animal.color = color


first_animal = Animal("Simon", 10)
second_animal = Animal("Boris", 12)
first_animal.change_color("red")


# 05.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


cat = Cat("Simon", 10)    
        

# 06.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Dog(Animal):
    def say(self):
        return "Woof"

    def __init__(self, nickname, weight, breed):
        super().__init__(nickname, weight)
        self.breed = breed      

    
dog = Dog("Barbos", 23, "labrador")        


# 07.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        return {'name': self.name, 'age': self.age, 'address': self.address}

class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()
		
		
# 08.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def info(self):        
        return f"{self.nickname}-{self.weight}"

class DogCat(Dog, Cat):
    def info(self):        
        return f"{self.nickname}-{self.weight}"


# 09.

from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        result = []
        for key in self.data:
            if self.data[key] == value:
                result.append(key)
        return result
		
		
# 10.

from collections import UserList

class AmountPaymentList(UserList):
    def amount_payment(self):
        return sum([value for value in self.data if value > 0])
		
		
# 11.

from collections import UserString


class NumberString(UserString):
    def number_count(self):
        return len([value for value in self.data if value.isdigit()])      
		
		
# 12.

class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    if not employee_id.startswith('01'):
        raise IDException
    id_list.append(employee_id)
    return id_list   
	
	
# 13.

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return "Meow"
      
    def change_weight(self, weight):
        self.weight = weight


# 14.

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        contact = {
            'id': Contacts.current_id,
            'name': name,
            'phone': phone,
            'email': email,
            'favorite': favorite
        }
        Contacts.current_id += 1
        self.contacts.append(contact)
        return contact
		
		
# 15.

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact["id"] == id:
                return contact
        return None
		
		
# 16.

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        self.contacts = list(filter(lambda contact: contact.get("id") != id, self.contacts))