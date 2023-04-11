# PySlideshow

Esta ferramenta é um gerador de slides que, permite ao utilizador, criar slideshows através de um ficheiro texto.

### MÓDULOS UTILIZADOS:

1. Lark - módulo que permite fazer o parsing do ficheiro texto escolhido pelo utilizador
2. Pillow PIL - módulo
3. Flit - módulo
4. Argparse - módulo
5. CV2 - módulo que transforma os slides produzidos em vídeo

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


