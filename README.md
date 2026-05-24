# CPF/CNPJ Validator

Aplicação web desenvolvida com Streamlit para validação e geração de documentos brasileiros. O projeto oferece suporte a CPF, CNPJ tradicional e ao novo padrão de CNPJ alfanumérico, seguindo as regras oficiais de cálculo dos dígitos verificadores.

## Funcionalidades

### Validação de documentos

- Validação de CPF
- Validação de CNPJ numérico
- Validação de CNPJ alfanumérico
- Remoção automática de caracteres de formatação
- Verificação dos dígitos verificadores

### Geração de documentos

- Geração de CPF válido
- Geração de CNPJ numérico válido
- Geração de CNPJ alfanumérico válido

## Tecnologias Utilizadas

- Python 3
- Streamlit
- Docker
- Docker Compose

## Estrutura do Projeto

```text
.
├── .dockerignore
├── Dockerfile
├── docker-compose.yaml
├── src
│   ├── HOME.py
│   ├── pages
│   │   ├── 1_VALIDADOR_CPF.py
│   │   ├── 2_VALIDADOR_CNPJ.py
│   │   ├── 3_GERADOR_CPF.py
│   │   ├── 4_GERADOR_CNPJ.py
│   │   └── 5_GERADOR_CNPJ_ALFANUM.py
│   └── utils
│       ├── cpf.py
│       └── cnpj.py
├── .gitignore
├── README.md
└── requirements.txt
```

### Organização dos Arquivos

| Arquivo | Descrição |
|----------|------------|
| `HOME.py` | Página inicial da aplicação |
| `1_VALIDADOR_CPF.py` | Interface para validação de CPF |
| `2_VALIDADOR_CNPJ.py` | Interface para validação de CNPJ |
| `3_GERADOR_CPF.py` | Interface para geração de CPF |
| `4_GERADOR_CNPJ.py` | Interface para geração de CNPJ numérico |
| `5_GERADOR_CNPJ_ALFANUM.py` | Interface para geração de CNPJ alfanumérico |
| `utils/cpf.py` | Implementação das regras de CPF |
| `utils/cnpj.py` | Implementação das regras de CNPJ |

## Execução Local

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/cpf-cnpj-validator.git
cd cpf-cnpj-validator
```

### 2. Crie um ambiente virtual

Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
streamlit run src/HOME.py
```

A aplicação estará disponível em:

```text
http://localhost:8501
```

## Executando com Docker

### Construir a imagem

```bash
docker build -t cpf-cnpj-validator .
```

### Executar o container

```bash
docker run --rm -it -p 8501:8501 cpf-cnpj-validator
```

## Executando com Docker Compose

Subir a aplicação:

```bash
docker compose up --build
```

Executar em segundo plano:

```bash
docker compose up -d --build
```

Encerrar os serviços:

```bash
docker compose down
```

## Algoritmos Implementados

### CPF

A validação de CPF contempla:

- Remoção de caracteres não numéricos
- Verificação do comprimento do documento
- Rejeição de sequências repetidas
- Cálculo dos dois dígitos verificadores

### CNPJ

A validação de CNPJ contempla:

- CNPJ numérico tradicional
- CNPJ alfanumérico
- Cálculo dos dígitos verificadores conforme especificação oficial
- Tratamento de caracteres de formatação

## Objetivo

Este projeto foi desenvolvido com fins educacionais e de demonstração técnica, servindo como referência para implementação dos algoritmos de validação e geração de documentos brasileiros em aplicações Python.
