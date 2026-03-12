from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from screen.cadastrar import Cadastrar
from screen.listar import Listar

import sys

class App:
    def __init__(self):
        self.app = QApplication(sys.argv)

        # Criar janela principal
        self.janela = QWidget()
        self.janela.setWindowTitle("Sistema Universidade")
        self.janela.resize(400, 200)

        # Criar layout
        self.layout = QVBoxLayout()
        self.janela.setLayout(self.layout)

        # Criar botões
        self.criar_botoes()

        self.janela.show()

    def criar_botoes(self):
        # Botão Listar
        botao_listar = QPushButton("Listar")
        botao_listar.clicked.connect(self.abrir_listagem)
        self.layout.addWidget(botao_listar)

        # Botão Cadastrar
        botao_cadastrar = QPushButton("Cadastrar")
        botao_cadastrar.clicked.connect(self.abrir_cadastro)
        self.layout.addWidget(botao_cadastrar)

    def abrir_listagem(self):
        self.tela_listar = Listar(self.app)
        self.tela_listar.janela.show()

    def abrir_cadastro(self):
        self.tela_cadastro = Cadastrar(self.app)
        self.tela_cadastro.janela.show()


if __name__ == "__main__":
    sistema = App()
    sys.exit(sistema.app.exec())