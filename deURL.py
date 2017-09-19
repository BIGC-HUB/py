import re, urllib.request, os, sys, random

def writeFile(path, s):
    # 打开
    fd = os.open(path, os.O_RDWR|os.O_CREAT)
    # 写入
    os.write(fd, bytes(s, 'UTF-8'))
    # 关闭
    os.close(fd)
    print('%s%s写入完成！' % os.getcwd(), path)

def main (url) :
    # 开始
    try :
        url = urllib.request.Request(url)
        url.add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/7.2.0.12990' ) #隐藏
        html = urllib.request.urlopen( url )
    except ( urllib.error.URLError ) :
        print( '网页打不开，请稍后 (或检查网络)' )
        sys.exit(0)
    # 解析 html
    miao = html.read().decode('UTF-8')
    # 写入
    writeFile("a.html", miao)

if __name__ == '__main__' :
    url = 'http://jandan.net/pic/'
    main(url)
