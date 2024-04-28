import os
import re
from email.parser import Parser
from bs4 import BeautifulSoup


def read_mail(path):
    if os.path.exists(path):
        with open(path) as fp:
            email = fp.read()
            return email
    else:
        print("file not exist!")


def emailInfo(emailpath):
    raw_email = read_mail(emailpath)  # 将邮件读到一个字符串里面
    # print('emailpath : ', emailpath)
    emailcontent = Parser().parsestr(raw_email)  # 经过parsestr处理过后生成一个字典
    # for k,v in emailcontent.items():
    #     print(k,v)
    # From = emailcontent['From']
    # To = emailcontent['To']
    # Subject = emailcontent['Subject']
    # Date = emailcontent['Date']
    # MessageID = emailcontent['Message-ID']
    # XOriginatingIP = emailcontent['X-Originating-IP']
    # if "<" in From:
    #     From = re.findall(".*<(.*)>.*", From)[0]
    # if "<" in To:
    #     To = re.findall(".*<(.*)>.*", To)[0]

    # print("From:\t", From)
    # print("X-Originating-IP", XOriginatingIP)
    # print("To:\t", To)
    # print("Subject:\t", Subject)
    # print("Message-ID:\t", MessageID)
    # print("Date:\t", Date)

    contents = ""
    # 循环信件中的每一个mime的数据块
    for par in emailcontent.walk():
        if not par.is_multipart():  # 这里要判断是否是multipart，是的话，里面的数据是无用的
            content = par.get_payload(decode=True)
            # print(str(content,"utf-8",errors='ignore'))
            # print("content:\t", content.decode(encoding='gbk'))  # 解码出文本内容，直接输出来就可以了。
            content = content.decode(encoding='gbk')
            contents = content + " "
    return contents


if __name__ == '__main__':
    email = "生日邀请ww.eml"
    # 提取<div>标签中的文本内容
    soup = BeautifulSoup(emailInfo(email), "html.parser")
    mail_content = soup.find("div").get_text()
    print(mail_content)
    match = re.search(r"(.*)\.eml",email)
    if match:
        result = match.group(1)+".txt"
        # 提取.eml文件名作为保存的txt文件名
        with open(result, "w", encoding="utf-8") as f:
            f.write(mail_content)

    else:
        print("match not exist!")
