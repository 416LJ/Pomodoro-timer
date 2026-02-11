# Pomodoro Timer

A simple Pomodoro Timer application built with Python and Tkinter. This app helps you manage your time effectively using the Pomodoro Technique.

## Features

- **Timer Mechanisms**:
  - **Work**: 25 minutes
  - **Short Break**: 5 minutes
  - **Long Break**: 10 minutes (triggered after 4 work sessions)
- **Visual Feedback**:
  - Dynamic timer display.
  - Checkmarks (✅) to track completed work sessions.
  - Text updates to indicate current phase (Work or Break).
- **Controls**:
  - **Start**: Begins the timer.
  - **Reset**: Stops the timer and resets progress.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- `tomato.png` image file in the same directory (included in repo).

## Usage

1. **Run the Application**:
   Navigate to the directory containing `main.py` and execute:

   ```bash
   python main.py
   ```

2. **Start Timer**:
   - Click the **Start** button to begin the session.
   - The timer will count down based on the current phase (Work, Short Break, or Long Break).

3. **Track Progress**:
   - Completed work sessions are marked with a green checkmark (✅).
   - After 4 work sessions, a long break is triggered.

4. **Reset**:
   - Click the **Reset** button to stop the timer and reset all progress.

## Code Structure

- `main.py`: Contains the main application logic and UI setup using Tkinter.
- `tomato.png`: Image resource used for the timer background.

## License

This project is open source.
