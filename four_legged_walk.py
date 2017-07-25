from time import sleep

def four_legged_walk(head, tail, step_duration = 0.5):

    '''
    Simple movement sequence for four legged Marty.

    Args:
        head: instance of Marty class
        tail: instance of Marty class
        step_duration: duration taken to excute a step
    '''

    #Move two alternating legs forward
    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, -40), (3, 0), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, 0), (3, -40), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)    #Wait for motion to be excuted

    #Move other two legs backward
    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, -40), (3, -20), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, 20), (3, -40), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)    #Wait for motion to be excuted

    #Straighten first two legs
    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, 0), (3, -20), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, 20), (3, 0), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)    #Wait for motion to be excuted

    #Straighten all legs
    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, 0), (3, 0), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, 0), (3, 0), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)    #Wait for motion to be excuted

    #Move two alternating legs forward
    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, 0), (3, 40), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, -40), (3, 0), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)    #Wait for motion to be excuted

    #Move other two legs backward
    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, 20), (3, 40), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, -40), (3, 20), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)    #Wait for motion to be excuted

    #Straighten first two legs
    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, 20), (3, 0), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, 0), (3, 20), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)    #Wait for motion to be excuted

    #Straighten all legs
    temp_sequence_1 = head.keyframe(step_duration, 4, [(6, 0), (3, 0), (4, 0), (1, 0)])
    head.ros_processed_command(110, *temp_sequence_1)
    temp_sequence_2 = tail.keyframe(step_duration, 4, [(0, 0), (3, 0), (4, 0), (1, 0)])
    tail.ros_processed_command(110, *temp_sequence_2)
    sleep(step_duration)    #Wait for motion to be excuted
