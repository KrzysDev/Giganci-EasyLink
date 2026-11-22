import atexit
import json
import tempfile
from pathlib import Path

from fastapi import APIRouter

from services.network_service import NetworkService

nts = NetworkService()

router = APIRouter()

_servers_file = Path(tempfile.gettempdir()) / "easylink_servers.json"


@router.get("/api/setup", tags=["setup"])
def setup_computers():
    servers = nts.get_servers()
    _servers_file.write_text(json.dumps(servers, indent=2))
    return {"servers": servers, "file": str(_servers_file)}


@atexit.register
def _cleanup():
    _servers_file.unlink(missing_ok=True)