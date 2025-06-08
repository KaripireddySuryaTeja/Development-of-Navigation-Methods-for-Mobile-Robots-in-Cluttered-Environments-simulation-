#This code implements wall snake navigation simulation of robot in clustered static environment
#Simulaton is performed on webots platform 
#For detailed and environmet, robot details checkouts report and videos attached

from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())
max_speed = 6.28
SPEED = 3.0
snake_toggle = False

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
        snake_toggle = not snake_toggle
        if snake_toggle:
            left_motor.setVelocity(SPEED)
            right_motor.setVelocity(-SPEED)
        else:
            left_motor.setVelocity(-SPEED)
            right_motor.setVelocity(SPEED)
    else:
        left_motor.setVelocity(SPEED)
        right_motor.setVelocity(SPEED)
