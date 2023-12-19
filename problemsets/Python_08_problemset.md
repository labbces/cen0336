### Python 8 - Estruturas de Dados - Conjunto de Problemas

__Não se esqueça de usar um conjunto de dados de teste pequeno ao testar seu código. Certifique-se de saber qual deve ser a resposta correta.__

1. Receba um arquivo multi-FASTA [Python_08.fasta](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_08.fasta) a partir da entrada do usuário e calcule a composição de nucleotídeos para cada sequência. Use uma estrutura de dados para contar. Imprima cada nome de sequência e sua composição no formato `seqNome\tA_contagem\tT_contagem\tG_contagem\C_contagem`

Aqui está a estrutura de uma estrutura de dados útil para armazenar essas informações
```
seqs[geneName][nucleotide]=count

seqs['geneA']['A'] = 2
seqs['geneA']['T'] = 3
seqs['geneA']['G'] = 3
seqs['geneA']['C'] = 1


seqs['geneB']['A'] = 1
seqs['geneB']['T'] = 5
seqs['geneB']['G'] = 2
seqs['geneB']['C'] = 2
``` 

2. Escreva um script que receba um arquivo multi-FASTA [Python_08.fasta](https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/Python_08.fasta) da entrada do usuário e divida cada sequência em códons (cada três nucleotídeos é um códon) apenas no primeiro quadro de leitura. Sua saída deve ser semelhante a isso:
```
seq1-frame-1-codons
CAT GCT TGA GTC
``` 
Escreva a saída para um arquivo chamado 'Python_08.codons-frame-1.nt'.

3. Agora, produza códons nos três primeiros quadros de leitura para cada sequência e imprima os IDs e registros de sequência para cada quadro e imprima em um arquivo chamado 'Python_08.codons-3frames.nt'

Por exemplo,
```
seq1-frame-1-codons
ATG TTG
seq-frame-2-codons
TGT TGA
``` 

4. Agora, obtenha o complemento reverso de cada sequência e imprima todos os seis quadros de leitura em um arquivo chamado 'Python_08.codons-6frames.nt'

5. Traduza cada um dos seis quadros de leitura em aminoácidos. Crie um arquivo para o qual você imprima os seis quadros de leitura (Python_08.codons-6frames.nt) e um arquivo para o qual você imprima a tradução dos seis quadros de leitura (Python_08.translated.aa). Use a seguinte tabela de tradução:

```python
tabela_de_traducao = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}
```

6. Encontre a sequência de peptídeo mais longa (M => Stop) de todos os seis quadros de leitura traduzidos para uma única sequência. Faça isso para todos os registros de sequência. Para cada sequência, imprima no formato FASTA os seis quadros de códons em um arquivo (Python_08.codons-6frames.nt), as traduções em um segundo arquivo (Python_08.translated.aa) e o peptídeo traduzido mais longo em um terceiro arquivo (Python_08.translated-longest.aa).

7. Finalmente, determine qual subconjunto de códons produziu o peptídeo mais longo para cada registro de sequência. Imprima isso em um quarto arquivo no formato FASTA (Python_08.orf-longest.nt).
