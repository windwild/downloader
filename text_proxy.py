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


def get_proxy():
	url = "http://proxies.site-digger.com/?token=sha1$3b09a$2a1446c3774a7d06b2d49da193b0540ef7f445d0&output=json"
	try:
		
        global queue
        starttime = int(time.time())
        crifanLib.initProxyAndCookie(proxy)
        request = urllib2.Request("http://zhijian.360.cn", timeout = 1)
        request.add_header('User-Agent',userAgent)
        request.add_header("Accept", "*/*")
        request.add_header('Referer', "http://zhijian.360.cn/")
        request.add_header("Accept-Language", "zh-cn")
        request.add_header("Accept-Encoding", "gzip, deflate")
        request.add_header("Connection", "Keep-Alive")
        f = urllib2.urlopen(request)
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
        f = urllib2.urlopen(request)
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



