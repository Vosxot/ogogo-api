import json
import os
import random

def load_config():
    cfg_path = os.path.join(os.path.dirname(__file__), "settings.json")
    with open(cfg_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)


    num = random.randint(1000, 9999)
    phone = f"99600000{num}"
    cfg["phone"] = phone
    cfg["otp"] = phone[-4:]


    with open(cfg_path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


    base = os.path.abspath(os.path.dirname(__file__) + "/..")
    cfg["cert_path"] = os.path.join(base, cfg["cert_path"])
    cfg["key_path"]  = os.path.join(base, cfg["key_path"])
    cfg["selfie_path"] = os.path.join(base, cfg["selfie_path"])

    return cfg
