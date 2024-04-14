import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def send_email(sender_email, sender_password, receiver_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email.")
        print(e)

def generate_daily_report():
    # 这里生成你的每日报告
    # 可以是从文件中读取数据、调用 API 获取数据等

    # 例子：获取当前日期
    today = datetime.date.today()
    report = f"这是 {today} 的每日报告。"

    return report

if __name__ == "__main__":
    # 配置发件人和收件人邮箱地址
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    receiver_email = "recipient_email@example.com"

    # 生成每日报告
    daily_report = generate_daily_report()

    # 发送邮件
    send_email(sender_email, sender_password, receiver_email, "每日报告", daily_report)
