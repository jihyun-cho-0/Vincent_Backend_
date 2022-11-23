from django.test import TestCase
import os
# Create your tests here.

# print(os.getcwd())
# print(os.path.abspath('.'))

absolute_path = os.path.dirname(__file__)
temp = '/media/temp/11_fg7op5y.png'
temp2 = temp.split('/')[-1]
absolut_temp = os.path.abspath('media/temp')
print(absolut_temp)

# full_path = os.path.join(absolute_path, temp2)
# print(full_path)