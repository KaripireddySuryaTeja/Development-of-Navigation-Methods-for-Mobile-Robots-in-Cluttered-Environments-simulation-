#This code implements Line Following simulation of robot in clustered static environment
#Simulaton is performed on webots platform 
#For detailed and environmet, robot details checkouts report and videos attached

from controller import Robot

def run_robot(robot):
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28  # Adjust for your robot's max speed

    # Initialize motors
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))

    # Initialize IR sensors
    left_sensor = robot.getDevice('left_line_sensor')
    center_sensor = robot.getDevice('center_line_sensor')
    right_sensor = robot.getDevice('right_line_sensor')

    left_sensor.enable(timestep)
    center_sensor.enable(timestep)
    right_sensor.enable(timestep)

    # Line detection threshold
    THRESHOLD = 500  # May need tuning depending on environment

    while robot.step(timestep) != -1:
        left_val = left_sensor.getValue()
        center_val = center_sensor.getValue()
        right_val = right_sensor.getValue()

        # Decide motor speed based on line position
        if center_val > THRESHOLD and left_val < THRESHOLD and right_val < THRESHOLD:
            # On track
            left_speed = max_speed
            right_speed = max_speed
            print("Move straight")

        elif left_val > THRESHOLD:
            # Line towards left — turn right
            left_speed = max_speed * 0.5
            right_speed = max_speed
            print("Veer right")

        elif right_val > THRESHOLD:
            # Line towards right — turn left
            left_speed = max_speed
            right_speed = max_speed * 0.5
            print("Veer left")

        else:
            # Lost line — reverse to search
            left_speed = -max_speed
            right_speed = -max_speed
            print("Line lost — reversing")

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == "__main__":
    robot = Robot()
    run_robot(robot)
