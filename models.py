from django.db import models
from django.utils import timezone
from . import textToWordcloud as ttwc


import pdb

class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateField('日付', default=timezone.now)

    #wordcloud_image =ttwc.create_wordcloud_ja(text)
