# 01.

import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, "wb") as fh:
        pickle.dump(contacts, fh)    

def read_contacts_from_file(filename):
    with open(filename, "rb") as fh:
        unpacked = pickle.load(fh)
    return unpacked
	
	
# 02.

import json


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w') as fh:
        json.dump({'contacts': contacts}, fh)    

def read_contacts_from_file(filename):
    with open(filename, 'r') as fh:
        unpacked = json.load(fh)    
    return unpacked['contacts']
	
	
# 03.

import csv


def write_contacts_to_file(filename, contacts):
    with open(filename, 'w', newline='') as csvfile:
        columns = contacts[0].keys()
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=columns)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

def read_contacts_from_file(filename):
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        contacts = [contact for contact in reader]
        for contact in contacts:
            contact['favorite'] = contact['favorite'] == 'True'
        return contacts
		
		
# 04.

import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts

    def save_to_file(self):
        with open(self.filename, 'wb') as fh:
            pickle.dump(self, fh)

    def read_from_file(self):
        with open(self.filename, 'rb') as fh:
            unpacked = pickle.load(fh)
        return unpacked
		
		
# 05.

