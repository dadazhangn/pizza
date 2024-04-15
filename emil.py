import win32com.client

def extract_foxmail_content():
    try:
        # 创建 Foxmail 应用对象
        foxmail_app = win32com.client.Dispatch("Foxmail.Application")
    except Exception as e:
        print("无法创建 Foxmail 应用对象：", e)
        return

    try:
        # 获取当前用户的默认邮箱账户
        mail_account = foxmail_app.Accounts.DefaultAccount

        # 进入收件箱文件夹
        inbox_folder = mail_account.GetFolder("收件箱")

        # 获取收件箱中的所有邮件
        emails = inbox_folder.Messages

        # 遍历邮件列表
        for email in emails:
            # 获取邮件内容
            subject = email.Subject
            sender = email.From
            receiver = email.To
            body = email.TextBody

            # 打印或保存邮件内容
            print("Subject:", subject)
            print("Sender:", sender)
            print("Receiver:", receiver)
            print("Body:", body)

            # 可以根据需要对邮件内容进行进一步处理
            # 比如保存到文件中、提取特定信息等

    except Exception as e:
        print("提取邮件内容时出现错误：", e)
    finally:
        # 退出 Foxmail 应用
        foxmail_app.Quit()

# 调用函数提取邮件内容
extract_foxmail_content()
