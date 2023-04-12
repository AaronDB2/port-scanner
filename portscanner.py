import socket
import termcolor

#  Function that executes scan_port on each specified port from the target IP address
def scan(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in range(1, ports):
        scan_port(target , port)

# Function for scanning if a port is open or not
def scan_port(ipaddress, port): 
    try:
        # Initiate socket object
        sock = socket.socket()

        # Connect to the socket
        sock.connect((ipaddress, port))
        print("[+] Port Opened" + str(port))
        # Close socket
        sock.close()
    except:
       pass

# Console inputs
targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter How Many Ports Do You Want To Scan: "))

# Check if there is a , in targets
if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
    # For each IP address scan the ports
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets, ports)