import os
import pandas as pd
import numpy as np
from math import isnan

# Use relative path so it works in both WSL and Windows!
base_dir = os.path.join("records", "test")

folders = [
    "anon_1_6_300_0.3_synthetic.json_09_28_00_40_21",
    "anon_1_6_300_0.6_synthetic.json_09_28_00_40_21",
    "anon_1_6_700_0.3_synthetic.json_09_28_00_40_21",
    "anon_1_6_700_0.6_synthetic.json_09_28_00_40_21"
]

inter_names = ["1_1", "2_1", "3_1", "4_1", "5_1", "6_1"]

for folder in folders:
    print(f"Processing folder: {folder}")
    folder_path = os.path.join(base_dir, folder)
    test_dir = os.path.join(folder_path, "test_round")
    metrics_file = os.path.join(folder_path, "metrics_log.csv")
    
    with open(metrics_file, "w") as f_metric:
        f_metric.write("round,travel_time\n")
        
        for cnt_round in range(300):
            record_dir = os.path.join(test_dir, f"round_{cnt_round}")
            if not os.path.exists(record_dir):
                continue
                
            ave_duration_all = []
            for inter_id in inter_names:
                csv_path = os.path.join(record_dir, f"vehicle_inter_{inter_id}.csv")
                if os.path.exists(csv_path):
                    df = pd.read_csv(csv_path, sep=',', header=0, dtype={0: str, 1: float, 2: float},
                                     names=["vehicle_id", "enter_time", "leave_time"])
                    duration = df["leave_time"].values - df["enter_time"].values
                    ave_duration = np.mean([t for t in duration if not isnan(t)])
                    ave_duration_all.append(ave_duration)
            
            if ave_duration_all:
                final_duration = np.mean(ave_duration_all)
                f_metric.write(f"{cnt_round},{final_duration}\n")

    print(f"-> Saved {metrics_file}")
print("All done!")