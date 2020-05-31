# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time,random
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr,formataddr
import smtplib
import threading
from fake_useragent import UserAgent
from pyquery import PyQuery as pq
import traceback, sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#去除警告信息
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#构造随机的useragent
ua = UserAgent()

#Ethereal请求头
cookies = {
    
}

params = (
    
)

#Underground请求头
cookies2 = {
    
    
}

headers2 = {
    
}

#Havoc请求头
headers3 = {
    
}

params3 = (
   
)

#Uperf请求头
cookies4 = {
    
}

headers4 = {
    
}



#Havoc
def spider_havoc(mylist,url_first):
    f=requests.get(url=url_first,headers=headers3,params=params3)
    f.encoding = 'gbk2312'
    listmain=f.text
    lb=BeautifulSoup(listmain,'lxml')
    lm=lb.find_all('ul',class_='timeline')
    lm_str=BeautifulSoup(str(lm),'lxml')
    lc = lm_str.find_all('a')
    new_lc = lc[0:10]
    for name in new_lc:
        names = name.string
        sname = ''.join(names.split())
        mylist.append(sname)
    return mylist

#Underground
def spider_underground(mylist,url_second):
    f=requests.get(url=url_second,headers=headers2,cookies=cookies2)
    f.encoding = 'gbk2312'
    listmain=f.text
    lb=BeautifulSoup(listmain,'lxml')
    lm=lb.find_all('div',class_='f1 flex-auto min-width-0 text-normal')
    lm_str=BeautifulSoup(str(lm),'lxml')
    lc = lm_str.find_all('a')
    new_lc = lc[0]
    for name in new_lc:
        names = name.string
        sname = ''.join(names.split())
        mylist.append(sname)
    return mylist

#Ethereal
def spider_ethereal(mylist,url_third,new_ua,proxies_eth):
    headers = {
    'authority': 'androidfilehost.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': new_ua,
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
}
    f=requests.get(url=url_third,headers=headers,params=params, cookies=cookies,verify=False,proxies = proxies_eth)
    f.encoding = 'gbk2312'
    listmain=f.text
    lb=BeautifulSoup(listmain,'lxml')
    lm=lb.find_all('div',class_='col-xs-8 col-sm-9 file-name')
    lm_str=BeautifulSoup(str(lm),'lxml')
    lc = lm_str.find_all('a')
    new_lc = lc[0]
    for name in new_lc:
        names = name.string
        sname = ''.join(names.split())
        mylist.append(sname)
    return mylist

#Uperf
def spider_uperf(mylist,url_second):
    f=requests.get(url=url_second,headers=headers4,cookies=cookies4)
    f.encoding = 'gbk2312'
    listmain=f.text
    lb=BeautifulSoup(listmain,'lxml')
    lm=lb.find_all('div',class_='f1 flex-auto min-width-0 text-normal')
    lm_str=BeautifulSoup(str(lm),'lxml')
    lc = lm_str.find_all('a')
    new_lc = lc[0]
    for name in new_lc:
        names = name.string
        sname = ''.join(names.split())
        mylist.append(sname)
    return mylist

#定义一个格式化函数（对含有中文的字段通过Header编码）
def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

#输入Email地址口令
from_addr = 'xxx'
password = 'xxx'
#输入收件人地址
to_addr = 'xxx'
#输入SMTP服务器地址
smtp_server = 'smtp.sina.com'

# msg = MIMEText("Hello!I'm Such!",'plain','utf-8')#第一个参数为正文，第二个参数表示为纯文本，第三个参数保证语言兼容性
#Havoc
msg = MIMEText('Havoc有更新！','plain','utf-8') #发送html格式
msg['From'] = _format_addr('Havoc <%s>'% from_addr)
msg['To'] = _format_addr('管理员 <%s>'% to_addr)
msg['Subject'] = Header('[Havoc]','utf-8').encode()

#Ethereal
msg2 = MIMEText('Ethereal内核有更新！','plain','utf-8') #发送html格式
msg2['From'] = _format_addr('Ethereal <%s>'% from_addr)
msg2['To'] = _format_addr('管理员 <%s>'% to_addr)
msg2['Subject'] = Header('[Ethereal]','utf-8').encode()

#Underground
msg3 = MIMEText('Underground内核有更新！','plain','utf-8') #发送html格式
msg3['From'] = _format_addr('Underground <%s>'% from_addr)
msg3['To'] = _format_addr('管理员 <%s>'% to_addr)
msg3['Subject'] = Header('[Underground]','utf-8').encode()

#Uperf
msg4 = MIMEText('Uperf有更新！','plain','utf-8') #发送html格式
msg4['From'] = _format_addr('Yc调度 <%s>'% from_addr)
msg4['To'] = _format_addr('管理员 <%s>'% to_addr)
msg4['Subject'] = Header('[Uperf]','utf-8').encode()

#发送文本邮件
def send_mail(msg):
    server = smtplib.SMTP(smtp_server,25) #SMTP协议默认端口为25
    server.set_debuglevel(1) #打印发送流程
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr],msg.as_string()) #[]表示可以有多个收件人，逗号分开
    server.quit()


#发送异常文本邮件
def send_mail_false(log):
    server = smtplib.SMTP(smtp_server,25) #SMTP协议默认端口为25
    server.set_debuglevel(1) #打印发送流程
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr],log.as_string()) #[]表示可以有多个收件人，逗号分开
    server.quit()

#spider
#havoc
def find_mido(list1):
    for i in range(0, len(list1)):
        if list1[i].find("mido") == 1:
            # print('Havoc有更新！')
            send_mail(msg)
            quit()
            global flag1
            flag1 = False
        else:
            pass


#Underground
def find_underground(list2):
    global old_name2
    if list2[0] != old_name2:
        # print('Underground有更新！')
        old_name2 = list2[0]
        send_mail(msg3)
        quit()
        global flag2
        flag2 = False
    else:
        pass

#Ethereal
def find_ethereal(list3):
    global old_name3
    if list3[0] != old_name3:
        # print('Ehthereal有更新！')
        old_name3 = list3[0]
        send_mail(msg2)
        quit()
        global flag3
        flag3 = False
    else:
        pass

#Uperf
def find_uperf(list4):
    global old_name4
    if list4[0] != old_name4:
        # print('Uperf有更新！')
        old_name4 = list4[0]
        send_mail(msg4)
        quit()
        global flag4
        flag4 = False
    else:
        pass

#处理函数
#havoc
def havoc_main():
    while True:
        global num1
        try:
            # print("Havoc启动成功！")
            sp1 = spider_havoc([],url_first)
            find_mido(sp1)
            global flag1
            if flag1 == False:
                # print("Uperf休眠")
                time.sleep(604800) #睡眠7天
                # print("Uperf重启")
                flag1 = True
            else:
                # print("Havoc休眠")
                time.sleep(300) #5分钟spider一次
            num1 = 0
        except Exception as e:
            # print('Havoc出现异常！')
            # print(e)
            num1 += 1
            time.sleep(600)
            if num1 >= 10:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                error = str(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))  # 将异常信息转为字符串
                log = MIMEText(error,'plain','utf-8')
                log['From'] = _format_addr('Havoc <%s>'% from_addr)
                log['To'] = _format_addr('管理员 <%s>'% to_addr)
                log['Subject'] = Header('[Havoc Error]','utf-8').encode()
                send_mail_false(log)
                num1 = 0
                time.sleep(1800)

#Underground
def underground_main():
    while True:
        global num2
        try:
            # print("Underground启动成功！")
            sp2 = spider_underground([],url_second)
            find_underground(sp2)
            global flag2
            if flag2 == False:
                # print("Underground休眠")
                time.sleep(604800) #睡眠7天
                # print("Underground重启")
                flag2 = True
            else:
                # print("Underground休眠")
                time.sleep(3600) #1h spider一次
            num2 = 0
        except Exception as e2:
            # print('Underground出现异常！')
            # print(e2)
            num2 += 1
            time.sleep(600)
            if num2 >= 10:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                error = str(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))  # 将异常信息转为字符串
                log2 = MIMEText(error,'plain','utf-8')
                log2['From'] = _format_addr('Underground <%s>'% from_addr)
                log2['To'] = _format_addr('管理员 <%s>'% to_addr)
                log2['Subject'] = Header('[Underground Error]','utf-8').encode()
                send_mail_false(log2)
                num2 = 0
                time.sleep(1800)

#Ethereal
def ethereal_main():
    get = GetProxy()
    # print("获取ip地址中...")
    get.start() #获取ip地址
    # print("获取ip地址成功")
    while True:
        global num3
        global ip_error
        try:
            # print("Ethereal启动成功！")
            new_ua = ua.random #刷新UserAgent
            sp3 = spider_ethereal([],url_third,new_ua,proxies_eth)
            find_ethereal(sp3)
            global flag3
            if flag3 == False:
                # print("Ethereal休眠")
                ip_error = 0
                time.sleep(604800) #睡眠7天
                # print("Ethereal睡眠完毕")
                # print("更新ip...")
                get.start()
                get.update_ip()
                for i in range(20-num3):  #判断处理空ip地址
                    if len(proxies_eth) == 0:
                        get.update_ip()
                        num3 += 1
                    else:
                        print("ip更新完成！")
                        print("新的ip：",proxies_eth)
                        break
                # print("Ethereal重启")
                flag3 = True
            else:
                # print("Ethereal休眠")
                time.sleep(3600) #1h spider一次
            num3 = 0
        except Exception as e3:
            # print('Ethereal出现异常！')
            # print(e3)
            # print("当前使用ip：",proxies_eth)
            # print("更新ip...")
            ip_error = num3 * 5 #每次从5个ip中检查出可用的ip
            get.update_ip() #更新ip
            num3 += 1
            for i in range(20-num3):  #判断处理不可用ip地址
                if len(proxies_eth) == 0:
                    get.update_ip()
                    num3 += 1
                else:
                    # print("ip更新完成！")
                    # print("新的ip：",proxies_eth)
                    break
            if num3 >= 20: #ip源收集地址单页100个ip，如果都不能用，则更新ip池，发送错误邮件
                get.start()
                exc_type, exc_value, exc_traceback = sys.exc_info()
                error = str(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))  # 将异常信息转为字符串
                log3 = MIMEText(error,'plain','utf-8')
                log3['From'] = _format_addr('Ethereal <%s>'% from_addr)
                log3['To'] = _format_addr('管理员 <%s>'% to_addr)
                log3['Subject'] = Header('[Ethereal Error]','utf-8').encode()
                send_mail_false(log3)
                num3 = 0
                time.sleep(1800)

#Uperf
def uperf_main():
    while True:
        global num4
        try:
            # print("Uperf启动成功！")
            sp4 = spider_uperf([],url_forth)
            find_uperf(sp4)
            global flag4
            if flag4 == False:
                # print("Uperf休眠")
                time.sleep(172800) #睡眠2天
                # print("Uperf睡眠完毕")
                # print("Uperf重启")
                flag4 = True
            else:
                # print("Uperf休眠")
                time.sleep(900) #15min spider一次
            num4 = 0
        except Exception as e4:
            # print('Uperf出现异常！')
            # print(e4)
            num4 += 1
            time.sleep(600)
            if num4 >= 10:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                error = str(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))  # 将异常信息转为字符串
                log4 = MIMEText(error,'plain','utf-8')
                log4['From'] = _format_addr('Uperf <%s>'% from_addr)
                log4['To'] = _format_addr('管理员 <%s>'% to_addr)
                log4['Subject'] = Header('[Uperf Error]','utf-8').encode()
                send_mail_false(log4)
                num4 = 0
                time.sleep(1800)

#ip地址池更新
class GetProxy(object):
    def __init__(self):
        # 代理ip网站
        self.url = 'https://www.xicidaili.com/wt/'
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
        # self.file = r'C:\Users\cheng\Desktop\havoc\proxies.txt'
        # 用于检查代理ip是否可用
        self.check_url = 'https://www.python.org/'
        self.title = 'Welcome to Python.org'


    def get_page(self):
        response = requests.get(self.url, headers=self.header)
        # print(response.status_code)
        return response.text

    def page_parse(self, response):
        stores = []
        result = pq(response)('#ip_list')
        for p in result('tr').items():
            if p('tr > td').attr('class') == 'country':
                ip = p('td:eq(1)').text()
                port = p('td:eq(2)').text()
                protocol = p('td:eq(5)').text().lower()
                # if protocol == 'socks4/5':
                #     protocol = 'socks5'
                proxy = '{}://{}:{}'.format(protocol, ip, port)
                stores.append(proxy)
        return stores

    def start(self):
        global proxies
        response = self.get_page()
        proxies = self.page_parse(response)

    #切换正在使用的ip
    def update_ip(self):
        global proxies_eth
        global ip_error
        global proxies
        proxies_eth.clear() #清除旧ip
        for proxy in proxies[ip_error:ip_error + 5]: #每次检查5个ip
            try:
                check = requests.get(self.check_url, headers=self.header, proxies={'http': proxy}, timeout=5)
                check_char = pq(check.text)('head > title').text()
                if check_char == self.title and len(proxies_eth) < 1:
                    proxy1 = {"http":proxy}
                    proxies_eth.update(proxy1)
                    i += 1
                else:
                    pass
            except Exception as e:
                continue

if __name__ == '__main__':
    url_first = 'https://sourceforge.net/p/havoc-os/activity/'
    url_second = 'https://github.com/Zile995/android_kernel_xiaomi_msm8953/releases'
    url_third = 'https://androidfilehost.com/?w=profile&uid=11410963190603853242'
    url_forth = 'https://github.com/yc9559/uperf/releases'
    #设置代理ip
    proxies_eth = {
    "http":"http://61.135.155.82:443"
}
    # print('Running...')

    flag1 = True
    flag2 = True
    flag3 = True
    flag4 = True
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0

    proxies = []
    ip_error = 0

    old_name2 = "UndergroundKernel-mido-20200407"
    old_name3 = "EtherealXO-27.0~Serenity-GCC930-STOCKVIB-Mido-20200424.zip"
    old_name4 = "v1(20200516)"

#启动多线程
    try:
        print('thread %s is runing...'%(threading.current_thread().name))
        t=threading.Thread(target=havoc_main,name='Havoc')
        t1=threading.Thread(target=underground_main,name='Underground')
        t2=threading.Thread(target=ethereal_main,name='Ethereal')
        t3=threading.Thread(target=uperf_main,name='Uperf')
        t.start()
        t1.start()
        t2.start()
        t3.start()

    except Exception as e:
        # print("主程序错误！")
        exc_type, exc_value, exc_traceback = sys.exc_info()
        error = str(repr(traceback.format_exception(exc_type, exc_value, exc_traceback)))  # 将异常信息转为字符串
        log5 = MIMEText(error,'plain','utf-8')
        log5['From'] = _format_addr('Main Checker <%s>'% from_addr)
        log5['To'] = _format_addr('管理员 <%s>'% to_addr)
        log5['Subject'] = Header('[Main Error]','utf-8').encode()
        send_mail_false(log5)