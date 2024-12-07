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
    msg['From'] = formataddr(("BPB Server Updater", sender_email))
    msg['To'] = receiver_email
    msg['Subject'] = "BPB Server Everyday"
    # 邮件正文内容
    msg.attach(MIMEText("每天的 BPB Server：\n服务器地址：\n\n" + bbb + """<hr style="border: none;margin: 16px 0px; border-top: 1px solid rgb(230, 232, 235);">""" + SOMEurl + """<span style="font-family: MiSans, &quot;HarmonyOS Sans SC&quot;, -apple-system, system-ui; font-size: 11pt; color: rgb(0, 0, 0); line-height: 1.6;"><br></span>""", 'plain'))
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
    print(Sender163)
    Password = os.getenv("PASSWORD")
    with open("O.txt", "w", encoding="utf-8") as clear:
        clear.write("")
    with open("OK.txt", "r", encoding="utf-8") as bba:        
        bbb = bba.read() # 满意了吧
    with open("OK.txt", "r", encoding="utf-8") as bpb:
        Bpb = bpb.readlines() # 原来的 only domains
    for link in Bpb:
        trojan_link = f"trojan://bpb-trojan@www.vpslook.com:443?security=tls&sni={link}&alpn=h3&fp=randomized&allowlnsecure=1&type=ws&host={link}&path=%2Ftr%3Fed%3D2560#{link}"
        trojan_link= trojan_link.replace("\n", "")
        with open("O.txt", "a", encoding="utf-8") as file:
            file.write(trojan_link+"\n")
    with open("O.txt", "r", encoding="utf-8") as e:
        SOMEurl = e.read()

    """Send Message"""
    email(ADqq)
    email(Ad163)