#This code implements wall zigzag navigation simulation of robot in clustered static environment
#Simulaton is performed on webots platform 
#For detailed and environmet, robot details checkouts report and videos attached

from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())
max_speed = 6.28
SPEED = 3.0
TURN_SPEED = 2.0
zigzag_dir = 1

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

prox_sensors = [robot.getDevice(f'ps{i}') for i in range(8)]
for sensor in prox_sensors:
    sensor.enable(timestep)

def read_front_obstacle():
    return any(prox_sensors[i].getValue() > 80 for i in [0, 1, 6, 7])

while robot.step(timestep) != -1:
    if read_front_obstacle():
        left_motor.setVelocity(TURN_SPEED)
        right_motor.setVelocity(-TURN_SPEED)
        zigzag_dir *= -1
    else:
        if zigzag_dir == 1:
            left_motor.setVelocity(SPEED)
            right_motor.setVelocity(SPEED * 0.8)
        else:
            left_motor.setVelocity(SPEED * 0.8)
            right_motor.setVelocity(SPEED)
