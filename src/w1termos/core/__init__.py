from w1termos import __name__
from pathlib import Path
from appdirs import user_state_dir
import os
from typing import Optional

data_dir = Path(user_state_dir(__name__))
if not data_dir.exists():
    data_dir.mkdir(exist_ok=True)

pid_file = data_dir / f"{__name__}.pid"

def check_pid() -> Optional[int]:
    try:
        assert pid_file.exists()
        pid = pid_file.read_text()
        assert pid
        os.kill(int(pid), 0)
        return int(pid)
    except (AssertionError, ValueError, OSError):
        return None