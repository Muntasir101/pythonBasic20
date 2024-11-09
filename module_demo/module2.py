import module1

module1.summation(10, 20)
module1.summation(20, 40)

from module1 import summation, subtract

subtract(20, 10)

from module1 import *

summation(20, 30)

import module3 as m3

m3.summation(20, 30)
m3.multiplication(4, 5)
m3.multiplication(10, 20)
m3.celsius_to_fahrenheit(40)