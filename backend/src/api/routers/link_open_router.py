import json
import tempfile
from pathlib import Path

import requests
from fastapi import APIRouter

router = APIRouter()

_servers_file = Path(tempfile.gettempdir()) / "easylink_servers.json"
_worker_port = 5000


@router.post("/api/open_link", tags=["core"])
def open_link(url: str):
    servers = json.loads(_servers_file.read_text()) if _servers_file.exists() else []

    results = []
    for ip in servers:
        try:
            response = requests.post(
                f"http://{ip}:{_worker_port}/api/open_link",
                params={"url": url},
                timeout=2,
            )
            results.append({"ip": ip, "ok": response.ok})
        except requests.RequestException:
            results.append({"ip": ip, "ok": False})

    return {"opened": results}