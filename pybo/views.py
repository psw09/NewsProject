import pymysql
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import NewsInfo


def index(request):
    newsList = NewsInfo.objects.all().order_by('-news_dttm')

    print(newsList)
    return render(request, 'pybo/index.html', {'newsList': newsList})


def newsDetail(request):
    newsId = request.GET.get('newsId')

    conn = pymysql.connect(host='localhost', user='root', password='root', db='news_db', charset='utf8')
    curs = conn.cursor()

    sql = """
            SELECT NEWS_ID, NEWS_TITLE, NEWS_CONTENT, NEWS_DTTM, NEWS_EDITOR, MEDIA_OUTLETS, NEWS_GOOD, NEWS_NOTGOOD
            FROM news_db.news_info
            WHERE NEWS_ID = {newsId}
          """.format(newsId=newsId)
    curs.execute(sql)
    rows = curs.fetchall()

    conn.close()

    newsList = {
        'newsId': rows[0][0]
        , 'newsTitle': rows[0][1]
        , 'newsContent': rows[0][2]
        , 'newsDttm': rows[0][3]
        , 'newsEditor': rows[0][4]
        , 'mediaOutlets': rows[0][5]
        , 'newsGood': rows[0][6]
        , 'newsNotgood': rows[0][7]
    }

    print(newsList)
    return render(request, 'pybo/newsDetail.html', newsList)


def newsInsert(request):
    conn = pymysql.connect(host='localhost', user='root', password='root', db='news_db', charset='utf8')
    curs = conn.cursor()

    sql = """
            SELECT NEWS_TITLE, NEWS_CONTENT, NEWS_DTTM, NEWS_EDITOR, MEDIA_OUTLETS
            FROM news_db.news_info

          """
    curs.execute(sql)
    rows = curs.fetchall()

    conn.close()
    newsList = {'newsList': rows}
    return render(request, 'pybo/newsInsert.html', newsList)


def newsInsertVal(request):
    if request.method == "POST":
        newsTitle = request.POST.get("newsTitle");
        newsContent = request.POST.get("newsContent");
        newsEditor = request.POST.get("newsEditor");
        mediaOutlets = request.POST.get("mediaOutlets");

    conn = pymysql.connect(host='localhost', user='root', password='root', db='news_db', charset='utf8')
    curs = conn.cursor()

    sql = """
            INSERT INTO news_info (NEWS_TITLE,
                                  NEWS_CONTENT,
                                  NEWS_DTTM,
                                  NEWS_EDITOR,
                                  MEDIA_OUTLETS)
                                 VALUES('{newsTitle}',
                                      '{newsContent}',
                                      now(),
                                      '{newsEditor}',
                                      '{mediaOutlets}')
          """.format(newsTitle=newsTitle, newsContent=newsContent, newsEditor=newsEditor, mediaOutlets=mediaOutlets)
    curs.execute(sql)

    conn.commit()
    conn.close()
    return redirect('/pybo')


def goodCnt(request):
    if request.method == "POST":
        goodCnt = request.POST.get("goodCnt");
        newsId = request.POST.get("newsId");

    print("newsId")

    goodCnt = int(goodCnt)+1
    conn = pymysql.connect(host='localhost', user='root', password='root', db='news_db', charset='utf8')
    curs = conn.cursor()

    sql = """
            UPDATE `news_db`.`news_info`
            SET
            `NEWS_GOOD` = {goodCnt}
            WHERE `NEWS_ID` ={newsId}
          """.format(goodCnt=goodCnt, newsId=newsId)
    curs.execute(sql)

    conn.commit()
    conn.close()

    goodCnt = {"goodCnt": goodCnt}
    return JsonResponse(goodCnt)


def notGoodCnt(request):
    if request.method == "POST":
        notGoodCnt = request.POST.get("notGoodCnt");
        newsId = request.POST.get("newsId");


    notGoodCnt = int(notGoodCnt)+1
    conn = pymysql.connect(host='localhost', user='root', password='root', db='news_db', charset='utf8')
    curs = conn.cursor()

    sql = """
            UPDATE `news_db`.`news_info`
            SET
            `NEWS_NOTGOOD` = {notGoodCnt}
            WHERE `NEWS_ID` ={newsId}
          """.format(notGoodCnt=notGoodCnt, newsId=newsId)
    curs.execute(sql)

    conn.commit()
    conn.close()

    notGoodCnt = {"notGoodCnt": notGoodCnt}
    return JsonResponse(notGoodCnt)


def newsDelete(request):
    newsId = request.GET.get('newsId')

    conn = pymysql.connect(host='localhost', user='root', password='root', db='news_db', charset='utf8')
    curs = conn.cursor()

    sql = """
        DELETE FROM `news_db`.`news_info`
        WHERE {newsId}
          """.format(newsId=newsId)
    curs.execute(sql)

    conn.commit()
    conn.close()
    return redirect('/pybo')