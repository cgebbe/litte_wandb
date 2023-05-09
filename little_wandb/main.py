# %%
# setup logging (wandb logs several DEBUG messages)
import logging

logging.basicConfig(level=logging.DEBUG)

# create a logger object
# logger = logging.getLogger()

# set the logging level to DEBUG
# logger.setLevel(logging.DEBUG)

# # create a console handler and set its level to DEBUG
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.DEBUG)

# # create a formatter and add it to the console handler
# formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
# console_handler.setFormatter(formatter)

# # add the console handler to the logger
# logger.addHandler(console_handler)

# %%
from wandb.sdk.wandb_init import _WandbInit
from wandb.sdk.wandb_settings import Settings

settings = Settings(
    **dict(
        _offline=True,
    )
)
settings


# %%
import wandb
from pprint import pprint
from pathlib import Path
from system_info import SystemInfo, SettingsStatic, Interface

REPO_DIR = Path(__file__).parents[1]
DATA_DIR = REPO_DIR / "data"


settings = wandb.setup().settings
settings._set_run_start_time()
settings.update(
    {
        "_offline": True,
        "save_code": True,
        "files_dir": DATA_DIR,
    }
)

dct = settings.make_static()
pprint(dct)
static_settings = SettingsStatic(dct)
static_settings


# %%
from pathlib import Path
from system_info import SystemInfo, SettingsStatic, Interface


class Writer(Interface):
    def __init__(self, outdir: Path) -> None:
        super().__init__()
        self.outdir = outdir

    def publish_stats(self, stats: dict) -> None:
        raise NotImplementedError

    def _publish_telemetry(self, telemetry: "TelemetryRecord") -> None:
        raise NotImplementedError

    def publish_files(self, files_dict: "FilesDict") -> None:
        # List of files t
        print(files_dict)


import time

# d = dict(
#     git_root=None,
#     git_remote=None,
#     git_remote_url=None,
#     git_commit=None,
#     files_dir=DATA_DIR,
#     program_relpath=None,
#     disable_git=False,
#     _os=None,
#     _python=None,
#     _start_time=time.time(),
#     docker=None,
#     _cuda=None,
#     _args=None,
#     disable_code=False,
#     _jupyter=None,
#     notebook_name=None,
#     _jupyter_path=None,
#     _jupyter_name=None,
#     _jupyter_root=None,
#     anonymous=None,
#     host=None,
#     username=None,
#     _save_requirements=None,
#     save_code=None,
#     program=None,
# )
# settings = SettingsStatic(d)
writer = Writer(DATA_DIR)
info = SystemInfo(static_settings, writer)
# info.publish()
probed = info.probe()
probed

# %%

"""
Does info.probe() add new information? It adds
- heartbeat 
- state = running
- codePath (= relative path of program)
- git remote and commit -> I likely get this via _save_git, or?!
- root (= base path of program)
"""

import pandas as pd

lst = []
for k, v in probed.items():
    v2 = dct.get(k)
    v3 = dct.get("_" + k)
    lst.append({"key": k, "probed": v, "org": v2, "_org": v3})

pd.DataFrame(lst)

# %%

info.publish(probed)
