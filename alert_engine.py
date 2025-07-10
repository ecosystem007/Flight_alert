import smtplib
from email.mime.text import MIMEText

def send_alert(flight_info, config):
    msg = MIMEText(f"检测到低价机票：{flight_info}", "plain", "utf-8")
    msg["Subject"] = "✈️ 低价机票提醒"
    msg["From"] = config["email"]["sender"]
    msg["To"] = config["email"]["receiver"]

    try:
        server = smtplib.SMTP_SSL(config["email"]["smtp_server"], 465)
        server.login(config["email"]["sender"], config["email"]["password"])
        server.sendmail(config["email"]["sender"], [config["email"]["receiver"]], msg.as_string())
        server.quit()
        print("✅ 邮件已发送")
    except Exception as e:
        print("❌ 邮件发送失败:", e)
