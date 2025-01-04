from kivy.app import App #Importa a classe App respomnsável por definir como uma aplicação móvel
from kivy.uix.screenmanager import Screen #Screen permite a criação de ecrãs

class InstrScr(Screen): #primeiro ecrã
    def __init__(self, **kwargs): #construtor da classe InstrScr, kwargs é um dicionário  
        super().__init__(*kwargs)
        
class PulseScr(Screen): 
    def __init__(self, **kwargs): 
        super().__init__(*kwargs)

class CheckSits(Screen): 
    def __init__(self, **kwargs): 
        super().__init__(*kwargs)
        
class PulseScr2(Screen): 
    def __init__(self, **kwargs): 
        super().__init__(*kwargs)
        
class Result(Screen): 
    def __init__(self, **kwargs): 
        super().__init__(*kwargs)
        
class HeartCheck(App):
    def build(self): #build e o método para rederinzação gráfica em Kivy
        return InstrScr()
    
    
HeartCheck().run() #run é o loop onde acontece o aplicativo