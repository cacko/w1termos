__name__ = "w1termos"

import logging
from corelog import register, Handlers
import uvicorn
from .config import app_config

register(app_config.w1termos.log_level, handler_type=Handlers.RICH)


def start():
    from w1termos.app import create_app

    try:
        uvicorn.run(
            create_app,
            host=app_config.w1termos.host,
            port=app_config.w1termos.port,
            log_level="info",
            loop="uvloop",
            factory=True,
            access_log=True,
        )

    except KeyboardInterrupt:
        pass
    except Exception as e:
        logging.exception(e)
