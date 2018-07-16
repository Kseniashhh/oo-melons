"""Classes for melon orders."""

from random import randint
from datetime import datetime
import time

class AbstractMelonOrder():

    def __init__(self, species, qty,country_code = None, is_christmas = False):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code
        self.is_christmas = is_christmas


    def get_total(self):
        """Calculate price, including tax."""

        #base_price = 5
        total = (1 + self.tax) * self.qty * self.get_base_price()

        if self.is_christmas == True:
            total = (total*1.5)
        

        if self.order_type == 'international' and self.qty < 10:
            total += 3

        return total


    def get_base_price(self):
        base_price = randint(5,10) 

        current_stamp = datetime.now().timestamp()
        readable_cur_stamp = time.ctime(current_stamp)

        time_lst = readable_cur_stamp.split(' ')
        hour_lst = time_lst[3].split(':')

        if time_lst[0] == "Sat" or time_lst[0] == "Sun":
            return base_price
        elif int(hour_lst[0]) >= 8 and int(hour_lst[0]) < 11:
            if int(hour_lst[1]) >= '00' and int(hour_lst[1]) <= 59:
                base_price +=4
            return base_price
        else:
            return base_price



    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code





class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


   

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17


class GovernmentMelonOrder(AbstractMelonOrder):
    """ A government order with 0 tax rate """
    order_type = "domestic"
    tax = 0
    passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
            
        