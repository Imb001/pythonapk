#import kivy
#from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
#from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton

from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
#from kivymd.uix.button.button import MDIconBotton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from kivymd.font_definitions import theme_font_styles
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.textinput import TextInput
from kivmob import KivMob
#import sqlite3
#from sqlite3 import Cursor, Error
import base64
import openai

import requests
import json

import arabic_reshaper
import bidi.algorithm


#Window.size = (320, 580)
#Window.keyboard_anim_args = {'d': 12, 't': 'in_out_expo'}
#Window.softinput_mode = "below_target"

key = bWltaT09c2stdEJFU25HTmVXcEN0UWp6VnJqVWdUM0JsYmtGSkVIZEk1WUJDeDNvNWp5eGF4SjNr

class ProfileCard(MDFloatLayout):
     pass

class SearchBar(MDFloatLayout):
     pass

#class Layout_(FloatLayout):
    #pass


class ComanadFloat(MDFloatLayout):
    pass

#class Copy_(MDIconButton):
	#pass

class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "RSan.ttf"
    #font_size = '15sp'

class Command_2(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "noto.ttf"
   # font_size = 20

class Response(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "RSan.ttf"
    #font_size = 

class Response_2(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "noto.ttf"
    #font_size = 20
    

class Ar_text(TextInput):
    #global str
    max_chars = NumericProperty(10)  # maximum character allowed
    str = StringProperty()

    def __init__(self, **kwargs):
        super(Ar_text, self).__init__(**kwargs)
        #self.text= bidi.algorithm.get_display(arabic_reshaper.reshape("اطبع شيئاً"))

    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        if self.text == "":
        	self.str = ""
        self.str = self.str+substring
        self.text = bidi.algorithm.get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(Ar_text, self).insert_text(substring, from_undo)
        # print("A")

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = bidi.algorithm.get_display(arabic_reshaper.reshape(self.str))
        # print("B")
    	
class Xchat(MDApp):
   # dialog = None
    
    def build(self):
        global screen_manager
        

        screen_manager = ScreenManager()
        
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"


        # screen_manager.add_widget(Builder.load_file("about_ass8.kv"))
        # screen_manager.add_widget(Builder.load_file("loading.kv"))
        screen_manager.add_widget(Builder.load_file("mode.kv"))


        screen_manager.add_widget(Builder.load_file("assistant.kv"))
        screen_manager.add_widget(Builder.load_file("assistchat.kv"))
        screen_manager.add_widget(Builder.load_file("assistchat2.kv"))
        screen_manager.add_widget(Builder.load_file("assistchat3.kv"))
        screen_manager.add_widget(Builder.load_file("assistchat4.kv"))
        screen_manager.add_widget(Builder.load_file("assistchat5.kv"))
        screen_manager.add_widget(Builder.load_file("assistchat6.kv"))
        screen_manager.add_widget(Builder.load_file("assistchat7.kv"))
        screen_manager.add_widget(Builder.load_file("assistchat8.kv"))
        

        screen_manager.add_widget(Builder.load_file("about_ass.kv"))
        screen_manager.add_widget(Builder.load_file("about_ass2.kv"))
        screen_manager.add_widget(Builder.load_file("about_ass3.kv"))
        screen_manager.add_widget(Builder.load_file("about_ass4.kv"))
        screen_manager.add_widget(Builder.load_file("about_ass5.kv"))
        screen_manager.add_widget(Builder.load_file("about_ass6.kv"))
        screen_manager.add_widget(Builder.load_file("about_ass7.kv"))
        screen_manager.add_widget(Builder.load_file("about_ass8.kv"))
    
        screen_manager.add_widget(Builder.load_file("about_mimi.kv"))
        
        f = open("textfile2.txt", "r")
        #r = f.read()
        r = self.dcod(f.read())
        
        openai.api_key = r[6:]
        f.close()

        #self.ads = KivMob('ca-app-pub-3940256099942544~3347511713')
        #self.ads.new_banner('ca-app-pub-3940256099942544/6300978111', top_pos=True)
        #self.ads.new_interstitial('ca-app-pub-3940256099942544/1033173712')
        #self.ads.request_interstitial()
        
        # sekf.cookies_db()
        
        return screen_manager
    
    #def on_start(self):
     #	screen_manager.current = "mode"
     #    Clock.schedule_once(self.login, 15)
        
    # def login(self, *args):
    #     screen_manager.current = "mode"
    #     self.call1()




    #def call1(self):
       # self.ads.request_banner()
     #   self.ads.show_banner()

   # def call2(self):
      #  self.ads.hide_banner()

    #def on_resume(self):
        #self.ads.request_interstitial()

    #def show2(self, *args):
        #if self.ads.is_interstitial_loaded():
           # self.ads.show_interstitial()

    # def chat_mode(self):
    #     global chat_version
    #     openai.api_key = "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"
    #     chat_version2 = "gpt-3.5-turbo" 

#    def cookies_db(self):
#        conn = None
#        try:
#            conn = sqlite3.connect("cookies.db")
#            query1 = ('''CREATE TABLE IF NOT EXISTS cookie_1 (
#                command TEXT (900) PRIMARY KEY
#                UNIQUE,
#                response TEXT
#                );''')
#            conn.execute(query1)
#        except Error as e:
#            print(e)
#        finally:
#            if conn:
#                conn.close()

#    def cookies_db_drop(self):
#        conn = None
#        try:
#            conn = sqlite3.connect("cookies.db")
#            query1 = ('''DROP TABLE cookie_1''')
#            conn.execute(query1)
#        except Error as e:
#            print(e)
#        finally:
#            if conn:
#                conn.close()

#    def create_cookies(self, a, b):
#        try:
#            connect = sqlite3.connect("cookies.db")
#            cursor = connect.cursor()      
#            query = ("INSERT OR REPLACE INTO cookie_1 (command, response) VALUES(?, ?);")
#            cursor.execute(query, [a, b])    
#            connect.commit()
#            connect.close()
#            return "success"
#            
#        except Exception as Error:
#            print(f"create_ac_cookies {Error}")

#    def copy_t(self):
#        try:
#            connect = sqlite3.connect("cookies.db")
#            cursor = connect.cursor()
#            cursor.execute("SELECT response FROM 'cookie_1';")
#            get_all = cursor.fetchall()
#            # g = len(get_all)
#            print(get_all)
#            connect.commit()
#            connect.close()
#            # return g

#        except Exception as Error:
#            print(f"teach_num error {Error}")
    def dcod(self, ds):
        base64_bytes = ds.encode("ascii")
        sample_s_b = base64.b64decode(base64_bytes)
        sample_s = sample_s_b.decode("ascii")
        return sample_s
  
    def prompt_res(self, *args):
        screen_manager.get_screen(page).send.icon = "send-outline"
        screen_manager.get_screen(page).text_input.hint_text ="Type here.."
      #  screen_manager.get_screen(page).copy_txt.text_color = .535, .600, .533, 1
        #screen_manager.get_screen(page).copy_txt.icon = "content-copy"


    def chat_send(self, page1):
        global size, halign, value, page
        page = page1
        screen = screen_manager.get_screen(page).text_input
        
        if screen != "" or screen != " ":
            value = screen.text
            if len(value) < 3:
                size = .10
                halign = "center"
            elif len(value) < 8:
                size = .26
                halign = "center"
            elif len(value) < 11:
                size = .22
                halign = "center"
            elif len(value) < 16:
                size = .36
                halign = "center"
            elif len(value) < 21:
                size = .46
                halign = "center"
            elif len(value) < 26:
                size = .58
                halign = "center"
            else:
                size = .77
                halign = "left" 
                
                
            if arabic == 'Yes':
                txt = self.arabic_c(value)
                
                screen_manager.get_screen(page).chat2.add_widget(Command_2(text=txt, size_hint_x=size, halign=halign)) 
                #Ar_text(str= " ")
                #screen_manager.get_screen(page).chat2.get_widget(Ar_text())
            else:     
                screen_manager.get_screen(page).chat_list.add_widget(Command(text=value, size_hint_x=size, halign=halign))
            
            screen_manager.get_screen(page).send.icon ="dots-horizontal"
            screen_manager.get_screen(page).text_input.hint_text ="replying in process.."

            if Clock.schedule_once(self.response, 2):
                Clock.schedule_once(self.prompt_res, 2)
              #  screen_manager.get_screen(page).copy_txt.text_color = .535, .600, .533, 1
           #     screen_manager.get_screen(page).copy_txt.icon = "content-copy"
    
            screen_manager.get_screen(page).text_input.text= ""
            
            #self.show2()
        
    def response(self, *args):
        global copy_text
        response = ""
     #   if len(value) != 0:
#            if value.lower() == "hi":
#            	response = "Welcome! How can I help You? Suddenly, he stops and looks around, as if something has caught his attention, Suddenly, he stops and looks around, as if something has caught his attention."

#            #    # for i in range(4):
#            #     #     screen_manager.get_screen('graphic').chat_list.add_widget(ResImageLayout())
#            else:
#             	response = "Sorry, I can not help you now, I am still under development"

#            # # coin = screen_manager.get_screen('mode').availCoin.text
#            # # current = float(coin) - 0.5
#            if arabic == 'Yes':
#            #     # print(arabic)
#                 txt = self.arabic_c(response)
#                 screen_manager.get_screen(page).chat2.add_widget(Response_2(text=txt, size_hint_x=.72,  halign="left"))
#            else:
#                 screen_manager.get_screen(page).chat_list.add_widget(Response(text=response, size_hint_x=.72,  halign="left"))
#            copy_text = response
#            screen_manager.get_screen(page).copy_txt.disable = False
#            screen_manager.get_screen(page).copy_txt.text_color = .535, .600, .533, 1 
#            # # screen_manager.get_screen('mode').availCoin.text = str(current)
#            # self.coin_balance(page)

        chat_version = "gpt-3.5-turbo" 
        loading = "No Internet Connection."
#        loading =	"eet Issac, your go-to AI chatbot assistant for all your science and technology needs. Isaac is an expert in the field, equipped with the latest knowledge and advancements in science and technology. With years of experience and a vast understanding of the subject matter, Isaac can assist you with anything from basic scientific concepts to complex technological innovations.Whether you need help with research, data analysis, or problem-solving, Isaac has got you covered. With a friendly and approachable demeanor, Isaac is always ready to answer your questions and guide you through the complexities of the world of science and technology. So why wait? Start chatting with Isaac today and take your knowledge and skills to the next l"

        if len(value) != 0:
            #try:
            bot = ""
            value2 = f'{assist} ({value}) "remove the introduction."'
            completion = openai.ChatCompletion.create(
                model= chat_version,
                messages= [{'role':'user', 'content':value2}]
                )
            x = json.loads(str(completion))
            bot = x['choices'][0]['message']['content']
            if arabic == 'Yes':
                    txt = self.arabic_c(bot)
                    screen_manager.get_screen(page).chat2.add_widget(Response_2(text=txt, size_hint_x=.72,  halign="left"))
            else:
              	screen_manager.get_screen(page).chat_list.add_widget(Response(text=bot, size_hint_x=.72,  halign="left"))
            copy_text = bot
            screen_manager.get_screen(page).copy_txt.disable = False
            screen_manager.get_screen(page).copy_txt.text_color = .535, .600, .533, 1
            #except:
        #    	if arabic == 'yes' :
            	#	screen_manager.get_screen(page).chat2.add_widget(Response_2(text=loading, size_hint_x=.72,  halign="left"))
           # 	else:
              #  	screen_manager.get_screen(page).chat_list.add_widget(Response(text=loading,  size_hint_x=.72,  halign="left"))
            		
            		
#                
#                # screen_manager.get_screen(page).chat_list2.add_widget(Response(text=bot, size_hint_x=.72, halign="left"))
#            except:
#                
#                if arabic == 'Yes':
#                    # print(arabic)
#                    txt = self.arabic_c(loading)
#                    screen_manager.get_screen(page).chat2.add_widget(Response_2(text=txt, size_hint_x=.72,  halign="left"))
#                else:
#                    screen_manager.get_screen(page).chat_list.add_widget(Response(text=loading, size_hint_x=.72, halign="left"))
#                # self.cookies_db()
#                # self.create_cookies(value, loading)
#                copy_text = loading
#                screen_manager.get_screen(page).copy_txt.disable = False
#                screen_manager.get_screen(page).copy_txt.text_color = .535, .600, .533, 1 
#                




    def copy_press(self):
        try:
            if screen_manager.get_screen(page).copy_txt.disable == False:
            # c = self.copy_t()
             #   print(copy_text)
                Clipboard.copy(copy_text)
            #    print('nothing to copy')
        #    if not self.dialog:
#                 self.dialog = MDDialog(
#                     text="Discard draft?",
#                     buttons=[
#                         MDFlatButton(
#                             text="OK",
#                             theme_text_color="Custom",
#                             text_color=self.theme_cls.primary_color,
#                             )],)
#                 self.dialog.open()
        except:
        	print('Nothing')


	   
	   
    def arabic_m(self):
        global arabic
        arabic = "Yes"

    def not_arabic(self):
        global arabic
        arabic = "No"
        

    def arabic_c(self, txt):
        reshaped_text = arabic_reshaper.reshape(txt)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        return bidi_text



############## CHAT ASSITANCTS ############################# 
    def a_chat_1(self):
        global assist
        assist = f"Act as Science & Technology Expert with the name Isaac"
        page = 'assistchat'
        self.chat_send(page)

    def a_chat_2(self):
        global assist
        assist = f"Act as Health &  Fitness Expert with the name Maya"
        page = 'assistchat2'
        self.chat_send(page)

    def a_chat_3(self):
        global assist
        assist = f"Act as Love & Emotion Expert with the name Kim"
        page = 'assistchat3'
        self.chat_send(page)

    def a_chat_4(self):
        global assist
        assist = f"Act as an Historian with the name Kia"
        page = 'assistchat4'
        self.chat_send(page)
    
    def a_chat_5(self):
        global assist
        assist = f"Act as a Philosophy & Politics Expert with the name Alex"
        page = 'assistchat5'
        self.chat_send(page)

    def a_chat_6(self):
        global assist
        assist = f"Act as a Business & Finance Expert with the name Quinn"
        page = 'assistchat6'
        self.chat_send(page)

    def a_chat_7(self):
        global assist
        assist = f"Act as an Islamic Religion Scholar with the name Ali"
        page = 'assistchat7'
        self.chat_send(page)

    def a_chat_8(self):
        global assist
        assist = f"Act as an Christianity Religion theologian with the name Mathew"
        page = 'assistchat8'
        self.chat_send(page)



  



if __name__ == "__main__":
    Xchat().run()
