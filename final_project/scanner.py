import nmap

def scan_target(target):
    scanner = nmap.PortScanner()

    print("Running advanced scan...")


    scanner.scan(target, arguments='-sS -sV -T4')

    results = []

    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()

            for port in ports:
                state = scanner[host][proto][port]['state']

                if state == "open":
                    service = scanner[host][proto][port]['name']

                    results.append({
                        "ip": host,
                        "port": port,
                        "service": service
                    })

    return results