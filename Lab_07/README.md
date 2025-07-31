<h1>
    <p align="center">
        LAB 07
    </p>
</h1>


### Questão 1: Usando o classificador HaarCascade, crie um programa que realize a detecção de rosto utilizando vídeo. Teste com imagens de diferentes resoluções e crie uma tabela com os tempos de execução em cada caso.
### Questão 2: Repita a questão anterior mas detecte também a boca e os olhos, diferenciando entre olho direito e olho esquerdo.
#### – Em ambas as questões inclua imagens de rostos com as seguintes características:
#### a: Vistos frontal e lateralmente;
#### b: Utilizando acessórios (chapéu, óculos, máscaras, etc);
#### c: Com e Sem barba, cabelos curtos/compridos/sem cabelo;
#### d: De pessoas de diferentes etnias.


## Resposta:

Questão 1: Foi feito o código [lab7_1.py](./lab7_1.py) para resolver a questão. Ela teve como imput a imagem:

<p align="center">
  <img src="images/oscar.jpg" width="500">
</p>

E ela resultou como imagens o seguinte, indo da menor para a maior respectivamente:

<p align="center">
  <img src="respostas_1/resultado_320x240.jpg">
  <img src="respostas_1/resultado_640x480.jpg" width="500">
  <img src="respostas_1/resultado_800x600.jpg" width="500">
  <img src="respostas_1/resultado_1280x720.jpg" width="500">
  <img src="respostas_1/resultado_1920x1080.jpg" width="500">
</p>

E essa é a tabela de execução:
<p align="center">
  <img src="tempo_1.png" width="500">
</p>

Questão 02:

Da questão 2, foi feito o código [lab7_2.py](./lab7_2.py) que gerava os seguintes resultados:

<p align="center">
  <img src="resposta_2/resultado_320x240_oscar.jpg">
  <img src="resposta_2/resultado_640x480_oscar.jpg" width="500">
  <img src="resposta_2/resultado_800x600_oscar.jpg" width="500">
  <img src="resposta_2/resultado_1280x720_oscar.jpg" width="500">
</p>

Com os seguintes tempos:
<p align="center">
  <img src="tempo_2.png" width="500">
</p>