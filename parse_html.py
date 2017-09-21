#coding=utf-8
import re, urllib.request, os, sys, random, json
# 写入
def save(path, s, append=False):
    if append:
        mode = os.O_RDWR|os.O_CREAT|os.O_APPEND
    else:
        mode = os.O_RDWR|os.O_CREAT
        # 删除
        if os.access(path, os.F_OK|os.R_OK|os.W_OK):
            os.remove(path)
    # 打开
    f = os.open(path, mode)
    # 写入
    os.write(f, bytes(s, 'UTF-8'))
    # 关闭
    os.close(f)
    print('写入完成！%s\%s' % (os.getcwd(), path))
# 读取
def load(path):
    # 打开
    f = os.open(path, os.O_RDWR|os.O_CREAT)
    # 读取
    db = f.read().decode('UTF-8')
    # 关闭
    os.close(f)
    return db
# html
def init_html(url):
    # 开始
    try :
        url = urllib.request.Request(url)
        url.add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/7.2.0.12990' ) #隐藏
        data = urllib.request.urlopen( url )
    except ( urllib.error.URLError ) :
        print( '网页打不开，请稍后 (或检查网络)' )
        sys.exit(0)
    # 解析 html
    html = data.read().decode('UTF-8')
    return html
# li
def init_li(li):
    arr = []
    for div in li:
        o = {}
        # o['url'] 网址
        o['url'] = re.search('href="(.+?)"', div).group(1)
        # o['img'] 图片
        o['img'] = re.search('src="(.+?)!list', div).group(1)
        # o['title'] 名称
        o['title'] = re.search('alt="(.+?)"', div).group(1)
        # o['money'] 价格
        o['money'] = re.search('<span class="item-price"><i>&yen;<\/i>(.+?)<\/span>', div).group(1)
        dateCity = re.search('<span class="item-time">(.+?)<\/span>', div).group(1).split(' ')
        # o['date'] 时间
        o['date'] = dateCity[0]
        # o['city'] 城市
        o['city'] = dateCity[1][0:2]
        arr.append(o)
    return arr
# json
def init_json(url):
    html = init_html(url)
    li = re.findall('<li class="wonderful-listItem ">([\s\S]+?)<\/li>', html)
    arr = init_li(li)
    return arr
# main
def main():
    # 1 - 245
    start = 1
    end = 2
    # 写入
    for i in range(start, end + 1):
        print('提示：正在写入页码……', i)
        url = 'http://hd.8264.com/xianlu-0-0-0-0-0-2-' + str(i)
        arr = init_json(url)
        data = json.dumps(arr, indent=2, ensure_ascii=False)
        # 写入
        save("%s.json" % i, data)

if __name__ == '__main__' :
    main()
    print('运行结束')

# '''
# 姓名：{name}
# 网址：{url}'''.format(**{
#     'name': '瓜',
#     'url': 'space.bilibili.com/39066904',
# })
