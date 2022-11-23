from django.test import TestCase
import os
# Create your tests here.

# print(os.getcwd())
# print(os.path.abspath('.'))

absolute_path = os.path.dirname(__file__)
absolute_temp = os.path.dirname('main')
temp = '/media/temp/11_fg7op5y.png'
temp2 = temp.split('/')[-1]

print(os.path.abspath(''))
# full_path = os.path.join(absolute_path, temp2)
# print(full_path)