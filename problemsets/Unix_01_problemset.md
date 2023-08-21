# Revisão rápida das bases de Unix e conjunto de problemas

comandos úteis
=========================

| command         | description                              |
| --------------- | ---------------------------------------- |
| `ls`            | list directory contents                  |
| `cd`            | change directory                         |
| `mkdir`         | make a directory                         |
| `rm`            | remove, or delete files and directories. Use caution, it is easy to delete more that you want. |
| `head`          | prints the top few lines to the terminal window |
| `tail`          | prints the last few lines to the terminal window |
| `sort`          | sorts the lines                          |
| `uniq`          | prints the unique lines                  |
| `grep`          | filnds the lines that contain a pattern  |
| `wc`            | counts the number of lines, characters and words |
| `mv`            | move files                               |
| `cp`            | copy files                               |
| `date`          | returns the current date and time        |
| `pwd`           | return working directory name            |
| `ssh`           | remote login                             |
| `scp`           | remote secure copy                       |
| `~`             | shortcut for your home directory         |
| `man <command>` | manual page for the command e.g. `man ls` to get the man page for `ls` |





### Execute os seguintes comandos

**Os arquivos que você vai usar nesta revisão estão no nosso [repositório github](https://github.com/labbces/cen0336). Haverá instruções sobre como recuperá-los mas para diante**

Vamos num diretório com muitos arquivos e faza uma lista desses arquivos


```bash
cd /bin/
ls
```

__Qual é a diferença entre esses dois comandos?__

Teste executando os dois!!
```
ls -l
ls -lt
```


__Pipes__ 

Você pode encadear mais de um comando usando uma tubulação `|` , assim a saída padrão do primeiro comando é enviada por uma tubulação ('piped') na entrada padrão do segundo comando.

Teste!!
```
ls -lt | head
```



__Ponto e vírgula__

Você pode encadear mais de um comando usando um ponto e vírgula `;` depois de cada comando. Desta forma, os comando serão executados de forma sequencial, e a saída de um comando NÃO é passada para o próximo.

Teste!!
```
date ; sleep 2 ; date
```
> Se você tem interesse em conhecer mais do comando `sleep`, execute `man sleep`


__Descarregando arquivos__. 

Mude para seu diretório home. Nessa pasta, geralmente, você tem permissões para escrever. Agora use o comando `wget` ou `curl` para descarregar arquivos. Em alguns sistemas só tem um desses comandos disponiveis
```
cd ~
curl -O https://raw.githubusercontent.com/labbces/cen0336/master/files/cuffdiff.txt
```

__Redirecionando STDOUT__  

Você pode redirecionar a saída de um comando para um arquivo. 
```
cd ~
grep Chr7 cuffdiff.txt > fav_chr_cuffdiff.txt
```



__Acrescentar a STDOUT no final de um arquivo que já existe__

Você pode pegar a saída de um comando, que normalmente apareceria na tela, e enviar para um arquivo que já existe

```
grep Chr9 cuffdiff.txt >> fav_chr_cuffdiff.txt
```



__Redirecionar a STDERR__  

Você pode redirecionar a STDERR num arquivo.

Vamos lembrar o que a STDERR é na verdade.
```
cat blablabla.txt
```
> O arquivo blablabla.txt não existe, então na sua tela vai aparecer `cat: blablabla.txt: No such file or directory`. Esta mensagem é uma mensagem de erro, e assim será interpretada pelo sistema operacional. As mensagems de erro aparecerão num dispositivo de saída chamado STDERR, que normalmente é a tela do monitor. 

Podemos redirecionar a saída STDERR, para que ela não fique na tela mas num arquivo: 

```
cat blablabla.txt 2> errors.txt
```
> Podemos redirecionar as messagems de erro, A.K.A. STDERR, a um novo arquivo, nomeado segundo nossa escolha


O que acontece quando tenta redirecionar a STDOUT?
```
cat blablabla.txt > errors.txt
```
> `cat: blablabla.txt: No such file or directory` aparece ainda na tela, por que a gente só redirecionou a STDOUT num arquivo, não a STDERR. Neste caso especifico não temos nada impresso na STDOUT e nosso arquivo estará vazio. Como você pode conferir isso?



__Redirecionando STDOUT e STDERR__

Voce pode redireciona a duas saídas STDOUT e STDERR em **dois arquivos separados** usando só um comando.

```
# Primeiro vamos imprimir na tela do terminal
cat fav_chr_cuffdiff.txt blablabla.file

# Redirecionando em dois arquivos, STDOUT no arquivo out.txt, e STDERR no arquivo err.txt 
cat fav_chr_cuffdiff.txt blablabla.file 1> out.txt 2> err.txt

# O seguinte comando faz a mesma coisa, vê a diferença?
cat fav_chr_cuffdiff.txt blablabla.file > out.txt 2> err.txt

```
> Confera o conteúdo dos arquivos `out.txt` e `err.txt`

Você tembém pode redirecionar as duas saídas STDOUT e STDERR para **o mesmo** arquivo.
```
cat fav_chr_cuffdiff.txt blablabla.file &> all_out_err.txt 
```
> Verifique o que está no arquivo `all_out_err.txt`

Problemas
===========

1. Entre no servidor o na sua máquina com Linux. 

2. Qual é a rota completa (absoluta) de seu diretório home?

3. Desloquese um diretorio para cima
    - Quantos arquivos tem esse diretorio?
    - Quantos diretórios?

4. No seu diretório home crie uma pasta chamada `problemsets`.

5. Vai na pasta problemsets. Verifique que está no diretório certo usando o comando `pwd`.

6. Use o comando `wget` para descarregar uma copia do aquivo <https://raw.githubusercontent.com/labbces/cen0336/master/files/sequences.nt.fa> dentro do diretório problemsets. Se `wget` não está disponivel no sistema, pode usar `curl -O` como alternativa.

7. Sem usar um editor de texto use comandos de unix para achar as seguintes caracteristicas do arquivo `sequences.nt.fa`.
  É o mesmo arquivo descarregado no passo anterior <https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/sequences.nt.fa>
      - Quantas linhas tem o arquivo?   
      - Quantos caracteres?    (Dica: confera as opções do comando wc)
      - Qual é a primeira linha no arquivo?    (Dica: Leia a página de manual do comando head)
      - Quais são as últimas três linhas?    (Dica: Leia a página de manual do comando tail)
      - Quantas sequências em formato fasta tem o arquivo?    (Dica: use grep) (Nota: O inicio de cada sequência é indicado pelo caractere `>`.)    

8. Renomeie o arquivo `sequences.nt.fa` como `cancer_genes.fasta`. (Dica: Leia a página de manual do comando mv)

9. Descarrege o arquivo remoto, cuffdiff.txt, na sua pasta problemsets. Aquí está a URL para descarregar: <https://raw.githubusercontent.com/labbces/cen0336/master/files/cuffdiff.txt>

Use o comando `wget` para descarregar uma copia do aquivo <https://raw.githubusercontent.com/labbces/cen0336/master/files/cuffdiff.txt> entro do diretório problemsets. Se `wget` não está disponivel no sistema, pode usar `curl -O` como alternativa.

10. Faça o seguinte para o arquivo `cuffdiff.txt`. Una descrição do conteúdo de cada coluna aparece na tabela que está no final.
    - Observe as primeiras linhas do arquivo.
    - Classifique o arquivo pela coluna 'log2(fold_change)', do valor mais alto para o mais baixo, salve na sua pasta problemsets num novo aquivo chamad `sorted.cuffdiff.out`.
    - Classifique o arquivo pela coluna 'log2(fold_change)', do valor mais alto para o mais baixo, imprima só as primeiras 100 linhas, e salve num arquivo chamado `top100.sorted.cuffdiff.out`.
    - Classifique o arquivo pela coluna 'log2(fold_change)', do valor mais alto para o mais baixo, imprima só as primeiras 100 linhas, e imprima só a primeira coluna. Assim terá uma lista dos 100 principais genes com as maiores mudanças de expressão. Certifique-se que sua lista esteja classificada pelo nome do gene, e que os nomes sejam únicos (que apareçam só uma vez na lista). Salve esta lista selecionada (curada) num arquivo chamado `differentially.expressed.genes.txt`.



__Formato do arquivo Cuffdiff__

| Número da Coluna | Nome da coluna       | Exemplo              | Descrição                        |
| ------------- | ----------------- | -------------------- | ---------------------------------------- |
| 1             | Tested id         | XLOC_000001          | A unique identifier describing the transcipt, gene, primary transcript, or CDS being tested |
| 2             | Tested id         | XLOC_000001          | A unique identifier describing the transcipt, gene, primary transcript, or CDS being tested |
| 3             | gene              | Lypla1               | The gene_name(s) or gene_id(s) being tested |
| 4             | locus             | chr1:4797771-4835363 | Genomic coordinates for easy browsing to the genes or transcripts being tested. |
| 5             | sample 1          | Liver                | Label (or number if no labels provided) of the first sample being tested |
| 6             | sample 2          | Brain                | Label (or number if no labels provided) of the second sample being tested |
| 7             | Test status       | NOTEST               | Can be one of OK (test successful), NOTEST (not enough alignments for testing), LOWDATA (too complex or shallowly sequenced), HIDATA (too many fragments in locus), or FAIL,  when an ill-conditioned covariance matrix or other numerical exception prevents testing. |
| 8             | FPKMx             | 8.01089              | FPKM of the gene in sample x             |
| 9             | FPKMy             | 8.551545             | FPKM of the gene in sample y             |
| 10            | log2(FPKMy/FPKMx) | 0.06531              | The (base 2) log of the fold change y/x  |
| 11            | test stat         | 0.860902             | The value of the test statistic used to compute significance of the observed change in FPKM |
| 12            | p value           | 0.389292             | The uncorrected p-value of the test statistic |
| 13            | q value           | 0.985216             | The FDR-adjusted p-value of the test statistic |
| 14            | significant       | no                   | Can be either "yes" or "no", depending on whether p is greater then the FDR after Benjamini-Hochberg correction for multiple-testing |

