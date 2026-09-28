# PressLight - Reinforcement Learning for Traffic Signal Control

This repository contains the implementation of **PressLight**, a Deep Reinforcement Learning (RL) agent that optimizes traffic signal control to minimize average travel time. It uses Max Pressure theory combined with a Deep Q-Network (DQN) and is simulated using the [CityFlow](https://cityflow-project.github.io/) traffic simulator.

## 🚦 Features
- **Deep Q-Network (DQN):** Learns optimal traffic light phases based on the "Max Pressure" state of the intersection.
- **CityFlow Integration:** Fast, multi-threaded traffic simulation.
- **Automated Metrics:** Scripts to automatically parse simulation logs and calculate the Average Travel Time per round.
- **Visualization:** Jupyter Notebooks for plotting the RL learning convergence and tools to generate CityFlow UI replays.

---

## 🛠️ Requirements & Installation

1. **Environment:** This codebase is designed to run in a Linux environment (or WSL on Windows).
2. **Python:** Python 3.8 is recommended.
3. **Dependencies:**
   ```bash
   pip install tensorflow pandas numpy matplotlib seaborn jupyter
   ```
4. **CityFlow Simulator:**
   You must install the CityFlow simulator from source or pip.
   ```bash
   pip install cityflow
   ```

---

## 🚀 How to Train the RL Agent

The repository comes configured with 4 different synthetic traffic scenarios (Light-Flat, Light-Peak, Heavy-Flat, Heavy-Peak).

To start training the models over 300 rounds, simply run:
```bash
python runexp.py
```
*Note: During training, CityFlow replay generation is intentionally disabled to save hard drive space. The neural networks (`.h5` files) will be saved inside the `model/test/` folder.*

---

## 📊 Generating and Visualizing Metrics

Once training is complete (or if you manually stop it), you can generate the learning curve metrics.

**1. Generate `metrics_log.csv`**
Run the automated metrics script to parse the thousands of output CSV files and calculate the Average Travel Time for every round:
```bash
python generate_all_metrics.py
```

**2. Plot the Learning Curve**
Open the provided Jupyter Notebook to visualize how the AI improved over time:
```bash
jupyter notebook Visualize_Metrics.ipynb
```
The notebook uses `seaborn` to plot the convergence of the Average Travel Time across all 4 traffic scenarios on a single graph.

---

## 🎥 Visualizing the Simulation in CityFlow Web UI

If you want to visually watch the cars and traffic lights to see the AI in action, you can generate a replay file.

**1. Generate the Replay**
Run the replay generation script. This script automatically loads your **best** trained model (e.g., Round 299) and runs a 1-minute test simulation while recording the visual data:
```bash
python generate_replay.py
```
This will output two files in your `records/test/...` folder:
- `roadnet_1_6.json` (Note: CityFlow will actually use `replay_roadnet.json` for drawing)
- `replay.txt`

**2. Watch the Replay**
1. Open the [CityFlow Web Visualizer](https://cityflow-project.github.io/web/).
2. For the **Roadnet File**, upload **`replay_roadnet.json`**. *(Do not use the original `roadnet_1_6.json`!)*
3. For the **Replay File**, upload **`replay.txt`**.
4. Click **Start** and watch your AI control the traffic!

---

## 🗑️ Space Management (Important)

Training for 300 rounds generates massive Experience Replay buffers (`.pkl` files) in the `records/.../train_round` directories. A full 300-round session can consume up to **3.8 GB** of space.

If you are pushing this code to GitHub, ensure that `.gitignore` is set up to block these files:
```text
records/
model/
data/
errors/
__pycache__/
*.h5
*.pkl
```
You can safely delete the `train_round` folders after training is fully completed, as they are only used by the AI during the learning phase.