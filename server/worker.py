import logging
import sys
import webbrowser
from pathlib import Path

import uvicorn
from fastapi import FastAPI

if getattr(sys, "frozen", False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).parent

app = FastAPI()

LOG_FILE = BASE_DIR / "easylink_worker.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


@app.get("/ping")
def ping():
    return {"ok": True}


@app.post("/api/open_link")
def open_link(url: str):
    logging.info("open_link: %s", url)
    webbrowser.open(url)
    return {"opened": url}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=5000,
        log_config=None,
        access_log=True,
    )