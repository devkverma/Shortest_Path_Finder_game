# Shortest Path Finder

This project demonstrates a pathfinding algorithm using the A* (A-star) algorithm with a graphical interface built using Pygame. The goal is to find the shortest path between a randomly placed start and end point on a grid, while avoiding randomly generated obstacles.

## Prerequisites

1. **Python**: Ensure you have Python 3.6 or later installed. You can download Python from the [official website](https://www.python.org/downloads/).

2. **Virtual Environment**: It is recommended to use a virtual environment to manage dependencies.

## Setup Instructions

1. **Create a Virtual Environment**:
   Navigate to your project directory and create a virtual environment using the following command:

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   Install the required Python packages using pip:

   ```bash
   pip install pygame numpy
   ```

4. **Clone the Repository**:
   If you have a repository URL, clone it using:

   ```bash
   git clone 'https://github.com/devkverma/Shortest_Path_Finder_game.git'
   cd Shortest_Path_Finder_game
   ```

5. **Run the Application**:
   Run the script using Python:

   ```bash
   python main.py
   ```


## Usage

- **Initialization**: The program initializes with a randomly placed start point, end point, and obstacles on a grid.

- **Controls**:
  - **Spacebar**: Executes the A* algorithm to find and display the shortest path from the start to the end.
  - **R Key**: Resets the grid, placing new obstacles, start, and end points.

- **Visualization**:
  - Obstacles are shown in the color specified by `OBSTACLECOLOR`.
  - The start point is colored with `STARTCOLOR`.
  - The end point is colored with `ENDCOLOR`.
  - The path found by the algorithm is displayed in `MAROON`.
  - Processed nodes are highlighted in `YELLOW`.

## Code Structure

- **`Board` Class**: Manages the grid, obstacles, and visual updates.
- **`AI` Class**: Implements the A* algorithm and heuristic function.
- **`main()` Function**: Handles user input and orchestrates the grid updates and pathfinding process.



## Acknowledgements

- Pygame for the graphical interface.
- Python libraries for numerical computations and algorithm implementations.

Feel free to reach out if you have any questions or issues with the code. Happy coding!