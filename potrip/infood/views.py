from io import BytesIO
from django.shortcuts import render
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import matplotlib.pyplot as plt5
import matplotlib.pyplot as plt6
import matplotlib.pyplot as plt7
import matplotlib.pyplot as plt8
import matplotlib.pyplot as plt9
import matplotlib.pyplot as plt10
import matplotlib.pyplot as plta
from apyori import apriori
from matplotlib import colors
import pymysql
import numpy as np
from PIL import Image
import os
import io
import urllib
import base64
import pandas as pd
import dataframe_image as dfi
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

plt.rcParams["font.family"] = "Microsoft JhengHei"
plt.rcParams['axes.unicode_minus']=False

# Create your views here.
def infood_view(request):
   
    plt.rcParams['font.sans-serif']="Microsoft JhengHei"
    plt.rcParams['axes.unicode_minus']=False 


    file = "C:/Users/Justin/OneDrive/桌面/INFOOD/ui/file/pit2.png"
    if os.path.exists(file):
        os.remove(file)
    else:
        print()
    #连接数据库
    db = pymysql.connect(host='localhost',user='root',passwd='1234',port=3306,db='in-food')

#开启一个游标cursor
    cursor=db.cursor()

#获取phone数据表里的所有数据
    sql='select * from food_inserttrack'
#执行sql中的语句
    cursor.execute(sql)
    s=cursor.execute(sql)

#---------------------------------------------------------------------抓出food_inserttrack名稱
    aursor=db.cursor()
#定义需要用上的空数据数组，然后通过遍历数据库的数据将数据附上去
    x1=[]
    x3=[]
    i=0
    e=0
    while i<s:
        aursor.execute("SELECT buyfrom FROM `in-food`.food_inserttrack")
        myresult = aursor.fetchall()
        if (myresult[i]) not in x1:
            x1.append( myresult[i])
            i=i+1
        else :
            i=i+1     
    while e<s:
        aursor.execute("SELECT buyfrom FROM `in-food`.food_inserttrack")
        myresult = aursor.fetchall()
        if  ("".join(myresult[e])) not in x3:
            x3.append( "".join(myresult[e]))
            e=e+1
        else :
            e=e+1 
#-----------------------------------------------------------------------抓出food_inserttrack有幾個值

    x2=[]
    ii=0
    p=x1.count(x1[ii])
    ss=len(x1)
    while ii<ss:
        p=myresult.count(x1[ii])
        x2.append(float(p))
        ii=ii+1
#------------------------------------------------------------------------
    plt.switch_backend('agg')
    plt.pie(x2,labels=x3,textprops = {"fontsize" : 16,"color":"#000000"},autopct="%2.1f%%",shadow=True,labeldistance=1.3)
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    datae=base64.encodebytes(buffer.getvalue()).decode()
    context= 'data:image/png;base64,' +str(datae)
    plt.close()
    aursor=db.cursor()
#---------------------------------------------------------------------豆蛋魚肉類回購次數
    wursor=("SELECT foodname FROM `in-food`.food_inserttrack where food_type='豆蛋魚肉類'")
    aursor.execute(wursor)
    rowa = [item[0] for item in aursor.fetchall()]
    x1=[]
    e=0
    s=len(rowa)
    while e<s:
        if e>=s:
            break 
        if  rowa[e] not in x1:
            if rowa.count(rowa[e]) >=2:
                x1.append(rowa[e])
                e=e+1
            else :
                e=e+1  
        else :
            e=e+1
#-------------------------------抓出有幾個值
    x2=[]
    ii=0
    ss=len(x1)
    while ii<ss:
        if ii>=ss:
            break
        else:    
            p=rowa.count(x1[ii])
            x2.append(float(p)-1)
            ii=ii+1  
#--------------------------購買次數-1=回購次數
    plt1.bar(x1, x2, color = '#2f83e4',align =  'center') 
    plt1.ylabel('',fontsize=15,labelpad=15) 
    plt1.xlabel('豆蛋魚肉類',fontsize=15,labelpad=15) 
    plt1.tight_layout()
    ax = plt1.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_facecolor('#ffffff')
    buffera=BytesIO()
    plt1.savefig(buffera,format='png')
    data1=base64.encodebytes(buffera.getvalue()).decode()
    context1= 'data:image/png;base64,' +str(data1)
    plt1.close()
    

    h1=[]
#25-40
    h2=[]
#41-65
    h3=[]
    h4=[]
#获取phone数据表里的所有数据
    cursor.execute("SELECT userid FROM `in-food`.user where userjob='學生';")
#执行sql中的语句
    myresult = cursor.fetchall()
    d=0
    s=len(myresult)
    while d<s:
        if (myresult[d]) not in h1:
            h1.append( "".join(myresult[d]))
            d=d+1
        else :
            d=d+1
    cursor.execute("SELECT userid FROM `in-food`.user where userjob='家庭主婦';")
#执行sql中的语句
    myresult = cursor.fetchall()
    d=0
    s=len(myresult)
    while d<s:
        if (myresult[d]) not in h2:
            h2.append( "".join(myresult[d]))
            d=d+1
        else :
            d=d+1
    cursor.execute("SELECT userid FROM `in-food`.user where userjob='上班族';")
#执行sql中的语句
    myresult = cursor.fetchall()
    d=0
    s=len(myresult)
    while d<s:
        if (myresult[d]) not in h3:
            h3.append( "".join(myresult[d]))
            d=d+1
        else :
            d=d+1
    cursor.execute("SELECT userid FROM `in-food`.user where userjob='其他';")
#执行sql中的语句
    myresult = cursor.fetchall()
    d=0
    s=len(myresult)
    while d<s:
        if (myresult[d]) not in h4:
            h4.append( "".join(myresult[d]))
            d=d+1
        else :
            d=d+1

#-----------------------------------------------------抓出各年齡層的id
    hh1=[0,0,0,0]#豆蛋魚肉類分類
    hh2=[0,0,0,0]#蔬菜類
    hh3=[0,0,0,0]#乳品類
    hh4=[0,0,0,0]#水果類
    hh5=[0,0,0,0]#全殼雜糧類
    hh6=[0,0,0,0]#油脂堅果類
#--------------------------------------------------------------------算第一層  
    j=0
    s=len(h1)
    while j<s:
        qursor=("SELECT food_type FROM `in-food`.food_inserttrack where userid='"+ h1[j]+"';")
        cursor.execute(qursor)
        row1 = [item[0] for item in cursor.fetchall()]
        y=0
        t=len(row1)
        while y<t:
                if row1[y] in '豆蛋魚肉類':
                    hh1[0]=hh1[0]+1
                   
                
                if row1[y] in '蔬菜類':
                    hh2[0]=hh2[0]+1
                   
                if row1[y] in '乳品類':
                    hh3[0]=hh3[0]+1
                      
                if row1[y] in '水果類':
                    hh4[0]=hh4[0]+1
                       
                if row1[y] in '全殼雜糧類':
                    hh5[0]=hh5[0]+1
                    
                if y>=t:
                    break    
                if row1[y] in '油脂堅果類':
                    hh6[0]=hh6[0]+1
                y=y+1
        j=j+1 
#--------------------------------------------------------------------算第二層  
    j=0
    s=len(h2)
    while j<s:
        qursor=("SELECT food_type FROM `in-food`.food_inserttrack where userid='"+ h2[j]+"';")
        cursor.execute(qursor)
        row2 = [item[0] for item in cursor.fetchall()]
        y=0
        t=len(row2)
        while y<t:
                if row2[y] in '豆蛋魚肉類':
                    hh1[1]=hh1[1]+1
                  
                if row2[y] in '蔬菜類':
                    hh2[1]=hh2[1]+1
                   
                if row2[y] in '乳品類':
                    hh3[1]=hh3[1]+1
                    
                if row2[y] in '水果類':
                    hh4[1]=hh4[1]+1
                      
                if row2[y] in '全殼雜糧類':
                    hh5[1]=hh5[1]+1
                    
                if y>=t:
                    break    
                if row2[y] in '油脂堅果類':
                    hh6[1]=hh6[1]+1
                y=y+1
        j=j+1   
#--------------------------------------------------------------------算第三層    
    j=0
    s=len(h3)
    while j<s:
        qursor=("SELECT food_type FROM `in-food`.food_inserttrack where userid='"+ h3[j]+"';")
        cursor.execute(qursor)
        row3 = [item[0] for item in cursor.fetchall()]
        y=0
        t=len(row3)
        while y<t:
                if row3[y] in '豆蛋魚肉類':
                    hh1[2]=hh1[2]+1
                   
                if row3[y] in '蔬菜類':
                    hh2[2]=hh2[2]+1
                   
                if row3[y] in '乳品類':
                    hh3[2]=hh3[2]+1
                       
                if row3[y] in '水果類':
                    hh4[2]=hh4[2]+1
                       
                if row3[y] in '全殼雜糧類':
                    hh5[2]=hh5[2]+1
                    
                if y>=t:
                    break    
                if row3[y] in '油脂堅果類':
                    hh6[2]=hh6[2]+1
                y=y+1
        j=j+1     
    j=0
    s=len(h4)
    while j<s:
        qursor=("SELECT food_type FROM `in-food`.food_inserttrack where userid='"+ h4[j]+"';")
        cursor.execute(qursor)
        row4 = [item[0] for item in cursor.fetchall()]
        y=0
        t=len(row4)
        while y<t:
                if row4[y] in '豆蛋魚肉類':
                    hh1[3]=hh1[3]+1
                   
                if row4[y] in '蔬菜類':
                    hh2[3]=hh2[3]+1
                    
                if row4[y] in '乳品類':
                    hh3[3]=hh3[3]+1
                     
                if row4[y] in '水果類':
                    hh4[3]=hh4[3]+1
                        
                if row4[y] in '全殼雜糧類':
                    hh5[3]=hh5[3]+1
                    
                if y>=t:
                    break    
                if row4[y] in '油脂堅果類':
                    hh6[3]=hh6[3]+1
                y=y+1
        j=j+1      
 #-------------------------------------------------------------------視覺化
    title=["學生","家庭主婦","上班族","其他"]
    data={
        "豆蛋魚肉類":hh1,
        "蔬菜類":hh2,
        "乳品類":hh3,
        "水果類":hh4,
        "全榖雜糧類":hh5,
        "油脂堅果類":hh6
    }
    df1=pd.DataFrame(data,index=title)
    plt2.switch_backend('agg')
    df1.plot(kind="bar",stacked=True,figsize=(10,8),fontsize=18,color=['#E44C41','#EFC32F','#8E5D9F','#2CB299','#38B1CC','#E6DAC9'])
    plt2.legend(loc="lower left",bbox_to_anchor=(0.83,1.0))
    plt2.xticks(rotation=0)
    plt2.tight_layout()
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_facecolor('#ffffff')
    buffera=BytesIO()
    plt2.savefig(buffera,format='png')
    data2=base64.encodebytes(buffera.getvalue()).decode()
    context2= 'data:image/png;base64,' +str(data2)
    plt2.close()

    

    h1=[]
    #25-40
    h2=[]
    #41-65
    h3=[]
    #获取phone数据表里的所有数据
    cursor.execute("select userid from user where FLOOR(DATEDIFF(now(),userborn) / 365.25)<24 ")
    #执行sql中的语句
    myresult = cursor.fetchall()
    d=0
    s=len(myresult)
    while d<s:
        if (myresult[d][0]) not in h1:
            h1.append( "".join(myresult[d][0]))
            d=d+1
        else :
            d=d+1
    cursor.execute("select userid from user where FLOOR(DATEDIFF(now(),userborn) / 365.25)<=40 and FLOOR(DATEDIFF(now(),userborn) / 365.25)>24 ")
    #执行sql中的语句
    myresult = cursor.fetchall()
    d=0
    s=len(myresult)
    while d<s:
        if (myresult[d][0]) not in h2:
            h2.append( "".join(myresult[d][0]))
            d=d+1
        else :
            d=d+1
    cursor.execute("select userid from user where FLOOR(DATEDIFF(now(),userborn) / 365.25)>40 ")
    #执行sql中的语句
    myresult = cursor.fetchall()
    d=0
    s=len(myresult)
    while d<s:
        if (myresult[d][0]) not in h3:
            h3.append( "".join(myresult[d][0]))
            d=d+1
        else :
            d=d+1
    #-----------------------------------------------------抓出各年齡層的id
    hh1=[0,0,0]#豆蛋魚肉類分類
    hh2=[0,0,0]#蔬菜類
    hh3=[0,0,0]#乳品類
    hh4=[0,0,0]#水果類
    hh5=[0,0,0]#全殼雜糧類
    hh6=[0,0,0]#油脂堅果類
    #--------------------------------------------------------------------算第一層  
    j=0
    s=len(h1)
    while j<s:
        qursor=("SELECT food_type FROM `in-food`.food_inserttrack where userid='"+ h1[j]+"';")
        cursor.execute(qursor)
        row1 = [item[0] for item in cursor.fetchall()]
        y=0
        t=len(row1)
        while y<t:
                if row1[y] in '豆蛋魚肉類':
                    hh1[0]=hh1[0]+1
                    
                if row1[y] in '蔬菜類':
                    hh2[0]=hh2[0]+1
                   
                if row1[y] in '乳品類':
                    hh3[0]=hh3[0]+1
                       
                if row1[y] in '水果類':
                    hh4[0]=hh4[0]+1
                      
                if row1[y] in '全殼雜糧類':
                    hh5[0]=hh5[0]+1
                    
                if y>=t:
                    break    
                if row1[y] in '油脂堅果類':
                    hh6[0]=hh6[0]+1
                y=y+1
        j=j+1 
    #--------------------------------------------------------------------算第二層  
    j=0
    s=len(h2)
    while j<s:
        qursor=("SELECT food_type FROM `in-food`.food_inserttrack where userid='"+ h2[j]+"';")
        cursor.execute(qursor)
        row2 = [item[0] for item in cursor.fetchall()]
        y=0
        t=len(row2)
        while y<t:
                if row2[y] in '豆蛋魚肉類':
                    hh1[1]=hh1[1]+1
                  
                if row2[y] in '蔬菜類':
                    hh2[1]=hh2[1]+1
                   
                if row2[y] in '乳品類':
                    hh3[1]=hh3[1]+1
                    
                if row2[y] in '水果類':
                    hh4[1]=hh4[1]+1
                      
                if row2[y] in '全殼雜糧類':
                    hh5[1]=hh5[1]+1
                    
                if y>=t:
                    break    
                if row2[y] in '油脂堅果類':
                    hh6[1]=hh6[1]+1
                y=y+1
        j=j+1   
    #--------------------------------------------------------------------算第三層    
    j=0
    s=len(h3)
    while j<s:
        qursor=("SELECT food_type FROM `in-food`.food_inserttrack where userid='"+ h3[j]+"';")
        cursor.execute(qursor)
        row3 = [item[0] for item in cursor.fetchall()]
        y=0
        t=len(row3)
        while y<t:
                if row3[y] in '豆蛋魚肉類':
                    hh1[2]=hh1[2]+1
                   
                if row3[y] in '蔬菜類':
                    hh2[2]=hh2[2]+1
                   
                if row3[y] in '乳品類':
                    hh3[2]=hh3[2]+1
                       
                if row3[y] in '水果類':
                    hh4[2]=hh4[2]+1
                        
                if row3[y] in '全殼雜糧類':
                    hh5[2]=hh5[2]+1
                    
                if y>=t:
                    break    
                if row3[y] in '油脂堅果類':
                    hh6[2]=hh6[2]+1
                y=y+1
        j=j+1     
     #-------------------------------------------------------------------視覺化
    title=["12-24歲","25-40歲","41-65歲"]
    data={
         "豆蛋魚肉類":hh1,
         "蔬菜類":hh2,
         "乳品類":hh3,
         "水果類":hh4,
         "全榖雜糧類":hh5,
         "油脂堅果類":hh6
    }
    df=pd.DataFrame(data,index=title,)
    df.plot(kind="bar",stacked=True,figsize=(10,8),fontsize=18,color=['#E44C41','#EFC32F','#8E5D9F','#2CB299','#38B1CC','#E6DAC9'])
    plt3.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
    plt3.xticks(rotation=0)
    plt3.tight_layout()
    ax2 = plt3.gca()
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.set_facecolor('#ffffff')
    bufferb=BytesIO()
    plt3.savefig(bufferb,format='png')
    data3=base64.encodebytes(bufferb.getvalue()).decode()
    context3= 'data:image/png;base64,' +str(data3)
    plt3.close()

    wursor=("SELECT foodname FROM `in-food`.food_inserttrack where food_type='蔬菜類'")
    aursor.execute(wursor)
    rowa = [item[0] for item in aursor.fetchall()]
    x3=[]
    e=0
    s=len(rowa)
    while e<s:
        if e>=s:
                    break 
        if  rowa[e] not in x3:
            if rowa.count(rowa[e]) >=2:
                x3.append(rowa[e])
                e=e+1
            else :
                e=e+1
        else :
            e=e+1
    #-------------------------------抓出有幾個值
    x4=[]
    ii=0
    ss=len(x3)
    while ii<ss:
        if ii>=ss:
            break
        else:    
            p=rowa.count(x3[ii])
            x4.append(float(p)-1)
            ii=ii+1
    #--------------------------購買次數-1=回購次數
    plt4.bar(x3, x4, color = '#00e5c1', align =  'center') 
    plt4.ylabel('',fontsize=15,labelpad=15) 
    plt4.xlabel('蔬菜類',fontsize=15,labelpad=15) 
    plt4.tight_layout()
    ax3 = plt4.gca()
    ax3.spines['top'].set_visible(False)
    ax3.spines['right'].set_visible(False)
    ax3.spines['left'].set_visible(False)
    ax3.spines['bottom'].set_visible(False)
    ax3 = plt4.gca()
    ax.set_facecolor('#ffffff')
    bufferc=BytesIO()
    plt4.savefig(bufferc,format='png')
    data4=base64.encodebytes(bufferc.getvalue()).decode()
    context4= 'data:image/png;base64,' +str(data4)
    plt4.close()

    wursor=("SELECT foodname FROM `in-food`.food_inserttrack where food_type='乳品類'")
    aursor.execute(wursor)
    rowa = [item[0] for item in aursor.fetchall()]
    x5=[]
    e=0
    s=len(rowa)
    while e<s:
        if e>=s:
                    break 
        if  rowa[e] not in x5:
            if rowa.count(rowa[e]) >=2:
                x5.append(rowa[e])
                e=e+1
            else :
                e=e+1  
        else :
            e=e+1
    #-------------------------------抓出有幾個值
    x6=[]
    ii=0
    ss=len(x5)
    while ii<ss:
        if ii>=ss:
            break
        else:    
            p=rowa.count(x5[ii])
            x6.append(float(p)-1)
            ii=ii+1
    #--------------------------購買次數-1=回購次數
    plt5.bar(x5, x6,color ='#23cbff',align = 'center') 
    plt5.ylabel('',fontsize=15,labelpad=15) 
    plt5.xlabel('乳品類',fontsize=15,labelpad=15) 
    plt5.tight_layout()
    ax4 = plt5.gca()
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.spines['left'].set_visible(False)
    ax4.spines['bottom'].set_visible(False)
    ax4 = plt5.gca()
    ax4.set_facecolor('#ffffff')
    bufferd=BytesIO()
    plt5.savefig(bufferd,format='png')
    data5=base64.encodebytes(bufferd.getvalue()).decode()
    context5= 'data:image/png;base64,' +str(data5)
    plt5.close()


    wursor=("SELECT foodname FROM `in-food`.food_inserttrack where food_type='水果類'")
    aursor.execute(wursor)
    rowa = [item[0] for item in aursor.fetchall()]
    x7=[]
    e=0
    s=len(rowa)
    while e<s:
        if e>=s:
                    break 
        if  rowa[e] not in x7:
            if rowa.count(rowa[e]) >=2:
                x7.append(rowa[e])
                e=e+1
            else :
                e=e+1 
        else :
            e=e+1
    #-------------------------------抓出有幾個值
    x8=[]
    ii=0
    ss=len(x7)
    while ii<ss:
        if ii>=ss:
            break
        else:    
            p=rowa.count(x7[ii])
            x8.append(float(p)-1)
            ii=ii+1
    plt6.bar(x7, x8, color = '#2f83e4', align =  'center') 
    plt6.ylabel('',fontsize=15,labelpad=15) 
    plt6.xlabel('水果類',fontsize=15,labelpad=15) 
    plt6.tight_layout()
    ax5 = plt6.gca()
    ax5.spines['top'].set_visible(False)
    ax5.spines['right'].set_visible(False)
    ax5.spines['left'].set_visible(False)
    ax5.spines['bottom'].set_visible(False)
    ax5 = plt.gca()
    ax5.set_facecolor('#ffffff')
    buffere=BytesIO()
    plt6.savefig(buffere,format='png')
    data6=base64.encodebytes(buffere.getvalue()).decode()
    context6= 'data:image/png;base64,' +str(data6)
    plt6.close()


    wursor=("SELECT foodname FROM `in-food`.food_inserttrack where food_type='全殼雜糧類'")
    aursor.execute(wursor)
    rowa = [item[0] for item in aursor.fetchall()]
    x9=[]
    e=0
    s=len(rowa)
    while e<s:
        if e>=s:
                    break 
        if  rowa[e] not in x9:
            if rowa.count(rowa[e]) >=2:
                x9.append(rowa[e])
                e=e+1
            else :
                e=e+1
        else :
            e=e+1
    #-------------------------------抓出有幾個值
    x10=[]
    ii=0
    ss=len(x9)
    while ii<ss:
        if ii>=ss:
            break
        else:    
            p=rowa.count(x9[ii])
            x10.append(float(p)-1)
            ii=ii+1
    plt7.bar(x9, x10,color='#00e5c1' ,align =  'center') 
    plt7.ylabel('',fontsize=15,labelpad=15) 
    plt7.xlabel('全殼雜糧類',fontsize=15,labelpad=15) 
    plt7.tight_layout()
    ax6 = plt7.gca()
    ax6.spines['top'].set_visible(False)
    ax6.spines['right'].set_visible(False)
    ax6.spines['left'].set_visible(False)
    ax6.spines['bottom'].set_visible(False)
    ax6.set_facecolor('#ffffff')
    bufferf=BytesIO()
    plt7.savefig(bufferf,format='png')
    data7=base64.encodebytes(bufferf.getvalue()).decode()
    context7= 'data:image/png;base64,' +str(data7)
    plt7.close()

    wursor=("SELECT foodname FROM `in-food`.food_inserttrack where food_type='油脂堅果類'")
    aursor.execute(wursor)
    rowa = [item[0] for item in aursor.fetchall()]
    x11=[]
    e=0
    s=len(rowa)
    while e<s:
        if e>=s:
                    break 
        if  rowa[e] not in x11:
            if rowa.count(rowa[e]) >=2:
                x11.append(rowa[e])
                e=e+1
            else :
                e=e+1
        else :
            e=e+1
    #-------------------------------抓出有幾個值
    x12=[]
    ii=0
    ss=len(x11)
    while ii<ss:
        if ii>=ss:
            break
        else:    
            p=rowa.count(x11[ii])
            x12.append(float(p)-1)
            ii=ii+1
    plt8.bar(x11, x12, color =  '#23cbff', align =  'center') 
    plt8.ylabel('',fontsize=15,labelpad=15) 
    plt8.xlabel('油脂堅果類',fontsize=15,labelpad=15) 
    plt8.tight_layout()
    ax7 = plt8.gca()
    ax7.spines['top'].set_visible(False)
    ax7.spines['right'].set_visible(False)
    ax7.spines['left'].set_visible(False)
    ax7.spines['bottom'].set_visible(False)
    ax7.set_facecolor('#ffffff')
    bufferg=BytesIO()
    plt8.savefig(bufferg,format='png')
    data8=base64.encodebytes(bufferg.getvalue()).decode()
    context8= 'data:image/png;base64,' +str(data8)
    plt8.close()

    os.unlink('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/infood.txt')
    sql1 =  'SELECT * INTO OUTFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/infood.txt" FROM  `in-food`.hotfood ; '
    cursor.execute(sql1)
    db.commit()
    color_list=['#0088A8','#003C9D','#00DDDD','#FFFF33','#33FF33']
    colormap=colors.ListedColormap(color_list)
    mask = np.array(Image.open('C:/Users/Justin/potrip/infood/wordart-09.png'))
    wc = WordCloud(background_color='white',    #   背景顏色
                font_path="./kaiu.ttf",
                mask=mask,
                colormap=colormap,
                max_words=100,
                min_font_size=15, 
                random_state=20,
                scale=4,
                width=2000, height=800,)      
    text = open("C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/infood.txt","r",encoding="utf-8").read()#   打開詞源的文本文件
    wc.generate(text)#   生成詞雲
    plt9.imshow(wc, interpolation='bilinear')
    plt9.axis("off")
    plt9.tight_layout(pad=0)
    image = io.BytesIO()
    plt9.savefig(image, format='png')
    image.seek(0)  # rewind the data
    string = base64.b64encode(image.read())
    image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
    plt9.close()


    connect_db  = pymysql.connect(host='localhost',user='root',passwd='1234',port=3306,db='in-food')
    with connect_db.cursor() as cursor:
        sql = """
        SELECT foodname,food_type, 
        CASE
            WHEN TIMESTAMPDIFF(MINUTE,now(), foodtime) < 0 THEN (TIMESTAMPDIFF(MINUTE,now(), foodtime)) 
            ELSE "0" 
        END AS grp 
        FROM `in-food`.food_inserttrack;
        """
        # 執行 SQL 指令
        cursor.execute(sql)
        # 提交至 SQL
        data = cursor.fetchall()
    p=0
    k=len(data)
    ht=[]
    while p<k:
        if p>=k:
            break
        if float((data[p][2])) < 0 :
            ht.append(data[p])
            p=p+1
        else:    
            p=p+1 
    y=0   
    u=len(ht)
    dat=[]
    while y<u:
        if y>=u:
            break
        else:  
            dat.append(ht[y][0])
            y=y+1  
    #-------------------------------------------------過期的被拿出來了        
    p2=0
    k2=len(ht)
    ht1=[]
    ht2=[]
    ht3=[]
    while p2<k2:
        if p2>=k2:
            break
        if ht[p2][0] not in ht1:
            ht1.append(ht[p2][0])
            ht2.append(ht[p2][1])
            p2=p2+1
        else:
            p2=p2+1
    p3=0
    k3=len(ht1)
    while p3<k3:
        if p3>=k3:
            break
        else:
            g=dat.count(ht1[p3])
            ht3.append(g)
            p3=p3+1     
         
    df = pd.DataFrame({'名稱':ht1,'類別':ht2,'次數':ht3})
    df=df.nlargest(10, '次數')
    df.index=['1','2','3','4','5','6','7','8','9','10']
    plt10.tight_layout()
    ax9 = plt10.axes(frame_on=False)# 不要額外框線
    ax9.xaxis.set_visible(False)  # 隱藏X軸刻度線
    ax9.yaxis.set_visible(False)  # 隱藏Y軸刻度線
    pp=pd.plotting.table(ax9, df, loc='center',rowColours =["#dcdcdc"] * 10,  colColours =["#7dd2f1"] * 10,rowLoc='center',cellLoc='center')
    pp.set_fontsize(13)
    pp.scale(1.2,2.2)
    image1 = io.BytesIO()
    plt10.savefig(image1, format='png')
    image1.seek(0)  # rewind the data
    string1 = base64.b64encode(image1.read())
    image_65 = 'data:image/png;base64,' + urllib.parse.quote(string1)
    plt10.axis('off')
    plt10.close()

    #定义需要用上的空数据数组，然后通过遍历数据库的数据将数据附上去
    aursor.execute("SELECT * FROM `in-food`.food_inserttrack")
    myresult1 = aursor.fetchall()
#执行sql中的语句
    
    x1=[]
    x3=[]
    i=0
    e=0
    q=len(myresult1)
    while i<q:
        aursor.execute("SELECT foodfrom FROM `in-food`.food_inserttrack")
        myresult = aursor.fetchall()
        if (myresult[i]) not in x1:
            x1.append( myresult[i])
            i=i+1
        else :
            i=i+1
    
    while e<q:
        aursor.execute("SELECT foodfrom FROM `in-food`.food_inserttrack")
        myresult = aursor.fetchall()
        if  ("".join(myresult[e])) not in x3:
            x3.append( "".join(myresult[e]))
            e=e+1
        else :
            e=e+1 
#-----------------------------------------------------------------------抓出food_inserttrack有幾個值

    x2=[]
    ii=0
    p=x1.count(x1[ii])
    ss=len(x1)
    while ii<ss:
        p=myresult.count(x1[ii])
        x2.append(float(p))
        ii=ii+1
#------------------------------------------------------------------------
    plta.switch_backend('agg')
    plta.pie(x2,labels=x3,textprops = {"fontsize" : 16,"color":"#000000"},autopct="%2.1f%%",shadow=True,labeldistance=1.3)
    buffer=BytesIO()
    plta.savefig(buffer,format='png')
    datab=base64.encodebytes(buffer.getvalue()).decode()
    contextc66= 'data:image/png;base64,' +str(datab)
    plta.close()


    connect_db  = pymysql.connect(host='localhost',user='root',passwd='1234',port=3306,db='in-food')
    with connect_db.cursor() as cursor:
        sqll = """
        SELECT `list_id`,`list_name` FROM `in-food`.order_list;
        """
    # 執行 SQL 指令
        cursor.execute(sqll)
    # 提交至 SQL
        data1 = cursor.fetchall()
    aursor=connect_db.cursor()
    aursor.execute("SELECT `list_id` FROM `order_list`  ORDER BY `list_id` DESC LIMIT 0 , 1;")
    data2 = aursor.fetchall()
    data3="".join('%s' %id for id in data2)
    t=0

    u1=[[] for _ in range(int(data3))]
    while t < int(data3) :
        if t >= int(data3):
            break
        rursor=connect_db.cursor()
        tt=t+1
        rursor.execute("SELECT list_name FROM order_list WHERE list_id='"+ str(tt) +"';")
        cho=rursor.fetchall()
        n=0
        eursor=connect_db.cursor()
        eursor.execute("SELECT COUNT(list_id) FROM order_list WHERE list_id='"+ str(tt) +"'")
        kkl=eursor.fetchall()
        kkl="".join('%s' %id for id in kkl) 
        kkl=int(kkl)
        while n < kkl:
            if n >= kkl:
                break
            (u1[t]).append(str(" ".join('%s' %id for id in cho[n])))
            n=n+1
        t=t+1
    association_rules = apriori(u1,min_support=0.16666, min_confidence=0.2, min_lift=2, max_length=2) 
    association_results = list(association_rules)
    len_result=len(association_results )
    u2=[[] for _ in range(len_result)]
    bigen=0
    while bigen < len_result:
        
        for item in association_results:
            if bigen >= len_result:
                break
            pair = item[0] 
            items = [x for x in pair]
            u2[bigen].append(items[0] )
            u2[bigen].append(items[1] )
            u2[bigen].append(str(item[2][0][3]))
            bigen=bigen+1
    u3=[]
    popr=0
    while popr < len_result:
        if (u2[popr][0]) not in u3:
                u3.append( "".join(u2[popr][0]))
                popr=popr+1
        else :
                popr=popr+1
    top1=str(u3[0])
    top2=str(u3[1])
    top3=str(u3[2])
    top4=str(u3[3])
    top5=str(u3[4])
    top6=str(u3[5])
    top7=str(u3[6])
    top8=str(u3[7])
    top9=str(u3[8])
    top10=str(u3[9])
    if request.method == "POST":
        select= request.POST['select']
        selectt=str(select)
        u4=[]
        u5=[]
        uine=0
        while uine < len_result:
            if uine >= len_result:
                break
            if (u2[uine][0]) == selectt:
                u4.append((u2[uine][1]))
                u5.append((u2[uine][2]))
                uine=uine+1
            else:
                uine=uine+1

        if 0 in range(len(u4)):
            topq1=str(u4[0])
        if 1 in range(len(u4)):
            topq2=str(u4[1])
        if 2 in range(len(u4)):
            topq3=str(u4[2])
        if 0 in range(len(u5)):
            topp1=(float(u5[0])*15)
        if 1 in range(len(u5)):
            topp2=(float(u5[1])*15)
        if 2 in range(len(u5)):
            topp3=(float(u5[2])*15)
    
    
    connect_db.close()
    db.close()
    return render(request,'index.html',locals()) 

 

