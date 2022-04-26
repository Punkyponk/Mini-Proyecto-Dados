# Mini-Proyecto-Dados
######################################################################################
## Este es un programa que genera un numero aleatorio de un Dado presionando un boton
######################################################################################












from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
class Dados(App):
	#Este es el constructor
    def __init__(self,**kwargs):
		# llamar al constructor de la clase base (App)
        super().__init__(**kwargs)
        # Defino un atributo
        
    def build(self):
         #Vamos a definir un layout
        gdl_principal = GridLayout(rows=3,cols=1)
        lbltitulo = Label(text='Aplicacion Dado')
        gdl_principal.add_widget(lbltitulo)
        #Grid medio
        gdl_medio = GridLayout(cols=2)
        lblresultado = Label(text='Resultado')
        gdl_medio.add_widget(lblresultado)
        lblnumdado = Label(text="")
        gdl_medio.add_widget(lblnumdado)
        gdl_principal.add_widget(gdl_medio)        
        #Boton
        btnaccion = Button(text="Presioname!!")
        gdl_principal.add_widget(btnaccion)
        self. gdl_principal =  gdl_principal
        return  gdl_principal
        
if __name__== '__main__':
    D = Dados()
    D.run()
