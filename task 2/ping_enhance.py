import argparse
import ipaddress
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import platform

def ping_ip(ip):
    print(f"Pinging {ip}...")
    if platform.system() == "Windows":
        result = subprocess.call(['ping', '-n', '1', str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        result = subprocess.call(['ping', '-c', '1', str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return ip, result == 0

def cidr_to_ips(cidr):
    try:
        network = ipaddress.ip_network(cidr, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError as e:
        print(f"Error with CIDR format: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Ping IPs in a given subnet.")
    parser.add_argument('subnet', type=str, help="Subnet in CIDR format (e.g., 192.168.56.0/24)")
    args = parser.parse_args()

    print(f"Scanning subnet: {args.subnet}")
    all_ips = cidr_to_ips(args.subnet)

    if not all_ips:
        print("No IPs to scan. Exiting.")
        return

    live_ips = []
    offline_ips = 0

    # Use ThreadPoolExecutor to ping IPs concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_ip = {executor.submit(ping_ip, ip): ip for ip in all_ips}
        for future in as_completed(future_to_ip):
            ip, is_live = future.result()
            if is_live:
                live_ips.append(ip)
            else:
                offline_ips += 1

    print(f"Live IPs: {len(live_ips)}")
    print(f"Offline IPs: {offline_ips}")
    print(f"Live IP addresses: {live_ips}")

if __name__ == "__main__":
    main()
