import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor

import requests


class NetworkService:
    def __init__(self, port=5000, endpoint="ping", timeout=1):
        self.port = port
        self.endpoint = endpoint
        self.timeout = timeout

    def get_my_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80)) 
        ip = s.getsockname()[0]
        s.close()
        return ip

    def get_computers(self):
        network = ipaddress.ip_network(self.get_my_ip() + "/24", strict=False)
        return [str(ip) for ip in network.hosts()]

    def has_ping(self, ip):
        try:
            response = requests.get(
                f"http://{ip}:{self.port}/{self.endpoint}", timeout=self.timeout
            )
            return response.ok
        except requests.RequestException:
            return False

    def get_servers(self):
        ips = self.get_computers()
        with ThreadPoolExecutor(max_workers=100) as pool:
            results = list(pool.map(self.has_ping, ips))
        return [ip for ip, ok in zip(ips, results) if ok]


if __name__ == "__main__":
    print(NetworkService().get_servers())