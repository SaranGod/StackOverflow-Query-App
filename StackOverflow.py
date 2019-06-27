#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from stackapi import StackAPI
from nltk.corpus import stopwords
import webbrowser
from nltk.tokenize import word_tokenize 
def callback(url):
    webbrowser.open_new(url)
import pickle
SITE = StackAPI('stackoverflow')
top = Tk()
top.title("StackOverflow Query System")
top.geometry("550x300+300+150")
top.resizable(width=True, height=True)
L2 = Label(top, text="Query:")
L2.grid(row=1,column=1)
E1 = Entry(top, bd =1)
E1.grid(row=1,column=2)
L3 = Label(top, text="Tags:")
L3.grid(row=2,column=1)
E2 = Entry(top, bd =1)
E2.grid(row=2,column=2)
L4 = Label(top, text="Number of Results")
L4.grid(row=3,column=1)
E3 = Entry(top, bd =1)
E3.grid(row=3,column=2)
t1=Frame(top)
t1.grid(row=5,column=2)
def search1():
    for widget in t1.winfo_children():
        widget.destroy()
    print("Search in progress..")
    #stop_words = set(stopwords.words('english'))
    quest=str(E1.get())
    #word_tokens = word_tokenize(quest)
    #print(word_tokens)
    #quest1=""
    #for w in word_tokens: 
    #    if w not in stop_words: 
    #        quest1=quest1+w
    #        quest1=quest1+" "
    #print(quest1)
    tags=str(E2.get())
    tags1=tags.split(",")
    number=E3.get()
    try:
        number1=int(number)
    except ValueError as e:
        error_num=Label(t1,text="Enter a number in the number of results field")
        error_num.pack()
    #print(quest1)
    import pandas as pd
    print(tags1)
    test=(SITE.fetch("search",intitle=quest,tagged=tags1,sort='relevance'))
    test1=pd.DataFrame(test['items'])
    for i in range(number1):
        try:
            text=test1['link'][i]
        except KeyError as e:
            error=Label(t1,text="End of Results")
            error.pack()
            break
        link1 = Label(t1, text=str(test1['title'][i]), fg="blue", cursor="hand1")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback(text))
B = Button(top, text ="Search", command = search1)
B.grid(row=4,column=1)
top.mainloop()


# In[ ]:




