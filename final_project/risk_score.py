def calculate_risk(port):

    # Common ports with real meaning
    if port == 22:   # SSH
        return 6
    elif port == 80: # HTTP
        return 3
    elif port == 443: # HTTPS
        return 2
    elif port == 21: # FTP
        return 7
    elif port == 445: # SMB (HIGH RISK)
        return 9
    elif port == 135: # RPC
        return 8
    else:
        return (port % 7) + 2   