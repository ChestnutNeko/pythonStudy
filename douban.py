# -*- codeing = utf-8 -*-

from bs4 import BeautifulSoup #网页解析
import re #正则表达式，进行文字匹配
import urllib.request,urllib.error #制定URL，获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行SQLite数据库操作

def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1、爬取网页
    datalist = getData(baseurl)
    # savepath = "豆瓣电影Top250.xls"
    dbpath = "movie.db"
    # 3、保存数据
    # saveData(datalist,savepath)
    saveDataDB(datalist,dbpath)

    # askURL("https://movie.douban.com/top250?start=")
# 影片链接
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片链接
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评论人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10): # 调用获取信息的页面10次
        url = baseurl + str(i*25)
        html = askURL(url) # 保存获取到的网页源码
        # 2、逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="item"):
            # print(item)
            data = []
            item = str(item)

            link = re.findall(findLink,item)[0]
            data.append(link)

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle,item)
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(" ") # 外国名字留空
            
            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if(len(inq) != 0):
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?"," ",bd)
            bd = re.sub("/"," ",bd)
            data.append(bd.strip())

            datalist.append(data)
    
    # print(datalist)
    return datalist

# 得到一个指定URL的网页内容
def askURL(url):
    head = { # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    } # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（本质上是告诉浏览器，我们可以接收什么水平的
    req = urllib.request.Request(url=url,headers=head)
    html = ""
    try:
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html
    

# 保存数据
def saveData(datalist,savepath):
    # 创建workbook对象
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    # 创建工作表
    sheet = book.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True)
    # 写入数据，行，列，内容
    col = ("电影详情链接","图片链接","影片中文名","影片外文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) # 列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    # 保存数据
    book.save(savepath)

def saveDataDB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
            insert into movie250 (info_link,pic_link,cname,score,ename,rated,introduction,info)
            values(%s)
        '''%",".join(data)
        # print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movie250
        (
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            introduction text,
            info text
        )
    ''' # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
    print("over")

# - ------- ---``- -------- ---``- 