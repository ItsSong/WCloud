#!/usr/bin/env python
#-*- coding = utf-8 -*-
import jieba
import wordcloud
f = open('新时代中国特色社会主义.txt','r',encoding="utf-8")
t = f.read()
f.close()

ls = jieba.lcut(t)   #分词，以列表形式返回
txt = " ".join(ls)   #将ls元素用空格分开
w = wordcloud.WordCloud(font_path="msyh.ttc",width=1000,height=700,background_color="white")
#设置词云字体微软雅黑；宽1000，高700；背景色白色
w.generate(txt)  #加载词云文本
w.to_file("grvernment.png")  #以图片格式输出词云文件