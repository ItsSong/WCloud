#!/usr/bin/env python
#-*- coding = utf-8 -*-

import jieba
import wordcloud
f = open('关于实施乡村振兴战略的意见.txt','r',encoding="utf-8")
t = f.read()
f.close()

ls = jieba.lcut(t)   #分词，以列表形式返回
txt = " ".join(ls)   #将ls元素用空格分开
w = wordcloud.WordCloud(font_path="msyh.ttc",max_words= 15,width=1000,height=700,background_color="white")
#设置词云字体微软雅黑；max_words= 15表示最多显示15个字；宽1000，高700；背景色白色
w.generate(txt)  #加载词云文本
w.to_file("country.png")  #以图片格式输出词云文件