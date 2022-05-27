from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import random

class Dados(App):
    #Este es el constructor
    def __init__(self,**kwargs):
        #Llamar al constructor de la clase base (App)
        super().__init__(**kwargs)
        #Defino un atributo

    #Eventos
    def btnAccion_dado(self,obj):
        #Generar el numero en el dado        
        num = random.randint(1,6)
        #Cambiar la etiqueta (atributo)
        self.lblNumDado.text = str(num)

    #Todos los elementos visuales se definene o encadenan aqui
    def build(self):
        #Vamos a definir un layout
        gdl_principal = GridLayout(rows=3,cols=1)
        #Etiqueta
        lblTitulo = Label(text="Aplicacion Dado")
        gdl_principal.add_widget(lblTitulo)
        #Grid medio
        gdl_medio = GridLayout(cols=2)
        lblResultado = Label(text="Resultado")
        gdl_medio.add_widget(lblResultado)
        lblNumDado = Label(text="6")
        gdl_medio.add_widget(lblNumDado)
        gdl_principal.add_widget(gdl_medio)
        #Boton
        btnAccion = Button(text="Presioname!!!")
            #Enlazar
        btnAccion.bind(on_press=self.btnAccion_dado) 
        gdl_principal.add_widget(btnAccion)
        #Atributos
        self.lblNumDado = lblNumDado
        self.gdl_principal = gdl_principal
        return gdl_principal

if __name__ == '__main__':
    D = Dados()
    D.run()
