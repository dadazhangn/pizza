import email
import os

# 读取.eml文件
file_path = "生日邀请ww.eml"  # 替换为实际.eml文件的路径
with open(file_path, "rb") as f:
    msg = email.message_from_binary_file(f)
# print(msg)
# 打印邮件信息
print("Subject:", msg["Subject"])
print("From:", msg["From"])
print("To:", msg["To"])
print("Date:", msg["Date"])

# 如果邮件有附件，则保存附件
if msg.get_content_maintype() == "multipart":
    for part in msg.walk():
        if part.get_content_maintype() == "multipart" or part.get("Content-Disposition") is None:
            continue
        file_name = part.get_filename()
        if file_name:
            file_path = os.path.join("attachments", file_name)
            with open(file_path, "wb") as f:
                f.write(part.get_payload(decode=True))
            print("Attachment saved to:", file_path)

# 打印邮件正文
body = msg.get_payload(decode=True).decode(msg.get_content_charset())
print("Body:")
print(body)