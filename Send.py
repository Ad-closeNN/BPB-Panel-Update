def email(email):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.utils import formataddr
    # 邮件的基本信息
    sender_email = Sender163
    receiver_email = email
    password = Password
    # 创建一个多部分的邮件
    msg = MIMEMultipart()
    msg['From'] = formataddr(("GitHub Actions", sender_email))
    msg['To'] = receiver_email
    msg['Subject'] = "BPB Server Everyday"
    # 邮件正文内容
    body = Bpb
    msg.attach(MIMEText("每天的 BPB VPN Server：\n" + body, 'plain'))
    # 发送邮件
    # 使用 163 的 SMTP 服务器
    server = smtplib.SMTP('smtp.163.com', 25)
    server.starttls()  # 启用 TLS
    server.login(sender_email, password)  # 登录
    server.sendmail(sender_email, receiver_email, msg.as_string())  # 发送邮件
    server.quit()  # 关闭连接

if __name__ == "__main__":
    import os
    ADqq = os.getenv("ADQQ")
    Ad163 = os.getenv("ADOST")
    Sender163 = os.getenv("SENDER")
    Password = os.getenv("PASSWORD")
    with open("OK.txt", "r", encoding="utf-8") as bpb:
        Bpb = bpb.read()
    
    """Send Message"""
    email(ADqq)
    email(Ad163)