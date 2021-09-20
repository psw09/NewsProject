from django.shortcuts import render, redirect

import my_settings
from .models import NewsInfo
import pymysql
from django import forms


def index(request):
    """
    pybo 목록 출력
    """
    newsList = NewsInfo.objects.all()

    return render(request, 'pybo/index.html', {'newsList': newsList})


def newsDetail(request):
    conn = pymysql.connect(host='localhost', user='root', password='root', db='news_db', charset='utf8')
    curs = conn.cursor()

    sql = """
            SELECT NEWS_TITLE, NEWS_CONTENT, NEWS_DTTM, NEWS_EDITOR, MEDIA_OUTLETS
            FROM news_db.news_info
          """
    curs.execute(sql)
    rows = curs.fetchall()
    print(rows)
    conn.close()
    newsList = {'newsList': rows}
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
    print(rows)
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
          """.format(newsTitle=newsTitle, newsContent=newsContent,newsEditor=newsEditor,mediaOutlets=mediaOutlets)
    curs.execute(sql)

    conn.commit()

    conn.close()
    return redirect('/pybo')