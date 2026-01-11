dict_ip_attempts = {
    "180.237.210.112": 9,
    "180.237.210.30": 5,
    "180.237.210.13": 2,
    "180.237.210.54": 10,
    "182.237.210.54": 10,
    "80.237.210.54": 10,
    "18.27.210.54": 10,
    "180.237.20.54": 10,
}

def ip_split(ip: str):
    parts = ip.split('.')
    return (int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]))

sorted_ips = sorted(dict_ip_attempts.keys(), key=ip_split)

for ip in sorted_ips:
    print(ip)
