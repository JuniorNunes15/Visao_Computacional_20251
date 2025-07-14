<h1>
    <p align="center">
        Atividade Homografia com 3 imagens
    </p>
</h1>

### Questão: Usando com obase o [código](./homography_Or.py) fornecido, aplique o processo de homografia usando 3 imagens para montar um panorama.


## Resposta:

O código original fornecido faz homografia com 2 imagens, para mudar o código para aceitar 3 apenas foi necessario adicionar uma terceira imagem que seria passada, fazer o processamento da imagem e na hora de fazer a homografia, passar duas imagens por vez.  

O código foi alterado para fazer a homografia das duas primeiras imagens e depois fazer a homografia do resultado das duas primeiras com a terceira imagem, dessa forma o código [homography.py](./homography.py) foi feito com essa alteração.  

Primeiramente tinha pensado em fazer em uma função que passa as imagens e faz a homografia, mas depois resolvi deixar sem função para ficar mais visivel o processo de homografia com as 3 imagens.  

## Imagens Utilizadas:
Foram utilizadas as seguintes imagens para testar o código:  

<p align="center">
  <img src="01.jpg" width="200"/>
  <img src="02.jpg" width="200"/>
  <img src="03.jpg" width="200"/>
  <img src="04.jpg" width="200"/>
  <img src="05.jpg" width="200"/>
  <img src="06.jpg" width="200"/>
</p>


## Primeiro Teste:
O primeiro teste foi feito com as imagens as 3 primeiras imagens, onde ele teve o seguinte resultado:

Após a homografia das duas primeiras imagens:
<p align="center">
    <img src="resultados_1/combined_image.jpg">
</p>

Após a homografia das tres imagens:
<p align="center">
    <img src="resultados_1/combined_image2.jpg">
</p>

O output final ficou como:
<p align="center">
    <img src="resultados_1/output_image.jpg">
</p>

## Segundo Teste:
O segundo teste foi feito utilizando as 3 ultimas imagens, onde foi gerado:

Após a homografia das duas primeiras imagens:
<p align="center">
    <img src="resultados_2/combined_image.jpg">
</p>

Após a homografia das tres imagens:
<p align="center">
    <img src="resultados_2/combined_image2.jpg">
</p>

O output final ficou como:
<p align="center">
    <img src="resultados_2/output_image.jpg">
</p>


## Teste Final:
Para o ultimo teste, decidi pegar algumas imagens mais distantes para ver ver oque iria sair, pegando a primeira imagem, a terceira e a quinta, teve como resultado o seguinte:

Após a homografia das duas primeiras imagens:
<p align="center">
    <img src="resultados_3/combined_image.jpg">
</p>

Após a homografia das tres imagens:
<p align="center">
    <img src="resultados_3/combined_image2.jpg">
</p>

O output final ficou como:
<p align="center">
    <img src="resultados_3/output_image.jpg">
</p>

Ecerrando assim essa questão.
