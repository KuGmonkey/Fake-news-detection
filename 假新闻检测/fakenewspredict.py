# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:58:44 2021

@author: PC
"""

"""
#爬虫得到所有新闻text
import urllib.request
import random
from csv import reader
from bs4 import BeautifulSoup
from ua_info import ua_list

def request_html(url):
    headers={'User _Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    request=urllib.request.Request(url,headers=headers)
    return request

def parse_html(html,f):
    soup=BeautifulSoup(html,'html.parser')
    line_name=soup.select('.rich_media_content > p > span')
    if(len(line_name)!=0):
        for item in line_name:
            temp =item.text   
            f.write('\n'+temp)
def run():
     for i in range(10141):
        f=open('C:\\Users\\PC\\Desktop\\test_text'+str(i)+'.txt','w',encoding='utf-8')
        url=test_dataset['News Url'][i]
        request=request_html(url)
        html=urllib.request.urlopen(request).read().decode('utf-8')
        parse_html(html,f)
        f.close()        

run()
"""

#数据导入
import numpy as np
import pandas as pd
train_dataset=pd.read_csv(r'C:\Users\PC\Desktop\train.csv')
test_dataset=pd.read_csv(r'C:\Users\PC\Desktop\test.csv')
path='C:\\Users\\PC\\Desktop\\'
train_text=[]
for i in range(10587):
    temp=open(path+'train_text\\'+str(i)+'.txt','r',encoding='utf-8',errors='ignore')
    text=temp.read()
    train_text.append(text)
test_text=[]
for i in range(10141):
    temp=open(path+'test_text\\'+str(i)+'.txt','r',encoding='utf-8',errors='ignore')
    text=temp.read()
    test_text.append(text)
#将train和test合到一起
alltext=train_text
alltext.extend(test_text)

#print(train_dataset.head())
#print(test_dataset.head())
#print(train_text)

#数据合并
alltitle=list(pd.concat([train_dataset['Title'],test_dataset['Title']],axis=0))
allOfiicialAccountName=list(pd.concat([train_dataset['Ofiicial Account Name'],test_dataset['Ofiicial Account Name']],axis=0))
allcontent=list(pd.concat([train_dataset['Report Content'],test_dataset['Report Content']],axis=0))
coll=[]
for i in range(20728):
    s=str(allOfiicialAccountName[i])+str(alltitle[i])+str(alltext[i])+str(allcontent[i])
    coll.append(s)
#print(coll)

#中文分词，去除停用词
stop_word=[]
stopwordfile=open('C:\\Users\\PC\\Desktop\\stop_word.txt','r',encoding='utf-8',errors='ignore')
f=stopwordfile.read()
for word in f:
    stop_word.append(word)
cutcoll=[]
import jieba
for text in coll:
    words=jieba.cut(text)
    s=''
    for word in words:
        if word not in stop_word:
            if s!='':
                s=s+' '+word 
            else:
                s=word
    cutcoll.append(s)
#print(cutcoll)
#tf-idf特征构建，得到文档-词矩阵features，即tf-idf加权文档矩阵
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD,LatentDirichletAllocation
vectorizer=TfidfVectorizer(min_df=3, ngram_range=(1, 2),use_idf=1,smooth_idf=1,sublinear_tf=1)
intifeatures=vectorizer.fit_transform(cutcoll)

svd=TruncatedSVD(n_components=100,random_state=1400)
lda=LatentDirichletAllocation(n_components=10,random_state=1337,n_jobs=6)
#svd降维
svdfeatures=svd.fit_transform(intifeatures)
svdfeatures=pd.DataFrame(svdfeatures)
#lda降维
ldafeatures=lda.fit_transform(intifeatures)
ldafeatures=pd.DataFrame(ldafeatures)
#两个降维结果合并
features=[]
features.append(svdfeatures)
features.append(ldafeatures)
features=pd.concat(features,axis=1)
print(features)

#岭回归分类器进行训练和预测
from sklearn.linear_model import RidgeClassifier
clf=RidgeClassifier(alpha=1.0,normalize=True)
clf.fit(features[:train_dataset.shape[0]],train_dataset['label'])

from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import accuracy_score
y_predict=clf.predict(features[10587:])
print(accuracy_score(test_dataset['label'], y_predict))
print(precision_recall_fscore_support(test_dataset['label'], y_predict,average='binary'))

#ROC曲线数据
from sklearn.metrics import roc_curve,auc
fpr,tpr,threshold=roc_curve(test_dataset['label'], y_predict,pos_label=0)
roc_auc=auc(fpr,tpr)

#绘制曲线
import matplotlib.pyplot as plt
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Roc曲线')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.plot(fpr,tpr,color='r',linestyle='-',linewidth=1.0,label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='b', linestyle='--', linewidth=1.0)
plt.legend(loc='lower right',bbox_to_anchor=(0.2,0.95))
plt.show()


