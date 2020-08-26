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

Você pode redirecionar a STDERR num arqiovo.

Vamos lembrar o que a STDERR é na verdaade.
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
> Examine the contents of `out.txt` and `err.txt`

You can also redirect both STDOUT and STDERR to **the same** file.
```
cat fav_chr_cuffdiff.txt blablabla.file &> all_out_err.txt 
```
> Check out what is in the `all_out_err.txt`

Problem Set
===========

1. Log into your machine. 

2. What is the full path to your home directory?

3. Go up one directory?
    - How many files does it contain?
    - How many directories?

4. Make a directory called `problemsets` in your home directory.

5. Navigate into this new directory called problemsets. Verify that you are in the correct directory by using `pwd`.

6. Use `wget` to copy <https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/sequences.nt.fa> from the web into your problemsets directory. If `wget` is not available on your system, use `curl -O` as an alternative.

7. Without using a text editor use unix commands to find these qualities for the file `sequences.nt.fa`.
  This file can be found here <https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/sequences.nt.fa>
      - How many lines does this file contain?   
      - How many characters?    (Hint: check out the options of wc)
      - What is the first line of this file?    (Hint: read the man page of head)
      - What are the last 3 lines?    (Hint: read the man page of tail)
      - How many sequences are in the file?    (Hint: use grep) (Note: The start of a sequence is indicated by a `>` character.)    

8. Rename `sequences.nt.fa` to `cancer_genes.fasta`. (Hint: read the man page for mv)

9. Copy this remote file, cuffdiff.txt, to your problemset directory. Here is the url you can use: <https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/cuffdiff.txt>

Use `wget` to copy <https://raw.githubusercontent.com/prog4biol/pfb2019/master/files/cuffdiff.txt> from the web into your problemsets directory. If `wget` is not available on your system, use `curl -O` as an alternative.




10. Do the following to `cuffdiff.txt`. The descriptions of each column in the file are in the table below.
    - Look at the first few lines of the file
    - Sort the file by log fold change 'log2(fold_change)', from highest to lowest, and save in a new file in your directory called sorted.cuffdiff.out
    - Sort the file (log fold change highest to lowest) then print out only the first 100 lines. Save in a file called `top100.sorted.cuffdiff.out`.
    - Sort the file by log fold change, print out the top 100, print only first column. This will be a list of the top 100 genes with the largest change in expression. Make sure your list is sorted by gene name and is unique. Save this curated list in a file called `differentially.expressed.genes.txt`.



__Cuffdiff file format__

| Column number | Column name       | Example              | Description                              |
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

