# Aplicação entrega 3 

## Aplicação desenvolvida para o trabalho final da disciplina SCC0240 - Bases de Dados

**Alunos**:
  - Arthur Vergaças | 12542672
  - Guilherme Panza | 12543519
  - Henrique Bovo | 12542539
  - Maria Júlia De Grandi | 12542501
  - Théo Bruno Riffel | 12547812

## Como executar o projeto

### Configurando a aplicação

A aplicação se conecta a um banco de dados. A configuração da conexão para acessar o seu banco é definida no arquivo `.env`, na raiz do projeto.

Por conveniência, é disponibilizado um arquivo `.env.sample` em que você pode preencher os dados de acesso ao seu banco. Com todos os dados preenchidos, basta renomear o arquivo para `.env` para que as configurações sejam carregadas pela aplicação.

### Rodando a aplicação

Para executar o projeto, você deve ter instalado na sua máquina o **Python** na versão **3.10 ou superior**.

Na _root_ do projeto, rode o seguinte comando para instalar as dependências do projeto:

```sh
pip install -r requirements.txt
```

Após instalar as bibliotecas com sucesso, basta rodar a aplicação através do seguinte comando:

```sh
python src/main.py
```
