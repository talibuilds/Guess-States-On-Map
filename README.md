# 🗺️ 28 Indian States Guess Game

A fun and interactive geography quiz built with **Python Turtle** — guess all 28 Indian states by typing their names!

---

## 🎮 Preview

![Game Preview](Preview.gif)

---

## 🚀 How to Play

1. Run `main.py`
2. A blank map of India will appear
3. Type a state name in the input box
4. If correct, the state name appears on the map at its location
5. Try to guess all **28 states**!

---

## 📦 Requirements

```bash
pip install pandas
```

> Python's built-in `turtle` module is used — no extra install needed.

---

## 📁 Project Structure

```
28 States Guess/
├── main.py            # Main game
├── calibrate_map.py   # Tool to re-calibrate state coordinates
├── 28_states.csv      # State names with map coordinates
├── IndiaMap.gif       # Blank India map image
└── Preview.gif        # Game preview animation
```

---

## 🛠️ Recalibrating Coordinates

If the state labels appear in wrong positions, run:

```bash
python calibrate_map.py
```

Click on the center of each state when prompted. The CSV will be updated automatically.

---

## 👤 Author

Made by **TALIB KHAN**
