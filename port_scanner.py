import argparse
import socket
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

THREAD_POOL_SIZE = 20

def scan_port(remote_host: str, port: int) -> Tuple[int, str]:
    """
    Scans a single port and returns the result as a tuple of port number and status.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    conn_status = sock.connect_ex((remote_host, port))
    sock.close()
    return port, 'open' if conn_status == 0 else 'closed'

def scan_ports_threaded(remote_host: str, ports: List[int]) -> List[Tuple[int, str]]:
    """
    Scans multiple ports using multiple threads and returns the results as a list of tuples.
    """
    with ThreadPoolExecutor(max_workers=THREAD_POOL_SIZE) as executor:
        results = list(executor.map(scan_port, [remote_host] * len(ports), ports))
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scan for open ports on a remote host.')
    parser.add_argument('remote_host', type=str, help='Remote host IP address or hostname')
    parser.add_argument('ports', type=int, nargs='+', help='One or more port numbers to scan')
    args = parser.parse_args()

    results = scan_ports_threaded(args.remote_host, args.ports)
    for port, status in results:
        print(f'Port {port} is {status}')
