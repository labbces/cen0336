Python 4 Problem Set -- Listas e Loops
===================

1. Para as próximas tarefas sobre listas, utilize o interpretador:
	
    1  Crie uma lista com 5 coisas que você gosta.
   	2.  Utilize a função `print()` para imprimir sua lista.
   	3.  Utilize a função `print()` para imprimir o elemento do meio.
   	4.  Agora, substitua o elemento do meio por outro item, como sua música favorita ou um pássaro cantor.
   	5.  Utilize a mesma instrução de impressão de b. para imprimir sua nova lista. Verifique as diferenças.
   	6.  Adicione um novo elemento no final. [Leia sobre append()](https://www.tutorialspoint.com/python/list_append.htm).  
	g.  Adicione um novo elemento no começo. [Leia sobre insert()](https://www.tutorialspoint.com/python/list_insert.htm).  
	h.  Adicione um novo elemento em algum lugar que não seja no início ou no final.
        i.  Remova um elemento do final. [Leia sobre pop()](https://www.tutorialspoint.com/python/list_pop.htm).  
        j.  Remova um elemento do começo.  
	k.  Remova um elemento de algum lugar que não seja no início ou no final. 
	l.  Use join para criar uma string. Junte os elementos com ', '. 
	
3. Escreva um script que divida uma string em uma lista. No seu script:
	- Salve a string `sapiens, erectus, neanderthalensis` como uma variável chamada `taxa`.
	- Print `taxa`.
	- Print `taxa[1]`, o que você obtém?
	- Print `type(taxa)`. Qual é o tipo?
	- Divida `taxa` em palavras individuais e print o resultado da divisão. (Pense em ', '.)
	- Armazene o resultado do `split` em uma nova variável chamada `species`.
	- Print `species`.
	- Print the `species[1]`, o que você obtém?
	- Print `type(species)`. Qual é o tipo?
	- Ordene a lista em ordem alfabética e print (dica: pesquise a função `sorted()`). 
	- Ordene a lista pelo comprimento de cada string e print. (A string mais curta deve vir primeiro). [Confira a documentação do argumento key](https://www.programiz.com/python-programming/methods/built-in/sorted).

4. Usando o interpretador Python, investigue a diferença entre essas duas maneiras de copiar uma lista. Cuidado! Uma delas pode NÃO ser o que você espera. 
   - Método 1:
     - Crie uma lista. Exemplo: `my_list = ['a', 'bb', 'ccc']`
     - Faça uma cópia usando o operador de atribuição `=`:  `list_copy = my_list`
     - Print a lista original `print(my_list)`
     - Altere a `list_copy` adicionando um novo elemento usando `append()`
     - print a lista original novamente `print(my_list)`
   - Método 2:  
     - Crie uma lista. Exemplo: `my_list2 = ['a', 'bb', 'ccc']`  
     - Faça uma cópia com o método `copy()`: `list_copy2 = my_list2.copy()`  
     - Print a lista original `print(my_list2)`
     - Altere a `list_copy2` adicionando um novo elemento usando `append()`   
     - print a lista original novamente `print(my_list2)`   

5. Escreva um script que use um loop `while` para imprimir os números de 1 a 100.

6. Escreva um script que use um loop while para calcular o [fatorial](https://en.wikipedia.org/wiki/Factorial) de 1000. 

7. Itere por cada elemento desta lista usando um loop `for`: [101,2,15,22,95,33,2,27,72,15,52]
	- print apenas os valores que são pares (dica: use o operador módulo).   
8. Ordene os elementos da lista acima e, em seguida, itere por cada elemento usando um loop `for` e:
   - print cada elemento.
   - Calcule duas somas acumulativas, uma de todos os valores pares e outra de todos os valores ímpares.
   - print apenas as duas somas finais. A saída do seu script deve ser:
   
   ```
   Soma dos números pares: 150 
   Soma dos números ímpares: 286
   ```
   
9. Escreva um script que use `range()` em um loop `for` para imprimir todos os números de 0 a 99. 
      - Modifique seu loop para imprimir todos os números de 1 a 100.
      
10. Crie um novo script que use a compreensão de lista para fazer o mesmo que o problema 8. (Use `range()` para imprimir todos os números de 1 a 100.)

11. Escreva um novo script que receba os valores de início e fim pela linha de comando. Se você chamar seu script assim `count.py 3 10`, ele imprimirá os números de 3 a 10.
      - Modifique seu script para imprimir apenas o número se ele for ímpar.
      
12. Escreva um novo script para criar uma lista com os seguintes dados `['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']`. Use um loop `for` para iterar por cada elemento desta lista e:
   - Print cada elemento.
   - Print o comprimento e a sequência, separados por uma guia. A saída deve se parecer com:
   
   ```
   14	ATGCCCGGCCCGGC
   25	GCGTGCTAGCAATACGATAAACCGG
   12	ATATATATCGAT
   8	ATGGGCCC
   ```
   
12. Use a compreensão de lista para gerar uma lista de tuplas. As tuplas devem conter sequências e comprimentos do problema anterior. Print o comprimento e a sequência (ou seja, "4\tATGC\n"). Uma lista de tuplas se parece com isso [(4,'ATGC'),(2,'GC')].

13. Modifique o script do #11 para que você também imprima o número (posição na lista) de cada sequência (ou seja, "1\t4\tACGT\n").

14. Você tem commitado seu trabalho?

## Problemas desafiadores e divertidos! Estes são scripts reais que você pode usar na vida real. Você já aprendeu tudo o que precisa para fazer cada um deles. Se você não tiver tempo suficiente nesta sessão para completar, volte e tente mais tarde.

1. Criar uma sequência embaralhada ([Fisher-Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle))
    - Use um loop `for` para realizar o seguinte procedimento N vezes (N = comprimento da sequência)
    - Selecione uma posição aleatória A com `randrange()`
    - Selecione uma posição aleatória B com `randrange()`
    - Troque as letras nos índices da lista A e B
    - Print a sequência final embaralhada
    - Lembre-se de testar seu código com dados de teste.

2. Calcular identidade de sequência: Comece com 2 sequências de DNA muito semelhantes. Use as suas favoritas ou use [Python_04.fasta](https://raw.githubusercontent.com/labbces/cen0336/master/files/Python_04.fasta)
    - Alinhe com ClustalW, TCoffee, ou alguma outra aplicação web de alinhamento.
    - A saída deve estar no formato FASTA.
    - Armazene (copie e cole) cada sequência alinhada, incluindo traços, como duas variáveis de string separadas.
    - Remova as quebras de linha (se houver). Caracteres de nova linha não fazem parte da sequência!
    - Use um loop `for` com `range()` para comparar cada índice para diferenças de nucleotídeos.
    - Relate a identidade percentual das duas sequências.

3. Um novo script de Fragmentos de Restrição:
   - Encontre [EcoRI](https://www.neb.com/products/r0101-ecori#Product%20Information) nesta sequência de DNA
```
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC
```
   - substitua o sítio EcoRI 'GAATTC' por 'G^AATTC'
   - divida a nova sequência formatada nos locais de corte, armazene os fragmentos resultantes em uma lista
   - itere sobre cada fragmento e relate
	- a posição de início na sequência original
	- a posição final na sequência original
	- o comprimento de cada fragmento
   - ordene os fragmentos por comprimento e imprima como apareceriam em um gel de agarose. (do maior para o menor)
