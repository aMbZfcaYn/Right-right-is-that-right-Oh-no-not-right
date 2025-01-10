from openai import OpenAI
from typing import List, Dict
from tkinter import Tk, messagebox

import pygame


import pygame,sys
from pygame.locals import *

window_w,window_h = 1280,720
screen = pygame.display.set_mode((window_w,window_h))

client = OpenAI(
    base_url='http://10.15.88.73:5033/v1',
    api_key='ollama',  # required but ignored
)

messages : List[Dict] = [
    {"role": "system", "content": "I'm an antique dealer.Plus I'm quite mean.I answer questions in no more than 20 words."}
]

def makeWords(txt, size, color):#文字渲染,返回 渲染的对象和尺寸
    my_font = pygame.font.Font('../font.ttf', size)
    r = my_font.render(str(txt), True, color)
    return (r, r.get_size())
 
 
class WordsOutput():
    def __init__(self, text, name, portrait):
        self.startx = 0  # 起始位置
        self.endx = 1280  # 边缘位置
        self.text = text
        self.name = name
        self.portrait = portrait #头像为surface对象
        self.portrait = pygame.transform.scale(self.portrait,(192,192))#压缩图片尺寸到192×192
        if self.portrait != None:  # 如果有头像则改变起始位置
            self.startx = 192#将起始x位置设置为头像宽度
        self.words = []  # 储存渲染出来的文字的列表
        self.analyzed = False  # 是否分析过
        self.interval = time.time()  # 计时器
        self.output_speed = 0.02  # 输出文字的间隔时间
        self.finished_writing = False  # 是否结束输出文字
        self.out_num = 0 #输出的文字编号
    def analyze(self):
        txt = self.text  # 将txt赋值为内容
        height = makeWords(txt[0], 35, (255, 255, 255))[1][1]  # 单个文字高度,用第一个字的高度
        txt_list = []  # 渲染出来的文字列表
        w_last = 0  # 叠加文字后的整体长度
        #初始高度位置
        start_y = 0
        #检测是否有头像
        if self.portrait != None:
            txt_list.append((self.portrait, (0, start_y)))
        #若有名字则将名字渲染出来存储进列表,改变排版
        if self.name != None:
            a = makeWords(self.name, 35, (255, 255, 0))
            txt_list.append((a[0], (self.startx, start_y)))
            start_y += a[1][1]
        #开始遍历文字
        for i in range(len(txt)):
            a = makeWords(txt[i], 35, (255, 255, 255))  # 渲染文字
            if self.startx+w_last+a[1][0] <= self.endx:  # 检测是否超出设定边缘
                #未超出则记录位置,渲染文字,存储进列表
                pos = (self.startx+w_last, start_y)
                txt_list.append((a[0], pos))
                w_last += a[1][0]
            else:
                #超出:换行,将x坐标设置为初始值,y则增加一个字的高度
                start_split = i-1
                start_y += a[1][1]
                w_last = 0
                a = makeWords(txt[i], 35, (255,255,255))
                pos = (self.startx+w_last, start_y)
                txt_list.append((a[0], pos))
                w_last += a[1][0]
        self.words = txt_list
        self.analyzed = True
    def paint(self):
        if self.analyzed == False:
            self.analyze()
        if time.time() >= self.interval + self.output_speed and self.out_num < len(self.words):#检测是否到输出下一个文字的时间并且还未输出完
            self.out_num+=1
            self.interval = time.time()#重置计时器
        for i in range(self.out_num):#绘制到达的文字
            img, pos = self.words[i]
            screen.blit(img, pos)
        if self.out_num == len(self.words): #如果绘制完了
            self.finished_writing = True 


while True:
    user_input = input("User input: ")
    if user_input.lower() in [ "exit", "quit"]:
        print("chat ends.")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama3.2",      
        messages=messages,    # a list of dictionary contains all chat dictionary
    )
    # 提取模型回复
    assistant_reply = response.choices[0].message.content
    print(f"Llama: {assistant_reply}")

    # 将助手回复添加到对话历史
    messages.append({"role": "assistant", "content": assistant_reply})
    
    
#创建计时器,通俗讲就是帧数限制器
clock = pygame.time.Clock()
#创建对话框列表,存储对话框
w1 = []
#实例化类,写入参数,分别为 内容,名字,头像
w1.append(WordsOutput("Hello pygame",None,None))
w1.append(WordsOutput("Hello pygame, let's go", "名字", None))
while True:
    screen.fill((0,0,0))#填充背景
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#检测退出
            exit()
        if event.type == MOUSEBUTTONDOWN:#检测鼠标是否按下
            if event.button == 1 and len(w1) > 0:#检测是否按下了左键,并且w1不是空列表
                if w1[0].finished_writing:#如果文字输出完成了,则删除显示的这一项
                    w1.pop(0)
    if len(w1) > 0:#如果w1不是空列表,则调用其第一项
        w1[0].paint()
    clock.tick(0)#将帧数限制设为无限制
    pygame.display.flip()



    
    '''



class PopupWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Popup Window")
        self.geometry("200x100")

    def show_message(self, message):
        messagebox.showinfo("Message", message)


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame Popup Message Box")

popup_window = PopupWindow()

running = True
while running:
    for event in pygame.event.get():
        user_input = input("User input: ")
        if user_input.lower() in [ "exit", "quit"]:
            print("chat ends.")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="llama3.2",      
            messages=messages,    # a list of dictionary contains all chat dictionary
        )
        # 提取模型回复
        assistant_reply = response.choices[0].message.content
        #print(f"Llama: {assistant_reply}")

        # 将助手回复添加到对话历史
        messages.append({"role": "assistant", "content": assistant_reply})

        popup_window.show_message(f"Llama: {assistant_reply}")

    screen.fill((255, 255, 255))
    pygame.display.flip()

'''