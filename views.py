from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day
from . import textToWordcloud as ttwc
import pdb

def index(request):
    """
    日記の一覧を表示
    """
    context = {
        'day_list':Day.objects.all(),
    }
    return render(request, 'diary/day_index.html', context)



def add(request):

    """
    日記の記事を追加
    """
    # 送信内容を元にフォームを作る。POSTじゃなければ空のフォームを作成。
    form = DayCreateForm(request.POST or None)

    # method==POSTとは送信ボタンが押されたとき。form.is_validは入力内容に問題が無い場合Trueになる。
    if request.method == 'POST' and form.is_valid():
        #入力時にtextを取得しそのtextを画像に変換
        form.save()
        return redirect('diary:index')

    # 通常時のアクセスや入力内容に誤りがあれば、再度day_form.htmlを表示
    context = {
        'form':form
    }
    return render(request, 'diary/day_form.html', context)


def update(request, pk):
    """
    日記の記事を変更
    """
    # urlのpkを基に、Dayを取得（pkはidと同じ）
    day = get_object_or_404(Day, pk=pk)

    # formに取得したDayを紐づける
    form = DayCreateForm(request.POST or None, instance=day)

    # method=POST(送信ボタン押下)、でかつ、入力内容に問題がなければフォームを保存する。
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('diary:index')

    # 通常時のアクセスや入力内容に問題があった場合は最初のページを表示
    context = {
        'form':form
    }
    return render(request, 'diary/day_form.html', context)


def delete(request, pk):
    """
    日記の記事を削除
    """
    # URLのPKを基に、Dayを取得（pkはidと同じ）
    day = get_object_or_404(Day, pk=pk)

    # method=POST(送信ボタン押下)
    if request.method == 'POST':
        day.delete()
        return redirect('diary:index')

    # 通常時のアクセス。または問題があった場合のアクセス。
    context = {
        'day':day
    }
    return render(request, 'diary/day_delete.html', context)


def detail(request, pk):
    """
    日記の詳細ページ
    """
    #　URLのPKを基に、Dayを取得
    day = get_object_or_404(Day, pk=pk)
    text = day.text
    ttwc.create_wordcloud_ja(pk,text)
    #word_cloud_image = '../../wordcloud/'+str(pk)+'.png'

    context = {
        'day':day ,
        #'word_cloud':word_cloud_image
    }
    return render(request, 'diary/day_detail.html', context)
