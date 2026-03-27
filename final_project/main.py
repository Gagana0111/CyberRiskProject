import pandas as pd
from email_alert import send_alert

# INPUT

target = input("Enter target IP or domain: ")

print("\nScanning target...")

data = [
    {"ip": target, "port": 22, "service": "ssh", "risk_score": 3},
    {"ip": target, "port": 80, "service": "http", "risk_score": 6},
    {"ip": target, "port": 445, "service": "smb", "risk_score": 9},  
]

df = pd.DataFrame(data)

print("\nScan Results:")
print(df)


# SAVE REPORT

df.to_csv("security_report.csv", index=False)
print("\nReport saved as security_report.csv")


# TOTAL RISK

total_risk = df["risk_score"].sum()
print("Total Risk Score:", total_risk)


# SEND EMAIL ALERT (FINAL LOGIC)

print("\nChecking for alerts...")

high_risk = df[df["risk_score"] >= 5]

if not high_risk.empty:
    print("Sending alert email...")
    
    send_alert(
        ip="Multiple Hosts",
        port="Multiple Ports",
        risk=int(high_risk["risk_score"].sum())
    )

    print("✅ Alert sent")
else:
    print("✅ No high-risk threats detected")