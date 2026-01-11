import socket
import sys

if len(sys.argv) < 2:
    print("Použití:")
    print("  python scanner.py <IP>")
    print("  python scanner.py <IP> <PORT>")
    sys.exit()

target = sys.argv[1]

single_port = False
open_found = False  # hlídá, jestli jsme něco našli

if len(sys.argv) == 3:
    ports = [int(sys.argv[2])]
    single_port = True
else:
    ports = range(1, 1001)

print(f"Skenuji {target}...")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
        open_found = True
    else:
        if single_port:
            print(f"[CLOSED] Port {port}")

    s.close()

# Pokud se nic nenašlo
if not open_found:
    print("❌ Žádný otevřený port nebyl nalezen")

print("Scan dokončen.")
