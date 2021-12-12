# Boas vindas ao Repositorio do API com Order With Python!

# Instruções para iniciar a API:

## 🗒 Como iniciar a API:

1. Verifique sua versão de Python

   - A versão deve ser igual a `Python 3.8.10`
   - Use o commando `python3 --version` para verificar sua versão.
   - Caso não tenha o python instalado no seu computador aqui segue o passo a passo:

    ### Ubuntu
    ```
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.8
    ```
    ### Windows
    ```
    # Download and Install python from https://www.python.org/downloads
    ```
2. Clone o repositório e inicie o projeto

    - Clone o repositório
    ```
    git clone git@github.com:Crypto-Mikael/PSEL-CROSSCOMMERCE.git
    cd PSEL-CROSSCOMMERCE
    ```
    - Estancie uma venv (Ubuntu)
    ```
    python3 -m venv env
    source env/bin/activate
    ```
    -- Estancie uma venv (Windows)
    ```
    python3 -m venv env
    .\env\Scripts\activate
    ```
    - Instale os modulos de dependencia do projeto
    ```
    pip3 install -r requirements.txt
    ```
    - Inicie a API localmente
    ```
    uvicorn main:app --reload
    ```
  
  
