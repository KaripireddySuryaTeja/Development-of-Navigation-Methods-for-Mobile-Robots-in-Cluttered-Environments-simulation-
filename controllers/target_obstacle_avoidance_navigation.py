#This code implements target obstacle avoidance navigation simulation of robot in clustered static environment
#This code should be updated according to environment-obstacles are predetermined in the code
#Braitenberg algorithm is used for obstacle avoidance 
#Simulaton is performed on webots platform 
#For detailed and environmet, robot details checkouts report and videos attached


from controller import Robot
import math

robot = Robot()
timestep = int(robot.getBasicTimeStep())
max_speed = 6.28

# Motors
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Proximity sensors
prox_sensors = [robot.getDevice(f'ps{i}') for i in range(8)]
for sensor in prox_sensors:
    sensor.enable(timestep)

# Example "target direction" - replace with actual sensor logic
def get_target_direction():
    # Fake function: simulate direction to target
    # Return: -1 (left), 0 (ahead), 1 (right)
    # Replace this with light sensor or camera logic if available
    # For now, randomly search as placeholder
    return 0  # pretend target is in front

# Obstacle detection
def read_front_obstacle():
    return any(prox_sensors[i].getValue() > 80 for i in [0, 1, 6, 7])

# Braitenberg-like avoidance behavior
def avoid_obstacles():
    sensor_values = [sensor.getValue() for sensor in prox_sensors]
    weights = [
        [-0.5, -1.0], [-0.3, -0.8], [-0.1, -0.5], [0, 0],
        [0, 0], [-0.5, -0.1], [-0.8, -0.3], [-1.0, -0.5]
    ]

    left_speed = 0.5 * max_speed
    right_speed = 0.5 * max_speed
    for i in range(8):
        left_speed += weights[i][0] * sensor_values[i] / 4096 * max_speed
        right_speed += weights[i][1] * sensor_values[i] / 4096 * max_speed

    # Clamp speeds
    left_speed = max(-max_speed, min(max_speed, left_speed))
    right_speed = max(-max_speed, min(max_speed, right_speed))
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)

# Main loop
while robot.step(timestep) != -1:
    if read_front_obstacle():
        avoid_obstacles()
    else:
        # Target seeking
        target_dir = get_target_direction()
        if target_dir == 0:
            # Target ahead
            left_motor.setVelocity(0.8 * max_speed)
            right_motor.setVelocity(0.8 * max_speed)
            print("Moving toward target")
        elif target_dir == -1:
            # Target to the left
            left_motor.setVelocity(0.3 * max_speed)
            right_motor.setVelocity(0.6 * max_speed)
            print("Turning left to target")
        elif target_dir == 1:
            # Target to the right
            left_motor.setVelocity(0.6 * max_speed)
            right_motor.setVelocity(0.3 * max_speed)
            print("Turning right to target")
