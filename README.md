# PySlideshow

Esta ferramenta é um gerador de slides que, permite ao utilizador, criar slideshows através de um ficheiro texto. Este ficheiro está escrito numa linguagem predefinida.

### Formato da Linguagem


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

        slide...
    img (query = "boneco de peluche", cont = "bl" )
     duration (time = 3)

        slide..
end
```

## 
