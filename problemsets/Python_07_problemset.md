Python 7 - Expressões Regulares - Conjunto de Problemas
===================

1. No arquivo [Python_07_nobody.txt](https://raw.githubusercontent.com/labbces/cen0336/master/files/Python_07_nobody.txt), encontre todas as ocorrências de 'Nobody' e imprima a posição.

2. No arquivo [Python_07_nobody.txt](https://raw.githubusercontent.com/labbces/cen0336/master/files/Python_07_nobody.txt), substitua todas as ocorrências de 'Nobody' pelo seu nome favorito e escreva um arquivo de saída com o nome dessa pessoa (ex. Michael.txt).

3. Usando correspondência de padrões, encontre todas as linhas de cabeçalho em [Python_07.fasta](https://raw.githubusercontent.com/labbces/cen0336/master/files/Python_07.fasta). Observe que o formato de um cabeçalho em um arquivo FASTA é uma linha que começa com um símbolo maior que é seguido por algum texto (por exemplo, `>seqName descrição`, onde seqName é o nome ou identificador da sequência. O identificador não pode ter espaços nele. A descrição que o segue pode ter espaços.)

4. Se uma linha corresponder ao formato de um cabeçalho FASTA, extraia o nome da sequência e a descrição usando subpadrões (grupos).
   - Imprima linhas parecidas com esta `id:"nome da sequência extraído" desc:"descrição extraída"`

5. Crie um analisador de FASTA ou modifique seu analisador de FASTA do conjunto de problemas anterior para usar expressões regulares. Certifique-se também de que seu analisador possa lidar com uma sequência que está dividida em várias linhas.

6. A enzima ApoI possui um local de restrição: R^AATTY onde R e Y são nucleotídeos degenerados. Consulte a tabela IUPAC para identificar as possibilidades de nucleotídeos para R e Y. Escreva uma expressão regular para encontrar e imprimir todas as ocorrências do local na seguinte sequência [Python_07_ApoI.fasta](https://raw.githubusercontent.com/labbces/cen0336/master/files/Python_07_ApoI.fasta).

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

11. Escreva um programa em Python para validar identificadores no formato EXP2026_B03_P12, composto pelo prefixo EXP, um ano com quatro dígitos, _B, um bloco com dois dígitos, _P e uma parcela com dois dígitos. Não aceite espaços ou caracteres adicionais.

A entrada de dados é a lista:

```python
identificadores = [
    "EXP2026_B03_P12", "EXP2026_B3_P12", "EXP2026_B03_P2", "exp2026_B03_P12", "EXP2026_B03_P12_extra"
]
```

A saida esperada é a seguinte:

```
EXP2026_B03_P12       -> Válido
EXP2026_B3_P12        -> Inválido
EXP2026_B03_P2        -> Inválido
exp2026_B03_P12       -> Inválido
EXP2026_B03_P12_extra -> Inválido
```

12. Escreva um programa em Python que extraia o identificador de cada amostra e seu valor de pH do [texto](../files/pH.txt) fornecido. Os identificadores são formados por `S` seguido de dois dígitos. Aceite valores inteiros ou com uma parte decimal separada por vírgula ou ponto. Preserve a representação original dos valores e ignore os registros sem resultado numérico.

A saida esperada é a seguinte:

```python
[('S01', '5,8'), ('S02', '6.2'), ('S03', '7')]
```

13. Escreva um programa em Python que leia, linha por linha, o arquivo [parcelas_npk_1000.txt](../files/parcelas_npk_1000.txt). Cada linha representa uma parcela fictícia e contém suas coordenadas geográficas, uma formulação NPK e a cultura plantada. Os nomes das culturas apresentam variações de escrita, e algumas formulações têm formato inválido. O programa deve reconhecer e padronizar os nomes das culturas com expressões regulares, selecionar apenas as formulações NPK válidas e contar quantas parcelas utilizam cada formulação em cada cultura.

O arquivo possui exatamente 1.000 linhas de dados, sem cabeçalho, codificadas em UTF-8. Cada linha contém três colunas separadas por tabulação `(\t)`.

| Coluna | Conteúdo | Exemplo |
| --- | --- | --- |
| 1 | Coordenadas na ordem latitude,longitude, em graus decimais | -22.700000,-47.600000 | 
| 2 | Formulação NPK, cuja validade deve ser verificada | 04-14-08 | 
| 3 | Nome da cultura, com possíveis variações de escrita | cana-de-açúcar | 

A vírgula separa latitude e longitude dentro da primeira coluna; o ponto é o separador decimal. As coordenadas devem ser lidas como uma única coluna. As colunas estão separadas por tabulação. Os nomes de algumas culturas contêm espaços.

Os nomes das culturas tem qeu ser padronizados, para ficar: soja, cana e milho. As expressões regulares devem ignorar diferenças entre maiúsculas e minúsculas. Aceite também espaços repetidos entre palavras e remova espaços nas extremidades de cada campo antes da verificação. A palavra açúcar pode aparecer com ou sem acentos. 

A seguinte tabela mostra as formas de nomes de cultura aceitas.

| Categoria padronizada | Formas aceitas |
|---|---|
| `soja` | `soja`, `soja comum` e `Glycine max` |
| `cana` | `cana`, `cana de açúcar`, `cana-de-açúcar`, `cana de acucar` e `cana-de-acucar` |
| `milho` | `milho`, `milho comum` e `Zea mays` |

Uma formulação NPK é válida neste exercício se, após a remoção de espaços nas extremidades, contiver exatamente três grupos de dois dígitos de 0 a 9, separados por hífens.

Formato da tabela de saída esperada:

| Formulação NPK | Soja | Cana | Milho | Total |
| 04-14-08 | 2| 0 | 0 | 2 |
| 20-05-20 | 0| 1 | 1 | 2 |
| Total válido | 2 | 1 | 1 | 4 |

14. Escreva um programa em Python que leia o arquivo [umidade_solo.txt](../files/umidade_solo.txt) linha por linha. Use expressões regulares para verificar o formato dos registros e extrair os dados. Utilize estruturas condicionais if, elif e else para tratar registros inválidos e classificar os valores válidos.

Conteúdo do arquivo umidade_solo.txt:

```
# data;talhao;umidade
2026-10-01;T01;umidade=18,5%
2026-10-01;T02;umidade=27.0%

2026-10-01;T03;umidade=38%
2026-10-01;T04;umidade=110%
2026-10-01;T05;umidade=sem_dado
2026-10-01;T6;umidade=24%
2026-10-01;T07;umidade=20%
2026-10-01;T08;umidade=35%
```
Requisitos:

- Abra o arquivo em modo de leitura com codificação UTF-8 e percorra-o com um laço for, sem utilizar read() ou readlines(). Mantenha o número original de cada linha.
- Ignore linhas vazias e linhas cujo primeiro caractere, após remover espaços das extremidades, seja #.
- Utilize uma expressão regular para verificar a linha inteira e extrair três campos: data no formato AAAA-MM-DD, talhão formado por T seguido de exatamente dois dígitos e umidade indicada por umidade=, um número e %. Aceite números inteiros ou decimais com vírgula ou ponto. Não aceite espaços internos nem texto adicional.
- Se a linha não corresponder ao formato, exiba seu número e a mensagem ERRO: formato inválido. Continue processando as demais linhas.
- Se o formato estiver correto, converta a umidade para float, substituindo a vírgula decimal por ponto quando necessário. Valores acima de 100 devem gerar a mensagem ERRO: umidade fora do intervalo de 0 a 100% e não devem ser classificados. Para este exercício, o formato numérico não aceita sinais; números negativos são, portanto, erros de formato.
- Para valores válidos entre 0 e 100, utilize if, elif e else para atribuir uma das seguintes categorias:
   - Menor que 20: ABAIXO_DA_FAIXA.
   - De 20 a 35, incluindo ambos os limites: DENTRO_DA_FAIXA.
   - Maior que 35: ACIMA_DA_FAIXA.
- Exiba o número da linha, a data, o talhão, a umidade com uma casa decimal e a categoria. Ao final, informe quantos registros foram válidos, quantos foram inválidos e quantos pertencem a cada categoria. Não conte comentários ou linhas vazias como registros.

Saída esperada:

```
Linha 2 | 2026-10-01 | T01 | 18.5% | ABAIXO_DA_FAIXA
Linha 3 | 2026-10-01 | T02 | 27.0% | DENTRO_DA_FAIXA
Linha 5 | 2026-10-01 | T03 | 38.0% | ACIMA_DA_FAIXA
Linha 6 | ERRO: umidade fora do intervalo de 0 a 100%
Linha 7 | ERRO: formato inválido
Linha 8 | ERRO: formato inválido
Linha 9 | 2026-10-01 | T07 | 20.0% | DENTRO_DA_FAIXA
Linha 10 | 2026-10-01 | T08 | 35.0% | DENTRO_DA_FAIXA

Registros válidos: 5
Registros inválidos: 3
Abaixo da faixa: 1
Dentro da faixa: 3
Acima da faixa: 1
```
