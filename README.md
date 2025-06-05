# 🕹️ Jogo da Forca - Flask

Este é um jogo da forca simples desenvolvido com **Python** e **Flask**. O jogador tenta adivinhar uma palavra secreta escolhida aleatoriamente de um arquivo JSON, com um número limitado de tentativas.

## 🚀 Funcionalidades

- Entrada de nome do jogador
- Exibição do progresso da palavra (letras adivinhadas)
- Validação de letras repetidas
- Fim de jogo ao vencer ou esgotar tentativas
- Flash messages para feedback
- Página de lista com todas as palavras do jogo

## 🧰 Tecnologias utilizadas

- Python 3.x
- Flask
- HTML/CSS (com Bootstrap)

## 📁 Estrutura do Projeto

```
jogo_da_forca/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── jogo.html
│   └── palavras.html
│
├── palavras.json
├── forca.py
├── README.md
└── requirements.txt
```

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/rhufy/jogo_da_forca.git
cd jogo_da_forca
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```bash
pip install flask
```

4. Execute a aplicação:

```bash
python forca.py
```

5. Acesse no navegador:

```
http://localhost:5000
```

## 📝 JSON de Palavras (`palavras.json`)

```json
{
  "palavras": [
    "abacaxi",
    "computador",
    "elefante",
    "bicicleta",
    "janela",
    "montanha",
    "girassol",
    "violino",
    "travesseiro",
    "dinossauro",
    "aspirador",
    "relampago",
    "estatua",
    "pirulito",
    "planeta",
    "chocolate",
    "brinquedo",
    "escola",
    "floresta",
    "oceano"
  ]
}
```

## ✅ TODO

- Adicionar contagem de partidas vencidas
- Interface mais estilizada com CSS customizado
- Responsividade para mobile

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
---

Desenvolvido por [João Carlos](https://www.linkedin.com/in/dev-joao-carlos/) 🚀
[github](https://github.com/rhufy)