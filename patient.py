from procedure import *

class Patient:

    def __init__(self, first, middle, last, address, city, state, zip, number, name_emer, num_emer):
        self.first = first
        self.middle = middle
        self.last = last
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.number = number
        self.name_emer = name_emer
        self.num_emer = num_emer

    def set_first(self, first):
        self.first = first

    def set_middle(self, middle):
        self.middle = middle

    def set_last(self, last):
        self.last = last
    
    def set_address(self, address):
        self.address = address

    def set_city(self,city):
        self.city = city

    def set_state(self, state):
        self.state = state

    def set_zip(self, zip):
        self.zip = zip
    
    def set_number(self, number):
        self.number = number

    def set_name_emer(self, name_emer):
        self.name_emer = name_emer

    def set_num_emer(self, num_emer):
        self.num_emer = num_emer


    def get_first(self):
        return self.first

    def get_middle(self):
        return self.middle

    def get_last(self):
        return self.last
    
    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip(self):
        return self.zip
    
    def get_number(self):
        return self.number

    def get_name_emer(self):
        return self.name_emer 

    def get_num_emer(self):
        return self.num_emer

