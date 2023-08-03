# Conjunto de problemas Unix 2


1. Se você ainda não o fez, siga [Steps 1-3 in Unix: GIT for Beginners](https://github.com/prog4biol/pfb2019#git-for-beginners). Aqui está um **sumário** destas etapas, **Por favor vá até a aula para ter o detalhamento**:
   NOTA: Não crie um repositório dentro de outro repositório.
   - Crie uma conta GitHub e clique em "Novo" para criar um novo repositório.
   - Adicione informação sobre seu repositório.
   - Por favor veja as notas de aula para passos mais detalhados. No sumário vocÊ fará o seguinte: Crie um diretório local (em sua máquina) com `mkdir <dirname>`, mova para um novo diretório com `cd <dirname>` e configure como um repositório com `git init`. Agora conecte-o em seu repositório remoto com `git remote add`.
   
   
   Não faça `git init` em seu diretório base. Faça um novo diretório (algo como pfb_problemsets ou problemsets ou problem_sets), mude o diretorio para o seu novo diretório, depois `git init` 

2. Mova quaisquer arquivos que você criou no conjunto de problemas Unix_01 para o seu repositório git de conjunto de problemas local.

3. Adicione todos os novos arquivos do seu repositório local para o seu repositório remoto
   - `git status` para ver todos os arquivos que você precisa adicionar 
   - `git add <filename>`  ou  `git add <filename1> <filename2> <filename3> ...`  
   - `git commit -m 'adding previous problem set files'`
   - `git push`
   - Visite o site do seu repositório Github (em github.com) e veja os arquivps do seu repositório local que você acabou de empurrar para o seu repositório remoto.

4. Se você está cansado de ficar digitando seu nome de usuário e senha github, crie e adicione um ssh key para sua conta github. Informação pode ser encontrada [Aqui](https://help.github.com/articles/connecting-to-github-with-ssh/) em github.com. Siga as intruções para esses dois passos no tutorial.
   - [Gerando uma nova SSH key e adicionando ao ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) 
   - [Adicionando uma nova SSH key a sua conta GitHub](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account)

5. Crie um diretório chamado `arquivos` no seu diretório de conjunto de problemas. 

6. Mova o arquivo que você renomeou de `sequences.nt.fa` para `cancer_genes.fasta` ao seu diretório `arquivos`

7. ADD/COMMIT/PUSH `cancer_genes.fasta` para seu repositório remoto
  - `git add files/cancer_genes.fasta`
  - `git commit -m 'adding cancer_genes.fasta'`
  - `git push`
  - Visite o site seu repositório GitHub (em github.com) e veja o arquivo do seu repositório local que você acabou de transferir para o seu repositório remoto.

8. Usando seu editor de texto vi crie um arquivo fasta e dê o nome `mysequences.txt`. Se assegure de que ele acabe em seu diretório de arquivos para conjuntos de problemas.

Esse é o formato do arquivo fasta:
```
>seqName description
ATGGCGTCTTGGCCTTAAAAGCTC
GGCGTCTTGGCCTTAAAAGCTCAT
ATTCTTGGCCTTAAATTGGCCTTG
```
  - Adicione 10 linhas de sequência 
  - Delete uma linha
  - Insira uma nova linha na linha 4
  - Copie a linha 5
  - Cole essa linha acima da linha 2
  - Configure para ver números de linha 
  - Corte a linha 3 e cole abaixo da linha 6
  - Vá até a linha 4
  - Delete a linha
  - Desfaça seu último delete
  - Pesquise por `CTT`
  - Encontre a próxima ocorrÊncia de `CTT`
  - Salve e saia


9. ADD/COMMIT/PUSH `mysequences.txt` em seu remoto.


10. Crie um diretório chamado `fastas`. (Dica: use mkdir)
11. Copie o arquivo fasta que você renomeou para `cancer_genes.fasta` ao diretório fasta.
12. Verifique que o arquivo está dentro do diretório fasta.  
13. Delete o arquivo original que você usou para copiar.  
14. Sincronize seu repositório remoto com o local. Se assegure de adicionar cada arquivo que você mudou ou usou `git add <filename>`. Não se esqueça do commit e push.
15. Pratique com `git rm`
  - Crie um arquivo chamado `oops` e adicione alguns caracteres de conteúdo.
  - Salve e saia. 
  - Add/Commit/Push esse arquivo
  - `git rm oops` 
  - `git commit -m 'removing oops'`
  - `git push`
16. Pratique com `rm`. Você pode identificar a pequena diferença do `git rm`
  - Crie um arquivo chamado `oops2`. adicione algum conteúdo. salve e saia
  - Add/Commit/Push esse arquivo
  - `rm oops2`
  - `git add oops2`
  - `git commit -m 'removing oops2'`
  - `git push`
17. Imagine isso: Você criou um arquivo, `git add`, mas percebeu que você não quer cometê-lo (commit). O que você faz? [da pesquisa do google](https://stackoverflow.com/questions/348170/how-do-i-undo-git-add-before-commit)
  - Crie um arquivo chamado `never`. 
  - `git add never`
  - `git reset never`
18. Leia a página para `rm` e `cp` para descobrir como remover e copiar um diretório.
19. Imprima seu histórico e redirecione ele ao arquivo chamado `unixBasics.history.txt`
20. Abra seu arquivo de histórico com seu editor de texto e delete quaisquer linhas que não queira manter. Veja isso [pesquisa no google](https://www.google.com/search?rlz=1C5CHFA_enUS596US596&q=vi+delete+entire+line&oq=vi+delete+entire+line&gs_l=psy-ab.3..0j0i5i30k1.28765.29854.0.30351.7.6.0.0.0.0.186.526.0j3.3.0....0...1.1.64.psy-ab..5.2.362...0i13k1j0i7i5i30k1.0.Ub2zfH_lp_o) para informações sobre deletar linhas inteiras no vi.
21. Se assegure de que todos os seus arquivos estão sincronizados com seu repositório remoto. (`git status`)
