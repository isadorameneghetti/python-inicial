# Sabor Express - Sistema de Gerenciamento de Restaurantes

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Concluído-green.svg)


## 📋 Sobre o Projeto

O **Sabor Express** é minha primeira aplicação em Python, desenvolvida durante o curso **"Python: crie sua primeira aplicação"** da Alura. Este projeto marca o início da minha jornada de aprendizado em programação, com o objetivo de me especializar em **Engenharia de Inteligência Artificial**.

O sistema é um gerenciador de restaurantes simples que permite cadastrar, listar e ativar/desativar restaurantes através de um menu interativo no terminal. Mais do que um projeto funcional, este repositório documenta **minha evolução como programador** - cada aula representa um degrau na escada que estou construindo rumo à Engenharia de IA.

## 🎯 Minha Trilha para Engenharia de IA

```
🚀 Python Básico (Sabor Express) ⬅️ Você está aqui
   ↓
🧠 Python: Orientação a Objetos (Próximo curso)
   ↓
📊 Bibliotecas Científicas (NumPy, Pandas, Matplotlib)
   ↓
🤖 Fundamentos de Machine Learning
   ↓
🧬 Deep Learning & Redes Neurais
   ↓
⚡ Engenharia de IA (Objetivo Final)
```

## 📁 Estrutura Completa do Projeto

```
PYTHON-INICIAL/
│
├── aula01/                          # 🎯 Fundamentos Básicos
│   ├── exercicios/                   # Prática dos conceitos
│   │   ├── exercicio02.py
│   │   ├── exercicio03.py
│   │   └── exercicio04.py
│   └── app.py                         # Primeira versão do sistema
│
├── aula02/                          # 🎯 Estruturas de Dados I
│   ├── exercicio/                     # Prática dos conceitos
│   │   ├── exercicio01.py
│   │   ├── exercicio02.py
│   │   ├── exercicio03.py
│   │   └── exercicio04.py
│   └── app.py                         # Evolução com funções
│
├── aula03/                          # 🎯 Controle de Fluxo
│   ├── exercicios/                    # Prática dos conceitos
│   │   ├── exercicio01.py
│   │   ├── exercicio02.py
│   │   ├── exercicio03.py
│   │   ├── exercicio04.py
│   │   ├── exercicio05.py
│   │   ├── exercicio06.py
│   │   └── exercicio07.py
│   └── app.py                         # Versão com listas
│
├── aula04/                          # 🎯 Funções e Modularização
│   ├── exercicios/                    # Prática dos conceitos
│   │   ├── exercicio01.py
│   │   ├── exercicio02.py
│   │   ├── exercicio03.py
│   │   ├── exercicio04.py
│   │   └── exercicio05.py
│   └── app.py                         # Versão com dicionários
│
├── aula05/                          # 🎯 Projeto Final
│   └── app.py                         # Versão final com docstrings
│
└── README.md                         # Documentação do projeto
```

## 🚀 A Evolução do Código (app.py)

Cada pasta contém um `app.py` que representa a versão do Sabor Express naquele estágio do aprendizado:

### 📍 **aula01/app.py** - O Primeiro Passo
```python
print('Sabor Express')
print("""
1. Cadastrar restaurante
2. Listar restaurante
3. Ativar restaurante
4. Sair
""")
opcao_escolhida = input('Escolha uma opção: ')
print(f'Você escolheu a opção: {opcao_escolhida}')
```
**Conceitos:** print(), input(), f-strings, menu simples

### 📍 **aula02/app.py** - Organização com Funções
```python
import os

def exibir_titulo():
    print('Sabor Express')

def finalizar_app():
    os.system('cls')
    print('Finalizando app\n')

def main():
    exibir_titulo()
    exibir_menu()
    escolher_opcao()
```
**Conceitos:** Funções, importação de módulos, estruturação inicial

### 📍 **aula03/app.py** - Listas e Navegação
```python
restaurantes = ['Pizza', 'Sushi']

def cadastrar_restaurante():
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)

def voltar_menu():
    input('\nPressione qualquer tecla para continuar...')
    main()
```
**Conceitos:** Listas, append(), navegação entre telas

### 📍 **aula04/app.py** - Dicionários e Estruturação
```python
restaurantes = [
    {'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False},
    {'nome': 'Sushi', 'categoria': 'Japonesa', 'ativo': True}
]

def listar_restaurante():
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'{nome} | {categoria} | {ativo}')
```
**Conceitos:** Dicionários, estruturas aninhadas, formatação

### 📍 **aula05/app.py** - Versão Profissional
```python
def cadastrar_restaurante():
    '''
    Essa função é responsável por cadastrar um novo restaurante.
    Solicita nome e categoria, cria um dicionário e adiciona à lista.
    '''
    iniciar_opcao('Cadastrar restaurante')
    nome_restaurante = input('Digite o nome do restaurante: ')
    # ... resto do código
```
**Conceitos:** Docstrings, boas práticas, código limpo

## 📚 O que Aprendi em Cada Aula

### **aula01 - Fundamentos Básicos**
- **Conceitos:** Variáveis, tipos primitivos, entrada/saída
- **Exercícios:** 3 exercícios práticos
- **Habilidade:** Criar programas simples com interação do usuário

### **aula02 - Estruturas de Dados I**
- **Conceitos:** Listas, operadores, condicionais básicas
- **Exercícios:** 4 exercícios práticos
- **Habilidade:** Armazenar e manipular coleções de dados

### **aula03 - Controle de Fluxo**
- **Conceitos:** Loops (for/while), condicionais avançadas
- **Exercícios:** 7 exercícios práticos
- **Habilidade:** Controlar o fluxo do programa e repetições

### **aula04 - Funções e Modularização**
- **Conceitos:** Criação de funções, parâmetros, retorno, escopo
- **Exercícios:** 5 exercícios práticos
- **Habilidade:** Organizar código em blocos reutilizáveis

### **aula05 - Projeto Final e Boas Práticas**
- **Conceitos:** Docstrings, documentação, código limpo
- **Habilidade:** Escrever código profissional e documentado

## 🛠️ Funcionalidades do Sistema (Versão Final)

### 1. **Cadastrar Restaurante**
- Solicita nome e categoria
- Cria dicionário com status inicial inativo
- Adiciona à lista de restaurantes

### 2. **Listar Restaurantes**
- Exibe todos os restaurantes cadastrados
- Formatação alinhada com `ljust()`
- Status visual (ativo/inativo)

### 3. **Ativar/Desativar Restaurante**
- Busca restaurante por nome
- Alterna status usando `not`
- Feedback específico da ação

### 4. **Menu Interativo**
- Interface limpa com tela reiniciada
- Tratamento de opções inválidas
- Pausa para visualização

## 💡 Conexão com o Futuro (Orientação a Objetos)

Este projeto me prepara para o próximo desafio. Veja como o mesmo sistema evoluirá com POO:

### Versão Atual (Estrutural)
```python
restaurantes = []  # Lista global

def cadastrar_restaurante():
    # Função solta
    pass
```

### Versão Futura (Orientada a Objetos)
```python
class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
    def ativar(self):
        self.ativo = True

class Sistema:
    def __init__(self):
        self.restaurantes = []
    
    def cadastrar(self, restaurante):
        self.restaurantes.append(restaurante)
```

## 🧠 Por que isso é importante para IA?

| Conceito Atual | Aplicação em IA |
|----------------|-----------------|
| **Listas** | Armazenar datasets |
| **Dicionários** | Features e labels estruturados |
| **Loops** | Processamento em lote |
| **Funções** | Pipelines de ML |
| **Modularização** | Arquitetura de modelos |

## 🚀 Como Executar

1. **Pré-requisito:** Python 3.x instalado
2. **Navegue até a aula desejada:**
   ```bash
   cd aula05
   ```
3. **Execute o programa:**
   ```bash
   python app.py
   ```

## 📊 Estatísticas do Projeto

- **Total de aulas:** 5
- **Total de exercícios:** 21
- **Versões do app:** 5 (uma por aula)
- **Linhas de código (versão final):** ~200
- **Conceitos aprendidos:** 15+

## 🎓 Sobre o Curso

**Python: crie sua primeira aplicação** - Alura
- **Carga horária:** 8 horas
- **Nível:** Iniciante
- **Conteúdo:** Fundamentos de Python do zero até uma aplicação funcional

## 🔮 Próximos Passos na Trilha IA

Com esta base sólida, estou pronto para:

1. **Curso: Python - Orientação a Objetos**
   - Classes, objetos, herança, polimorfismo
   - Encapsulamento e abstração

2. **Projeto: Refatorar Sabor Express com POO**
   - Aplicar conceitos aprendidos
   - Comparar abordagens

3. **Bibliotecas Científicas**
   - NumPy para arrays multidimensionais
   - Pandas para manipulação de dados

## 💭 Reflexão Final

> "Este repositório é mais que um simples projeto de curso. É o registro do meu primeiro passo na programação, onde cada aula, cada exercício e cada versão do app representam um degrau na escada que estou construindo rumo à Engenharia de Inteligência Artificial. O Sabor Express pode ser simples, mas é a fundação sobre a qual construirei sistemas muito mais complexos."

---

**Desenvolvido com dedicação durante o curso "Python: crie sua primeira aplicação" da Alura** 🐍

*"Todo engenheiro de IA começa com um primeiro 'Hello World'. Este é o meu."*