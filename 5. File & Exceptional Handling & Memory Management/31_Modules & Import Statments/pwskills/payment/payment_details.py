# calling course details here
import os , sys
from os.path import dirname , join , abspath

# abspath is now helping in tracking
sys.path.insert(0, abspath(join(dirname(__file__) , "..")))

from course import course_details

def payment():
    print("this is my payment details")

course_details.course()