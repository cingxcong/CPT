import glob
import os
from os.path import basename, dirname, isfile


def __list_all_modules():
    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    enable_eval = os.getenv("ENABLE_EVAL_MODULE", "").strip().lower() in {
        "1", "true", "yes", "on"
    }

    all_modules = [
        basename(path)[:-3]
        for path in mod_paths
        if isfile(path)
        and path.endswith(".py")
        and not path.endswith("__init__.py")
        and (basename(path)[:-3] != "eval" or enable_eval)
    ]

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
