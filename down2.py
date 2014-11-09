#!/usr/bin/python
# -*- coding: utf-8 -*-
import crifanLib
import urllib2
import thread
import random
import time
from Queue import Queue
import datetime
queue = Queue()

success = 0

def getProxy():
    # list from 
    list = [
        {"http":"http://111.13.2.130:80"},
        {"http":"http://119.4.95.135:80"},
        {"http":"http://117.21.192.10:80"},
        {"http":"http://61.156.35.2:3128"},
        {"http":"http://183.203.8.148:8080"},
        {"http":"http://103.249.181.5:3128"},
        {"http":"http://202.171.253.111:80"},
        {"http":"http://120.192.200.73:80"},
        {"http":"http://111.206.81.248:80"},
        {"http":"http://61.156.35.2:3128"},
        {"http":"http://207.91.10.234:8080"},
        {"http":"http://124.95.163.102:80"},
        {"http":"http://223.99.188.74:8090"},
        {"http":"http://218.108.242.108:3128"},
        {"http":"http://221.10.102.199:83"},
        {"http":"http://118.97.95.182:8080"},
        {"http":"http://27.50.128.242:88"},
        {"http":"http://218.206.83.89:80"},
        {"http":"http://117.79.64.84:80"},
        {"http":"http://111.13.2.137:80"},
        {"http":"http://111.13.2.139:80"},
        {"http":"http://218.108.232.99:80"},
        {"http":"http://111.13.2.130:80"},
        {"http":"http://111.11.184.83:80"},
        {"http":"http://111.11.184.83:80"},
        {"http":"http://117.27.245.98:80"},
        {"http":"http://125.39.66.76:80"},
        {"http":"http://202.107.85.47:3128"},
        {"http":"http://122.227.8.190:80"},
        {"http":"http://103.249.181.5:3128"},
        {"http":"http://221.183.16.219:80"},
        {"http":"http://218.108.242.108:3128"},
        {"http":"http://183.207.228.8:80"},
        {"http":"http://183.203.8.148:8080"},
        {"http":"http://111.11.184.17:80"},
        {"http":"http://218.59.144.95:80"},
        {"http":"http://223.99.188.74:8090"},
        {"http":"http://223.99.188.74:8090"},
        {"http":"http://111.13.12.202:80"},
        {"http":"http://121.42.24.86:80"},
        {"http":"http://119.4.95.135:80"},
        {"http":"http://122.227.8.190:80"},
        {"http":"http://58.137.171.115:8080"},
        {"http":"http://120.192.200.72:80"},
        {"http":"http://36.250.74.88:80"},
        {"http":"http://111.11.184.19:80"},
        {"http":"http://111.11.184.36:80"},
        {"http":"http://117.79.64.84:80"},
        {"http":"http://113.57.230.49:81"},
        {"http":"http://111.1.3.38:8000"},
        {"http":"http://221.183.16.219:80"},
        {"http":"http://183.207.232.193:8080"},
        {"http":"http://111.13.2.143:80"},
        {"http":"http://218.59.144.95:80"},
        {"http":"http://183.207.232.193:8080"},
        {"http":"http://218.108.232.99:80"},
        {"http":"http://218.201.38.49:80"},
        {"http":"http://111.206.81.248:80"},
        {"http":"http://120.192.200.72:80"},
        {"http":"http://111.206.81.248:80"},
        {"http":"http://202.56.231.117:8080"},
        {"http":"http://202.70.2.107:8088"},
        {"http":"http://120.192.200.73:80"},
        {"http":"http://117.135.194.53:80"},
        {"http":"http://111.11.184.43:80"},
        {"http":"http://122.227.8.190:80"},
        {"http":"http://111.13.109.51:80"},
        {"http":"http://203.151.21.184:3128"},
        {"http":"http://27.50.128.242:88"},
        {"http":"http://210.73.218.136:3128"},
        {"http":"http://223.99.188.74:8090"},
        {"http":"http://120.202.249.230:80"},
        {"http":"http://61.156.35.2:3128"},
        {"http":"http://117.135.194.52:80"},
        {"http":"http://37.239.46.50:80"},
        {"http":"http://111.206.81.248:80"},
        {"http":"http://117.135.194.52:80"},
        {"http":"http://113.105.142.228:80"},
        {"http":"http://117.135.194.53:80"},
        {"http":"http://117.135.194.53:80"},
        {"http":"http://58.215.142.208:80"},
        {"http":"http://121.14.138.50:17210"},
        {"http":"http://91.238.231.226:3128"},
        {"http":"http://91.238.231.226:3128"},
        {"http":"http://117.21.192.10:80"},
        {"http":"http://218.108.168.69:80"},
        {"http":"http://222.29.197.234:8080"},
        {"http":"http://123.125.114.167:80"},
        {"http":"http://123.125.114.167:80"},
        {"http":"http://112.5.253.83:80"},
        {"http":"http://112.5.253.83:80"},
        {"http":"http://101.69.197.23:80"},
        {"http":"http://120.203.214.187:80"},
        {"http":"http://183.207.228.8:80"},
        {"http":"http://85.114.141.191:80"},
        {"http":"http://111.13.2.140:80"},
        {"http":"http://111.1.61.23:80"},
        {"http":"http://183.207.228.9:80"},
        {"http":"http://111.11.184.44:80"},
        {"http":"http://111.13.2.138:80"},
        {"http":"http://111.13.2.139:80"},
        {"http":"http://111.205.122.222:80"},
        {"http":"http://125.39.66.76:80"},
        {"http":"http://111.11.184.84:80"},
        {"http":"http://117.27.245.98:80"},
        {"http":"http://124.95.163.102:80"},
        {"http":"http://122.227.8.190:80"},
        {"http":"http://218.65.132.38:80"},
        {"http":"http://111.13.2.138:80"},
        {"http":"http://117.27.157.111:8081"},
        {"http":"http://211.143.146.239:80"},
        {"http":"http://218.65.132.38:80"},
        {"http":"http://111.13.2.139:80"},
        {"http":"http://111.11.184.83:80"},
        {"http":"http://120.203.214.144:80"},
        {"http":"http://111.13.12.216:80"},
        {"http":"http://183.203.8.148:8080"},
        {"http":"http://218.107.217.70:3129"},
        {"http":"http://120.202.249.230:80"},
        {"http":"http://149.255.255.242:80"},
        {"http":"http://123.177.20.220:80"},
        {"http":"http://120.192.200.72:80"},
        {"http":"http://111.13.109.54:80"},
        {"http":"http://113.107.57.76:80"},
        {"http":"http://60.221.253.204:80"},
        {"http":"http://85.114.141.191:80"},
        {"http":"http://202.29.238.242:3128"},
        {"http":"http://203.86.8.235:8088"},
        {"http":"http://221.183.16.219:80"},
        {"http":"http://111.13.109.51:80"},
        {"http":"http://183.207.229.138:80"},
        {"http":"http://119.4.95.136:80"},
        {"http":"http://211.143.146.239:80"},
        {"http":"http://183.207.232.193:8080"},
        {"http":"http://183.207.232.119:8080"},
        {"http":"http://117.21.192.10:80"},
        {"http":"http://59.151.103.15:80"},
        {"http":"http://113.105.224.78:80"},
        {"http":"http://202.29.238.242:3128"},
        {"http":"http://218.108.168.69:80"},
        {"http":"http://111.13.2.142:80"},
        {"http":"http://58.42.236.241:80"},
        {"http":"http://85.114.141.191:80"},
        {"http":"http://117.21.192.7:80"},
        {"http":"http://60.190.138.151:80"},
        {"http":"http://60.190.138.151:80"},
        {"http":"http://58.42.236.241:80"},
        {"http":"http://123.177.20.220:80"},
        {"http":"http://203.80.144.4:80"},
        {"http":"http://218.90.174.167:3128"},
        {"http":"http://223.99.188.74:8090"},
        {"http":"http://203.80.144.4:80"},
        {"http":"http://37.239.46.58:80"},
        {"http":"http://221.176.14.72:80"},
        {"http":"http://117.167.100.247:8123"},
        {"http":"http://120.236.23.130:80"},
        {"http":"http://183.207.229.138:80"},
        {"http":"http://125.39.66.76:80"},
        {"http":"http://60.55.43.74:80"},
        {"http":"http://211.162.0.170:80"},
        {"http":"http://202.171.253.109:80"},
        {"http":"http://218.201.38.49:80"},
        {"http":"http://36.250.74.87:80"},
        {"http":"http://117.177.240.43:80"},
        {"http":"http://203.80.144.4:80"},
        {"http":"http://111.11.184.44:80"},
        {"http":"http://101.69.197.23:80"},
        {"http":"http://111.13.12.216:80"},
        {"http":"http://85.114.141.191:80"},
        {"http":"http://60.190.138.148:80"},
        {"http":"http://120.203.214.187:80"},
        {"http":"http://119.4.115.51:8090"},
        {"http":"http://218.207.172.237:80"},
        {"http":"http://36.250.74.87:80"},
        {"http":"http://218.206.83.89:80"},
        {"http":"http://117.21.192.10:80"},
        {"http":"http://123.125.114.167:80"},
        {"http":"http://182.118.31.110:80"},
        {"http":"http://111.11.184.43:80"},
        {"http":"http://111.11.184.40:80"},
        {"http":"http://111.11.184.83:80"},
        {"http":"http://119.4.95.136:80"},
        {"http":"http://111.1.61.23:80"},
        {"http":"http://36.250.74.88:80"},
        {"http":"http://203.151.21.184:3128"},
        {"http":"http://183.203.8.148:8080"},
        {"http":"http://113.105.142.228:80"},
        {"http":"http://111.11.184.79:80"},
        {"http":"http://182.118.23.7:8081"},
        {"http":"http://119.4.95.136:80"},
        {"http":"http://113.57.230.49:81"},
        {"http":"http://111.13.109.53:80"},
        {"http":"http://220.181.32.106:80"},
        {"http":"http://182.118.31.110:80"},
        {"http":"http://58.56.124.192:80"},
        {"http":"http://202.107.85.47:3128"},
        {"http":"http://113.140.25.4:81"},
        {"http":"http://111.205.122.222:80"},
        {"http":"http://59.151.103.14:80"},
        {"http":"http://183.207.229.138:80"},
        {"http":"http://123.125.114.167:80"},
        {"http":"http://182.118.31.110:80"},
        {"http":"http://41.73.230.39:8080"},
        {"http":"http://211.144.81.68:18000"},
        {"http":"http://181.49.15.166:3128"},
        {"http":"http://222.85.1.123:8118"},
        {"http":"http://122.227.8.190:80"},
        {"http":"http://59.46.72.245:8080"},
        {"http":"http://113.105.142.228:80"},
        {"http":"http://125.39.66.75:80"},
        {"http":"http://124.95.163.102:80"},
        {"http":"http://61.19.121.154:3128"},
        {"http":"http://190.121.230.148:8080"},
        {"http":"http://111.13.2.138:80"},
        {"http":"http://112.5.253.83:80"},
        {"http":"http://113.214.13.1:8000"},
        {"http":"http://115.239.210.199:80"},
        {"http":"http://115.29.166.133:82"},
        {"http":"http://111.1.3.38:8000"},
        {"http":"http://123.125.114.167:80"},
        {"http":"http://119.80.160.50:80"},
        {"http":"http://112.5.253.83:80"},
        {"http":"http://111.11.184.82:80"},
        {"http":"http://115.236.59.194:3128"},
        {"http":"http://59.151.103.15:80"},
        {"http":"http://183.207.229.137:80"},
        {"http":"http://119.97.146.148:80"},
        {"http":"http://36.250.74.87:80"},
        {"http":"http://218.108.232.99:80"},
        {"http":"http://60.190.138.151:80"},
        {"http":"http://60.190.138.151:80"},
        {"http":"http://111.67.76.6:80"},
        {"http":"http://111.11.184.103:80"},
        {"http":"http://120.192.200.73:80"},
        {"http":"http://125.39.66.76:80"},
        {"http":"http://120.203.214.144:80"},
        {"http":"http://183.207.228.6:80"},
        {"http":"http://111.11.184.83:80"},
        {"http":"http://36.250.74.88:80"},
        {"http":"http://115.239.210.199:80"},
        {"http":"http://121.14.138.50:17210"},
        {"http":"http://223.99.189.102:8090"},
        {"http":"http://115.28.11.165:8888"},
        {"http":"http://164.100.137.145:80"},
        {"http":"http://111.13.109.54:80"},
        {"http":"http://118.97.95.182:8080"},
        {"http":"http://117.21.192.9:80"},
        {"http":"http://112.65.44.67:3128"},
        {"http":"http://222.85.1.123:8118"},
        {"http":"http://101.4.60.43:80"},
        {"http":"http://111.11.184.17:80"},
        {"http":"http://85.19.211.48:80"},
        # {"http":"http://111.161.126.84:80"},
    ]
    return random.choice(list)

def getUserAgent():
    list = [
    'Mozilla/5.0 (Linux; Android 4.4.2; H30-T00 Build/HuaweiH30-T00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-N7100 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 4.2.1; zh-cn; MI 3 Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 XiaoMi/MiuiBrowser/1.0',
    'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; M353 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.114 Mobile Safari/537.36'
    ]
    return random.choice(list)

def access(proxy,url,userAgent):
    try:
        global queue
        starttime = int(time.time())
        crifanLib.initProxyAndCookie(proxy)
        request = urllib2.Request(url)
        request.add_header('User-Agent',userAgent)
        request.add_header("Accept", "*/*")
        request.add_header('Referer', "http://zhijian.360.cn/")
        request.add_header("Accept-Language", "zh-cn")
        request.add_header("Accept-Encoding", "gzip, deflate")
        request.add_header("Connection", "Keep-Alive")
        f = urllib2.urlopen(request,timeout = 300)
        data = f.read()
        global success
        success += 1
        speed = len(data)/(int(time.time()) - starttime)
        print "success:%d @ %s @ %f"%(success,datetime.datetime.now().strftime('%X'),speed) 
        f = open("proxy.log","a")
        f.write(proxy["http"]+"\n")
    except Exception, e:
        pass
        print e
    queue.put(1)


def main():
    global queue
    threads = []
    for i in xrange(20):
        queue.put(1)

    for x in xrange(10000):
        queue.get()
        # print getProxy()
        threads.append(thread.start_new(access, (getProxy(), "http://shouji.360tpcdn.com/141022/9b0725db456095ade7a40313df14317c/air.com.goodgamestudios.empirefourkingdoms.qihu_1011052.apk",getUserAgent())))

    for t in threads:
        t.join()  


if __name__ == '__main__':
    main()



