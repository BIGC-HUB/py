import re, urllib.request, os, sys, random

def new ( ) :
    # 获取最新地址
    try :
        url = urllib.request.Request('http://jandan.net/ooxx/')
        url.add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/7.2.0.12990' ) #隐藏
        html = urllib.request.urlopen( url )
    except ( urllib.error.URLError ) :
        print( '网页打不开，请稍后 (或检查网络)' )
        sys.exit(0)
    miao = html.read( ).decode( 'UTF-8' )
    miao= re.search( '<span class="current-comment-page">\[(.+?)\]</span>' , miao ).group(1)
    return miao
def img (url) :
    # 打开网页并解析
    url = urllib.request.Request( url )
    url.add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/7.2.0.12990' ) #隐藏
    miao = urllib.request.urlopen( url ).read( ).decode( 'UTF-8' )
    img = re.findall( '<img src="(.+?)" /></p>' , miao )
    for i in range(len(img)):
        img[i] = 'http:' + img[i]
    return img
def down (miao) :
    # 下载图片并保存
    page = r'http://jandan.net/ooxx/page-%s#comments' % miao
    # 文件夹
    if not os.path.exists( r'./miao' ) :
        os.makedirs( r'./miao' )
    # 下载
    arr = img(page)
    for i in range(len(arr)):
        url = arr[i]
        path = './miao/%s.jpg' % i
        urllib.request.urlretrieve(url , path)
def kaishi ( ) :
    # 开始么
    miao = int( new( ) )
    print('最新页面地址：%s' % miao )
    while True :
        try :
            miao = int ( input ( '——————————\n第几页开始：' ) )
            x = int( input ( '要下载几页：' ) )
            break
        except ( ValueError ) :
            print( '请输入整数' )
    print( '正在下载 (～￣▽￣)～* 请耐心等候' )
    try :
        for i in range( x ) :
            down( miao - i )
            print( '第 %s 页完成' % ( miao - i ) )
    except ( urllib.error.URLError ) :
        print( '网页打不开 (╯▔皿▔)╯ 请稍后 (或检查网络)' )
        sys.exit(0)
    print( '\n完成 (●ˇ∀ˇ●) 保存在 %s\miao' % os.getcwd( ) )

if __name__ == '__main__' :
    kaishi( )
