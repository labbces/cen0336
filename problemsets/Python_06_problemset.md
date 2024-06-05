Python 6 - IO - Conjunto de Problemas
===================

1. Escreva um script para fazer o seguinte com [Python_06.txt](https://raw.githubusercontent.com/labbces/cen0336/master/files/Python_06.txt)
   - Abrir e ler o conteúdo.  
   - Converter para maiúsculas cada linha
   - Imprimir cada linha no STDOUT


2. Modifique o script do problema anterior para escrever o conteúdo em um novo arquivo chamado "Python_06_uc.txt"


3. Abra e imprima o complemento reverso de cada sequência em [Python_06.seq.txt](https://raw.githubusercontent.com/labbces/cen0336/master/files/Python_06.seq.txt). Cada linha está no seguinte formato:    `seqName\tsequence\n`. Certifique-se de imprimir a saída no formato fasta, incluindo o nome da sequência e uma observação na descrição de que este é o complemento reverso. Imprima no STDOUT e capture a saída em um arquivo com redirecionamento de linha de comando '>'. 
   - **Lembre-se de que é sempre uma boa ideia começar com um conjunto de teste para o qual você conhece a saída correta.**

4. Abra o arquivo [FASTQ](https://en.wikipedia.org/wiki/FASTQ_format) [Python_06.fastq](https://raw.githubusercontent.com/labbces/cen0336/master/files/Python_06.fastq) e percorra cada linha do arquivo. Conte o número de linhas e o número de caracteres por linha. Faça com que seu programa relate o:  
    - número total de linhas  
    - número total de caracteres  
    - comprimento médio da linha     

5. Escreva o seu primeiro parser FASTA. Este é um script que lê um arquivo FASTA e armazena cada registro FASTA separadamente para fácil acesso para análises futuras.

Coisas a serem lembradas:
   - abra seu arquivo
   - leia cada linha
   - sua linha é uma linha de cabeçalho? é uma linha de sequência?
   - um único registro FASTA tem uma linha de sequência ou várias linhas de sequência?
   
   DICAS: use I/O de arquivo, instruções if e dicionários para escrever o seu primeiro parser FASTA. Algumas outras funções e métodos úteis são find, split e concatenação de string.
   
   No final, seu script deve retornar o seguinte:
   
   fastaDict = {
      'seq1' : 'AAGAGCAGCTCGCGCTAATGTGATAGATGGCGGTAAAGTAAATGTCCTATGGGCCACCAATTATGGTGTATGAGTGAATCTCTGGTCCGAGATTCACTGAGTAACTGCTGTACACAGTAGTAACACGTGGAGATCCCATAAGCTTCACGTGTGGTCCAATAAAACACTCCGTTGGTCAAC' ,
      'seq2' : 'GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGATCTTAACCATGAGGCTGAGAAGCGATGTCCTGACCGGCCTGTCCTAACCGCCCTGACCTAACCGGCTTGACCTAACCGCCCTGACCTAACCAGGCTAACCTAACCAAACCGTGAAAAAAGGAATCT' ,
      'seq3' : 'ATGAAAGTTACATAAAGACTATTCGATGCATAAATAGTTCAGTTTTGAAAACTTACATTTTGTTAAAGTCAGGTACTTGTGTATAATATCAACTAAAT' ,
      'seq4' : 'ATGCTAACCAAAGTTTCAGTTCGGACGTGTCGATGAGCGACGCTCAAAAAGGAAACAACATGCCAAATAGAAACGATCAATTCGGCGATGGAAATCAGAACAACGATCAGTTTGGAAATCAAAATAGAAATAACGGGAACGATCAGTTTAATAACATGATGCAGAATAAAGGGAATAATCAATTTAATCCAGGTAATCAGAACAGAGGT' }




6. Você vai gerar algumas listas de genes que são salvos em arquivos, adicionar seus conteúdos a conjuntos e compará-los. 

__Gerar Listas de Genes:__


_Obter todos os genes:_

1. Acesse o [Ensembl Biomart](http://useast.ensembl.org/biomart/martview/4b8fb1941e75e7763e8c4ccf1ffcd9c5).
2. No menu suspenso, selecione "Ensembl Genes 98" (ou a versão mais atual)
3. No menu suspenso, selecione "Alpaca Genes" 
4. No lado esquerdo, clique em Atributos
5. Expanda GENE:
6. Desmarque "transcript stable ID".
7. Clique em Resultados (canto superior esquerdo)
8. Exporte todos os resultados para "Arquivo" "TSV" --> GO
9. Renomeie o arquivo para "alpaca_all_genes.tsv"

_Na mesma janela do Ensembl, siga os passos abaixo para obter genes que foram rotulados com o termo de Gene Ontology "proliferação de células-tronco". Para obter informações adicionais sobre a proliferação de células-tronco, verifique [proliferação de células-tronco](http://purl.obolibrary.org/obo/GO_0072089)_

10. Clique em "Filtros"
11. Em "Gene Ontology", marque "Nome do termo Go" e insira "proliferação de células-tronco"
12. Clique em Resultados (canto superior esquerdo)
13. Exporte todos os resultados para "Arquivo" "TSV" --> GO
14. Renomeie o arquivo para "alpaca_stemcellproliferation_genes.tsv"

_Na mesma janela do Ensembl, siga os passos abaixo para obter genes que foram rotulados com o termo de Gene Ontology "pigmentação". Para obter informações adicionais sobre pigmentação, verifique [pigmentação](http://purl.obolibrary.org/obo/GO_0043473)_


15. Clique em "Filtros"
16. Em "Gene Ontology", marque "Nome do termo Go" e insira "pigmentação"
17. Clique em Resultados (canto superior esquerdo)
18. Exporte todos os resultados para "Arquivo" "TSV" --> GO
19. Renomeie o arquivo para "alpaca_pigmentation_genes.tsv"


__Abra cada um dos três arquivos e adicione os IDs de gene a um conjunto. Um conjunto por arquivo.__

A. Encontre todos os genes que não são genes de proliferação celular.  
B. Encontre todos os genes que são genes de proliferação de células-tronco e genes de pigmentação.  
*Nota* Certifique-se de NÃO adicionar o cabeçalho ao conjunto.  

__Agora, vamos fazer isso novamente com fatores de transcrição.__
 
1. Volte para a janela do Ensembl Biomart
2. Desmarque o "Nome do Termo GO"
3. Selecione "Acesso ao Termo GO"
4. Insira esses dois IDs de acesso que, na maioria dos organismos, serão todos os fatores de transcrição
   - GO:0006355 é "regulação da transcrição dependente de DNA”. 
   - GO:0003677 é "ligação ao DNA"
5. Clique em Resultados (canto superior esquerdo)
6. Exporte todos os resultados para "Arquivo" "TSV" --> GO
7. Renomeie o arquivo para "alpaca_transcriptionFactors.tsv"

__Abra esses dois arquivos: 1) o arquivo de lista de genes de fatores de transcrição e 2) o arquivo de lista de genes de proliferação celular. Adicione cada um a um conjunto, Um conjunto por arquivo__

A. Encontre todos os genes que são fatores de transcrição para a proliferação celular


__Agora faça o mesmo na linha de comando com o comando `comm`. Talvez seja necessário `ordenar` cada arquivo primeiro.__


## Extra: Expandindo um exercício do Conjunto de Problemas 5 sobre composição de nucleotídeos
  - obtenha o arquivo bruto [Python_06.seq.txt](https://raw.githubusercontent.com/labbces/cen0336/master/files/Python_06.seq.txt)
  - em um script, abra este arquivo
  - itere sobre cada linha neste arquivo (seqName\tsequence\n)
     - para cada sequência:
         - calcule e armazene a contagem de cada caractere de nucleotídeo único em um dicionário
         - relate o nome, o total de cada contagem de nucleotídeos e o conteúdo de GC

