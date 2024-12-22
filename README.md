# Simulador Circuitos Digitais

O **Simulador Circuitos Digitais** é uma ferramenta interativa para simular os sistemas físicos propostos em laboratórios de circuitos digitais. Este projeto está em estágio inicial de desenvolvimento, e alguns recursos ainda estão sendo implementados. Confira o progresso do projeto [aqui](https://github.com/users/brunocardosofs/projects/4).

## Requisitos
- **Python:** 3.13.1 ou superior. Baixe a versão mais recente no [site do python](https://www.python.org/downloads/).

### Dependências
- **Interface gráfica:** PySide6 (versão 6.8.1.1).

## Usando o programa

Siga estas etapas para rodar o programa:

1. **Configure um ambiente virtual (opcional, mas recomendado):** Leia como criar um ambiente virtual [aqui](https://docs.python.org/3/library/venv.html).

2. **Instale as dependências:**

    No terminal, navegue até a pasta do projeto e execute:  
    ~~~bash
    pip install -r requirements.txt
     ~~~

3. **Execute o programa:**
    ~~~
    python main.py
    ~~~

### Compilando com nuitka
**O Nuitka é usado para criar um executável do programa, permitindo que ele seja executado sem a necessidade de Python instalado.**

1. **Instale as dependências para a compilação:**

    No terminal, navegue até a pasta do projeto e execute:  
    ~~~bash
    pip install -r requirements-build.txt
     ~~~

2. **Compile o executável:**
 
    ~~~bash
    python build.py
     ~~~

3. **O executável estará disponível na pasta**
    ~~~
    <pasta-do-projeto>/.output/main.dist/
    ~~~