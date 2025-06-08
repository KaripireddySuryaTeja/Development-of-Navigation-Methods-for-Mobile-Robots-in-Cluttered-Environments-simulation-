#This code implements wall follower simulation of robot in clustered static environment
#Simulaton is performed on webots platform 
#For detailed and environmet, robot details checkouts report and videos attached

from controller import Robot

def run_robot(robot):
    # Time step of the current world
    timestep = int(robot.getBasicTimeStep())

    # Max speed of e-puck
    max_speed = 6.28

    # Initialize motors
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')

    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))

    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    # Initialize proximity sensors
    prox_sensors = []
    for i in range(8):
        sensor = robot.getDevice(f'ps{i}')
        sensor.enable(timestep)
        prox_sensors.append(sensor)

    # Main loop
    while robot.step(timestep) != -1:
        # Read sensor values
        sensor_values = [sensor.getValue() for sensor in prox_sensors]

        # Group sensors for better obstacle detection
        front_sensors = [sensor_values[0], sensor_values[7], sensor_values[6]]
        left_sensors = [sensor_values[5], sensor_values[4]]
        right_sensors = [sensor_values[2], sensor_values[1]]

        # Threshold for obstacle detection
        WALL_THRESHOLD = 80

        # Determine if there's a wall
        front_wall = any(val > WALL_THRESHOLD for val in front_sensors)
        left_wall = any(val > WALL_THRESHOLD for val in left_sensors)
        right_wall = any(val > WALL_THRESHOLD for val in right_sensors)

        # Set default speeds
        left_speed = max_speed
        right_speed = max_speed

        # Control logic
        if front_wall:
            # Obstacle ahead: turn right in place
            left_speed = max_speed
            right_speed = -max_speed
            print("Front blocked — turning right")
        elif not left_wall:
            # No wall on left: turn left to find wall
            left_speed = max_speed * 0.25
            right_speed = max_speed
            print("No wall on left — turning left")
        else:
            # Wall on the left: follow it by going straight
            left_speed = max_speed
            right_speed = max_speed
            print("Wall on left — moving forward")

        # Apply speeds to motors
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if _name_ == "_main_":
    my_robot = Robot()
    run_robot(my_robot)