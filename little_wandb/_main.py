import wandb
import pprint
from pathlib import Path
from wandb.sdk.internal.system.system_info import SystemInfo, SettingsStatic, Interface
import logging

_LOGGER = logging.getLogger(__name__)


def _get_settings(logdir: Path, track_code: bool) -> SettingsStatic:
    settings = wandb.setup().settings
    settings._set_run_start_time()
    settings.update(
        {
            "_offline": True,
            "save_code": track_code,
            "files_dir": logdir,
        }
    )

    dct = settings.make_static()
    _LOGGER.debug(pprint.pformat(dct))
    return SettingsStatic(dct)


class _DummyInterace(Interface):
    def publish_stats(self, stats: dict) -> None:
        raise NotImplementedError

    def _publish_telemetry(self, telemetry: "TelemetryRecord") -> None:
        raise NotImplementedError

    def publish_files(self, files_dict: "FilesDict") -> None:
        s = pprint.pformat(files_dict["files"])
        _LOGGER.info(f"Wrote the following files: \n{s}")


def dump_infos(logdir: Path, track_code: bool = True):
    writer = _DummyInterace()
    settings = _get_settings(logdir=logdir, track_code=track_code)
    info = SystemInfo(settings, writer)

    info_dct = info.probe()
    _LOGGER.debug(pprint.pformat(info_dct))

    logdir.mkdir(exist_ok=True, parents=True)
    info.publish(info_dct)
