# objective is to access payment wala function from here only
# the file is untracket so it is showing error
# so if i want to track this, mujhe saare ke saare path collapse krne padenge
import os , sys
from os.path import dirname , join , abspath

# abspath is now helping in tracking
sys.path.insert(0, abspath(join(dirname(__file__) , "..")))

# dono jagah import karoge toh cirular loop mein fasjoge toh jab yha se import kroge toh vha comment krdena we are commenting 1 and 2
# 1. from payment import payment_details

def course():
    print("this is my course details")

# 2. payment_details.payment()