# Plant Finder :cactus:

### Descrição:
Aplicação em Python que faz raspagem de informações das plantas no site do [Jardineiro.net](https://www.jardineiro.net/plantas-de-a-a-z) e formata os dados.


### Principais tecnologias utilizadas:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Habilidades Desenvolvidas: 

- Aplicar técnicas de raspagem de dados;
- Extrair dados de conteúdo HTML através de seletores;
- Formatação de dados presentes no HTML

### Como rodar a aplicação:

```bash
# Clone o repositório:
git clone https://github.com/Marcuscps19/crawler-plant-finder.git

# Entre no diretório
cd crawler-plant-finder

# Crie o ambiente virtual para o projeto
python3 -m venv .venv && source .venv/bin/activate
```

No arquivo plant_finder/scraper.py, possui uma função plants_infos, ao ser chamada exibirá uma a uma as informações das plantas, descomente as seguintes linhas no final do documento e execute com o [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner).

```
  if(__name__ == '__main__'):
    plants_infos()
```

Para parar a execução, utilize Ctrl + C no terminal, são mais de 900 plantas.

#### Funcionalidades:

Atualmente esse Web Crawler busca as informações de cada planta no site, formata e as exibem com o print.
A exibição com o print é provisória.

#### Próximos Passos:

   Esse crawler salvará as informações no [MongoDB Atlas]https://www.mongodb.com/atlas/database e através de uma API [Node](https://nodejs.org/en/), consumirá esses dados e os exibirão em uma página web feita com [Javascript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) e [ReactJS](https://pt-br.reactjs.org/docs/getting-started.html) com busca aprimorada dessas informações.
