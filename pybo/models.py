from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()



class CommentInfo(models.Model):
    comment_id = models.IntegerField(db_column='COMMENT_ID', primary_key=True)  # Field name made lowercase.
    comment_content = models.CharField(db_column='COMMENT_CONTENT', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    member = models.ForeignKey('MemberInfo', models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    news = models.ForeignKey('NewsInfo', models.DO_NOTHING, db_column='NEWS_ID')  # Field name made lowercase.
    comment_dttm = models.DateTimeField(db_column='COMMENT_DTTM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment_info'


class MemberInfo(models.Model):
    member_id = models.CharField(db_column='MEMBER_ID', primary_key=True, max_length=1000)  # Field name made lowercase.
    member_nm = models.CharField(db_column='MEMBER_NM', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    member_tel = models.CharField(db_column='MEMBER_TEL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    member_addr = models.CharField(db_column='MEMBER_ADDR', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    memeber_pass = models.CharField(db_column='MEMEBER_PASS', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member_info'


class NewsInfo(models.Model):
    news_id = models.IntegerField(db_column='NEWS_ID', primary_key=True)  # Field name made lowercase.
    news_title = models.CharField(db_column='NEWS_TITLE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    news_content = models.TextField(db_column='NEWS_CONTENT', blank=True, null=True)  # Field name made lowercase.
    news_good = models.IntegerField(db_column='NEWS_GOOD', blank=True, null=True)  # Field name made lowercase.
    news_notgood = models.IntegerField(db_column='NEWS_NOTGOOD', blank=True, null=True)  # Field name made lowercase.
    news_dttm = models.DateTimeField(db_column='NEWS_DTTM', blank=True, null=True)  # Field name made lowercase.
    news_editor = models.CharField(db_column='NEWS_EDITOR', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    media_outlets = models.CharField(db_column='MEDIA_OUTLETS', max_length=1000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'news_info'