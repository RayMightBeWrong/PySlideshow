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

Usando # é possível definir variáveis que depois são chamadas, novamente, usando #

#### Tags e slides

Existem 4 tipos de tags:

###### text
1. text - define o conteúdo
2. font - define a font do texto
3. size - define o tamanho do texto
4. cont - define o container em que se coloca o texto
5. color - define a cor do texto
6. center - opcional, pode ser TRUE ou FALSE (por defeito) e decide se o texto deve ser centrado

###### img
1. query - indica que pesquisa é que deve ser feito para obter a imagem
2. src - indica aonde está imagem, caso seja uma imagem que exista localmente
3. cont - define o container em que se coloca a imagem
4. center - opcional, pode ser TRUE ou FALSE (por defeito) e decide se a imagem deve ser centrada
    
###### duration
Tem apenas um atributo, "time", que define a duração de um slide no vídeo

###### slide
Assinala que se deve produzir um slide com as tags que estão "abertas"

Cada tag (exceto o slide) é "fechada" usando um ".".


