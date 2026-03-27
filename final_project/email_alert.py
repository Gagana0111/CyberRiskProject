import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def send_alert(ip, port, risk):

    sender_email = "your_email@gmail.com"
    receiver_email = "your_email@gmail.com"
    app_password = "**************"

    # Risk level
    
    if risk >= 15:
        risk_level = "CRITICAL"
        color = "#ff4c4c"
    elif risk >= 8:
        risk_level = "HIGH"
        color = "#f59e0b"
    else:
        risk_level = "MEDIUM"
        color = "#10b981"

    subject = f"🚨 {risk_level} Security Alert"

    html_body = f"""
    <html>
    <body style="font-family: Arial; background:#0b0f19; color:white; padding:20px;">

        <div style="background:{color}; padding:15px; border-radius:8px; text-align:center;">
            <h2>🚨 {risk_level} ALERT</h2>
        </div>

        <div style="background:#111827; padding:20px; border-radius:10px; margin-top:15px;">
            <h3>🔍 Threat Summary</h3>
            <p><b>Target:</b> {ip}</p>
            <p><b>Ports:</b> {port}</p>
            <p><b>Total Risk Score:</b> {risk}</p>
            <p><b>Time:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

            <hr>

            <h3>🛠️ Action</h3>
            <ul>
                <li>Check open ports</li>
                <li>Apply firewall rules</li>
                <li>Monitor suspicious activity</li>
            </ul>
        </div>

        <p style="font-size:12px; color:gray;">
        Automated Cyber Risk Alert System
        </p>

    </body>
    </html>
    """

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.attach(MIMEText(html_body, "html"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        print("✅ Email sent successfully")

    except Exception as e:
        print("❌ Email failed:", e)