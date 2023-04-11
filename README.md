# PySlideshow

Esta ferramenta é um gerador de slides capaz de criar slideshows através de um ficheiro texto.

### MÓDULOS UTILIZADOS:

1. Lark - módulo usado para fazer o parsing do ficheiro texto escolhido pelo utilizador
2. Pillow PIL - módulo usado para criar slides (imagens) através da informação recolhida
3. Flit - módulo que permite empacotar um projeto Python
4. Argparse - módulo que permite fazer o parsing de argumentos e opções no terminal
5. CV2 - módulo usado transforma os slides produzidos em vídeo

### FORMATO DA LINGUAGEM:

##### Exemplo:

```
config = {
    width: 1920,
    height: 1080
}

#black = (10,30,40)
#white = 0xFFFFF1

start 
    text (text = "../atuamae/", font = "asdsad", size = 12, cont = "rl", color = #white)
        img (query = "boneco de peluche", cont = "bl" )
            duration (time = 3)
                slide
            .
        .
    .
    img (query = "boneco de peluche", cont = "bl" )
        duration (time = 3)
            slide
        .
    .
end
```


