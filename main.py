from kivy.app import App #Importa a classe App responsável por definir como uma aplicacao móvel
from kivy.uix.screenmanager import ScreenManager, Screen #Screen permite a criacao de Ecras
from kivy.uix.label import Label #Label permite renderizar texto
from kivy.uix.button import Button #Permite renderizar botoes
from kivy.uix.textinput import TextInput #Permite renderizar um objeto que recebe texto do utilizador
from kivy.uix.boxlayout import BoxLayout #Layout em caixas permite organizar os objetos no ecra 

from instructions import txt_instruction, txt_test1, txt_sits, txt_test3

from ruffier import test
 
#Variaveis Globais
age = 0 #idade
name = '' #nome
p1, p2, p3 = 0, 0, 0 #pulsação 1, 2 e 3 igual a zero

class InstrScr(Screen): 
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       instr = Label(text=txt_instruction)
 
       lbl1 = Label(text='Enter your name:', halign='right')
       self.in_name = TextInput(multiline=False)
       lbl2 = Label(text='Enter your age:', halign='right')
 
       self.in_age = TextInput(text='0', multiline=False)
       self.btn = Button(text='Start', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
       self.btn.on_press = self.next
 
       line1 = BoxLayout(size_hint=(0.8, None), height='30sp') 
       line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
       line1.add_widget(lbl1)
       line1.add_widget(self.in_name)
       line2.add_widget(lbl2)
       line2.add_widget(self.in_age)
 
       outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
       outer.add_widget(instr)
       outer.add_widget(line1)
       outer.add_widget(line2)
       outer.add_widget(self.btn)
 
       self.add_widget(outer)

   def next(self): #crição do metodo next, responsavel por realizar a troca de ecrã
        global name, age #indicamos as variaveis que queremos utilizar fora do metodo
        name = self.in_name.text # atualização do valor da variavel com o nome preenchido pelo utilizador
        age = self.in_age.text # atualização do valor da variavel com a idade preenchida pelo utilizador
        self.manager.current = 'pulse1'
 
 
class PulseScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
      
       instr = Label(text=txt_test1)
      
       line = BoxLayout(size_hint=(0.8, None), height='30sp')
       lbl_result = Label(text='Enter the result:', halign='right')
       self.in_result = TextInput(text='0', multiline=False)
      
       line.add_widget(lbl_result)
       line.add_widget(self.in_result)
 
       self.btn = Button(text='Next', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
       self.btn.on_press = self.next
 
       outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
       outer.add_widget(instr)
       outer.add_widget(line)
       outer.add_widget(self.btn)
 
       self.add_widget(outer)
 
   def next(self): #crição do metodo next, responsavel por realizar a troca de ecrã
       global p1
       p1 = self.in_result.text
       self.manager.current = 'sits'

class CheckSits(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       instr = Label(text=txt_sits)
 
       self.btn = Button(text='Next', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
       self.btn.on_press = self.next
 
       outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
       outer.add_widget(instr)
       outer.add_widget(self.btn)
 
       self.add_widget(outer)

   def next(self): #crição do metodo next, responsavel por realizar a troca de ecrã
       self.manager.current = 'pulse2'
 
class PulseScr2(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       instr = Label(text=txt_test3)
 
       line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
       lbl_result1 = Label(text='Result:', halign='right')
       self.in_result1 = TextInput(text='0', multiline=False)
 
       line1.add_widget(lbl_result1)
       line1.add_widget(self.in_result1)
 
       line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
       lbl_result2 = Label(text='Result after test:', halign='right')
       self.in_result2 = TextInput(text='0', multiline=False)
 
       line2.add_widget(lbl_result2)
       line2.add_widget(self.in_result2)
 
       self.btn = Button(text='Finalize', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
       self.btn.on_press = self.next
 
       outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
       outer.add_widget(instr)
       outer.add_widget(line1)
       outer.add_widget(line2)
       outer.add_widget(self.btn)
 
       self.add_widget(outer)

 
   def next(self): #crição do metodo next, responsavel por realizar a troca de ecrã
       global p2, p3
       p2 = self.in_result1.text
       p3 = self.in_result2.text
       self.manager.current = 'result'

class Result(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
       self.instr = Label(text = '')
       self.outer.add_widget(self.instr)
 
       self.add_widget(self.outer)

   def before(self):
        global name
        self.instr.text = name + '\n' + test(P1, P2, P3, age)

 
class HeartCheck(App):
    def build(self): #build é o método para renderizacao grafica em Kivy
        sm = ScreenManager()
        sm.add_widget(InstrScr(name = 'instr'))
        sm.add_widget(PulseScr(name = 'pulse1'))
        sm.add_widget(CheckSits(name = 'sits'))
        sm.add_widget(PulseScr2(name = 'pulse2'))
        sm.add_widget(Result(name = 'result'))
        
        return sm
 
HeartCheck().run()
