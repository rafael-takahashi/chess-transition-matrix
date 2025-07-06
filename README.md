# Análise de Resultados de Partidas de Xadrez com Python e R

Este projeto realiza a análise de resultados de partidas de xadrez a partir de arquivos PGN, focando em um jogador específico. Utiliza Python para extrair os resultados e R para montar e analisar a matriz de transição de uma cadeia de Markov.

## Como executar

Para a instalação da biblioteca `python-chess`

```bash
pip install -r requirements.txt
```

Para instalar o pacote necessário para análise da cadeia de Markov, abra o R ou RStudio e execute o comando:

```r
install.packages("markovchain")
```

No terminal, dê permissão de execução (se necessário) e execute:

```bash
chmod +x script.sh
./script.sh
