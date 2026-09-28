import cityflow
import os
import json

class Engine:
    def __init__(self, interval, thread_num, save_replay, rl_traffic_light, lane_change, seed):
        self.interval = interval
        self.thread_num = thread_num
        self.save_replay = save_replay
        self.rl_traffic_light = rl_traffic_light
        self.seed = seed
        self.roadnet_file = None
        self.flow_file = None
        self.eng = None

    def load_roadnet(self, file_path):
        self.roadnet_file = file_path

    def load_flow(self, file_path):
        self.flow_file = file_path
        
        # Build the config using absolute paths to bypass the CityFlow directory bug
        work_dir = os.path.dirname(self.roadnet_file)
        config = {
            "interval": self.interval,
            "seed": self.seed,
            "dir": "",
            "roadnetFile": self.roadnet_file,
            "flowFile": self.flow_file,
            "rlTrafficLight": self.rl_traffic_light,
            "saveReplay": self.save_replay,
            "roadnetLogFile": os.path.join(work_dir, "replay_roadnet.json"),
            "replayLogFile": os.path.join(work_dir, "replay.txt")
        }
        config_path = os.path.join(work_dir, "config.json")
        with open(config_path, 'w') as f:
            json.dump(config, f)
            
        self.eng = cityflow.Engine(config_path, thread_num=self.thread_num)
        
    def __getattr__(self, name):
        if name == "print_log":
            return lambda *args, **kwargs: None
        return getattr(self.eng, name)