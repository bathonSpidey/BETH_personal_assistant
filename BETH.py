#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:07:52 2019

@author: abir
"""
#importing all the libraries
import wx
from gtts import gTTS
import wikipedia
from io import BytesIO
from tempfile import TemporaryFile
from pygame import mixer
import wolframalpha
from random import randint

#Initializing beth
mp3_fp1 = BytesIO()
tts1 = gTTS('Hello! my Name is BETH. Short for Basic Embodiment of a Talking Humanoid. I am here to help ', 'en')
mixer.init()
sf1 = TemporaryFile()
tts1.write_to_fp(sf1)
sf1.seek(0)
mixer.music.load(sf1)
mixer.music.play()

#Code for GUI shout out to khanrad tutorials on youtube
class MyFrame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(500, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="BETH")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am B.E.T.H your personal Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(500,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        ask = self.txt.GetValue()
        ask = ask.lower()
        
        if ask=='who are you' or ask=='what are you':
            response=['I am whatever you want me to be', 'I can be your friend or your enemy',
                      'What do you think I am?','I am an pseudo A.I created by a boy who has nowhere to go' ]
            a=randint(0, 3)
            print(response[a])
            tts3 = gTTS(response[a], 'en')
            mixer.init()
            sf3 = TemporaryFile()
            tts3.write_to_fp(sf3)
            sf3.seek(0)
            mixer.music.load(sf3)
            mixer.music.play()
        elif ask=='who created you':
            response2=['I was created by a man who refused to give up', 'I was inspired from a strong and amazing woman',
                       'Like all creation in the cosmos, I was built up from tiny particles yet to be discovered by man']
            a=randint(0, 2)
            print(response2[a])
            tts3 = gTTS(response2[a], 'en')
            mixer.init()
            sf3 = TemporaryFile()
            tts3.write_to_fp(sf3)
            sf3.seek(0)
            mixer.music.load(sf3)
            mixer.music.play()
        else:
            try:
                #wolframalpha
                app_id="WYPU95-T5W9K54VQX"
                client=wolframalpha.Client(app_id)
                res=client.query(ask)
                answer=next(res.results).text
                print(answer)
                tts2 = gTTS(answer, 'en')
                mixer.init()
                sf2 = TemporaryFile()
                tts2.write_to_fp(sf2)
                sf2.seek(0)
                mixer.music.load(sf2)
                mixer.music.play()
            
            except:
                #wikipedia
                print(wikipedia.summary(ask))


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
app.MainLoop()
