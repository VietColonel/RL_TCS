import os
import json
import pickle
from model_test import test

base_name = "anon_1_6_300_0.3_synthetic.json_09_28_00_40_21"
record_dir = os.path.join("records", "test", base_name)
model_dir = os.path.join("model", "test", base_name)
cnt_round = 299 # The final round to visualize

# Load configurations
with open(os.path.join(record_dir, "exp.conf"), "r") as f:
    dic_exp_conf = json.load(f)
with open(os.path.join(record_dir, "traffic_env.conf"), "r") as f:
    dic_traffic_env_conf = json.load(f)

# Fix JSON string keys back to integers for the PHASE dictionary
if "PHASE" in dic_traffic_env_conf and "anon" in dic_traffic_env_conf["PHASE"]:
    dic_traffic_env_conf["PHASE"]["anon"] = {int(k): v for k, v in dic_traffic_env_conf["PHASE"]["anon"].items()}


# Enable replay saving!
dic_traffic_env_conf["SAVEREPLAY"] = True

# Overwrite CityFlow config.json to save replay
config_path = os.path.join(record_dir, "config.json")
with open(config_path, "r") as f:
    cityflow_config = json.load(f)
cityflow_config["saveReplay"] = True
with open(config_path, "w") as f:
    json.dump(cityflow_config, f)

print(f"Generating CityFlow replay for round {cnt_round}...")
test(model_dir, cnt_round, dic_exp_conf["RUN_COUNTS"], dic_traffic_env_conf, False)

print("\nSuccess! Replay generated.")
print(f"Roadnet file: {cityflow_config['roadnetFile']}")
print(f"Replay file: {cityflow_config['replayLogFile']}")
