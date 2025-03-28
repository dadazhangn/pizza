# 从邮箱中抓取最新的若干封邮件（已完成）
# 读取这些邮件的subject和sender以及内容（已完成）
# 在excel表格中写入对应的主题和sender（已完成）

import poplib
import email
from email.parser import Parser
import xlwt

host = 'imap.163.com'
username = 'ZK19856632314@163.com'
password = 'VIFNGSCGMUILNADY'


def get_email(topK):  # get least K emails

    server = poplib.POP3_SSL(host, 995)
    print(server.getwelcome())  # connected to email server

    server.user(username)
    server.pass_(password)  # log in the email account

    resp, mails, octets = server.list()
    print('Emails in account： ' + str(len(mails)))  # get some basic
    # info of account

    resp_status = []
    msg_contents = []  # K emails contents
    octets = []
    total_mails = len(mails)
    for i in range(topK):
        j = total_mails - i
        resp_statu, line, octet = server.retr(j)  # get one email content
        resp_status.append(resp_statu)
        msg_content = b'\r\n'.join(line).decode('gbk')  # line is list,
        # convert to string
        msg_contents.append(msg_content)
        octets.append(octet)

    msg = []
    for message in msg_contents:
        msg.append(Parser().parsestr(message))  # parser every email

    server.quit()

    return msg  # K emails ready to be read


def get_subject(message):
    subject = message.get('Subject')
    h = email.header.Header(subject)
    dh = email.header.decode_header(subject)
    head_line = dh[0][0].decode('utf-8')
    return head_line


def get_sender(message):
    sender = message.get('From')
    sender_addr = email.utils.parseaddr(sender)
    return sender_addr[1]


def get_content(message):
    parts = message.walk()
    content = ''
    for part in parts:
        if content == '':
            if part.is_multipart() is False:
                print(type(part))
                content = part.get_payload(decode=True).decode('utf-8')
                # there are twice content, one is text, one is HTML
    return content


msg = get_email(5)
hl = []
senders = []
contents = []

# write contents to an excel

f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
sheet1.write(0, 0, 'from')
sheet1.write(0, 1, 'content')
i = 1

for mssg in msg:
    head_line = get_subject(mssg)
    hl.append(head_line)
    sender = get_sender(mssg)
    senders.append(sender)
    sheet1.write(i, 0, sender)  # write the sender to excel
    content = get_content(mssg)
    sheet1.write(i, 1, content)  # write the content to excel
    contents.append(content)
    i += 1

f.save('excel.xls')
print('Please check with excel')
