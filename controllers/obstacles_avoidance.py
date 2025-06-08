#This code implements obstacles avoidance simulation of robot using Braitenberg-like in clustered static environment
#This code should be updated according to environment  
#Simulaton is performed on webots platform 
#For detailed and environmet, robot details checkouts report and videos attached

from controller import Robot
import math

def run_robot(robot):
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28

    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    prox_sensors = []
    for i in range(8):
        sensor = robot.getDevice(f'ps{i}')
        sensor.enable(timestep)
        prox_sensors.append(sensor)

    # Main loop
    while robot.step(timestep) != -1:
        sensor_values = [sensor.getValue() for sensor in prox_sensors]

        # Normalize sensor values (0 to 1)
        sensor_values = [min(val / 4096, 1.0) for val in sensor_values]

        # Obstacle avoidance weights (Braitenberg-like)
        braitenberg_weights = [
            [-0.5, -1.0],  # ps0
            [-0.3, -0.8],  # ps1
            [-0.1, -0.5],  # ps2
            [0.0, 0.0],    # ps3
            [0.0, 0.0],    # ps4
            [-0.5, -0.1],  # ps5
            [-0.8, -0.3],  # ps6
            [-1.0, -0.5],  # ps7
        ]

        # Initialize speeds with forward movement
        left_speed = 0.5 * max_speed
        right_speed = 0.5 * max_speed

        # Add obstacle avoidance influence
        for i in range(8):
            left_speed += braitenberg_weights[i][0] * sensor_values[i] * max_speed
            right_speed += braitenberg_weights[i][1] * sensor_values[i] * max_speed

        # Clamp speeds
        left_speed = max(-max_speed, min(max_speed, left_speed))
        right_speed = max(-max_speed, min(max_speed, right_speed))

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if _name_ == "_main_":
    my_robot = Robot()
    run_robot(my_robot)