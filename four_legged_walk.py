from martypy import Marty
from time import sleep

head = Marty('socket://192.168.0.33')
tail = Marty('socket://192.168.0.34')

head.enable_motors()
tail.enable_motors()

head.hello()
tail.hello()

raw_input('Press Enter...')

def my_walk(step_duration = 0.5):

    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, -40), (3, 0), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, 0), (3, -40), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)

    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, -40), (3, -20), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, 20), (3, -40), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)

    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, 0), (3, -20), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, 20), (3, 0), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)

    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, 0), (3, 0), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, 0), (3, 0), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)

    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, 0), (3, 40), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, -40), (3, 0), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)

    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, 20), (3, 40), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, -40), (3, 20), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)

    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, 20), (3, 0), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, 0), (3, 20), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)

    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, 0), (3, 0), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, 0), (3, 0), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)

for i in range(5):
    my_walk(0.3)
