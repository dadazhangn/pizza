
import imaplib
import email
import datetime


class EmailUtil:
     """
     Email帮助类
     """
     host = 'imap.163.com'  # 主机IP或者域名
     port = '993'  # 端口
     username = 'ZK19856632314@163.com'  # 用户名
     password = 'VIFNGSCGMUILNADY'  # 密码或授权码
     imap = None  # 邮箱连接对象

     mail_box = 'ZK19856632314@163.com'

     def __init__(self, host, port):
         """初始化方法"""
         self.host = host
         self.port = port
         # 初始化一个邮箱链接对象
         self.imap = imaplib.IMAP4_SSL(host=self.host, port=int(self.port))

     def login(self, username, password):
         """登录"""
         self.username = username
         self.password = password
         self.imap.login(user=self.username, password=self.password)

     def get_mail(self):
         """获取邮件"""
         self.mail_box = mail_box
         email_infos = []
         if self.imap is not None:
             self.imap.select(readonly=True)
             typ, data = self.imap.search(None, 'ALL')  # 返回一个元组，data为此邮箱的所有邮件数据
             #  数据格式 data =  [b'1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18']
             if typ == 'OK':
                 for num in data[0].split():
                     if int(num) > 10:
                         # 超过20，退出循环，不输出
                         break
                     typ1, data1 = self.imap.fetch(num, '(RFC822)')  # 通过邮箱编号和选择获取数据
                     if typ1 == 'OK':
                         print('**********************************begin******************************************')
                         msg = email.message_from_string(data1[0][1].decode("utf-8"))  # 用email库获取解析数据(消息体)
                         # 获取邮件标题并进行进行解码，通过返回的元组的第一个元素我们得知消息的编码
                         msgCharset = email.header.decode_header(msg.get('Subject'))[0][1]
                         # print('msg = ',msg)
                         # print('msgCharset= ',msgCharset)  # gb2312
                         recv_date = self.get_email_date(email.header.decode_header(msg.get('Date')))
                         mail_from = email.header.decode_header(msg.get('From'))[0][0]
                         if type(mail_from) == bytes:
                             mail_from = mail_from.decode(msgCharset)

                         mail_to = email.header.decode_header(msg.get('To'))[0][0]
                         subject = email.header.decode_header(msg.get('Subject'))[0][0].decode(msgCharset)  # 获取标题并通过标题进行解码

                         print("Message %s\n%s\n" % (num, subject))  # 打印输出标题
                         print('mail_from:' + mail_from + ' mail_to:' + mail_to + ' recv_date:' + str(recv_date))
                         # # 邮件内容
                         # for part in msg.walk():
                         #     if not part.is_multipart():
                         #         name = part.get_param("name")
                         #         if not name:  # 如果邮件内容不是附件可以打印输出
                         #             print(part.get_payload(decode=True).decode(msgCharset))
                         # print('***********************************end*****************************************')
                         email_info = {
                             "num": num,
                             "subject": subject,
                             "recv_date": recv_date,
                             "mail_to": mail_to,
                             "mail_from": mail_from
                         }
                         email_infos.append(email_info)
         else:
             print('请先初始化并登录')
         return email_infos

     def get_email_content(self, num):
         content = None
         typ1, data1 = self.imap.fetch(num, '(RFC822)')  # 通过邮箱编号和选择获取数据
         if typ1 == 'OK':
             print('**********************************begin******************************************')
             msg = email.message_from_string(data1[0][1].decode("utf-8"))  # 用email库获取解析数据(消息体)
             print(msg)
             # 获取邮件标题并进行进行解码，通过返回的元组的第一个元素我们得知消息的编码
             msgCharset = email.header.decode_header(msg.get('Subject'))[0][1]
             # transfer_encoding = email.header.decode_header(msg.get('Content-Transfer-Encoding'))
             transfer_encoding = email.utils.parseaddr(msg.get('Content-Transfer-Encoding'))[1]
             print("transfer_encoding:",transfer_encoding)
             print("charset:",msgCharset)
             # 邮件内容
             for part in msg.walk():
                 if not part.is_multipart():
                     name = part.get_param("name")
                     if not name:  # 如果邮件内容不是附件可以打印输出
                         if transfer_encoding == '8bit':
                             content = part.get_payload(decode=False)
                         else:
                             content = part.get_payload(decode=True).decode(msgCharset)

             print(content)
             print('***********************************end*****************************************')
         return content

     def get_email_date(self, date):
         """获取时间"""
         utcstr = date[0][0].replace('+00:00', '')
         utcdatetime = None
         localtimestamp = None
         try:
             utcdatetime = datetime.datetime.strptime(utcstr, '%a, %d %b %Y %H:%M:%S +0000 (GMT)')
             localdatetime = utcdatetime + datetime.timedelta(hours=+8)
             localtimestamp = localdatetime.timestamp()
         except:
             try:
                 utcdatetime = datetime.datetime.strptime(utcstr, '%a, %d %b %Y %H:%M:%S +0800 (CST)')
                 localtimestamp = utcdatetime.timestamp()
             except:
                 utcdatetime = datetime.datetime.strptime(utcstr, '%a, %d %b %Y %H:%M:%S +0800')
                 localtimestamp = utcdatetime.timestamp()
         return localtimestamp


if __name__ == '__main__':
     host = 'imap.163.com'  # 主机IP或者域名
     port = '993'  # 端口
     username = 'ZK19856632314@163.com'  # 用户名
     password = 'VIFNGSCGMUILNADY'  # 密码或授权码
     imap = None  # 邮箱连接对象
     mail_box = 'ZK19856632314@163.com'  # 邮箱名
     eamil_util = EmailUtil(host=host, port=port)
     eamil_util.login(username=username, password=password)
     eamil_util.get_mail()
     print('done')