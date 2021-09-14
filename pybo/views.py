from django.shortcuts import render

import my_settings
from .models import NewsInfo
import pymysql


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
