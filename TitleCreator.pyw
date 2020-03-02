import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyperclip as pyp
from selenium import webdriver
from bs4 import BeautifulSoup
import time,os

# 変数定義
back = "#66a5ad"
fcolor = "#FFFFFF"
nextc = ""
status = ""
title = ""
selfa = ""
listed = []
result = '/'.join(listed)

# ウィンドウ配置
root = tk.Tk()
root.title("Internal Title Creator")
root.geometry("400x500")
root.configure(bg=back)

# Title Creator
Creator = tk.Label(text=u'Title Creator', foreground=fcolor, background=back, font=(u'Impact',20))
Creator.pack()
# NextC 記入フレーム定義
root2 = tk.Frame(background=back)
root2.pack(pady=10,fill="both",expand=1)
# NextC 記入欄
Static1 = tk.Label(root2, text=u'Next C :', foreground=fcolor, background=back, font=(u'Impact',12),width=15)
Static1.grid(row=0, column=0,sticky='E')
EditBox1 = tk.Entry(root2,width=6)
EditBox1.grid(row=0, column=1)
'''
closeBox = tk.IntVar()
C = tk.Checkbutton(root2,background=back,text="close", variable=closeBox,
                         onvalue=1, offvalue=0, height=5,width=20)
C.grid(row=0, column=2)
'''
# Status 記入フレーム定義
statusFrame = tk.Frame(background=back)
statusFrame.pack(pady=10,fill="both",expand=1)
# Status 記入欄
labelTop = tk.Label(statusFrame,text = "Status :", foreground=fcolor, background=back, font=(u'Impact',12),width=15)
labelTop.grid(row=0, column=0,sticky='E')
EditBox2 = ttk.Combobox(statusFrame, width=5,
                            values=[
                                    "PR", 
                                    "SD",
                                    "PQ",
                                    "WC",
                                    "MR"])
EditBox2.grid(row=0, column=1,sticky='E')
EditBox2.current(0)

# Sev 記入フレーム定義
sevFrame = tk.Frame(background=back)
sevFrame.pack(pady=5,fill="both",expand=1)
# Sev 記入欄
labelTop = tk.Label(sevFrame,text = "Severity :", foreground=fcolor, background=back, font=(u'Impact',12),width=15)
labelTop.grid(row=0, column=0,sticky='E')
SevBox = ttk.Combobox(sevFrame, width=3,
                            values=[
                                    "C", 
                                    "B",
                                    "A"])
SevBox.grid(row=0, column=1,sticky='E')
SevBox.current(0)

# Level 記入フレーム定義
levelFrame = tk.Frame(background=back)
levelFrame.pack(pady=5,fill="both",expand=1)
# Level 記入欄
Static5 = tk.Label(levelFrame, text=u'Service Level :', foreground=fcolor, background=back, font=(u'Impact',12),width=15)
Static5.grid(row=0, column=0,sticky='E')
levelBox = tk.Entry(levelFrame,width=15)
levelBox.insert(tk.END,"Professional")
levelBox.grid(row=0, column=2,sticky='E')

# Product 記入フレーム定義
proFrame = tk.Frame(background=back)
proFrame.pack(pady=5,fill="both",expand=1)
# Product 記入欄
Static6 = tk.Label(proFrame, text=u'Product :', foreground=fcolor, background=back, font=(u'Impact',12),width=15)
Static6.grid(row=0, column=0,sticky='E')
proBox = tk.Entry(proFrame,width=20)
proBox.grid(row=0, column=1,sticky='E')

# Title 記入フレーム定義
TitleFrame = tk.Frame(background=back)
TitleFrame.pack(pady=5,fill="both",expand=1)
# Title 記入欄
Static3 = tk.Label(TitleFrame, text=u'Title :', foreground=fcolor, background=back, font=(u'Impact',12),width=15)
Static3.grid(row=0, column=0,sticky='E')
EditBox3 = tk.Entry(TitleFrame,width=40)
EditBox3.grid(row=0, column=1,sticky='E')

# Self A 記入フレーム定義
selfaFrame = tk.Frame(background=back)
selfaFrame.pack(pady=5,fill="both",expand=1)
# Self A 記入欄
labelTop = tk.Label(selfaFrame,text = "Self A :", foreground=fcolor, background=back, font=(u'Impact',12),width=15)
labelTop.grid(row=0, column=0,sticky='E')
EditBox4 = ttk.Combobox(selfaFrame, width=3,
                            values=[
                                    "5", 
                                    "4",
                                    "3",
                                    "2",
                                    "1"])
EditBox4.grid(row=0, column=1,sticky='E')
EditBox4.current(2)

# 出力処理
def CreateTitle():
  # 取得処理
  listed = []
  nextc = EditBox1.get()
  listed.append(nextc)
  status = EditBox2.get()
  listed.append(status)
  level = levelBox.get()
  listed.append(level)
  sev = SevBox.get()
  listed.append(sev)
  product = proBox.get()
  listed.append(product)
  title = EditBox3.get()
  listed.append(title)
  selfa = EditBox4.get()
  listed.append(selfa)
  # check 処理
  if nextc == "":
    res = messagebox.showinfo("未入力", "NextC が未入力です")
    return print(res)
  elif product == "":
    res = messagebox.showinfo("未入力", "Product が未入力です")
    return print(res)
  elif title == "":
    res = messagebox.showinfo("未入力", "タイトル が未入力です")
    return print(res)
  if len(nextc) != 4:
    res = messagebox.showinfo("日付ミス", "日付が正確ではありません")
    return print(res)
  for i in range(0, 4):
    if not nextc[i].isdecimal():
      res = messagebox.showinfo("日付ミス", "日付が正確ではありません")
      return print(res)
  # 出力
  # 改行と空白を削除
  for i in range(len(listed)):
    listed[i] = (listed[i].strip('\n'))
    listed[i] = (listed[i].strip())
  # 結合
  result = '/'.join(listed)
  resultBox.delete('1.0', 'end')
  resultBox.insert(tk.END,result)
  #resultBox.pack()
  # コピー処理
  clip = resultBox.get('1.0', 'end')
  pyp.copy(clip)
# ボタン埋まる回避処理
def click(event):
  root.after(1, CreateTitle)

# スクレイピング
def Scrape():

  listed = []
  nextc = EditBox1.get()
  if nextc == "":
    res = messagebox.showinfo("未入力", "NextC が未入力です")
    return print(res)
  EditBox3.delete(0, tk.END)
  proBox.delete(0,tk.END)
  listed.append(nextc)
  status = EditBox2.get()
  listed.append(status)
  level = levelBox.get()
  listed.append(level)

  '''
  casenum = resultBox.get('1.0', 'end')
  url = "https://servicedesk.microsoft.com/#/customer/case/" + str(casenum)
  ''' 
  url = "http://goodmorningspa.sakura.ne.jp/sd.html"
  driver = webdriver.Edge()
  driver.get(url)
  time.sleep(1)
  html = driver.page_source.encode('utf-8')
  soup = BeautifulSoup(html, "html.parser")

  sevd = soup.find_all("a",class_="select-anchor ng-binding")[-1]
  sev = sevd.get("title")
  listed.append(sev)

  # Product 取得
  pro = soup.select('input')[7]
  product = pro.get('data-bi-name')
  proBox.insert(tk.END,product)
  listed.append(product)

  # Title 取得
  titled = soup.find_all("span",class_="ng-binding")[7]
  title = titled.string
  EditBox3.insert(tk.END,title)
  listed.append(title)

  # Self A 代入
  selfa = EditBox4.get()
  listed.append(selfa)

  driver.close()
  result = '/'.join(listed)
  resultBox.delete('1.0', 'end')
  resultBox.insert(tk.END,result)

# ボタン埋まる回避処理2
def click2(event):
  root.after(1, Scrape)

# 削除処理
def DeleteData(event):
  EditBox1.delete(0, tk.END)
  EditBox3.delete(0, tk.END)
  proBox.delete(0,tk.END)
  resultBox.delete('1.0', 'end')
  nextc = ""
  title = ""
  result = '/'.join(listed)
# クリップボードにコピー
def CopyClip(event):
  clip = resultBox.get('1.0', 'end')
  pyp.copy(clip)

# ボタン表示領域フレーム定義
ButtonFrame = tk.Frame(background=back)
ButtonFrame.pack(pady=10)
# 出力ボタン
Button1 = tk.Button(ButtonFrame,text=u'Create Internal Title')
Button1.bind("<Button-1>",click) 
Button1.pack(side="left",padx=5)
# リセットボタン
Button2 = tk.Button(ButtonFrame, text=u'All Clear')
Button2.bind("<Button-1>",DeleteData) 
Button2.pack(side="left",padx=5)
# コピーボタン
Button3 = tk.Button(ButtonFrame,text=u'Copy')
Button3.bind("<Button-1>",CopyClip) 
Button3.pack(side="left",padx=5)
# Scrape ボタン
Button4 = tk.Button(ButtonFrame,text=u'Scrape')
Button4.bind("<Button-1>",click2) 
Button4.pack(side="left",padx=5)

#出力表示領域フレーム定義
outputFrame = tk.Frame(background=back)
outputFrame.pack(pady=10)

# 結果表示欄
resultBox = tk.Text(outputFrame,height=6)
resultBox.pack(padx=8,pady=8)

# 俺
iino = tk.Label(outputFrame, text=u'Powered by Yosuke Iino', foreground="#CCCCCC", background=back, font=(u'meiryo',7))
iino.pack(side="right",fill="y")

# 描画開始
root.mainloop()
