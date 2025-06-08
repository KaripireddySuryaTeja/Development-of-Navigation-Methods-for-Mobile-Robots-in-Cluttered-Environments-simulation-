# 🤖 Development of Navigation Methods for Mobile Robots in Cluttered Environments

This Webots-based simulation project explores multiple autonomous navigation strategies for mobile robots operating in cluttered environments. Each method is implemented using the Python Webots controller API, targeting core robotics challenges like obstacle avoidance, wall following, target seeking, and path patterning.

---

## 📁 Project Structure

[
Development of Navigation Methods/
│
├── controllers/
│ ├── obstacle_avoidance.py
│ ├── wall_follower.py
│ ├── line_follower.py
│ ├──Robot_Vacuum_Navigation_Algorithms/
│ │ ├── random_navigation.py
│ │ ├── zigzag_navigation.py
│ │ ├── spiral_navigation.py
│ │ └── snake_navigation.py
│ └── target_avoidance_navigation.py
│
├── Simulation/
│ ├── images/
│ └──  Videos/
│
├── report.pdf
├── Presentation.pptx
└── README.md
]


---

## 🧠 Navigation Techniques Implemented

### 1. 🚧 **Obstacle Avoidance**
- Uses proximity sensors and Braitenberg weights to steer away from obstacles.

### 2. 🧱 **Wall Follower**
- Maintains close distance to left-hand wall using grouped sensor inputs.

### 3. ➖ **Line Follower**
- Tracks a black line using left, center, and right sensors.
- Aligns direction and reverses when off-line.

### 4. 🎲 **Random Navigation**
- Random turning decisions to simulate unpredictable coverage.
- Avoids getting stuck by turning on collisions.

### 5. 🪜 **Zigzag Navigation**
- Alternates left and right motions to create sweeping zigzag paths.
- On obstacle detection, flips the zigzag direction.

### 6. 🌀 **Spiral Navigation**
- Simulates increasing spiral pattern to gradually cover space.
- Resets angle if obstacle is encountered.

### 7. 🐍 **Snake Navigation**
- Performs alternate left-right turning after collisions.
- Moves straight otherwise for organic “snake-like” path.

### 8. 🎯 **Target-Finding + Obstacle Avoidance**
- Uses simulated or sensor-based directional awareness toward a target.
- Avoids obstacles dynamically en route to the target.

---

## 🔧 How to Run the Simulations

1. **Open Webots**.
2. Load a world from the `/worlds` folder (e.g., `obstacle_avoidance.wbt`) or create worlds according to simulation.
3. Ensure the robot controller is set correctly in the robot properties.
4. Click the **Play** button in Webots to start the simulation.

---

## 🛠 Requirements

- [Webots](https://cyberbotics.com) R2022 or later
- Python 3.x
- e-puck or similar robot model with:
  - 8 proximity sensors (`ps0` to `ps7`)
  - Differential drive motors
  - (Optional) Line sensors or camera/light sensor for advanced modes

---

## 📸 Screenshots

See the `Simulation/images/` or `Simulation/Videos/` folder for visuals of each behavior in action.

---

## 📄 Project Report

A detailed report is available in `report.pdf` including:
- Architecture overview
- Flowcharts
- Sensor usage
- Behavior comparison
- Performance metrics

---

## 👤 Author

**Karipireddy Surya Teja Gopal Reddy**  
Dept. of Computer Science and Engineering,
National Institute of Technology Meghalaya  
Contact: karipireddysuryateja@gmail.com

---

## 🧪 Future Work

- Camera-based colored object detection for real targets
- SLAM integration (Simultaneous Localization & Mapping)
- PID-based smoother line tracking
- Path memory & learning with AI

---

## 📜 License

This project is developed for academic and research use. Open for non-commercial contributions.  
Attribution is appreciated.