# Hand Gesture Controlled Car

## Overview
This project implements a **hand gesture-controlled car simulation** using **OpenCV, Mediapipe, and Pygame**. The car moves in different directions based on the movement of the index finger, tracked using a webcam.

## Features
- **Real-time hand tracking** using Mediapipe
- **Gesture-based control** to move the car **Up, Down, Left, and Right**
- **Interactive UI** with a Pygame-rendered car
- **Seamless OpenCV integration** for webcam input
- **Rotating car sprite** based on movement direction

## Technologies Used
- **Python** (Main programming language)
- **Pygame** (For graphical interface and car movement)
- **OpenCV** (For capturing video input from the webcam)
- **Mediapipe** (For real-time hand tracking and landmark detection)
- **NumPy** (For efficient mathematical computations)

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.7+** installed.

### Install Dependencies
Run the following command to install the required libraries:
```sh
pip install pygame opencv-python mediapipe numpy
```

### Run the Project
1. Clone this repository:
   ```sh
   git clone https://github.com/RaviKumar300/finger_tracked_car.git
   cd finger_tracked_car
   ```
2. Run the script:
   ```sh
   python car_mov_index.py
   ```

## How It Works
- The webcam detects your **index finger movement**.
- The **direction of movement** (up, down, left, right) is determined.
- The **car moves** accordingly in the Pygame window.
- The car **rotates** based on movement direction.
- The camera feed with hand tracking is displayed in an OpenCV window.
- Press **'q'** to exit the program.

## Controls (Based on Index Finger Direction)
| Gesture  | Action |
|----------|--------|
| Finger Up    | Move Up |
| Finger Down  | Move Down |
| Finger Left  | Move Left |
| Finger Right | Move Right |

## File Structure
```
├── car_mov_index.py       # Main script for car movement & hand tracking
├── png-transparent-car-game-racing.png  # Car image used in the game
├── README.md              # Project documentation
```

## Future Enhancements
- Add **speed control** based on distance of finger from the palm
- Implement **multi-hand support** for advanced gestures
- Improve **UI with background & obstacle detection**

## License
This project is open-source and available under the **MIT License**.

---
**Author:** Ravi Kumar

For any queries, feel free to contact or raise an issue in the repository!

