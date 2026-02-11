# Projeto Universidade

Modelagem em Orientaçao à Objetos das Entidades Alunos, Cursos e Turmas.

# Casos de Uso
```mermaid
flowchart LR
    Usuario([secretaria])

    UC1((Cadastrar Alunos))
    UC2((Editar Alunos))
    UC3((Transferir Aluno))

    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3
```

## Diagrama de classes
```mermaid
classDiagram
    class Aluno{
        - Nome
        - Email
        - CPF
        - Telefone
        - Endereço
        - Matricula
        + Cadastrar()
        + editar()
        + transferir()
    }
```

## Dependencias
- **VSCode**: IDE(Interface de Desenvolvimento)

- **Mermaid**: Linguagem para confecçao de Diagramas em documentos MD (Mark Down)

- **Material Icon Theme**: Tema para as pastas.

- **Git Lens**: Interface grafica pra o 
versionamento .git integrada ao VSCode.