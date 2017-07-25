from martypy import Marty
from time import sleep
from four_legged_walk import four_legged_walk

#Edit these to put your Martys IP instead
head = Marty('socket://192.168.0.33')
tail = Marty('socket://192.168.0.34')

head.enable_motors()
tail.enable_motors()

#Set all motors to default zero position
head.hello()
tail.hello()

# Pause until user presses Enter
raw_input('Press Enter...') #Python 2
# input('Press Enter...') #Python 3


for i in range(5):  #Five movements
    four_legged_walk(head, tail, 0.3)
