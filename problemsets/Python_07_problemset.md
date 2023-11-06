Python 7 - Expressões Regulares - Conjunto de Problemas
===================

1. No arquivo [Python_07_nobody.txt](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_07_nobody.txt), encontre todas as ocorrências de 'Nobody' e imprima a posição.

2. No arquivo [Python_07_nobody.txt](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_07_nobody.txt), substitua todas as ocorrências de 'Nobody' pelo seu nome favorito e escreva um arquivo de saída com o nome dessa pessoa (ex. Michael.txt).

3. Usando correspondência de padrões, encontre todas as linhas de cabeçalho em [Python_07.fasta](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_07.fasta). Observe que o formato de um cabeçalho em um arquivo FASTA é uma linha que começa com um símbolo maior que e é seguido por algum texto (por exemplo, `>seqName descrição`, onde seqName é o nome ou identificador da sequência. O identificador não pode ter espaços nele. A descrição que o segue pode ter espaços.)

4. Se uma linha corresponder ao formato de um cabeçalho FASTA, extraia o nome da sequência e a descrição usando subpadrões (grupos).
   - Imprima linhas parecidas com esta `id:"nome da sequência extraído" desc:"descrição extraída"`

5. Crie um analisador de FASTA ou modifique seu analisador de FASTA do conjunto de problemas anterior para usar expressões regulares. Certifique-se também de que seu analisador possa lidar com uma sequência que está dividida em várias linhas.

6. A enzima ApoI possui um local de restrição: R^AATTY onde R e Y são nucleotídeos degenerados. Consulte a tabela IUPAC para identificar as possibilidades de nucleotídeos para R e Y. Escreva uma expressão regular para encontrar e imprimir todas as ocorrências do local na seguinte sequência [Python_07_ApoI.fasta](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_07_ApoI.fasta).

```
>seq1
GAATTCAAGTTCTTGTGCGCACACAAATCCAATAAAAACTATTGTGCACACAGACGCGAC
TTCGCGGTCTCGCTTGTTCTTGTTGTATTCGTATTTTCATTTCTCGTTCTGTTTCTACTT
AACAATGTGGTGATAATATAAAAAATAAAGCAATTCAAAAGTGTATGACTTAATTAATGA
GCGATTTTTTTTTTGAAATCAAATTTTTGGAACATTTTTTTTAAATTCAAATTTTGGCGA
AAATTCAATATCGGTTCTACTATCCATAATATAATTCATCAGGAATACATCTTCAAAGGC
AAACGGTGACAACAAAATTCAGGCAATTCAGGCAAATACCGAATGACCAGCTTGGTTATC
AATTCTAGAATTTGTTTTTTGGTTTTTATTTATCATTGTAAATAAGACAAACATTTGTTC
CTAGTAAAGAATGTAACACCAGAAGTCACGTAAAATGGTGTCCCCATTGTTTAAACGGTT
GTTGGGACCAATGGAGTTCGTGGTAACAGTACATCTTTCCCCTTGAATTTGCCATTCAAA
ATTTGCGGTGGAATACCTAACAAATCCAGTGAATTTAAGAATTGCGATGGGTAATTGACA
TGAATTCCAAGGTCAAATGCTAAGAGATAGTTTAATTTATGTTTGAGACAATCAATTCCC
CAATTTTTCTAAGACTTCAATCAATCTCTTAGAATCCGCCTCTGGAGGTGCACTCAGCCG
CACGTCGGGCTCACCAAATATGTTGGGGTTGTCGGTGAACTCGAATAGAAATTATTGTCG
CCTCCATCTTCATGGCCGTGAAATCGGCTCGCTGACGGGCTTCTCGCGCTGGATTTTTTC
ACTATTTTTGAATACATCATTAACGCAATATATATATATATATATTTAT
```


7. Determine o(s) local(is) de corte físico(s) pelo ApoI na sequência acima. Imprima a sequência com "^" no local de corte.

   Dicas:  
   - Use `sub()`
   - Use subpadrões (parênteses e `group()`) para encontrar o local de corte dentro do padrão.
   - Exemplo: se o padrão for GACGT^CT a sequência a seguir

```
AAAAAAAAGACGTCTTTTTTTAAAAAAAAGACGTCTTTTTTT
```
   queremos exibir o local de corte assim:

```
AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT
```

8. Agora que você fez sua digestão de restrição, determine os comprimentos de seus fragmentos e os ordene por comprimento (na mesma ordem em que seriam separados em um gel de eletroforese).

   Dica: Converta esta string:

```
AAAAAAAAGACGT^CTTTTTTTAAAAAAAAGACGT^CTTTTTTT
```

   Para esta lista:

```
["AAAAAAAAGACGT","CTTTTTTTAAAAAAAAGACGT","CTTTTTTT"]
```

9. Baixe este arquivo: ftp://ftp.neb.com/pub/rebase/bionet.txt de enzimas e seus locais de corte para preencher um dicionário de enzimas associadas a seus padrões de reconhecimento. Pule as 10 primeiras linhas de cabeçalho e esteja ciente de como as colunas estão delimitadas. Você vai modificar este script na próxima pergunta.

10. Escreva um script que receba dois argumentos da linha de comando: o nome de uma enzima e um arquivo fasta com uma sequência a ser cortada. Carregue um dicionário de nomes de enzimas e locais de corte do código que você desenvolveu na pergunta 9.
    Se a enzima estiver presente no dicionário e puder cortar a sequência, imprima:
      - a sequência, anotada com os locais de corte
      - o número de fragmentos
      - os fragmentos em sua ordem natural (não ordenada)
      - os fragmentos em ordem ordenada (do maior para o menor)
