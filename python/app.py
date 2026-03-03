from PySide6.QtWidgets import QApplication, QPushButton
    
from.screen.cadastrar import Cadastrar

from screen.listar import Listar
    
import sys 

class App:
    def __init__(self):


        self.app = QApplication(sys.argv)


        self.janela = ()
        self.layout = ()
    
        self.janela.setWindowTitle("Sistema Universidade")
        self.janela.resize(400, 200)
        self.janela.setLayout(self.layout)
        
        self.criar_botao()
        
        self.janela.show()
        
        
    def criar_botao(self):
        botao_listar= QPushButton("Listar")
        self.layout.addWidget(botao_listar)
        botao_listar.clicked.connect(self.abrir_listagem)
        
        def abrir_listagem(self):
            tela_listagem = Listar(self.app)
            tela_listagem.janela.show()
            
            
        def abrir_cadastro(self):    
            self.tela_cadastro = Cadastrar(self.app)
            self.tela_cadastro.janela.show()
            
        
if __name__ == " __main__":
        system = App()     
        sys.exit(system.app.exec())
    
# app = QApplication(sys.argv)
    
# # Tela = Cadastrar (app)
# Tela = Listar (app)
# Tela.janela.show(app)
# sys.exit(Tela.app.exec()) 