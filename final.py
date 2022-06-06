#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import datasets
import pydotplus
import os
os.environ["PATH"]+=os.pathsep + "C:\Program Files\Graphviz\bin"

data=pd.read_csv('勇士隊例行賽數據.csv')
WL=data.iloc[:,1].to_numpy()
x=data.iloc[:,3:].to_numpy()
print(data)
print(x)
clf=tree.DecisionTreeClassifier(criterion='entropy').fit(x,WL)


# In[44]:


clf.score(x,WL)


# In[45]:


#dot_data=tree.export_graphviz(clf,out_file=None)
#graph=pydotplus.graph_from_dot_data(dot_data)
#graph.write_pdf('warrior.pdf')


# In[46]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,WL,random_state=1,test_size=0.3,stratify = WL)
clf=tree.DecisionTreeClassifier(criterion='entropy',random_state=14).fit(X_train,y_train)
clf.score(X_train,y_train)


# In[47]:


clf.score(X_test,y_test)


# In[48]:


clf=tree.DecisionTreeClassifier(criterion='entropy',random_state=14,max_depth=5).fit(X_train,y_train)


# In[49]:


clf.score(X_train,y_train)


# In[50]:


clf.score(X_test,y_test)


# In[51]:


dot_data=tree.export_graphviz(clf,out_file=None)
graph=pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('warrior_1.pdf')


# In[52]:


import tkinter as tk
def outcome(PTS,FG,P_3,FTM,FT,REB,AST,STL,BLK,TOV,PF):
    if(AST<=22.5):
        if(TOV<=16.5):
            result = tk.Label(frame3,text='lose',font=('Arial',12))
            result.grid(row=4,column=0,padx=10,pady=10,sticky='w')
        else:
            if(FTM<=9.5):
                result = tk.Label(frame3,text='lose',font=('Arial',12))
                result.grid(row=4,column=0,padx=10,pady=10,sticky='w')
            else:
                result = tk.Label(frame3,text='win',font=('Arial',12))
                result.grid(row=4,column=0,padx=10,pady=10,sticky='w')
    else:
        if(AST<=29.5):
            if(BLK<=5.5):
                if(REB<=42):
                    if(PTS<=125):
                        result = tk.Label(frame3,text='lose',font=('Arial',12))
                        result.grid(row=4,column=0,padx=10,pady=10,sticky='w')
                    else:
                        result = tk.Label(frame3,text='win',font=('Arial',12))
                        result.grid(row=4,column=0,padx=10,pady=10,sticky='w')
                else:
                    if(TOV<=15.5):
                        result = tk.Label(frame3,text='win',font=('Arial',12))
                        result.grid(row=4,column=0,padx=10,pady=10,sticky='w')
                    else:
                        result = tk.Label(frame3,text='lose',font=('Arial',12))
                        result.grid(row=4,column=0,padx=10,pady=10,sticky='w')
            else:
                if(TOV<=21.5):
                    result = tk.Label(frame3,text='win',font=('Arial',12))
                    result.grid(row=4,column=0,padx=10,pady=10,sticky='w')  
                else:
                    result = tk.Label(frame3,text='lose',font=('Arial',12))
                    result.grid(row=4,column=0,padx=10,pady=10,sticky='w')
        else:
            if(PTS<=102.5):
                result = tk.Label(frame3,text='lose',font=('Arial',12))
                result.grid(row=4,column=0,padx=10,pady=10,sticky='w')
            else:
                result = tk.Label(frame3,text='win',font=('Arial',12))
                result.grid(row=4,column=0,padx=10,pady=10,sticky='w')
            
def button_event():
    pts = text_1.get("1.0",  tk.END+"-1c")
    PTS=float(pts.lstrip()) #去掉空白
    fg = text_2.get("1.0",  tk.END+"-1c")
    FG = float(fg.lstrip()) #去掉空白
    p_3 = text_3.get("1.0",  tk.END+"-1c")
    P_3=float(p_3.lstrip()) #去掉空白
    ftm = text_4.get("1.0",  tk.END+"-1c")
    FTM = float(ftm.lstrip()) #去掉空白
    ft = text_5.get("1.0",  tk.END+"-1c")
    FT = float(ft.lstrip()) #去掉空白
    reb = text_6.get("1.0",  tk.END+"-1c")
    REB = float(reb.lstrip()) #去掉空白
    ast = text_7.get("1.0",  tk.END+"-1c")
    AST = float(ast.lstrip()) #去掉空白
    stl = text_8.get("1.0",  tk.END+"-1c")
    STL = float(stl.lstrip()) #去掉空白
    blk = text_9.get("1.0",  tk.END+"-1c")
    BLK = float(blk.lstrip()) #去掉空白
    tov = text_10.get("1.0",  tk.END+"-1c")
    TOV = float(tov.lstrip()) #去掉空白
    pf = text_11.get("1.0",  tk.END+"-1c")
    PF = float(pf.lstrip()) #去掉空白
    outcome(PTS,FG,P_3,FTM,FT,REB,AST,STL,BLK,TOV,PF)


# In[53]:



win = tk.Tk()
win.title('勇士隊勝負預測')
win.geometry('800x400')
frame1 = tk.Frame(win)
frame2 = tk.Frame(win)
frame3 = tk.Frame(win)
frame1.place(x=0, y=0)
frame1.config(height=200, width=600)
frame2.place(x=10, y=125)
frame2.config(height=50, width=600)
frame3.place(x=0, y=190)

label_1 = tk.Label(frame1,text='得分:',font=('Arial',12))
label_1.grid(row=0,column=0,padx=10,pady=10,sticky='w')
text_1 = tk.Text(frame1,width=5,height=2)
text_1.grid(row=0,column=1, sticky='w')

label_2 = tk.Label(frame1,text='得分命中率%:',font=('Arial',12))
label_2.grid(row=0,column=2,padx=10,pady=10,sticky='w')
text_2 = tk.Text(frame1,width=5,height=2)
text_2.grid(row=0,column=3, sticky='w')

label_3 = tk.Label(frame1,text='三分命中率%:',font=('Arial',12))
label_3.grid(row=0,column=4,padx=10,pady=10,sticky='w')
text_3 = tk.Text(frame1,width=5,height=2)
text_3.grid(row=0,column=5, sticky='w')

label_4 = tk.Label(frame1,text='罰球命中數:',font=('Arial',12))
label_4.grid(row=0,column=6,padx=10,pady=10,sticky='w')
text_4 = tk.Text(frame1,width=5,height=2)
text_4.grid(row=0,column=7, sticky='w')

label_5 = tk.Label(frame1,text='罰球命中率:',font=('Arial',12))
label_5.grid(row=0,column=8,padx=10,pady=10,sticky='w')
text_5 = tk.Text(frame1,width=5,height=2)
text_5.grid(row=0,column=9, sticky='w')

label_6 = tk.Label(frame2,text='籃板:',font=('Arial',12))
label_6.grid(row=1,column=0,padx=10,pady=10,sticky='w')
text_6 = tk.Text(frame2,width=5,height=2)
text_6.grid(row=1,column=1, sticky='w')

label_7 = tk.Label(frame2,text='助攻:',font=('Arial',12))
label_7.grid(row=1,column=2,padx=10,pady=10,sticky='w')
text_7 = tk.Text(frame2,width=5,height=2)
text_7.grid(row=1,column=3, sticky='w')

label_8 = tk.Label(frame2,text='抄截:',font=('Arial',12))
label_8.grid(row=1,column=4,padx=10,pady=10,sticky='w')
text_8 = tk.Text(frame2,width=5,height=2)
text_8.grid(row=1,column=5, sticky='w')

label_9 = tk.Label(frame2,text='火鍋:',font=('Arial',12))
label_9.grid(row=1,column=6,padx=10,pady=10,sticky='w')
text_9 = tk.Text(frame2,width=5,height=2)
text_9.grid(row=1,column=7, sticky='w')

label_10 = tk.Label(frame2,text='失誤:',font=('Arial',12))
label_10.grid(row=1,column=8,padx=10,pady=10,sticky='w')
text_10 = tk.Text(frame2,width=5,height=2)
text_10.grid(row=1,column=9, sticky='w')

label_11 = tk.Label(frame2,text='犯規:',font=('Arial',12))
label_11.grid(row=1,column=10,padx=10,pady=10,sticky='w')
text_11 = tk.Text(frame2,width=5,height=2)
text_11.grid(row=1,column=11, sticky='w')

button = tk.Button(frame3,width=10,height=2,text='開始預測',font=('Arial',12),command=button_event)
button.grid(row=2,padx=5,pady=5,sticky='w')

win.mainloop()


# In[ ]:




