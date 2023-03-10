# Case Processo Seletivo GVCode
### Classificação de elementos de uma lista

## Features
### Opções de classificação
- Palavras
- Números
- Caracteres.

### Formas de classificação
Ver [_comandos_](https://github.com/Tiui50/GVCode-PS-lista-elementos/tree/thiago#comandos "Comandos!")
- Alfabética  
- Alfabética invertida 
- Crescente 
- Decrescente.

### Formas de entrada
- Manual;
- Arquivo (.txt)

## Execução
### Iniciar o programa

    python3 index.py
    
### Comandos

    classify: Classifica uma lista de elementos
        -f [<caminho do arquivo .txt>] : Usa entrada por arquivo em vez de manual (default)
        --dedupe : Desduplica os itens da lista
        --invert : Inverte a classificação (ordem decrescente ou alfabética invertida)
        --no-numbers : Excluí todos os números de uma lista
        -s [<caminho do arquivo para salvar>]: Salva a lista classificada (**CUIDADO!** O programa sobre escreverá o arquivo .txt caso ele já exista!)
    exit : Sai do programa.
