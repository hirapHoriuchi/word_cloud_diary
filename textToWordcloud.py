#coding: utf-8
from matplotlib import pyplot as plt
from wordcloud import WordCloud
import MeCab
import os
import pdb
import oseti

def create_wordcloud_ja(pk,text):
    current_dir = os.getcwd()
    analyzer = oseti.Analyzer()
    fontpath = '~/../usr/share/fonts/truetype/dejavu/Yasashisa.ttf'
    stop_words_ja = ['もの', 'こと', 'とき', 'そう', 'たち', 'これ', 'よう', 'これら', 'それ','です','ます']

    #形態素解析
    tagger = MeCab.Tagger()
    tagger.parse('')
    node = tagger.parseToNode(text)
    posi = 0
    nega = 0
    object_ngaposi = analyzer.count_polarity(text)
    posi = object_ngaposi[0]['positive']
    nega = object_ngaposi[0]['negative']


    word_list = []
    while node:
        word_type = node.feature.split(',')[0]
        word_surf = node.surface.split(',')[0]
        if word_type == '名詞' and word_surf not in stop_words_ja:
            word_list.append(node.surface)
        node = node.next

    word_chain = ' '.join(word_list)
    #pdb.set_trace()
    if posi >= nega:
         wc = WordCloud(font_path=fontpath,
                          width=500,
                          height=300,
                          background_color='white',
                          stopwords=set(stop_words_ja)).generate(word_chain)
    else :
        wc = WordCloud(font_path=fontpath,
                          width=500,
                          height=300,
                          stopwords=set(stop_words_ja)).generate(word_chain)

    wc.to_file("media/images/" + str(pk)+ ".png")
    print('generate :'+ str(pk)+ ".png")


def proccess_word_rstrip(text):
  text = text.replace('\n',' ')
  text = text.replace('\r',' ')
  return text


def create_spa_wordcloud_ja(text):
    current_dir = os.getcwd()
    fontpath = '~/../usr/share/fonts/truetype/dejavu/Yasashisa.ttf'
    stop_words_ja = ['もの', 'こと', 'とき', 'そう', 'たち', 'これ', 'よう', 'これら', 'それ','です','ます']

    #形態素解析
    tagger = MeCab.Tagger()
    tagger.parse('')
    node = tagger.parseToNode(text)

    word_list = []
    while node:
        word_type = node.feature.split(',')[0]
        word_surf = node.surface.split(',')[0]
        if word_type == '名詞' and word_surf not in stop_words_ja:
            word_list.append(node.surface)
        node = node.next

    word_chain = ' '.join(word_list)
    #pdb.set_trace()
    wc = WordCloud(font_path=fontpath,
                          width=500,
                          height=300,
                          stopwords=set(stop_words_ja)).generate(word_chain)

    wc.to_file("media/images/" + "spa"+ ".png")
    print('generate :'+ "spa"+ ".png")
    img_root = "media/images/" + "spa"+ ".png"
    #return word_cloud_image
    return img_root
