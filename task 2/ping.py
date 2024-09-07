import argparse
import ipaddress
import subprocess

# a function to ping the ip addresses
def ping_ip(ip):    
    print(f"Pinging {ip}...")
    result = subprocess.call(['ping', '-n', '1', str(ip)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result == 0


# simply here we call all the funtions we made above 
# in addation to that in fact it first gather or read the argument(input)from the command line
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

    live_ips = []
    offline_ips = 0

    print(f"Scanning subnet: {args.subnet}")
    all_ips = cidr_to_ips(args.subnet)


    for ip in all_ips:
        if ping_ip(ip):
            live_ips.append(ip)
        else:
            offline_ips += 1
          
        #   output results
    print(f"Live IPs: {len(live_ips)}")
    print(f"Offline IPs: {offline_ips}")
    print(f"Live IP addresses: {live_ips}")



if __name__ == "__main__":
    main()
