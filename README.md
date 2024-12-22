# Simulador Circuitos Digitais
### Versão do Interpretador Python: 3.12.1
* Baixe essa versão do Python [aqui](https://www.python.org/downloads/release/python-3121/)

### Dependências
* PySide6 - 6.8.1.1

### Usando o programa
**Antes de começar a usar o programa lembre-se de que ele ainda está em desenvolvimento, logo, muitos recursos ainda não estão disponíveis pois ainda não foram desenvolvidos. Confira o estado atual de desenvolvimento [aqui](https://github.com/users/brunocardosofs/projects/4).**

Para abrir o programa, primeiro instale todas as dependências, você pode instalar cada uma [manualmente](#dependências) ou usar o requirements.txt presente neste repositório.
* O ideal é que seja utilizado um ambiente virtual do python (venv), leia sobre isso [aqui](https://docs.python.org/3/library/venv.html).
* Após clonar este repositório, abra um terminal e navegue até a pasta do projeto
* Use o PIP para instalar as dependências

    ~~~
    pip install -r requirements.txt
    ~~~

* Com o terminal aberto na pasta do projeto, inicie o arquivo main.py

    ~~~
    python main.py
    ~~~

### Compilando com nuitka
**Você pode gerar um executável do programa para utilizá-lo sem a necessidade de fazer isso a partir do python.**

Para fazer isso, primeiro instale o nuitka, você pode usar o requirements-build.txt presente neste repositório.
* Abra um terminal e navegue até a pasta do projeto
* Use o PIP para instalar as dependências

    ~~~
    pip install -r requirements-build.txt
    ~~~

* Com o terminal aberto na pasta do projeto, inicie o arquivo build.py

    ~~~
    python build.py
    ~~~