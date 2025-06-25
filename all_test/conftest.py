import os
import json
import pytest
import requests

@pytest.fixture(scope="session")
def config():
    here = os.path.dirname(__file__)
    cfg_path = os.path.join(here, "config", "settings.json")
    with open(cfg_path, encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def session(config):
    s = requests.Session()
    # клиентский сертификат для mTLS
    s.cert   = (config["cert_path"], config["key_path"])
    # доверяем системному CA
    s.verify = True
    return s
