# PressLight - Modernized Reinforcement Learning for Traffic Signal Control

This repository contains a modernized implementation of **PressLight**, a Deep Reinforcement Learning (RL) agent that optimizes traffic signal control to minimize average travel time. Originally created over 7 years ago, this project has been fully upgraded and revived to work flawlessly on modern systems (Python 3.8+) while maintaining the core Max Pressure theory and Deep Q-Network (DQN) architecture. 

Simulations are powered by the open-source [CityFlow](https://cityflow-project.github.io/) traffic simulator.

## ✨ Modernization Contributions
The original 7-year-old PressLight codebase was heavily outdated and suffered from broken dependencies. Our key contributions in this repository include:
- **Python 3.8+ Upgrade:** Upgraded syntax, packages, and environment configurations.
- **Keras 3 Compatibility:** Refactored the Deep Q-Network code to safely handle tensor shapes, prevent OOM (Out-of-Memory) crashes on modern GPUs, and safely fallback to CPU for ultra-fast training.
- **Multiprocessing Fixes:** Fixed critical fork/spawn pipeline crashes in CityFlow's C++ engine, allowing stable background logging without segmentation faults.
- **Automated Metrics & Visualizations:** Added brand-new scripts to automate the generation of travel time metrics, CityFlow replays, and Jupyter Notebook learning curves.

---

## 🛠️ Requirements & Installation (WSL / Ubuntu)

Because CityFlow compiles C++ components, we strongly recommend running this natively on Linux or via **Windows Subsystem for Linux (WSL2: Ubuntu)**.

**1. Install System Dependencies (WSL/Ubuntu):**
```bash
sudo apt update
sudo apt install build-essential cmake
```

**2. Setup Python Environment:**
We recommend using Conda:
```bash
conda create -n cityflow_env python=3.8
conda activate cityflow_env
pip install tensorflow pandas numpy matplotlib seaborn jupyter
```

**3. Install CityFlow Simulator:**
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
- `roadnet_1_6.json`
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
errors/
__pycache__/
*.h5
*.pkl
```
You can safely delete the `train_round` folders after training is fully completed, as they are only used by the AI during the learning phase.