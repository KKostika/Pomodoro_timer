# Pomodoro Timer – Python GUI with Sound Alerts 🎧🍅

This project is a playful yet functional Pomodoro Timer built with Python's `tkinter` for GUI and `pygame` for sound playback. It helps users manage focused work sessions and breaks using the Pomodoro technique, enhanced with motivational sound effects and visual feedback.

## 🎯 Features

- ⏱️ **Work/Break Cycles**:
  - 25-minute work sessions
  - 5-minute short breaks
  - 30-minute long breaks after every 4 work sessions

- 🖼️ **Visual Interface**:
  - Tomato-themed timer display
  - Dynamic labels and checkmarks for completed sessions

- 🔔 **Sound Alerts**:
  - Start bell: Seatbelt sound
  - Break bell: Drumroll
  - Long break bell: Audience cheering

- 💬 **Custom Messages**:
  - Fun and encouraging labels during each phase (e.g. “Take A Nap – You Are A Princess!”)

## 🛠️ Technologies Used

- `tkinter` – GUI framework
- `pygame` – Sound playback
- `math` – Countdown calculations


## 🚀 How to Run

1. Install dependencies:

```bash
pip install pygame

Run the script:
python pomodoro_timer.py

🧾 Customization
You can adjust the timer durations by modifying these constants:

python
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
You can also replace sound files with your own .mp3 clips for a personalized experience.
👩‍💻 Author
Kyriaki Kostika

