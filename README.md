# Relatorio-1---S202
Relatório 1

Crie uma classe chamada Animal com os seguintes atributos:
- nome (string)
- idade (inteiro)
- especie (string)
- cor (string)
- som (string)

A classe deve ter os seguintes métodos:
- emitir_som(): imprime o som do animal na tela
- mudar_cor(nova_cor): muda a cor do animal para a cor especificada

Agora, crie uma classe chamada Elefante que herda da classe Animal. A classe Elefante deve ter um atributo adicional chamado tamanho (string). Além disso, deve ter os seguintes métodos:
- trombar(): imprime o som do elefante na tela
- mudar_tamanho(novo_tamanho): muda o tamanho do elefante para o tamanho especificado 

Por fim, crie um programa que instancie um objeto da classe Elefante, peça ao usuário que digite o nome, idade, espécie, cor e tamanho do elefante. Em seguida, o programa deve imprimir o som do elefante na tela e mudar sua cor e tamanho com base em algumas condições:
- Se o elefante é da espécie "Africano" e tem idade menor que 10 anos, o tamanho deve ser mudado para "pequeno" e o som deve ser mudado para "Paaah"
- Se o elefante é da espécie "Africano" e tem idade maior ou igual a 10 anos, o tamanho deve ser mudado para "grande" e o som deve ser mudado para "PAHHHHHH"
- Se o elefante é de qualquer outra espécie, o tamanho e o som devem permanecer os mesmos. 

O programa deve, então, imprimir o novo som e o novo tamanho do elefante na tela.
