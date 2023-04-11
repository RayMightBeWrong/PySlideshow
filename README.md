# PySlideshow

Esta ferramenta é um gerador de slides capaz de criar slideshows através de um ficheiro texto.

### MÓDULOS UTILIZADOS:

1. Lark - módulo usado para fazer o parsing do ficheiro texto escolhido pelo utilizador
2. Pillow PIL - módulo usado para criar slides (imagens) através da informação recolhida
3. Flit - módulo que permite empacotar um projeto Python
4. Argparse - módulo que permite fazer o parsing de argumentos e opções no terminal
5. CV2 - módulo usado transforma os slides produzidos em vídeo

### FORMATO DA LINGUAGEM:

#### Exemplo:

```
config = {
    width: 1920,
    height: 1080
}

#text1 = "Hello World!"

start 
    text (text = #text1, font = "Times New Roman", size = 12, cont = "rl", color = "white")
        img (query = "planet earth", cont = "bl" )
            duration (time = 3)
                slide
            .
        .
    .
end
```

#### Config (opcional)

Na configuração é escolhido a resolução dos slides

#### Variáveis (opcional)

Usando # é possível definir variáveis que depois são chamados, novamente, usando #

#### Tags e slides

Existem 4 tipos de tags:
1. text
2. img
3. duration
4. slide

