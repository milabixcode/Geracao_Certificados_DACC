# Certificate Generator

Ferramenta para vasculhar planilhas e gerar todos os certificados de alguém que estuda no CC na uff.

## Como usar

Para ter acesso às planilhas do Drive, é necessário entrar em um projeto do Google Cloud com permissão para
acesso à API do Drive. O passo a passo dessa configuração pode ser encontrado no [Quickstart de Python](https://developers.google.com/drive/api/quickstart/python?hl=en).

## TODO

- Avaliar se vai dar para baixar as planilhas como CSV ou precisaremos de uma lib para trabalhar com planilhas

- Normalizar o máximo de planilhas que der com base nos dados das entidades
- Strategies
  - BaseExtractor
  - Criar N formas diferentes de tirar os dados da planilha, de acordo com a planilha
- Fazer o gerador de certificados gerar uma pasta com todos os certificados que ele encontrar de uma vez

## Done

- Usar `poetry` e `pyenv`
- Pensar em como obter as planilhas do drive de forma fácil
  - vamos usar a API do Google Drive para baixar os documentos
- Feita a listagem das planilhas da árvore de arquivos da pasta de Eventos

## Futuro

- Fazer uma linha de comando para poder usar a ferramenta de várias formas diferentes
  - Obter todos os certificados conhecidos do aluno
  - sugestão: enviar emails para todos os certificados de uma planilha nova em específico
- Adicionar um email sender para enviar certificados por email
- Dar uma olhada na lib `typer` pra fazer a linha de comando
