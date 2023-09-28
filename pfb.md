# Introdução a programação de computadores aplicada a ciências biológicas - CEN0336 
Tradução e modificação do material associado a [programmingforbiology.org](http://programmingforbiology.org), associado a disciplina ["CEN0336 - Introdução a Programação de Computadores Aplicada a Ciências Biológicas"](https://uspdigital.usp.br/jupiterweb/obterDisciplina?sgldis=CEN0336&codcur=11061&codhab=4)

__Criador e Instrutor da versão em Português__
Diego M. Riaño-Pachón


__Criadores do material na versão em Inglês__
Simon Prochnik
Sofia Robb

# Aulas de Python


## Python 1


### Visão geral de Python

Python é uma linguagem de script. Ela é útil para desenvolvimento de projetos científicos de médio porte. Quando você executa um script de Python, o interpretador da linguagem irá gerar um código em bytes e interpretá-lo. Esse processo acontece automaticamente, você não precisa se preocupar com isso. Linguagens compiladas como C e C++ vão rodar muito mais rapidamente, mas são também muito mais complicadas de programar. Programas usando linguagens como Java (que também são compiladas) são adequados para projetos grandes com programação colaborativa, mas não são executados tão rapidamente como C e são mais complexos de escrever que Python.

Python tem

- tipos de dados
- funções
- objetos
- classes
- métodos

**Tipos de dados** correspondem aos diferentes tipos de dados que serão discutidos em mais detalhes posteriormente. Exemplos de tipos de dados incluem números inteiros e cadeias de caracteres (texto). Eles podem ser armazenados em variáveis.

**Funções** fazem algo com dados, como cálculos. Algumas funções estão disponíveis de forma nativa em Python. Você pode também criar suas próprias funções.

**Objetos** correspondem a maneiras de agrupar conjuntos de dados e funções (métodos) que agem nestes dados.

**Classes** correspondem a uma maneira de encapsular (organizar) variáveis e funções. Objetos usam variáveis e métodos da classe às quais pertencem. 

**Métodos** são funções que pertencem a uma classe. Objetos que pertencem a uma classe podem usar métodos daquela classe.

### Rodando Python

Há duas versões de Python: Python 2 e Python 3. Nós usaremos Python 3. Esta versão conserta problemas de Python 2 e é incompatível em alguns aspectos com Python 2. Muitos códigos já foram desenvolvidos em Python 2 (é uma versão mais antiga), mas muitos códigos já foram e estão sendo desenvolvidos em Python 3.

#### Interpretador interativo

Python pode ser executado em uma linha por vez em um interpretador interativo. É como se usasse a linha de comando de Shell (que estudamos nas duas primeiras aulas/ capítulos), mas agora com a linguagem Python. Para executar o interpretador, execute o seguinte código no seu terminal:  

`$ python3`

Nota: '$' indica o prompt de comando. Lembre-se do Unix 1 que cada computador tem seu próprio prompt!

Primeiros comandos em Python:

```python
>>> print("Olá, turma 2022!")
Olá, turma 2022!
```

> Nota: `print` é uma função. Nomes de funções precedem (); assim, de maneira formal a função é `print()`


#### Scripts em Python são arquivos de texto

* O mesmo código acima é digitado em um arquivo usando um editor de texto.
* Scripts em Python são sempre salvos em arquivos cujos nomes têm a extensão '.py' (o nome do arquivo termina com '.py').
* Poderíamos executar o código `ola.py`

Conteúdos do arquivo:

```python
print("Olá, turma 2022!")
```

#### Rodando scripts em Python

Digitar o comando `python3` seguido do nome do script faz com que Python execute o código. Lembre-se que nós vimos que podemos também executar o código de forma interativa executando apenas `python3` (ou `python`) na linha de comando.

Execute o script desta forma (% representa o prompt):

```bash
% python3 ola.py 
```

Este procedimento gera o seguinte resultado no terminal:

```bash
print("Olá, turma 2022!")
```

#### Uma forma mais rápida/melhor de rodar scripts em Python

Se você tornar script em um executável, você pode executá-lo sem precisar digitar `python3` antes. Use o comando `chmod` para alterar as permissões do script desta forma:

`chmod +x ola.py`

Você pode verificar as permissões assim:

```
% ls -l ola.py 
-rwxr-xr-x  1 sprochnik  staff  60 Oct 16 14:29 ola.py
```

Os primiros 10 caracteres que ver na tela possuem significados especiais. O primeiro (`-`) diz a você qual tipo de arquivo `ola.py` é. `-` significa um arquivo normal, 'd' um diretório, '1' um link. Os próximos nove caracteres aparecem em três sets de três. O primeiro set se refere às suas permissões, o segundo as permissões do grupo, e o último de quaisquer outros. Cada set de trÊs caracteres mostra em ordem 'rwx' para leitura, escrita, execução. Se alguém não tem uma permissão, um `-` é mostrado ao invés de uma letra. Os três caracteres 'x' significam que qualquer um pode executar ou rodar o script.  

Nós também precisamos adicionar uma linha no começo do script que pede para o python3 interpretar o script. Essa linha começa com `#`, então aparece como um comentário para o python. O '!' é importante como o espaço entre `env` e `python3`. O programa `/usr/bin/env` procura por onde `python3` está instalado e roda o script com `python3`. Os detalhes podem parecer um pouco complexos, mas você pode apenas copiar e colar essa linha 'mágica'.

Esse arquivo ola.py agora se parece com isso

```python
#!/usr/bin/env python3
print("Olá, turma 2022!")
```

Agora você pode simplesmente digitar o símbolo para o diretório atual `.` seguido por um `/` e o nome do script para rodá-lo. Como isso: 

```
% ./ola.py
Olá, turma 2022!
```



### Sintaxe


#### Nomes de variável em Python

Um nome de variável em Python é o nome usado para identificar uma variável, função, classe, módulo ou outro objeto. Um nome de variável inicia com uma letra, de `A` a `Z` ou de `a` a `z`, ou então com um travessão (`_`), seguido de zero ou mais letras, travessões e dígitos (`0` a `9`).

Python não permite caracteres como `@`, `$` e `%` dentro do nome de variável. Python é uma linguagem "sensível a minúsculas e maiúsculas" (muitas vezes referido com o anglicismo "case sentitive"). Portanto, `seq_id` e `seq_ID` são dois nomes diferentes de variável em Python.

#### Convenções para nomeação de nomes de variável em Python

 * A primeira letra deve ser minúscula, exceto em nomes de classes. Classes devem começar com letra maiúscula (p.e. `Seq`).
 * Private variable names begin with an underscore (ex. `_private`).
 * Strong private variable names begin with two underscores (ex. `__private`).
 * Nomes especiais de variável definidas pela linguagem começam e terminam com dois travessões (p.e. `__special__`).


Selecionar bons nomes de variável para objetos que você nomeia é muito importante. Não chame suas variáveis de `item` ou `minha_lista` ou `dados` ou `var`, exceto em casos que você esteja trabalhando com trechos de códigos muito simples (a título de testes) ou fazendo algum gráfico. Não dê `x` ou `y` como nome de variáveis. Todos estes nomes não são descritivos para o tipo de informação encontrado naquela variável ou objeto.

Uma escolha ainda pior é dar nomes de variáveis que contêm nomes de genes como `sequencias`. Por que é uma ideia ruim? Pense no que poderia acontecer se você encher seu carro de combustível em um comércio chamado "posto de gasolina" que vendesse limonada em vez de gasolina ou etanol combustível.

Em Ciência da Computação, os nomes devem sempre descrever de forma acurada os objetos aos quais estejam vinculados. Isso reduz a possibilidade de `bugs` no seu código, torna muito mais fácil o seu entendimento se você volta ao seis meses depois ou por pessoas com as quais compartilha seu código. Embora pensar em bons nomes para variáveis tome um pouco mais de tempo e esforço, isso prenive problemas no futuro!

#### Palavras reservadas

A lista a seguir compreende as palavras reservadas de Python. Elas são palavras especiais que já têm um propósito em Python e, portanto, não podem ser usadas como nomes de variáveis.

```
and         exec        not
as          finally     or
assert      for         pass
break       from        print
class       global      raise
continue    if          return
def         import      try
del         in          while
elif        is          with
else        lambda      yield
except      list        hash
```

#### Linhas e indentação

Python considera como um bloco de código linhas adjacentes que apresentam o mesmo nível de indentação. Isso mantém organizadas as linhas de código que são executadas de forma conjunta. Espaçamento e/ou indentação incorretos irão causar erros ou podem fazer que seu código seja executado de uma forma que você não espera. Ambientes de Desenvolvimento Interativo (IDEs) e editores de texto podem ajudar a indentar códigos corretamente.

O número de espaços na indentação precisa ser consistente, mas este número não é específico. Todas as linhas de código ou sentenças dentro de um bloco precisa ser identado com o mesmo número. Por exemplo, usando quatro espaços:


```python
#!/usr/bin/env python3
mensagem = '' # cria uma variável vazia
for x in (1,2,3,4,5):
    if x > 4:
        print("Olá")
        mensagem = 'x é grande'
    else:
        print(x)
        mensagem = 'x é pequeno'
    print(mensagem)
print('Pronto!')
```


#### Comentários

Incluir comentários no seu código é uma prática essencial. Anotar o que uma linha ou bloco de código faz ajudará o programador e os leitores do código. Incluindo você!

Comentários iniciam com o símbolo `#`. Todos os caracteres depois deste símbolo, até o final da linha, são parte do comentário e serão ignorados pelo interpretador de Python.

A primeira linha de um script começa com `#!`, um exemplo especial de comentário que tem a função especial no Unix de informar ao Shell como executar o script.

```python
#!/usr/bin/env python3

# este é meu primeiro código
print("Olá, turma 2022!") # esta linha imprema o conteúdo na tela
```


#### Linhas em branco

Linhas em branco são importantes para aumentar a legibilidade do código. Você deve separar com uma linha em branco trechos de código que vão juntos, organizando em "parágrafos" de código. Linhas em branco são ignoradas pelo interpretador de Python.


### Tipos de dados e variáveis

Esta é a sua primeira oportunidade de olhar para variáveis e tipos de dados. Cada tipo será discutido em mais detalhes nas seções subsequentes.

O primeiro conceito a ser considerado é que os tipos de dados de Python podem ser ou não mutáveis. Números literais, strings e tuplas não podem ser alterados. Listas, dicionários e sets podem. Da mesma forma, variáveis individuais também podem ser alteradas. Você pode armazenar dados na memória por meio da atribução de variáveis, o que pode ser feito usando o sinal "=".

#### Números e Strings

Números e strings são dois tipos comuns de dados. Números literais e strings como `5` ou `meu nome é` são imutáveis. No entanto, seus valores podem ser armazenados em variáveis, as quais podem ser alteradas.

Por exemplo:

```python
contagem_genes = 5
# alterando o valor de contagem_genes
contagem_genes = 10
```
>Lembre-se que da seção anterior sobre nomes de variáveis e objetos (e variáveis são objetos em Python).

Diferentes tipos de dados podem ser atribuídos a variáveis, como inteiros (`1`,`2`,`3`), números de ponto flutuante (`3.1415`) e strings (`"texto"`).

Por exemplo:

```python
contagem   = 10    # este é um inteiro
média = 2.531      # este é um número de ponto flutuante
mensagem = "Bem-vindo ao interpretador de Python" # isso é uma string
```

`10`, `2.531`, e `"Bem-vindo ao interpretador de Python"` são peças de dados singulares (escalares) e cada um é armazenado em sua própria variável.

Coleções de dados podem também ser armazenados em tipos de dados especiais, i.e., tuplas, listas, sets, e dicionários. Você deveria sempre tentar armazenar semelhantes com semelhantes, de forma tal que cada elemento da coleção deveria ser do mesmo tipo de dado, como um valor de expressão de RNA-seq ou uma contagem de quantos exons estão em um gene ou uma sequência de leitura. Para o quê você imagina que isso deve ser?

#### Listas

- Listas são usadas para armazenar coleções de dados ordenados (indexados).
- Listas são mutáveis: o número de elementos em uma lista e o que é armazenado em cada elemento podem ser alterados.
- Listas são delimitadas por colchetes e seus itens separados por vírgula.


```python
[ 'atg' , 'aaa' , 'agg' ]
```

| Índice | Valor |
| ----- | ----- |
| 0     | atg   |
| 1     | aaa   |
| 2     | agg   |

> A indexação de listas começa em 0

#### Tuplas

- Tuplas são similares a listas e contêm coleçaões de dados ordenados (indexados).
- **Tuplas são imutáveis: você não consegue alterar os valores ou número de elementos**
- A tupla é delimitada por parênteses e seus itens são separados por vírgula.
```python
( 'Jan' , 'Fev' , 'Mar' , 'Abr' , 'Mai' , 'Jun' , 'Jul' , 'Ago' , 'Set' , 'Out' , 'Nov' , 'Dez' )
```


| Índice | Valor |
| ----- | ----- |
| 0     | Jan   |
| 1     | Fev   |
| 2     | Mar   |
| 3     | Abr   |
| 4     | Mai   |
| 5     | Jun   |
| 6     | Jul   |
| 7     | Ago   |
| 8     | Set   |
| 9     | Out   |
| 10    | Nov   |
| 11    | Dez   |



#### Dicionário

- Dicionários são bons para armazenar dados que podem ser representados em uma tabela de duas colunas.

- Eles armazenam coleções de dados em pares de chave/valor, sem ordenação específica.

- Um dicionário é delimitado por chaves e conjuntos de Chave/Valor separados por vírgula.

- Um sinal de dois-pontos é colocado entre cada chave e valor. Vírgulas separam pares de chave:valor.


```python
{ 'TP53' : 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC' , 'BRCA1' : 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' }
```


| Chave |                  Valor                   |
| ----- | ---------------------------------------- |
| TP53  | GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC |
| BRCA1 | GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA |



#### Parâmetros de linha de comando: uma lista especial de parâmetros

Parâmetros de linha de comando são colocados após o nome do script ou programa. Antes do primeiro parâmetro e entre parâmetros adicionais há espaçamento.
Os parâmetros permitem ao usuário fornecer informação ao script quando ele está sendo executado. Python armazena cada trecho do comando em uma lista especial chamada `sys.argv`.

Você precisará importar o módulo chamado `sys` no início do seu script desta forma:

```python
#!/usr/bin/env python3
import sys
```

Vamos imaginar que um script é chamado `amigos.py`. Se você escrever isso na linha de comando:

```bash
$ amigos.py Maria Carlos
```

Isso acontece dentro do script:

> o nome do script 'amigos.py' e as strings 'Maria' e 'Carlos' aparecem na lista chamada `sys.argv`.  

> Estes são os parâmetros da linha de comando, ou argumentos que queira passar para o script. 
> `sys.argv[0]` é o nome do script.
> Você pode acessar valores dos outros parâmetros pelos seus índices, começando com 1, então `sys.argv[1]` contém 'Maria' e `sys.argv[2]` contém 'Carlos'. Você acessa elementos em uma lista adicionando colchetes e o ínidce numérico depois do nome da lista.  
> Se você quisesse imprimir uma mensagem dizendo que estas duas pessoas são amigas, você poderia escrever um código como este


```python
#!/usr/bin/env python3
import sys
friend1 = sys.argv[1] # get first command line parameter
friend2 = sys.argv[2] # get second command line parameter
# now print a message to the screen
print(friend1,'and',friend2,'are friends')
```

A vantagem de obter input do usuário da linha de comando é que você pode escrever um script que é genérico. Ele pode imprimir uma mensagem com qualquer input que o usuário fornecer. Isso o torna flexível.
O usuário também fornece todos os dados que o script precisa na linha de comando de forma que o script não precisa pedir ao usuário para inserir o nome e esperar até que o usuário o faça. O script pode rodar por conta própria sem mais interações do usuário. Isso permite que o usuário trabalhe em outra coisa. Muito prático! 

#### Com que tipo de objeto estou trabalhando?

Você tem um identificador no seu código chamado `dados`. Isso representa uma string, uma lista ou um dicionário? Python tem algumas funções que ajudam a descobrir isso.

| Função       | Descrição                                             |
| ------------ | ----------------------------------------------------- |
| `type(dados)` | diz a qual classe seu objeto pertence                 |
| `dir(dados)`  | diz quais métodos estão disponíveis para o seu objeto |
| `id(dados)`   | diz qual o identificador único do seu objeto          |

Nós cobriremos `dir()` em mais detalhes mais adiante.

```python
>>> data = [2,4,6]
>>> type(data)
<class 'list'>
>>> data = 5
>>> type(data)
<class 'int'>
>>> id(data)
44990666544 
```



---

### [Link to Python 1 Problem Set](problemsets/Python_01_problemset.md)

-------

## Python 2

### Operadores

Um operador em uma linguagem de programação é um símbolo que faz o cumpridor ou intérprete para performar operações matemáticas, relativas ou lógicas e produzir um resultado. Aqui explicaremos o conceito de operadores. 

#### Operadores aritméticos  

Em Python nós podemos escrever declarações que performam cálculos matemáticos. Para fazer isso nós precisamos usar operadores que são específicos para este propósito. Aqui estão operadores aritméticos: 

| Operador | Descrição                                                    | Exemplo          | Resultado   |
| -------- | ------------------------------------------------------------ | ---------------- | ----------- |
| `+`      | Adição                                                       | `3+2`            | 5           |
| `-`      | Subtração                                                    | `3-2`            | 1           |
| `*`      | Multiplicação                                                | `3*2`            | 6           |
| `/`      | Divisão                                                      | `3/2`            | 1.5         |
| `%`      | Módulo (divide o operador da esquerda pelo da direita e retorna o lembrete) | `3%2`            | 1           |
| `**`     | Expoente                                                     | `3**2`           | 9           |
| `//`     | Divisão de piso (resultado é o quociente com os dígitos depois do ponto removidos). | `3//2`  `-11//3` | 1        -4 |


__Módulo__

![3 dividido por 2 é 1 com um restante de 1. Módulo retorna o restatne](images/modulus.png)

__Exemplos de piso__

```python
>>> 3/2
1.5
>>> 3//2
1
>>> -11/3
-3.6666666666666665
>>> -11//3
-4
>>> 11/3
3.6666666666666665
>>> 11//3
3
```



#### Operadores de atribuição  

Nós usamos operadores de atribuição para atribuir valores para variáveis. Você tem usado `=` como operador de atribuição. aqui estão outros: 

| Operador | Equivalente a          | Exemplo                     | resultado assume o valor |
| -------- | ---------------------- | --------------------------- | ------------------- |
| `=`      | `a = 3`                | `result = 3`                | 3                   |
| `+=`     | `result = result + 2`  | `result = 3 ; result += 2`  | 5                   |
| `-=`     | `result = result - 2`  | `result = 3 ; result -= 2`  | 1                   |
| `*=`     | `result = result * 2`  | `result = 3  ; result *= 2` | 6                   |
| `/=`     | `result = result / 2`  | `result = 3 ; result /= 2`  | 1.5                 |
| `%=`     | `result = result % 2`  | `result = 3 ; result %= 2`  | 1                   |
| `**=`    | `result = result ** 2` | `result = 3 ; result **= 2` | 9                   |
| `//=`    | `result = result // 2` | `result = 3 ; result //= 3` | 1                   |





#### Operadores de comparação

Estes operadores comparam dois valores e retornam verdadeiro ou falso.   


| Operador | Descrição             | Exemplo  | Resultado |
| -------- | --------------------- | -------- | ------ |
| `==`     | equal to              | `3 == 2` | Falso  |
| `!=`     | not equal             | `3 != 2` | Verdadeiro  |
| `>`      | greater than          | `3 > 2`  | Verdadeiro  |
| `<`      | less than             | `3 < 2`  | Falso  |
| `>=`     | greater than or equal | `3 >= 2` | Verdadeiro  |
| `<=`     | less than or equal    | `3 <= 2` | Falso  |



#### Operadores lógicos

Operadores lógicos permitem combinar dois ou mais conjuntos de comparações. Você pode combinar os resultados de diferentes formas. Por exemplo você pode 1) querer que todos as declarações sejam verdade, 2) que apenas uma declaração precise ser verdadeira, ou 3) que a declaração precise ser falsa.

| Operador | Descrição                                | Exemplo        | Resultado |
| -------- | ---------------------------------------- | -------------- | ------ |
| `and`    | Verdadeiro se o operador da esquerda e o da direita forem verdade | `3>=2 and 2<3` | Verdadeiro  |
| `or`     | Verdadeiro se o operador da esquerda ou o da direita forem verdade | `3==2 or 2<3`  | Falso   |
| `not`    | Inverte o status lógico           | `not False`    | Verdadeiro  |



#### Operadores de filiação   

Você pode testar para ver se o valor é incluído em uma string, tupla ou lista. Você pode também testar que o valor não está incluso na string, tupla ou lista. 

| Operador | Descrição                                |
| -------- | ---------------------------------------- |
| `in`     | Verdadeiro se o valor é incluso em uma lista, tupla ou string |
| `not in` | Verdadeiro se o valor é ausente em uma lista, tupla ou string |

Por Exemplo:  
```python
>>> dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
>>> 'TCT' in dna
True
>>>
>>> 'ATG' in dna
False
>>> 'ATG' not in dna
True
>>> codons = [ 'atg' , 'aaa' , 'agg' ]
>>> 'atg' in codons
True
>>> 'ttt' in codons
False
```



#### Operador Precedente

Operadores são listados em ordem de precedência. Os maiores listados primeiro. Nem todos operadores listados aqui são mencionados acima. 

| Operador                                 | Descrição                                |
| ---------------------------------------- | ---------------------------------------- |
| `**`                                     | Exponenciação (Eleva o poder)            |
| `~` `+` `-`                              | Complemento, unário mais e menos (nomes de métodos que os dois últimos são +@ e -@) |
| `*` `/` `%` `//`                         | Multiplica, divide, módulo e divisão de piso |
| `+` `-`                                  | Adição e subtração                       |
| `>>` `<<`                                | Deslocamento parte por parte de direita e esquerda |
| `&`                                      | Deslocamento 'AND'                       |
| `^` `\|`                                 | Bitwise exclusivo 'OR' e regular 'OR'    |
| `<=` `<` `>` `>=`                        | Operadores de comparação                 |
| `<>` `==` `!=`                           | Operadores de igualdade                  |
| `=` `%=` `/=` `//=` `-=` `+=` `*=` `**=` | Operadores de atribuição                 |
| `is`                                     | Operadores de identidade                 |
| `is not`                                 | Operador de não identidade               |
| `in`                                     | Operador de filiação                     |
| `not in`                                 | Operador de filiação negativa            |
| `not` `or` `and`                         | Operadores lógicos                       |

Nota: Saiba mais a respeito [bitwise operators](https://www.tutorialspoint.com/python/bitwise_operators_example.htm). 

### Verdade


Vamos voltar um pouco... O que é verdade?  

Tudo é verdade, exceto por:  


| expressão               | VERDADEIRO/FALSO |
| ----------------------- | ---------- |
| `0`                     | FALSO      |
| `None`                  | FALSO      |
| `False`                 | FALSO      |
| `''` (string vazia)      | FALSO      |
| `[]` (lista vazia)      | FALSO      |
| `()` (tupla vazia)      | FALSO      |
| `{}` (dicionário vazio) | FALSO      |

O que significa que estes são verdade: 


| expressão                         | VERDADEIRO/FALSO |
| --------------------------------- | ---------- |
| `'0'`                             | VERDADEIRO |
| `'None'`                          | VERDADEIRO |
| `'False'`                         | VERDADEIRO |
| `'True'`                          | VERDADEIRO |
| `' '` (string de um espaço vazio)  | VERDADEIRO |



#### Use `bool()` para testar a verdade    

`bool()` é uma função que testará se um valor é verdade.

```python
>>> bool(True)
True
>>> bool('True')
True
>>>
>>>
>>> bool(False)
False
>>> bool('False')
True
>>>
>>>
>>> bool(0)
False
>>> bool('0')
True
>>>
>>>
>>> bool('')
False
>>> bool(' ')
True
>>>
>>>
>>> bool(())
False
>>> bool([])
False
>>> bool({})
False
```


### Lógica: Declarações de controle 


Declarações de controle são usadas para direcionar o fluxo do seu código e criar oportunidade para tomada de decisão. Os fundamentos das declarações de controle são construindo a verdade.

#### Declaração If

- Use a declaração `if` para testar a verdade e executar linhas do código caso seja verdade.  
- Quando a expressão avalia como verdade cada uma das declarações recuadas abaixo da declaração `if`, também conhecidas como o bloco de declarações aninhadas, serão executadas.


**if**

```python
expressão if :
  declaração
  declaração
```

Por Exemplo:  
```python
dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
if 'AGC' in dna:
  print('found AGC in your dna sequence')
```
Returns:  
```
found AGC in your dna sequence
```

**else**

- A porção `if` da declaração if/else statement se comporta como antes. 
- O primeiro bloco recuado é executado se a condição é verdadeira. .
- Se a condição for falsa, o segundo bloco else recuado é executado.

```python
dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
if 'ATG' in dna:
  print('found ATG in your dna sequence')
else:
  print('did not find ATG in your dna sequence')
```
Returns:  
```
did not find ATG in your dna sequence
```


#### if/elif

- A condição `if` é testada como antes, e o bloco recuado é executado caso a condição for verdadeira.
- Se for falsa, o bloco recuado seguindo o `elif` é executado se a primeira condição `elif` for verdadeira. 
- Quaisquer condições restantes `elif` serão testadas em ordem até que uma verdadeira for encontrada. Se nenhuma for, o bloco recuado `else` é executado.

```python
count = 60
if count < 0:
  message = "is less than 0"
  print(count, message)
elif count < 50:
  message = "is less than 50"
  print (count, message)
elif count > 50:
  message = "is greater than 50"
  print (count, message)
else:
  message = "must be 50"
  print(count, message)
```
Returns:  
```
60 is greater than 50
```

Vamos mudar a contagem para 20, qual declaração será executada?   

```python
count = 20
if count < 0:
  message = "is less than 0"
  print(count, message)
elif count < 50:
  message = "is less than 50"
  print (count, message)
elif count > 50:
  message = "is greater than 50"
  print (count, message)
else:
  message = "must be 50"
  print(count, message)
```
Returns:  
```
20 is less than 50
```

O que acontece quando a contagem é 50?  

```python
count = 50
if count < 0:
  message = "is less than 0"
  print(count, message)
elif count < 50:
  message = "is less than 50"
  print (count, message)
elif count > 50:
  message = "is greater than 50"
  print (count, message)
else:
  message = "must be 50"
  print(count, message)
```
Returns:  
```
50 must be 50
```




### Números


Python reconhece 3 tipos de números: inteiros, números de ponto flutuante e números complexos. 

#### inteiros  

- Conhecidos como int
- Um int pode ser positivo ou negativo
- e **não** contém um ponto decimal ou expoente.

#### número de ponto flutuante  

- Conhecido como float
- Um ponto flutuante pode ser positivo ou negativo
- E **contém** um ponto decimal (`4.875`) ou expoente (`4.2e-12`)

#### número complexo  

- conhecido como complex
- está na forma de a+bi onde bi é uma parte imaginária.

#### Funções de conversão    

As vezes um tipo de número precisa ser mudado por outro para a função poder trabalhar. Aqui está a lista de funções para converter tipos de números:

| função          | Descrição                                |
| --------------- | ---------------------------------------- |
| `int(x)`        | para converter x para um inteiro simples |
| `float(x)`      | para converter x para um número de ponto flutuante |
| `complex(x)`    | para converter x para um número complexo com parte real x e parte imaginária zero |
| `complex(x, y)` | para converter x e y para um número complexo com parte real x e parte imaginária y |

```python
>>> int(2.3)
2
>>> float(2)
2.0
>>> complex(2.3)
(2.3+0j)
>>> complex(2.3,2)
(2.3+2j)
```


#### Funções numéricas

Aqui está a lista de funções que usam números como argumentos. Elas são úteis como arredondamento.



| função            | Descrição                                |
| ----------------- | ---------------------------------------- |
| `abs(x)`          | O valor absoluto de x: a distância (positiva) entre x e zero. |
| `round(x [,n])`   | x arredondado para n dígitos do ponto decimal. round() arredonda para um inteiro se o valor é exatamente entre dois inteiros, então round(0.5) é 0 e round(-0.5) é 0. round(1.5) é 2. **Arredondar para um número fixo de lugares decimais pode fornecer resultados imprevisíveis.** |
| `max(x1, x2,...)` | O último argumento é retornado           |
| `min(x1, x2,...)` | O menor argumento é retornado            |

```python
>>> abs(2.3)
2.3
>>> abs(-2.9)
2.9
>>> round(2.3)
2
>>> round(2.5)
2
>>> round(2.9)
3
>>> round(-2.9)
-3
>>> round(-2.3)
-2
>>> round(-2.009,2)
-2.01
>>> round(2.675, 2)  # note this rounds down
2.67
>>> max(4,-5,5,1,11)
11
>>> min(4,-5,5,1,11)
-5
```


Muitas funções numéricas não são construídas dentro da central do Python e precisam ser importadas para dentro do script se quisermos usá-las. Para incluir elas, no topo do script digite:
`import math`

Estas próximas funções são encontradas no módulo matemático e precisam ser importadas. Para usá-las, preceda a função com o nome do módulo, i.e, `math.ceil(15.5)`  


| math.function    | Descrição                                |
| ---------------- | ---------------------------------------- |
| `math.ceil(x)`   | retorna o menor inteiro maior ou igual que x |
| `math.floor(x)`  | retorna o maior inteiro menor ou igual que x. |
| `math.exp(x)`    | O exponencial de x: e<sup>x</sup> é retornado |
| `math.log(x)`    | O logarítmo natural de x, para x > 0 é retornado |
| `math.log10(x)`  | O logarítmo de base 10 de x para x > 0 é retornado |
| `math.modf(x)`   | As partes fracionárias e inteiras de x são retornadas em uma tupla de dois itens |
| `math.pow(x, y)` | O valor de x criado pelo poder y é retornado |
| `math.sqrt(x)`   | Retorna a raíz quadrada de x para x >= 0   |


```python
>>> import math
>>>
>>> math.ceil(2.3)
3
>>> math.ceil(2.9)
3
>>> math.ceil(-2.9)
-2
>>> math.floor(2.3)
2
>>> math.floor(2.9)
2
>>> math.floor(-2.9)
-3
>>> math.exp(2.3)
9.974182454814718
>>> math.exp(2.9)
18.17414536944306
>>> math.exp(-2.9)
0.05502322005640723
>>>
>>> math.log(2.3)
0.8329091229351039
>>> math.log(2.9)
1.0647107369924282
>>> math.log(-2.9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: math domain error
>>>
>>> math.log10(2.3)
0.36172783601759284
>>> math.log10(2.9)
0.4623979978989561
>>>
>>> math.modf(2.3)
(0.2999999999999998, 2.0)
>>>
>>> math.pow(2.3,1)
2.3
>>> math.pow(2.3,2)
5.289999999999999
>>> math.pow(-2.3,2)
5.289999999999999
>>> math.pow(2.3,-2)
0.18903591682419663
>>>
>>> math.sqrt(25)
5.0
>>> math.sqrt(2.3)
1.51657508881031
>>> math.sqrt(2.9)
1.70293863659264
```

### Comparando dois números

Algumas vezes, é necessário comparar dois números e descobrir se o primeiro é menor, igual ou maior que o segundo. 

A simples função `cmp(x,y)` não é disponível em Python 3. 

Use este idioma ao invés:  
```python
cmp = (x>y)-(x<y)
```

Ele retorna três diferentes valores dependendo do x e do y

- se x<y, o -1 é retornado

- se x>y, o 1 é retornado

- x == y, o 0 é retornado

---

### [Link to Python 2 Problem Set](problemsets/Python_02_problemset.md)

----

##  Python 3

### Sequências

Na próxima seção, nós iremos aprender sobre as strings, tuplas, e listas. Todos estes são exemplos de sequências em python. uma sequência de caracteres `'ACGTGA'`, uma tupla `(0.23, 9.74, -8.17, 3.24, 0.16)`, e uma lista `['dog', 'cat', 'bird']` são sequências de diferentes tipos de dados. Veremos mais detalhes em breve.

Em Python, um tipo de objeto consegue operações que pertencem àquele tipo. Sequências tem operações sequenciais então as strings podem também usar operações sequenciais. Strings também possuem suas próprias operações específicas.

Você pode perguntar qual a extensão de qualquer sequência

```python
>>>len('ACGTGA') # extensão de uma string
6
>>>len( (0.23, 9.74, -8.17, 3.24, 0.16) )   # extensão de uma tupla, precisa de dois parênteses (( ))
5
>>>len(['dog', 'cat', 'bird'])  # extensão de uma lista
3
```

Você pode também usar funções de strings específicas, mas não em listas e vice versa. Nós vamos aprender mais sobre isso posteriormente. `rstrip()` é um método de string ou função. Você obtém um erro se você tentar usar isso em uma lista.

```python
>>> 'ACGTGA'.rstrip('A')
'ACGTG'
>>> ['dog', 'cat', 'bird'].rstrip()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'rstrip'
```

### Quais funções vão com meu objeto?

Como descobrir quais funções servem com um objeto? Existe uma função prática `dir()`. Como um exemplo quais funções você pode acionar em sua string `'ACGTGA'`?

```python
>>> dir('ACGTGA')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```
`dir()` irá retornar todos os atributos de um objeto, dentre eles estão funções. Tecnicamente, funções pertencentes a uma classe específica (tipo de objeto) são chamadas de métodos.
Você pode chamar `dir()` em qualquer objeto, mais comumente, você usará isso na esfera interativa do Python.

### Strings


- Uma string é uma série de caracteres começando e terminando com marcas de aspas únicas ou duplas.
- Strings são um exemplo de uma sequência de Python. Uma sequência é definida como um grupo ordenado posicionalmente. Isso significa que cada elemento no grupo tem uma posição, começando com zero, i.e. 0,1,2,3 e assim até você chegar no final da string. 

#### Aspas  

- Única (')  
- Dupla (")   
- Tripla (''' or """)   

Notas sobre as aspas:  

- Aspas únicas e duplas são equivalentes.  
- O nome de uma variável dentro das sentenças é apenas o identificador da string, não o valor armazenado dentro da variável. `format()` é útil para interpolação de variáveis em python
- Sentenças triplas (únicas ou dobradas) são usadas antes e depois de uma string que abrange múltiplas linhas. 

Uso de exemplos das aspas:  

```python
palavra = 'word'
sentença = "This is a sentence."
parágrafo = """This is a paragraph. Isso é feito de múltiplas linhas e sentenças. 
E assim vai.
"""
```

#### Strings e a função `print()` 

Nós vimos exemplos de `print()` antes. Vamos conversar sobre isso um pouco mais. `print()` é uma função que assume um ou mais argumentos separados por vírgulas.

Vamos usar a função `print()` para imprimir uma string.  
```python
>>>print("ATG")  
ATG
```

Vamos atribuir uma string a uma variável e imprimir a variável.
```python
>>>dna = 'ATG'
ATG
>>> print(dna)
ATG
```

O que acontece se nós colocarmos a variável nas sentenças?  
```python
>>>dna = 'ATG'
ATG
>>> print("dna")
dna
```
> A string literal 'dna' é impressa na tela, não os conteúdos 'ATG'

Vamos ver o que acontece quando nós demos `print()` em duas strings literais como argumentos.  
```python
>>> print("ATG","GGTCTAC")
ATG GGTCTAC
```
> Nós conseguimos as duas strings literais impressas na tela separadas por um espaço

E se vocÊ não quiser suas strings separadas por um espaço? use o operador concatenação para concatenar as duas strings antes ou dentro da função `print()`. 
```python
>>> print("ATG"+"GGTCTAC")
ATGGGTCTAC
>>> combined_string = "ATG"+"GGTCTAC"
ATGGGTCTAC
>>> print(combined_string)
ATGGGTCTAC
```
> Nós conseguimos duas strings impressas na tela sem ser separadas por um espaço.
> Você pode também usar isso
```python
>>> print('ATG','GGTCTAC',sep='')
ATGGGTCTAC
```

Agora, vamos imprimir uma variável e uma string literal.
```python
>>>dna = 'ATG'
ATG
>>> print(dna,'GGTCTAC')
ATG GGTCTAC
```
> Nós conseguimos o valor da variável e a string literal impressa na tela separada por um espaço

Como poderíamos imprimir os dois sem um espaço?
```python
>>>dna = 'ATG'
ATG
>>> print(dna + 'GGTCTAC')
ATGGGTCTAC
```

Algo para se pensar sobre: valores de variáveis são variáveis. Em outras palavras, eles são mutáveis e alteráveis.  
```python
>>>dna = 'ATG'
ATG
>>> print(dna)
ATG
>>>dna = 'TTT'
TTT
>>> print(dna)
TTT
```
> O novo valor da variável 'dna' é impresso no visor quando `dna` é um argumento para a função `print()`.

#### `print()` e erros comuns

Vamos olhar os erros típicos que você encontrará quando usar a função `print()`.

O que acontecerá se você esquecer de fechar suas sentenças?
```
>>> print("GGTCTAC)
  File "<stdin>", line 1
    print("GGTCTAC)
                  ^
SyntaxError: EOL while scanning string literal
```
> Nós obtemos um'SyntaxError' se a sentença de encerramento não for usada.

O que acontecerá se você se esquecer de incluir uma string que você quer imprimir nas sentenças?
```python
>>> print(GGTCTAC)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'GGTCTAC' is not defined
```
> Nós obtemos um 'NameError' quando a string literal não for inclusa nas sentenças porque o Python está procurando uma variável com o nome GGTCTAC

```python
>>> print "boo"
  File "<stdin>", line 1
    print "boo"
              ^
SyntaxError: Missing parentheses in call to 'print'
```
Em python2, o comando era `print`, mas isso mudou para `print()` em python3, então não se esqueça dos parênteses!

#### Caracteres especiais e de escape

Como você incluiria uma nova linha, retorno de transporte, ou tab em sua string?  

| Caractere de escape | Descrição     |
| ---------------- | --------------- |
| \\n              | Nova linha      |
| \\r              | Retorno de transporte |
| \\t              | Tab             |


Vamos incluir alguns caracteres de escape em suas strings e funções `print()`.
```python
>>> string_with_newline = 'this sting has a new line\nthis is the second line'
>>> print(string_with_newline)
this sting has a new line
this is the second line
```
> Nós imprimimos uma nova linha na tela

`print()` adiciona espaços entre argumentos e uma nova linha ao final. Você pode mudar isso com `sep=` e `end=`. Aqui está um exemplo:
`print('one line', 'second line' , 'third line', sep='\n', end = '')`

Uma forma mais limpa para fazer isso é expressar uma string de múltiplas linhas inclusa em aspas triplas (""").
```python
>>> print("""this string has a new line
... this is the second line""")
this string has a new line
this is the second line
```

Vamos imprimir um caractere tab (\t).
```python
>>> line = "value1\tvalue2\tvalue3"
>>> print(line)
value1	value2	value3
```
> Nós obtemos as três palavras separadas por caracteres tab. Um formato comum para dados é separar colunas com tabs como isso.

Você pode adicionar uma barra invertida antes de qualquer caractere para forçar de ser impresso como um literal. Isso é chamado 'escaping'. Só é realmente útil para imprimir sentenças literais ' and " 

```python
>>> print('this is a \'word\'')  # if you want to print a ' inside '...'
this is a 'word'
>>> print("this is a 'word'") # maybe clearer to print a ' inside "..."
this is a 'word'
```
> Em ambos os casos a sentença atual única é impressa na tela 

Se você quiser todos caracteres em sua string para permanecer exatamente como são, declare sua string uma string crua literal com 'r' antes da primeira sentença. Isso parece feio, mas funciona.
```python
>>> line = r"value1\tvalue2\tvalue3"
>>> print(line)
value1\tvalue2\tvalue3
```
> Nossos caracteres de escape '\t' declare como nós digitamos, eles não são convertidos para caracteres tab de fato.

#### Concatenação

Para concatenar strings use o operador de concatenação '+'  

```python
>>> promoter= 'TATAAA'
>>> upstream = 'TAGCTA'
>>> downstream = 'ATCATAAT'
>>> dna = upstream + promoter + downstream
>>> print(dna)
TAGCTATATAAAATCATAAT
```
> O operador de concatenação pode ser usado para combinar strings. A nova combinação de strings pode ser armazenada em uma variável. 

#### A diferença entre a string + e o integrador +

O que acontece se você usar `+` com números (estes são inteiros ou ints)?

```python
>>> 4+3
7

```

Para strings, `+` concatena; para inteiros, `+` soma.

Você precisa converter os números para strings antes de poder concatená-las

```python
>>> str(4) + str(3)
'43'
```

#### Determinar a extensão de uma string

Use a função `len()` para calcular a extensão de uma string. Essa função assume a sequência como um argumento e retorna uma int


```python
>>> print(dna)
TAGCTATATAAAATCATAAT
>>> len(dna)
20
```
> A extensão de uma string, incluindo espaços, é calculada e apresentada. 

O valor que `len()` retorna pode ser armazenado em uma variável.  
```python
>>> dna_length = len(dna)
>>> print(dna_length)
20
```
Você pode misturar strings e ints em `print()`, mas não em concatenação.

```python
>>> print("The lenth of the DNA sequence:" , dna , "is" , dna_length)
The lenth of the DNA sequence: TAGCTATATAAAATCATAAT is 20
```




#### Alterando o caso da string

Alterando o caso da string é um pouco distinto do que você pode esperar inicialmente. Por exemplo, para diminuir uma string precisamos utilizar um método. Um método é uma função específica para um objeto. Quando nós assumimos uma string a uma variável estamos criando uma instância de um objeto de string. Esse objeto tem uma série de métodos que funcionarão nos dados que estão armazenados no objeto. Lembre-se que `dir()` irá te dizer todos os métodos que estão disponíveis para um objeto. A função `lower()` é um método de string. 

Vamos criar um novo objeto de string.    
```python
dna = "ATGCTTG"
```
> Parece familiar?

Agora que nós temos um objeto de string nós podemos usar os métodos de string. A forma que você utiliza um método consiste em inserir um '.' entre o objeto e o nome do método.
```python
>>> dna = "ATGCTTG"
>>> dna.lower()
'atgcttg'
```
> o método lower() retorna os conteúdos armazenados na variável 'dna' em letra minúscula. 

Os conteúdos da variável 'dna' não se alteraram. Strings são imutáveis. Se você quiser manter a versão minúscula de uma string, armazene ela em uma nova variável.
```python
>>> print(dna)
ATGCTTG
>>> dna_lowercase = dna.lower()
>>> print(dna)
ATGCTTG
>>> print(dna_lowercase)
atgcttg
```
O método de string pode ser guardado dentro de outras funções.
```python
>>> dna = "ATGCTTG"
>>> print(dna.lower())
atgcttg
```
> Os conteúdos de 'dna' são transformados em minúsculos e trasnportados para a função `print()`.

Se você tentar usar um método de string em um objeto que não é uma string você receberá um erro. 

```python
>>> nt_count = 6
>>> dna_lc = nt_count.lower()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'lower'
```
> Você obtém um AttributeError quando você usa um método em um tipo de objeto incorreto. Nós recebemos que o objeto int (um int é retornado por `len()`) não tem uma função chamada inferior.

Vamos tornar uma string maiúscula agora.

```python
>>> dna = 'attgct'
>>> dna.upper()
'ATTGCT'
>>> print(dna)
attgct
```
> Os conteúdos de uma variável 'dna' são retornados em maiúsculo. Os conteúdos de 'dna' não foram alterados.

#### Encontrar e contar

O índice posicional de uma string exata em uma string maior pode ser encontrado e retornado com o método de string 
`find()`. Uma string exata é dada como um argumento e o índice de sua primeira ocorrência é retornado. -1 é retornado se nada for encontrado.

```python
>>> dna = 'ATTAAAGGGCCC'
>>> dna.find('T')
1
>>> dna.find('N')
-1
```

> O subtermo 'T' é encontrado pela primeira vez no índice 1 na string 'dna' então 1 é retornado. O subtermo 'N' não foi encontrado, então -1 é retornado. `count(str)` retorna o número (como um int) que se encaixa exatamente com a string que encontrou

```python
>>> dna = 'ATGCTGCATT'
>>> dna.count('T')
4
```
> O número de vezes que 'T' for encontrado é retornado. A string armazenada em 'dna' não é alterada.


#### Substituir uma string com outra

`replace(str1,str2)` retorna uma nova string com todas as combinações de `str1` em uma string substituída com `str2`. 


```python
>>> dna = 'ATGCTGCATT'
>>> dna.replace('T','U')
'AUGCUGCAUU'
>>> print(dna)
ATGCTGCATT
>>> rna = dna.replace('T','U')
>>> print(rna)
AUGCUGCAUU
```
> Todos as ocorrências de T são substitupidas por U. A nova string é retornada. A string original não foi de fato alterada. Se você quiser reutilizar a nova string, armazene ela em uma variável.



#### Extraindo um subtermo, ou separando

Partes de uma string podem ser localizadas baseadas na posição e retornadas. Isso é porque uma string é uma sequência. Coordenadas começam em 0. Você adiciona a coordenada em colchetes depois do nome da string. 

Você pode chegar a qualquer parte da string com a seguinte sentença [start : end : step].  

Essa string 'ATTAAAGGGCCC' é feita da seguinte sequência de caracteres, e posições (começando em zero).



| Posição/Índice | Caractere |
| -------------- | --------- |
| 0              | A         |
| 1              | T         |
| 2              | T         |
| 3              | A         |
| 4              | A         |
| 5              | A         |
| 6              | G         |
| 7              | G         |
| 8              | G         |
| 9              | C         |
| 10             | C         |
| 11             | C         |

Vamos retornar os 4°, 5° e 6° nucleotídeos. Para isso, nós precisamos começar contando em 0 e lembrando que o python conta os vãos entre cada caractere, começando com zero. 

```
index      0   1   2   3   4   5   6   7   8 ...
string       A   T   T   A   A   A   G   G  ...
```



```python
>>> dna = 'ATTAAAGGGCCC'
>>> sub_dna = dna[3:6]
>>> print(sub_dna)
AAA
```
> Os caracteres com índices 3, 4, 5 são retornados. Em outras palavras, todo caractere começando com o índice 3 e acima mas não incluindo, o índice de 6 que retornado. 

Vamos retornar os primeiros 6 caracteres.
```python
>>> dna = 'ATTAAAGGGCCC'
>>> sub_dna = dna[0:6]
>>> print(sub_dna)
ATTAAA
```
> Todo caractere começando no índice 0 e acima mas não incluindo o de índice 6 são retornados. Esse é o mesmo que dna[:6]

Vamos retornar todos os caracteres do índice 6 até o fim da string.
```python
>>> dna = 'ATTAAAGGGCCC'
>>> sub_dna = dna[6:]
>>> print(sub_dna)
GGGCCC
```
> Quando o segundo argumento é deixado em branco, todos caracteres do índice 6 e acima são retornados.

Vamos retornar os últimos 3 caracteres.
```python
>>> sub_dna = dna[-3:]
>>> print(sub_dna)
CCC
```
> Quando o segundo argumento é deixado em branco e o primeiro argumento é negativo (-X), X caracteres do final da string são retornados.

#### Reverter uma string ou uma lista

 Não existe função de reverso, você precisa usar uma fatia com patamar -1 e início e fim vazios.

Para uma string, se parece com isso

```python
>>> dna='GATGAA'
>>> dna[::-1]
'AAGTAG'
```


#### Outros métodos de string

Desde que estes são métodos, se certifique de utilizar na sentença `string.method()`.

| função                         | Descrição                                |
| ------------------------------ | ---------------------------------------- |
| `s.strip()`                    | retorna uma string com o espaço em branco removido do começo e fim |
| `s.isalpha()`                  | testa se todos caracteres da string são alfabéticos. Retorna verdadeiro ou falso. |
| `s.isdigit()`                  | testa se todos caracteres da string são nnuméricos. Retorna verdadeiro ou falso. |
| `s.startswith('other_string')` | testa se a string começa com a string fornecida como argumento. Retorna verdadeiro ou falso. |
| `s.endswith('other_string')`   | testa se a string termina com a string fornecida como argumento. Retorna verdadeiro ou falso. |
| `s.split('delim')`             | separa a string no delimitador exato fornecido. Retorna a lista de subtermos. Se o argumento é fornecido, a string será separada no espaço em branco. |
| `s.join(list)`                 | O oposto de `split()`. Os elementos de uma lista serão concatenados juntos usando a string armazenada em 's' como um delimitadoras. |


__split__
`split` é um método ou forma de partir uma string em um grupo de caracteres. O que é retornado é uma lista de elementos com caracteres que são usados para partir removidos. Iremos através das listas em mais detalhes na próxima sessão. Não se preocupe com isso.

Vamos olhar para essa string:
```
00000xx000xx000000000000xx0xx00
```
Vamos separar em 'xx' e obter uma lista dos 0's  

O que é o What 's' em `s.split(delim)` ?

O que é 'delim' em `s.split(delim)` ?

Vamos tentar isso:
```python
>>> string_to_split='00000xx000xx000000000000xx0xx00'
>>> string_to_split.split('xx')
['00000', '000', '000000000000', '0', '00']
>>> zero_parts = string_to_split.split('xx')
>>> print(zero_parts)
['00000', '000', '000000000000', '0', '00']
```
> Nós começamos com uma string e agora temos uma lista com todos os delimitadores removidos

Aqui está outro exemplo. Vamos dividir em tabs para obter uma lista dos números em colunas separadas tab.   
```python
>>> input_expr = '4.73\t7.91\t3.65'
>>> expression_values = input_expr.split('\t')
>>> expression_values
['4.73', '7.91', '3.65']
```



__join__
`join` é um método ou uma forma de pegar uma lista de elementos, de coisas, e transformar em uma string com algo posto entre cada elemento. A lista será coberta na próxima seção com mais detalhes.


Vamos aplicar em uma lista de Ns `list_of_Ns = ['NNNNN', 'NNN', 'N', 'NNNNNNNNNNNNNNN', 'NN']` em 'xx' para obter essa string:
```
NNNNNxxNNNxxNxxNNNNNNNNNNNNNNNxxNN
```


O que é o 's' em `s.join(list)` ?

O que é a 'list' em `s.join(list)` ?

```python
>>> list_of_Ns = ['NNNNN', 'NNN', 'N', 'NNNNNNNNNNNNNNN', 'NN']
>>> list_of_Ns
['NNNNN', 'NNN', 'N', 'NNNNNNNNNNNNNNN', 'NN']
>>>
>>> string_of_elements_with_xx = 'xx'.join(list_of_Ns)
>>> string_of_elements_with_xx
'NNNNNxxNNNxxNxxNNNNNNNNNNNNNNNxxNN'
```
> Nós começamos com uma lista e agora temos todos os elementos em uma string com o delimitador adicionado entre cada elemento.


Vamos pegar uma lista de valores de expressão e criar uma string delimitada tab que abrirá bem em uma planilha com cada valor em sua própria coluna:
```python
>>> expression_values = ['4.73', '7.91', '3.65']
>>>expression_values
['4.73', '7.91', '3.65']
>>> expression_value_string = '\t'.join(expression_values)
>>> expression_value_string
'4.73\t7.91\t3.65'
```
> imprima isso em um arquivo e abra ele em Excel, é lindo!!



### Formatação de string

Strings podem ser formatadas usando a função `format()`. Bem intuitivo, mas espere até ver os detalhes! Por exemplo, se você quiser incluir strings literais e variáveis em sua declaração de impressão e não quer concatenar ou usar múltiplos argumentos na função `print()` você pode usar formatação de string.  

```python
>>> string = "This sequence: {} is {} nucleotides long and is found in {}."
>>> string.format(dna,dna_len,gene_name)
'This sequence: TGAACATCTAAAAGATGAAGTTT is 23 nucleotides long and is found in Brca1.'
>>> print(string) # string.format() does not alter string
This sequence: {} is {} nucleotides long and is found in {}.
>>> new_string = string.format(dna,dna_len,gene_name)
>>> print(new_string)
This sequence: TGAACATCTAAAAGATGAAGTTT is 23 nucleotides long and is found in Brca1.
```
Nós colocamos juntamente três variáveis e strings literais em uma string única usando a função `format()`. A string original não é alterada, uma nova string é retornada e incorpora os argumentos. Você pode salvar o valor retornado em uma nova variável. Cada `{}` é um espaço reservado para a string que precisa ser inserida.  

Algo legal sobre `format()` é que você pode imprimir int e tipos variáveis de string sem converter primeiramente.

Você pode também chamar diretamente `format()` dentro de uma função `print()`. Aqui estão dois exemplos

```python
>>> string = "This sequence: {} is {} nucleotides long and is found in {}."
>>> print(string.format(dna,dna_len,gene_name))
This sequence: TGAACATCTAAAAGATGAAGTTT is 23 nucleotides long and is found in Brca1.
```
Ou use a função `format()` em uma string literal:
```python
>>> print( "This sequence: {} is {} nucleotides long and is found in {}.".format(dna,dna_len,gene_name))
This sequence: TGAACATCTAAAAGATGAAGTTT is 23 nucleotides long and is found in Brca1.
```
#### A mini-linguagem `format()` 

Até agora, nós usamos apenas `{}` para mostrar onde inserir o valor de uma variável em uma string. Você pode adicionar caracteres especiais dentro de `{}` para mudar a forma que a variável é formatada quando é inserida dentro da string. 

> Você pode numerar estes, não necessariamente em ordem.

```python
>>> '{0}, {1}, {2}'.format('a', 'b', 'c')
'a, b, c'
>>> '{2}, {1}, {0}'.format('a', 'b', 'c')
'c, b, a'
```

Para mudar o espaçamento das strings e a forma que os números são formatados, você adiciona `:` e outros caracteres especiais como isso `{:>5}` para corrigir uma string em um campo de cinco caracteres

Vamos corrigir justificando alguns números.  

```python
>>> print( "{:>5}".format(2) )
    2
>>> print( "{:>5}".format(20) )
   20
>>> print( "{:>5}".format(200) )
  200
```

E sobre preencher com zeros? Isso significa que o campo de cinco caracteres será preenchido conforme preciso com zeros a esquerda de quaisquer números que você quer apresentar
```python
>>> print( "{:05}".format(2) )
00002
>>> print( "{:05}".format(20) )
00020
```

Use um `<` para indicar justificação à esquerda.
```python
>>> print( "{:<5} genes".format(2) )
2     genes
>>> print( "{:<5} genes".format(20) )
20    genes
>>> print( "{:<5} genes".format(200) )
200   genes
```
Alinhamento ao centro é feito com `^` ao invés de `>` ou `<`. Você pode também preencher com caracteres sem ser 0. Aqui vamos tentar `_` ou sublinhar como em `:_^`. O símbolo de preencher vai antes do símbolo de alinhamento.
```python
>>> print( "{:_^10}".format(2) )
____2_____
>>> print( "{:_^10}".format(20) )
____20____
>>> print( "{:_^10}".format(200) )
___200____

```

#### Sumário de símbolos de formatação especiais até agora

__Aqui estão algumas das opções de ALINHAMENTO:__

| Opção  | Significado                              |      |
| ------ | ---------------------------------------- | ---- |
| `<`    | Força o campo para estar alinhado a esquerda com o espaço disponível (Isso é o padrão para a maioria dos objetos). |      |
| `>`    | Força o campo para estar alinhado a direita com o espaço disponível (Isso é o padrão para números). |      |
| `=`    | Força o campo para o preenchimento ser posto de pois do sinal (se tiver) mas antes dos dígitos. Isso é usado para imprimir campos na forma ‘+000000120’. Essa opção de alinhamento é apenas válida para tipos numéricos. |      |
| `^`    | Força o campo para ser centralizado com o espaço disponível. |      |

>Aqui está um exemplo 
>
>`{  :    x  <  10   s}`
>
> preencher com `x`   
> justificamento à esquerda `<`  
> `10` um campo com dez caracteres 
> `s` uma string


__Tipos comuns__

| tipo | descrição                                |
| ---- | ---------------------------------------- |
| b    | converte para binário                    |
| d    | inteiro decimal                          |
| e    | expoente, precisão padrão é 6, usa `e`   |
| E    | expoente, usa `E`                        |
| f    | ponto de flutuação, precisão padrão é 6 (também F) |
| g    | número genérico, flutua para valores próximos de 0, expoente para outros; também G |
| s    | string, tipo padrão (conforme exemplo acima) |
| x    | converte para hexadecimal, também X        |
| %    | converte para % multiplicando por 100      |


#### Qual é o ponto?


Muito pode ser feito com a função `format()`. Aqui está um último exemplo, mas não a última funcionalidade desta função. vamos circular um número de ponto de flutuação para algumas casas decimais, começando com muitos. (o padrão é 6). Note que a função circula para a casa decimal mais próxima, mas nem sempre exatamente da forma que você espera por conta da forma que os computadores representam decimais com 1s e 0s.

```python
'{:f}'.format(3.141592653589793)
'3.141593'
>>> '{:.4f}'.format(3.141592653589793)
'3.1416'
```

---

### [Link to Python 3 Problem Set](problemsets/Python_03_problemset.md)



---
## Python 4

### Listas e Tuplas




#### Listas

Listas são tipos de dados que armazenam uma coleção de dados. 


- Listas são usadas para armazenar uma coleção de dados ordenada e *indexada*.
- Valores são separados por vírgulas
- Valores são anexados entre colchetes '[]'
- Listas podem crescer e encolher
- Valores são mutáveis

```python
[ 'atg' , 'aaa' , 'agg' ]
```

#### Tuplas

- Tuplas são usadas para armazenar uma coleção de dados ordenada e indexada
- Valores são separados por vírgulas
- Valores são anexados entre parenteses '()'
- Tuplas **NÃO** podem crescer ou encolher
- Valores são imutáveis

```python
( 'Jan' , 'Fev' , 'Mar' , 'Abr' , 'Mai' , 'Jun' , 'Jul' , 'Ago' , 'Set' , 'Out' , 'Nov' , 'Dez' )
```

Muitas funções e métodos retornam tuplas como `math.modf(x)`. Essa função retorna as partes fracionais e inteiras de `x` em uma tupla de dois itens. Aqui não existe motivos para mudar a sequência.

```python
>>> math.modf(2.6)
(0.6000000000000001, 2.0)
```

#### De volta às listas

#### Acessando valores em listas

Para recuperar um valor em uma lista utilize o índice do valor nesse formato list[index]. Isso retornará o valor do índice especificado, começando com 0. 

Aqui está uma lista:  
```python
>>> codons = [ 'atg' , 'aaa' , 'agg' ]
```
> Existem 3 valores com os índices 0, 1, 2

| Índice | Valor |
| ----- | ----- |
| 0     | atg   |
| 1     | aaa   |
| 2     | agg   |

Vamos acessar o valor de índice 0. Você vai precisar de um número de índice (`0`) dentro de colchetes desta forma `[0]` . Isso vai após o nome da lista (`codons`)
```python
>>> codons = [ 'atg' , 'aaa' , 'agg' ]
>>> codons[0]
'atg'
```
O valor pode ser salvo em uma variável, e ser usado depois.
```python
>>> codons = [ 'atg' , 'aaa' , 'agg' ]
>>> first_codon = codons[0]
>>> print(first_codon)
atg
```
> Cada valor pode ser salvo em uma nova variável para usar posteriormente.

Os valores podem ser recuperados e usados diretamente.
```python
>>> codons = [ 'atg' , 'aaa' , 'agg' ]
>>> print(codons[0])
atg
>>> print(codons[1])
aaa
>>> print(codons[2])
agg
```
> Os 3 valores são acessados independentemente e impressos imediatamente. Eles não são armazenados em uma variável.


Se você deseja acessar os valores começando pelo fim da lista, use índices negativos.
```python
>>> codons = [ 'atg' , 'aaa' , 'agg' ]
>>> print(codons[-1])
agg
>>> print(codons[-2])
aaa
```
> Usar um índice negativo retornará os valores do final da lista. Por exemplo, -1 é o índice do último valor 'agg'. Esse valor também possui um índice de 2.

#### Alterando valores em uma lista

Valores individuais podem ser alterados usando o valor de índice e o operador de atribuição.

```python
>>> print(codons)
['atg', 'aaa', 'agg']
>>> codons[2] = 'cgc'
>>> print(codons)
['atg', 'aaa', 'cgc']
```
E sobre atribuir um valor para um índice que não existe?
```python
>>> codons[5] = 'aac'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
```
> codon[5] não existe, e quando tentamos atribuir valor para esse índice ocorre um IndexError. Se você deseja adicionar novos elementos no final da lista use `codons.append('taa')` ou `codons.extend(list)`. Veja abaixo mais detalhes.

#### Extraindo um subconjunto de uma lista, ou Recortando

Isso funciona da mesma forma com as listas como com as strings. Isso é porque ambos são sequências, ou cooleções ordenadas de dados com informação posicional. Lembre-se que Python conta as divisões entre os elementos, começando com 0.

| Índice | Valor |
| ----- | ----- |
| 0     | atg   |
| 1     | aaa   |
| 2     | agg   |
| 3     | aac   |
| 4     | cgc   |
| 5     | acg   |

use a syntaxe [start : end : step] para dividir sua sequência python 

```python
>>> codons = [ 'atg' , 'aaa' , 'agg' , 'aac' , 'cgc' , 'acg']
>>> print (codons[1:3])
['aaa', 'agg']
>>> print (codons[3:])
['aac', 'cgc', 'acg']
>>> print (codons[:3])
['atg', 'aaa', 'agg']
>>> print (codons[0:3])
['atg', 'aaa', 'agg']
```
> `codons[1:3]` retorna todo valor começando com o valor de códons[1] até mas não incluindo os códons[3]  
> `codons[3:]` retorna todo valor começando com o valor de códons[3] e todos os valores posteriores.  
> `codons[:3]` retorna todo valor até mas não incluindo códons[3]  
> `codons[0:3]` é o mesmo que `codons[:3]`   


#### Lista de operadores

| Operador | Descrição     | Exemplo                                  |
| -------- | ------------- | ---------------------------------------- |
| `+`      | Concatenação | `[10, 20, 30] + [40, 50, 60]` retorna `[10, 20, 30, 40, 50, 60]` |
| `*`      | Repetição    | `['atg'] * 4` retorna `['atg','atg','atg','atg']` |
| `in`     | Filiação     | `20 in [10, 20, 30]`  retorna `True`     |

#### Lista de funções

| Funções                                 | Descrição                                | Exemplo                                  |
| --------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `len(list)`                             | retorna o comprimento ou o número de valores em uma lista | `len([1,2,3])` retorna `3`               |
| `max(list)`                             | retorna o valor com o maior ASCII (=último no alfabeto ASCII) | `max(['a','A','z'])` retorna `'z'`       |
| `min(list)`                             | retorna o valor com o menor ASCII (=primeiro no alfabeto ASCII) | `min(['a','A','z'])` retorna `'A'`       |
| `list(seq)`                             | converte uma tupla em uma lista          | `list(('a','A','z'))` retorna `['a', 'A', 'z']` |
| `sorted(list, key=None, reverse=False)` | retorna uma lista organizada baseada na chave fornecida | `sorted(['a','A','z'])` retorna `['A', 'a', 'z']` |
| `sorted(list, key=str.lower, reverse=False)`  | `str.lower()` faz com que todos os elementos fiquem minúsculos antes de organizar | `sorted(['a','A','z'],key=str.lower)` retorna `['a', 'A', 'z']` |


#### Lista de métodos

Lembre-se que métodos são utilizados no seguinte formato list.method().   

Para esses exemplos utilize: `nums = [1,2,3]` e `codons = [ 'atg' , 'aaa' , 'agg' ]`

| Métodos                   | Descrição                                | Exemplo                                  |
| ------------------------- | ---------------------------------------- | ---------------------------------------- |
| `list.append(obj)`        | anexa um objeto no final de uma lista  | nums.append(9) ; print(nums) ; retorna [1,2,3,9] |
| `list.count(obj)`         | conta as ocorrências de um objeto em uma lista | nums.count(2) retorna 1                  |
| `list.index(obj)`         | retorna o menor índice em que o objeto fornecido é encontrado | nums.index(2) retorna 1                  |
| `list.pop()`              | remove e retorna o últio valor de uma lista. A lista é agora um elemento mais curta | nums.pop() retorna 3                     |
| `list.insert(index, obj)` | insere um valor ao índice fornecido. Lembre-se de pensar sobre as divisões entre os elementos | nums.insert(0,100) ; print(nums) retorna [100, 1, 2, 3] |
| `list.extend(new_list)`   | anexa `new_list` ao final de `list`  | nums.extend([7, 8]) ; print(nums) retorna [1, 2, 3, 7,8] |
| `list.pop(index)`         | remove e retorna o valor do argumento indexado. A lista é agora um valor mais curta | nums.pop(0) retorna 1                    |
| `list.remove(obj)`        | encontra o menor índice do objeto fornecido e remove ele da lista. A lista é agora um elemento mais curta | codons.remove('aaa') ; print(codons) retorna  [ 'atg' , 'agg' ] |
| `list.reverse()`          | inverte a ordem da lista          | nums.reverse() ; print(nums) retorna [3,2,1] |
| `list.copy()`             | Retorna uma cópia rasa da lista. Rasa vs [Deep](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/) apenas importa em estruturas de data multidimensionais. |                                          |
| `list.sort([func])`       | organiza uma lista utilizando a função fornecida. Não retorna uma lista. A lista foi alterada. Uma organização de lista avançada será coberta assim que escrever suas próprias funções for discutido. | codons.sort() ; print(codons) retorna ['aaa', 'agg', 'atg'] |


Tome cuidado em como você faz uma cópia de sua lista
```python
>>> my_list=['a', 'one', 'two']
>>> copy_list=my_list
>>> copy_list.append('1')
>>> print(my_list)
['a', 'one', 'two', '1']
>>> print(copy_list)
['a', 'one', 'two', '1']
```
> Não foi o que esperava?! Ambas listas foram alteradas porque nós apenas copiamos um ponteiro para a lista original quando escrevemos `copy_list=my_list`. 

Vamos copiar a lista utilizando o método `copy()`.
```python
>>> my_list=['a', 'one', 'two']
>>> copy_list=my_list.copy()
>>> copy_list.append('1')
>>> print(my_list)
['a', 'one', 'two']
```
> Agora sim, nós obtivemos o esperado desta vez!



#### Construindo uma lista um valor por vez

Agora que você já viu a função `append()` nós podemos ir em como construir uma lista valor por vez.

```python
>>> words = []
>>> print(words)
[]
>>> words.append('one')
>>> words.append('two')
>>> print(words)
['one', 'two']
```
> Nós começamos com uma lista vazia chamada 'words'. Nós usamos `append()` para adicionar o valor 'one' depois o valor 'two'. Finalizamos a lista com dois valores. Você pode adicionar uma lista inteira em outra lista com `words.extend(['three','four','five'])`



### Loops

Todas as codificações pelas quais percorremos até então foram executadas linha por linha. Algumas vezes existem blocos de códigos que queremos executar mais do que uma vez. Loops permitem que façamos isso.  



Existem dois tipos de loops:
1. while loop
2. for loop


#### While loop 

O while loop vai continuar a executar um bloco de código enquanto a expressão de teste apresentar `Verdadeiro`. 

#### Sintaxe de Loop While

```python
while expression:
  # estas declarações são executadas sempre que o código entrar em loop 
  statement1
  statement2
  more_statements
# código logo abaixo é executado depois que o while loop existir
rest_of_code_goes_here
more_code
```
> A condição é a expressão. O bloco de código while loop é uma coleção de declarações recuadas/indentadas seguindo a expressão.


Código: 
```python
#!/usr/bin/env python3

contagem = 0
while contagem < 5:
  print("contagem:" , contagem)
  contagem+=1
print("Done") 
```


Saída:
```
$ python while.py
contagem: 0
contagem: 1
contagem: 2
contagem: 3
contagem: 4
Done
```
> A condição while foi verdadeira 5 vezes e o bloco de código while foi executado 5 vezes.
>
> - contagem é igual a 0 quando começamos
> - 0 é menos que 5 então executamos o bloco while
> - contagem é impressa 
> - contagem é incrementada (contagem = count + 1)
> - contagem é agora igual a 1.
> - 1 é menor que 5 então executamos o bloco while pela segunda vez.
> - isso permanece até que a contagem seja 5. 
> - 5 não é menor que 5 então nós saímos do bloco while
> - A primeira linha seguindo a declaração while é executada, "Done" é impresso 

#### Loops infinitos

Um loop infinito ocorre quando um condição while é sempre verdadeira. Aqui está um exemplo de um loop infinito.

```python
#!/usr/bin/env python3

contagem = 0
while contagem < 5:            # isso é normalmente um bug!!
  print("contagem:" , contagem)   # esqueça de incrementar contagem no loop!!
print("Done") 
```

Saída:
```
$ python infinite.py
contagem: 0
contagem: 0
contagem: 0
contagem: 0
contagem: 0
contagem: 0
contagem: 0
contagemcontagem: 0
...
...
```
> O que fez com que a condição seja sempre `Verdadeira`? 
> A condição que incrementa a contagem está faltando, então sempre será inferior a 5. Para impedir o código de imprimir para sempre utilize ctrl+c. Um comportamento como esse é quase sempre devido a um bug no código.

Uma forma melhor de escrever um loop infinito é com `True`. Você precisará incluir algo como `if ...: break` 

```python
#!/usr/bin/env python3
contagem=0
while True:
  print("contagem:",contagem)
  # Provavelmente você precisará adicionar um "if...: break"
  # para poder sair do loop infinito
print('Finished the loop')
```




#### For Loops

Um for loop é um loop que executa o bloco de códigos for para qualquer membro de uma sequência, por exemplo os elementos de uma lista ou as letras de uma string.

#### For Loop Syntaxe

```python
for iterating_variable in sequence:
  statement(s)
```

Um exemplo de sequência é uma lista. Vamos usar um for loop com uma lista de palavras. 

Código:
```python
#!/usr/bin/env python3

words = ['zero','um','dois','três','quatro']
for word in words:
  print(word)
```
> Perceba como eu nomeei minhas variáveis, a lista é plural e a variável interativa é singular

Saída: 
```
python3 list_words.py
zero
um
dois
três
quatro
```

Esse próximo exemplo é utilizando um for loop para interagir em uma string. Lembre-se que uma string é uma sequência como uma lista. Cada caractere possui uma posição. Olhe novamente em "Extraindo uma substring, ou Recortando" na seção [Strings](#strings) para ver outras formas em que strings podem ser tratadas como listas.

Código:
```python
#!/usr/bin/env python3

dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
for nt in dna:
  print(nt)
```

Saída:
```
$ python3 for_string.py
G
T
A
C
C
T
T
...
...
```
> Essa é uma forma fácil de acessar cada caractere em uma string. É especialmente bom para sequências de DNA.


Outro exemplo de interagir em uma lista de variáveis, estes números de tempo.

Código:
```python
#!/usr/bin/env python3

numbers = [0,1,2,3,4]
for num in numbers:
  print(num)
```

Saída:
```
$ python3 list_numbers.py
0
1
2
3
4
```

Python tem uma função chamada `range()` que retornará números que podem ser convertidos em lista. 
```python
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
```

A função `range()` pode ser utilizada em conjunto com um for loop para interar em um alcance de números. Alcance também começa com 0 e pensa sobre os espaços entre os números.  

Código:
```python
#!/usr/bin/env python3

for num in range(5):
  print(num)
```

Saída:
```
$ python list_range.py
0
1
2
3
4
```
> Como pode ver esta é a mesma saída que quando utilizamos a lista `numbers = [0, 1, 2, 3, 4]`
> E esse tem a mesma funcionalidade que um while loop com a condição `count = 0` ; `count < 5`.

Esse é o while loop equivalente

Código:
```python
count = 0
while count < 5:
  print(count)
  count+=1
```

Saída:
```
0
1
2
3
4
```


#### Controle de loop

As declarações de controle de loop permitem alteração no fluxo normal de execução. 

| Declaração de controle | Descrição                             |
| ----------------- | ---------------------------------------- |
| `break`           | Um loop é terminado quando uma declaração break é executada. Todas as linhas de código após o break, mas dentro do bloco de loop não são executadas. Sem mais interações do loop performando |
| `continue`        | Uma única interação de uma loop é terminada quando a declaração continue é executada. A próxima interação vai proceder normalmente. |


#### Controle de loop: Break  

Código:
```python
#!/usr/bin/env python3

count = 0
while count < 5:
  print("count:" , count)
  count+=1
  if count == 3:
    break
print("Done")
```

Saída:
```
$ python break.py
count: 0
count: 1
count: 2
Done
```
> Quando a contagem é igual a 3, a execução do while loop é terminada, no entanto a condição inicial permanece verdadeira (count < 5).

#### Controle de loop: Continue

Código:
```python
#!/usr/bin/env python3

count = 0
while count < 5:
  print("count:" , count)
  count+=1
  if count == 3:
    continue
  print("line after our continue")
print("Done")
```

Saída:
```
$ python continue.py
count: 0
line after our continue
count: 1
line after our continue
count: 2
count: 3
line after our continue
count: 4
line after our continue
Done
```
> Quando a contagem é igual a 3 o continue é executado. Isso faz com que todas as linhas contendo o bloco de loop sejam puladas. "Linha após o nosso continue" não é impresso quando a contagem é igual a 3. O próximo loop é executado normalmente.

#### Iteradores

Um iterável é qualquer tipo de dado que pode ser interado, ou pode ser usado em uma interação. Um interável pode ser transformado em um interador com a função `iter()`. Isso significa que você pode utilizar a função `next()`.

```python
>>> codons = [ 'atg' , 'aaa' , 'agg' ]
>>> codons_iterator=iter(codons)
>>> next(codons_iterator)
'atg'
>>> next(codons_iterator)
'aaa'
>>> next(codons_iterator)
'agg'
>>> next(codons_iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
> Um interador permite que você obtenha o próximo elemento no interador até que não existam mais elementos. Se você quer ir através de cada elemento novamente, você precisará redefinir o interador.

Exemplo de utilização de um interador em um for loop:
```python
codons = [ 'atg' , 'aaa' , 'agg' ]
>>> codons_it = iter(codons)
>>> for codon in codons_it :
...   print( codon )
...
atg
aaa
agg
```
> Isso é bom se você tem uma lista muito larga que você não deseja manter na memória. Um interador permite que você vá através de cada elemento mas sem manter a lista completa na memória. Sem interadores toda a lista permanece na memória.


#### Compreensão de lista

Compreensão de lista é uma forma de fazer uma lista sem digitar cada elemento. Existem muitas formas de usar compreensão de lista para gerar listas. Alguns são relativamente complexos, mas úteis. 

Aqui está um exemplo fácil:
```python
>>> dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG']
>>> lengths = [len(dna) for dna in dna_list]
>>> lengths
[4, 8, 3, 8]
```
Isso é como você pode fazer o mesmo com um for loop:
```python
>>> lengths = []
>>> dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG']
>>> for dna in dna_list:
...   lengths.append(len(dna))
...
>>> lengths
[4, 8, 3, 8]
```

Utilizando condições:

Isso vai apenas retornar o comprimento de um elemento que começa com 'A':
```python
>>> dna_list = ['TAGC', 'ACGTATGC', 'ATG', 'ACGGCTAG']
>>> lengths = [len(dna) for dna in dna_list if dna.startswith('A')]
>>> lengths
[8, 3, 8]
```
> Esse gera a seguinte lista: [8, 3, 8]

Aqui está um exemplo de utilização de operadores matemáticos para gerar uma lista:
```python
>>> two_power_list = [2 ** x for x in range(10)]
>>> two_power_list
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```
> Isso cria uma lista do produto de [2^0 , 2^1, 2^2, 2^3, 2^4, 2^5, 2^6, 2^7, 2^8, 2^9 ]

---

### [Link to Python 4 Problem Set](problemsets/Python_04_problemset.md)



---
## Python 5


### Dictionaries


Dictionaries are another iterable, like a string and list. Unlike strings and lists, dictionaries are not a sequence, or in other words, they are __unordered__ and the position is not important. 

Dictionaries are a collection of key/value pairs. In Python, each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: `{}`

Each key in a dictionary is unique, while values may not be. The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

Data that is appropriate for dictionaries are two pieces of information that naturally go together, like gene name and sequence. 

| Key   | Value                                    |
| ----- | ---------------------------------------- |
| TP53  | GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC |
| BRCA1 | GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA |

#### Creating a Dictionary

```python
genes = { 'TP53' : 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC' , 'BRCA1' : 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' }
```

Breaking up the key/value pairs over multiple lines make them easier to read.
```python
genes = { 
           'TP53' : 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC' , 
           'BRCA1' : 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' 
         }
```

#### Accessing Values in Dictionaries

To retrieve a single value in a dictionary use the value's key in this format `dict[key]`. This will return the value at the specified key. 

```python
>>> genes = { 'TP53' : 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC' , 'BRCA1' : 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' }
>>>
>>> genes['TP53']
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC
```
> The sequence of the gene TP53 is stored as a value of the key 'TP53'. We can access the sequence by using the key in this format dict[key]

The value can be accessed and passed directly to a function or stored in a variable.
```python
>>> print(genes['TP53'])
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC
>>>
>>> seq = genes['TP53']
>>> print(seq)
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC
```


#### Changing Values in a Dictionary

Individual values can be changed by using the key and the assignment operator.

```python
>>> genes = { 'TP53' : 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC' , 'BRCA1' : 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' }
>>>
>>> print(genes)
{'BRCA1': 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA', 'TP53': 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC'}
>>>
>>> genes['TP53'] = 'atg'
>>>
>>> print(genes)
{'BRCA1': 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA', 'TP53': 'atg'}
```
> The contents of the dictionary have changed.

Other assignment operators can also be used to change a value of a dictionary key. 
```python
>>> genes = { 'TP53' : 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC' , 'BRCA1' : 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' }
>>>
>>> genes['TP53'] += 'TAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTG'
>>>
>>> print(genes)
{'BRCA1': 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA', 'TP53': 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTG'}
```
> Here we have used the '+=' concatenation assignment operator. This is equivalent to  `genes['TP53'] = genes['TP53'] + 'TAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTG'`.

#### Accessing Each Dictionary Key/Value

Since a dictionary is an iterable object, we can iterate through its contents.

A for loop can be used to retrieve each key of a dictionary one a time:
```python
>>> for gene in genes:
...   print(gene)
...
TP53
BRCA1
```

Once you have the key you can retrieve the value:
```python
>>> for gene in genes:
...   seq = genes[gene]
...   print(gene, seq[0:10])
...
TP53 GATGGGATTG
BRCA1 GTACCTTGAT
```

#### Building a Dictionary one Key/Value at a Time

Building a dictionary one key/value at a time is akin to what we just saw when we change a key's value.
Normally you won't do this. We'll talk about ways to build a dictionary from a file in a later lecture.

```python
>>> genes = {}
>>> print(genes)
{}
>>> genes['Brca1'] = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
>>> genes['TP53'] = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC'
>>> print(genes)
{'Brca1': 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA', 'TP53': 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC'}
```
> We start by creating an empty dictionary. Then we add each key/value pair using the same syntax as when we change a value.  
> dict[key] = new_value  


#### Checking That Dictionary Keys Exist

Python generates an error (NameError) if you try to access a key that does not exist.  

```python
>>> print(genes['HDAC'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'HDAC' is not defined
```

#### Dictionary Operators

| Operator | Description                              |
| -------- | ---------------------------------------- |
| `in`     | `key in dict` returns True if the key exists in the dictionary |
| `not in` | `key not in dict` returns True if the key does not exist in the dictionary |

Because Python generates a NameError if you try to use a key that doesn't exist in the dictionary, you need to check whether a key exists before trying to use it.

The best way to check whether a key exists is to use `in`

```python
>>> gene = 'TP53'
>>> if gene in genes: 
...     print('found')
... 
found
>>> 
>>> if gene in genes:
...     print(genes[gene])
... 
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC
>>> 
```


#### Building a Dictionary one Key/Value at a Time using a loop

Now we have all the tools to build a dictionary one key/value using a for loop. This is how you will be building dictionaries more often in real life.


Here we are going to count and store nucleotide counts:  

```python
#!/usr/bin/env python3

# create a new empty dictionary
nt_count={}

# loop example from loops lecture
dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
for nt in dna:

  # is this nt in our dictionary?
  if nt in nt_count:
    # if it is, lets increment our count
    previous_count = nt_count[nt]
    new_count = previous_count + 1
    nt_count[nt] = new_count
  else:
    # if not, lets add this nt to our dictionary and make count = 1
    nt_count[nt] = 1;

print(nt_count)
```
> {'G': 20, 'T': 21, 'A': 13, 'C': 16}

What is another way we could increment our count?

```python
nt_count={}

dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
for nt in dna:
  if nt in nt_count:
    nt_count[nt] += 1
  else:
    nt_count[nt] = 1;

print(nt_count)
```
> remember that `count=count+1` is the same as `count+=1`



#### Sorting Dictionary Keys

If you want to print the contents of a dictionary, you should sort the keys then iterate over the keys with a for loop. Why do you want to sort the keys?

```python
for gene_key in sorted(genes): # python allows you to use this shortcut in a for loop
                               # you don't have to write genes.keys() in a for loop
                               # to iterate over the keys
  print(gene_key, '=>' , genes[gene_key])
```
> This will print keys in the same order every time you run your script. Dictionaries are unordered, so without sorting, you'll get a different order every time you run the script, which could be confusing.


#### Dictionary Functions

| Function         | Description                              |
| ---------------- | ---------------------------------------- |
| `len(dict)`      | returns the total number of key/value pairs |
| `str(dict)`      | returns a string representation of the dictionary |
| `type(variable)` | Returns the type or class of the variable passed to the function. If the variable is dictionary, then it would return a dictionary type. |

These functions work on several other data types too!

#### Dictionary Methods

| Method                                 | Description                              |
| -------------------------------------- | ---------------------------------------- |
| `dict.clear()`                         | Removes all elements of dictionary dict  |
| `dict.copy()`                          | Returns a shallow copy of dictionary dict. [Shallow vs. deep](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/) copying only matters in multidimensional data structures. |
| `dict.fromkeys(seq,value)`             | Create a new dictionary with keys from seq (Python sequence type) and values set to value. |
| `dict.items()`                         | Returns a list of (key, value) tuple pairs |
| `dict.pop(key)`                        | Removes the key:value pair and returns the value |
| `dict.keys()`                          | Returns list of keys                     |
| `dict.get(key, default = None)`        | get value from dict[key], use default if not present |
| `dict.setdefault(key, default = None)` | Similar to get(), but will set dict[key] = default if key is not already in dict |
| `dict.update(dict2)`                   | Adds dictionary dict2's key-values pairs to dict |
| `dict.values()`                        | Returns list of dictionary dict's values |


### Sets


A set is another Python data type. It is essentially a dictionary with keys but no values.

- A set is unordered 
- A set is a collection of data with no duplicate elements. 
- Common uses include looking for differences and eliminating duplicates in data sets. 

Curly braces `{}` or the `set()` function can be used to create sets. 

> Note: to create an empty set you have to use `set()`, not `{}` the latter creates an empty dictionary.

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                     
{'orange', 'banana', 'pear', 'apple'}
```
> Look, duplicates have been removed

Test to see if an value is in the set
```python
>>> 'orange' in basket                 
True
>>> 'crabgrass' in basket
False
```
> The in operator works the same with sets as it does with lists and dictionaries


Union, intersection, difference and symmetric difference can be done with sets
```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                 
{'a', 'r', 'b', 'c', 'd'}
```
> Sets contain unique elements, therefore, even if duplicate elements are provided they will be removed.

#### Set Operators

**Difference**

The difference between two sets are the elements that are unique to the set to the left of the `-` operator, with duplicates removed.

![Set Difference](images/set_difference.png)

```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a - b                             
{'r', 'd', 'b'}
```
> This results the letters that are in a but not in b

**Union**

The union between two sets is a sequence of the all the elements of the first and second sets combined, with duplicates removed.

![Set Union](images/set_union.png)

```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a | b                          
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
```
> This returns letters that are in a or b both

**Intersection**

The intersection between two sets is a sequence of the elements which are in both sets, with duplicates removed.

![Set Intersection](images/set_intersection.png)

```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a & b                            
{'a', 'c'}
```
> This returns letters that are in both a and b


**Symmetric Difference**

The symmetric difference is the elements that are only in the first set plus the elements that are only in the second set, with duplicates removed.

![Set Symmetric Difference](images/set_symmetric_difference.png)

```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a ^ b                             
{'r', 'd', 'b', 'm', 'z', 'l'}
```
> This returns the letters that are in a or b but not in both (also known as exclusive or)

#### Set Functions

| Function      | Description                              |
| ------------- | ---------------------------------------- |
| `all()`       | returns True if all elements of the set are true (or if the set is empty). |
| `any()`       | returns True if any element of the set is true. If the set is empty, return False. |
| `enumerate()` | returns an enumerate object. It contains the index and value of all the items of set as a pair. |
| `len()`       | returns the number of items in the set.  |
| `max()`       | returns the largest item in the set.     |
| `min()`       | returns the smallest item in the set.    |
| `sorted()`    | returns a new sorted list from elements in the set (does not alter the original set). |
| `sum()`       | returns the sum of all elements in the set. |



#### Set Methods

| Method                                  | Description                              |
| --------------------------------------- | ---------------------------------------- |
| `set.add(new)`                          | adds a new element                       |
| `set.clear()`                           | remove all elements                      |
| `set.copy()`                            | returns a shallow copy of a set          |
| `set.difference(set2)`                  | returns the difference of set and set2   |
| `set.difference_update(set2)`           | removes all elements of another set from this set |
| `set.discard(element)`                  | removes an element from set if it is found in set. (Do nothing if the element is not in set) |
| `set.intersection(sets)`                | return the intersection of set and the other provided sets |
| `set.intersection_update(sets)`         | updates set with the intersection of set and the other provided sets |
| `set.isdisjoint(set2)`                  | returns True if set and set2 have no intersection |
| `set.issubset(set2)`                    | returns True if set2 contains set        |
| `set.issuperset(set2)`                  | returns True if set contains set2        |
| `set.pop()`                             | removes and returns an arbitrary element of set. |
| `set.remove(element)`                   | removes element from a set.              |
| `set.symmetric_difference(set2)`        | returns the symmetric difference of set and set2 |
| `set.symmetric_difference_update(set2)` | updates set with the symmetric difference of set and set2 |
| `set.union(sets)`                       | returns the union of set and the other provided sets |
| `set.update(set2)`                      | update set with the union of set and set2 |





#### Build a dictionary of NT counts using a set and loops

Let us put a twist on our nt count script. Let's use a set to find all the unique nts, then use the string `count()` method to count the nucleotide instead if incrementing the count as we did earlier.

Code:  


```python
#!/usr/bin/env python3

# create a new empty dictionary
nt_count = {}

# get a set of unique characters in our DNA string

dna = 'GTACCNTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
unique = set(dna)

print('unique nt: ', unique) ## {'C', 'A', 'G', 'T', 'N'}

# iterate through each unique nucleotide
for nt in unique:
  # count the number of this unique nt in dna
  count = dna.count(nt)

  # add our count to our dict
  nt_count[nt] = count


print('nt count:', nt_count)

```


Output:  


```
unique nt:  {'N', 'C', 'T', 'G', 'A'}
nt count: {'G': 20, 'T': 21, 'A': 13, 'C': 16, 'N': 1}

```
> We have the count for all NTs even ones we might not expect.

---

### [Link to Python 5 Problem Set](problemsets/Python_05_problemset.md)



---
## Python 6


### I/O and Files


I/O stands for input/output. The in and out refer to getting data into and out of your script. It might be a little surprising at first, but writing to the screen, reading from the keyboard, reading from a file, and writing to a file are all examples of I/O.


#### Writing to the Screen

You should be well versed in writing to the screen. We have been using the `print()` function to do this.  


```python
>>> print ("Hello, PFB2019!")
Hello, PFB2019!
```
> Remember this example from one of our first lessons?

#### Reading input from the keyboard

This is something new. There is a function which prints a message to the screen and waits for input from the keyboard. This input can be stored in a variable. It always starts as a string. Convert to an int or float if you want a number. When you are done entering text, press the enter key to end the input. A newline character is not included in the input.

```python 
>>> user_input = input("Type Something Now: ")
Type Something Now: Hi
>>> print(user_input)
Hi
>>> type(user_input)
<class 'str'>
```
#### Reading from a File

Most of the data we will be dealing with will be contained in files. 

The first thing to do with a file is open it. We can do this with the `open()` function. The `open()` function takes the file name and access mode as arguments and returns a file object.

The most common access modes are read (r) and write (w).

#### Open a File

```python
>>> file_object = open("seq.nt.txt","r")
```
> 'file_object' is a name of a variable. This can be anything, but make it a helpful name that describes what kind of file you are opening.


#### Reading the contents of a file

Now that we have opened a file and created a file object we can do things with it, like read it. Let's read all the contents at once.  

Let's go to the command line and  `cat` the contents of the file to see what's in it first.

```bash
$ cat seq.nt.txt
ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAG
ACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG
$ 
```

Note the new lines. Now, lets print the contents to the screen with Python. We will use `read()` to read the entire contents of the file into a variable. 
```python
>>> file = open("seq.nt.txt","r")
>>> contents = file.read()
>>> print(contents)  # note newline characters are part of the file!
ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAG
ACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG

>>> file.close()
```
> The complete contents can be retrieved with the `read()` method. Notice the newlines are maintained when `contents` is printed to the screen. `print()` adds another new line when it is finished printing.
> It is good practice to close your file. Use the `close()` method. 


Here's another way to read data in from a file. A `for` loop can be used to iterate through the file one line at a time.
```python
#!/usr/bin/env python3

file = open("seq.nt.txt","r")
for line in file: # Python magic: reads in a line from file
  print(line)
```

Output:
```
$ python3 file_for.py
ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAG

ACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG

```
> Notice the blank line at after each line we print. `print()` adds a newline and we have a newline at the end of each line in our file. Use `rstrip()` method to remove the newline from each line.

Let's use `rstrip()` method to remove the newline from our file input.
```python
$ cat file_for_rstrip.py
#!/usr/bin/env python3

file_object = open("seq.nt.txt","r")
for line in file_object:
  line = line.rstrip()
  print(line)
```
> `rstrip()` without any parameters returns a string with whitespace removed from the end.

Output:
```
$ python3 file_for_rstrip.py
ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAG
ACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG
```

> Where do the newlines in the above output come from?

#### Opening a file with `with open() as fh:`

Many people add this, because it closes the file for you automatically. Good programming practice. Your code will clean up as it runs. For more advanced coding, `with ... as ...` saves limited resources like filehandles and database connections. For now, we just need to know that the `with ... as ...:` does the same as `fh = open(...) ... fh.close()`. So here's what the adapted code looks like

```python
#!/usr/bin/env python3

with open("seq.nt.txt","r") as file_object: #cleans up after exiting 
                                            # the 'with' block
  for line in file_object:
    line = line.rstrip()
  	print(line)
#file gets closed for you here.
```

#### Writing to a File

Writing to a file just required opening a file for writing then using the `write()` method.  

The `write()` method is like the `print()` function. The biggest difference is that it writes to your file object instead of the screen. Unlike `print()`, it does not add a newline by default.  `write()` takes a single string argument. 

Let's write a few lines to a file named "writing.txt".  
```python
#!/usr/bin/env python3

fo = open("writing.txt" , "w")
fo.write("One line.\n")
fo.write("2nd line.\n")
fo.write("3rd line" + " has extra text\n")
some_var = 5
fo.write("4th line has " + str(some_var) + " words\n")
fo.close()
print("Wrote to file 'writing.txt'") # it's nice to tell the user you wrote a file
```

Output:
```
$ python3 file_write.py
Wrote to file 'writing.txt'
$ cat writing.txt
One line.
2nd line.
3rd line has extra text
4th line has 5 words
```
Now, let's get crazy! Lets read from one file a line at a time. Do something to each line and write the results to a new file.
```python
#!/usr/bin/env python3

total_nts = 0
# open two file objects, one for reading, one for writing
with open("seq.nt.txt","r") as seq_read, open("nt.counts.txt","w") as seq_write:
  for line in seq_read:
    line = line.rstrip()
    nt_count = len(line)
    total_nts += nt_count
    seq_write.write(str(nt_count) + "\n")

  seq_write.write("Total: " + str(total_nts) +"\n")

print("Wrote 'nt.counts.txt'")
```

Output:
```
$ python3 file_read_write.py
$ cat nt.counts.txt
71
71
Total: 142
```
> The file we are reading from is named, "seq.nt.txt"  
> The file we are writing to is named, "nt.counts.txt"  
> We read each line, calculate the length of each line, and print the length  
> We also create a variable to keep track of the total nt count  
> At the end, we print out the total count of nts  
> Finally, we close each of the files  



#### Building a Dictionary from a File

This is a very common task. It will use a loop, file I/O, and a dictionary.

Assume we have a file called "sequence_data.txt" that contains tab-delimited gene names and sequences that looks something like this

```
TP53    GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC
BRCA1   GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA
```

How can we read this whole file in to a dictionary? 

```python
#!/usr/bin/env python3

genes = {}
with open("sequence_data.txt","r") as seq_read:
  for line in seq_read:
    line = line.rstrip()
    gene_id,seq = line.split() #split on whitespace
    genes[gene_id] = seq
print(genes)
```

Output:
```
{'TP53': 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC', 'BRCA1': 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'}
```

---



### [Link to Python 6 Problem Set](problemsets/Python_06_problemset.md)



---
## Python 7

### Regular Expressions

Regular Expressions is a language for pattern matching. Many different computer languages incorporate regular expressions, as do some unix commands, like grep and sed. So far we have seen a few functions for finding exact matches in strings, but this is not always sufficient.  

Functions that utilize regular expressions allow for non-exact pattern matching.  

These specialized functions are not included in the core of Python. We need to import them by typing
`import re`
at the top of your script

```python 
#!/usr/bin/env python3

import re
```

First we will go over a few examples then go into the mechanics in more detail.  

Let's start simple and find an exact match for the EcoRI restriction site in a string.
```python
>>> dna = 'ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG'
>>> if re.search(r"GAATTC",dna):
...   print("Found an EcoRI site!")
...
Found an EcoRI site!
>>>
```
> Since we can search for control characters like a tab (\t), it is good to get in the habit of using the raw string function 
> `r`
>  when defining patterns.

> Here we used the `search()` function with two arguments, 1) our pattern and 2) the string we want to search. 


Let's find out what is returned by the `search()` function. 
```python
>>> dna = 'ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG'
>>> found=re.search(r"GAATTC",dna)
>>> print(found)
<_sre.SRE_Match object; span=(70, 76), match='GAATTC'>
```
>Information about the first match is returned


How about a non-exact match. Let's search for a methylation site that has to match the following criteria:  
- G or A 
- followed by C
- followed by one of anything or nothing
- followed by a G 

This could match any of these:  
- GCAG  
- GCTG  
- GCGG  
- GCCG  
- GCG  
- ACAG  
- ACTG  
- ACGG  
- ACCG  
- ACG  

We could test for each of these, or use regular expressions. This is exactly what regular expressions can do for us.  
```python
>>> dna = 'ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG'
>>> found=re.search(r"[GA]C.?G",dna)
>>> print(found)
<_sre.SRE_Match object; span=(7, 10), match='ACG'>
```
> Here you can see in the returned information that ACG starts at string postion 7 (nt 8). 
>
> The first position following the end of the match is at string postion 10 (nt 11).

What about other potential matches in our DNA string? We can use `findall()` function to find all matches.

```python
>>> dna = 'ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG'
>>> found=re.findall(r"[GA]C.?G",dna)
>>> print(found)
['ACG', 'GCTG', 'ACTG', 'ACCG', 'ACAG', 'ACCG', 'ACAG']
```
> `findall()` returns a list of all the pieces of the string that match the regex.

A quick count of all the matching sites can be done by counting the length of the returned list.

```python
>>> len (re.findall(r"[GA]C.?G",dna))
7
```

> There are 7 methylation sites.
>
> Here we have another example of nesting. 
>
> We call the `findall()` function, searching for all the matches of a methylation site. 
>
> This function returns a list, the list is past to the `len()` function, which in turn returns the number of elements in the list.


__Let' Try It__  
![try it](images/Try-It-Now.jpg)

1. If you want to find just the first occurrence of a pattern, what method do you use?

2. If you want to find all the occurrences of a pattern, what method do you use?

3. What operator have we seen that will report if an exact match is in a sequence (string, list, etc)?

4. What string method have we seen that will count the number of occurrences of an exact match in a string?


Let's talk a bit more about all the new characters we see in the pattern.

The pattern in made up of atoms.  Each atom represents **ONE** character.

#### Individual Characters

| Atom                               | Description                              |
| ---------------------------------- | ---------------------------------------- |
| a-z, A-Z, 0-9 and some punctuation | These are ordinary characters that match themselves |
| "."                                | The dot, or period. This matches any single character except for the newline. |


#### Character Classes

A group of characters that are allowed to be matched one time. There are a few predefined classes, which are symbols that means a series of characters.

| Atom  | Description                              |
| ----- | ---------------------------------------- |
| `[ ]` | A bracketed list of characters, like `[GA]`. This indicates a single character can match any character in the bracketed list. |
| `\d`  | Digits. Also can be written `[0-9]`      |
| `\D`  | Not digits. Also can be written`[^0-9]`  |
| `\w`  | Word character. Also can be written `[A-Za-z0-9_]` Note underscore is part of this class |
| `\W`  | Not a word character, or `[^A-Za-z0-9_]` |
| `\s`  | White space character. Also can be written `[ \r\t\n]`. Note the space character after the first `[` |
| `\S`  | Not whitespace. Also `[^ \r\\t\n]`       |
| `[^]` |a carat within a bracketed list of characters indicates anything but the characters that follows |

#### Anchors

A pattern can be anchored to a region in the string:

| Atom | Description                              |
| ---- | ---------------------------------------- |
| `^`  | Matches the beginning of the string      |
| `$`  | Matches the end of the string            |
| `\b` | Matches a word boundary between `\w` and `\W` |

Examples:

```
g..t
```
> matches "gaat", "goat", and "gotta get a goat" (twice)


<br><br> 
```
g[gatc][gatc]t
```
> matches "gaat", "gttt", "gatt", and "gotta get an agatt" (once) 


<br><br> 
```
\d\d\d-\d\d\d\d
```
> matches 867-5309, and 5867-5309 but not 8-67-5309.

<br><br> 

```
^\d\d\d-\d\d\d\d
```
>  matches 867-5309 and 867-53091 but not 5867-5309.
<br><br> 
```
^\d\d\d-\d\d\d\d$
```
> only matche 3 digits followed by a dash followed by 4 digits, not extra characters anywhere are allowed
<br><br> 



#### Quantifiers

Quantifiers quantify how many atoms are to be found. By default an atom matches only once. This behaviour can be modified following an atom with a quantifier.

| Quantifier | Description                              |
| ---------- | ---------------------------------------- |
| `?`        | atom matches zero or exactly once        |
| `*`        | atom matches zero or more times          |
| `+`        | atom matches one or more times           |
| `{3}`      | atom matches exactly 3 times             |
| `{2,4}`    | atom matches between 2 and 4 times, inclusive |
| `{4,}`     | atom matches at least 4 times            |

Examples:  

```
goa?t
```
> matches "goat" and "got".  Also any text that contains these words.

```
g.+t
```
>  matches "goat", "goot", and "grant", among others.

```
g.*t
```
>  matches "gt", "goat", "goot", and "grant", among others.

```
^\d{3}-\d{4}$
```
>  matches US telephone numbers (no extra text allowed).

__Let' Try It__  
![try it](images/Try-It-Now.jpg)

1. What would be a pattern to recognize an email address?
2. What would be a pattern to recognize the ID portion of a sequence record in a FASTA file?


#### Variables and Patterns

Variables can be used to store patterns.  

```python
>>> pattern = r"[GA]C.?G"
>>> len (re.findall(pattern,dna))
7
```
> In this example, we stored our methylation pattern in the variable named 'pattern' and used it as the first argument to `findall`.


#### Either Or

A pipe '|' can be used to indicated that either the pattern before or after the '|' can match. Enclose the two options in parenthesis.

```
big bad (wolf|sheep)
```
> This pattern must match a string that contains:
>
> - "big" followed by a space followed by 
> - "bad" followed by 
> - a space followed by 
> - *either* "wolf" or "sheep"
>
>  This would match:
>
> - "big bad wolf"
> - "big bad sheep"

__Let' Try It__  
![try it](images/Try-It-Now.jpg)

1. What would a pattern to match 'ATG' followed by a C or a T look like?


#### Subpatterns

Subpatterns, or parts of the pattern enclosed in parenthesis can be extracted and stored for later use. 
```
Who's afraid of the big bad w(.+)f
```
> This pattern has only one subpattern (.+)

You can combine parenthesis and quantifiers to quantify entire subpatterns.

```
Who's afraid of the big (bad )?wolf\?
```
> This matches:
>
> - "Who's afraid of the big bad wolf?"
> - As well as "Who's afraid of the big wolf?".
>
> The 'bad ' is optional, it can be present 0 or 1 times in our string.
>
> This also shows how to literally match special characters. Use a '\\' in to escape them.

__Let' Try It__  
![try it](images/Try-It-Now.jpg)

1. What pattern could you use to capture the ID in a sequence record of a FASTA file in a subpattern.

Example FASTA sequence record.

```
  >ID Optional Descrption
  SEQUENCE
  SEQUENCE
  SEQUENCE 
```





#### Using Subpatterns Inside the Regular Expression Match

This is helpful when you want to find a subpattern and then match the contents again. They can be used within the function call and used after the function call.

__Subpatterns within the function call__

Once a subpattern matches, you can refer to it within the same regular expression.  The first subpattern becomes \\1, the second \\2, the third \\3, and so on.

```
Who's afraid of the big bad w(.)\1f
```
> This would match:
>
> -  "Who's afraid of the big bad woof"
> -  "Who's afraid of the big bad weef"
> -  "Who's afraid of the big bad waaf"  
>
> But Not:
>
> -  "Who's afraid of the big bad wolf"
> -  "Who's afraid of the big bad wife" 


In a similar vein, 
```
\b(\w+)s love \1 food\b
```
> This pattern will match 
>
> - "dogs love dog food"  
> - But not "dogs love monkey food".  
>
> We were able to use the subpattern within the regular expression by using `\1`
>
>  If there were more subpatterns they would be `\2`, `\3` , `\4`, etc



#### Using Subpatterns Outside the Regular Expression

Subpatterns can be retrieved after the `search()` function call, or outside the regular expression, by using the `group()` method. This is a method and it belongs to the object that is returned by the `search()` function.

The subpatterns are retrieved by a number. This will be the same number that could be used within the regular expression, i.e.,

  - `\1` within the subpattern can be used outside with `search_found_obj.group(1)`
  - `\2` within the subpattern can be used outside with `search_found_obj.group(2)`
  - `\3` within the subpattern can be used outside with `search_found_obj.group(3)`  
  - and so on


Example:
```python
>>> dna = 'ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG'
>>> found=re.search( r"(.{50})TATTAT(.{25})"  , dna )
>>> upstream = found.group(1)
>>> print(upstream)
TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA
>>> downstream = found.group(2)
>>  print(downstream)
CCGGTTTCCAAAGACAGTCTTCTAA
```
> 1. This pattern will recognize a consensus transcription start site (TATTAT) 
> 2. And store the 50 base pairs upstream of the site 
> 3. And the 25 base pairs downstream of the site


If you want to find the upstream and downstream sequence of ALL 'TATTAT' sites, use the `findall()` function.
```python
>>> dna="ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG"
>>> found = re.findall( r"(.{50})TATTAT(.{25})"  , dna )
>>> print(found)
[('TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA', 'CCGGTTTCCAAAGACAGTCTTCTAA'), ('TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA', 'CCGGTTTCCAAAGACAGTCTTCTAA')]
```
> The subpatterns are stored in tuples within a list. More about this type of data structure later.

Another option for retrieving the upstream and downstream subpatterns is to put the `findall()` in a for loop

```python
>>> dna="ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG"
>>> for (upstream, downstream) in re.findall( r"(.{50})TATTAT(.{25})"  , dna ):
...   print("upstream:" , upstream)
...   print("downstream:" , downstream)
...
upstream: TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA
downstream: CCGGTTTCCAAAGACAGTCTTCTAA
upstream: TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA
downstream: CCGGTTTCCAAAGACAGTCTTCTAA
```
> 1. This code executes the `findall()` function once 
> 2. The subpatterns are returned in a tuple 
> 3. The subpatterns are stored in the variables upstream and downstream  
> 4. The for block of code is executed  
> 5. The `findall()` searches again  
> 6. A match is found 
> 7.  New subpatterns are returned and stored in the variables upstream and downstream
> 8. The for block of code gets executed again 
> 9.  The `findall()` searches again, but no match is found  
> 10. The for loop ends  



Another way to get this done is with an iterator, use the `finditer()` function in a for loop. This allows you to not store all the matches in memory. `finditer()` also allows you to retrieve the postion of the match.

```python
>>> dna="ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG"
>>> for match in re.finditer(r"(.{50})TATTAT(.{25})"  , dna):
...   print("upstream:" , match.group(1))
...   print("downstream:" , match.group(2))
...
upstream: TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA
downstream: CCGGTTTCCAAAGACAGTCTTCTAA
upstream: TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA
downstream: CCGGTTTCCAAAGACAGTCTTCTAA
```
> 1. This code executes `finditer()` function once. 
> 2. The match object is returned. A match object will have all the information about the match.
> 3.  In the for block we call the `group()` method on the first match object returned
> 4. We print out the first and second subpattern using the `group()` method
> 5. The `finditer()` function is executed a second time and a match is found
> 6. The second match object is returned
> 7.  The second subpatterns are retrieved from the match object using the `group()` method 
> 8. The `finditer()` function is executed again, but no matches found, so the loop ends  


#### Get position of the subpattern with `finditer()`

The match object contains information about the match that can be retrieved with match methods like `start()` and `end()`

```python
#!/usr/bin/env python3

import re

dna="ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG"

for found in re.finditer(r"(.{50})TATTAT(.{25})"  , dna):
  whole    = found.group(0)
  up       = found.group(1)
  down     = found.group(2)
  up_start = found.start(1) + 1   # need to convert from 0 to 1 notation 
  up_end   = found.end(1) 
  dn_start = found.start(2) + 1
  dn_end   = found.end(2)

  print( whole , up , up_start, up_end , down , dn_start , dn_end , sep="\t" )
```
> we can use these match object methods `group()`, `start()`, `end()` to get the string, start position, and end position of each subpattern. 

```
$ python3 re.finditer.pos.py
TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAA	TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA	98	148	CCGGTTTCCAAAGACAGTCTTCTAA	154	179
TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAA	TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA	320	370	CCGGTTTCCAAAGACAGTCTTCTAA	376	401
```



**FYI:** `match()` function is another regular expression function that looks for patterns. It is similar to search but it only looks at the beginning of the string for the pattern while `search()` looks in the entire string. Usually `finditer()` , `search()`, and `findall()` will be more useful.


#### Subpatterns and Greediness

By default, regular expressions are "greedy".  They try to match as much as they can. Use the quantifier '?' to make the match not greedy. The not greedy match is called 'lazy' 

```python
>>> str = 'The fox ate my box of doughnuts'
>>> found = re.search(r"(f.+x)",str)
>>> print(found.group(1))
fox ate my box
```
> The pattern f.+x does not match what you might expect, it matches past 'fox' all the way out to 'fox ate my box'.  The '.+' id is greedy As many characters as possible are found that are between the 'f' and the 'x'. 


Let's make this match lazy by using '?'
```python
>>> found = re.search(r"(f.+?x)",str)
>>> print(found.group(1))
fox
```
> The match is now lazy and will only match 'fox'


#### Practical Example: Codons

Extracting codons from a string of DNA can be accomplished by using a subpattern in a `findall()` function. Remember the `findall()` function will return a list of the matches.  

```python
>>> dna = 'GTTGCCTGAAATGGCGGAACCTTGAA'
>>> codons = re.findall(r"(.{3})",dna)
>>> print(codons)
['GTT', 'GCC', 'TGA', 'AAT', 'GGC', 'GGA', 'ACC', 'TTG']
```

Or you can use a for loop to do something to each match.
```python
>>> for codon in re.findall(r"(.{3})",dna):
...   print(codon)
...
GTT
GCC
TGA
AAT
GGC
GGA
ACC
TTG
>>>
```
> `finditer()` would also work in this for loop.  
>  Each codon can be accessed by using the `group()` method.

  

#### Truth and Regular Expression Matches

The `search()`, `match()`, `findall()`, and `finditer()` can be used in conditional tests. If a match is not found an empty list or 'None' is returned. These are both False.

```python
>>> found=re.search( r"(.{50})TATTATZ(.{25})"  , dna )
>>> if found:
...    print("found it")
... else:
...    print("not found")
...
not found
>>> print(found)
None
```
> None is False so the else block is executed and "not found" is printed


Nest it!
```python
>>> 
>>> if re.search( r"(.{50})TATTATZ(.{25})"  , dna ):
...    print("found it")
... else:
...    print("not found")
...
not found
>>> print(found)
None
```



#### Using Regular expressions in substitutions 

Earlier we went over how to find an **exact pattern** and replace it using the `replace()` method. To find a pattern, or inexact match, and make a replacement the regular expression `sub()` function is used. This function takes the pattern, the replacement, the string to be searched, the number of times to do the replacement, and flags.

```python
>>> str = "Who's afraid of the big bad wolf?"
>>> re.sub(r'w.+f' , 'goat', str)
"Who's afraid of the big bad goat?"
>>> print(str)
Who's afraid of the big bad wolf?
```
> The `sub()` function returns "Who's afraid of the big bad goat?"  
> The value of variable str has not been altered  
> The new string can be stored in a new variable for later use.

Let's save the new string that is returned in a variable
```python
>>> str = "He had a wife."
>>> new_str = re.sub(r'w.+f' , 'goat', str)
>>> print(new_str)
He had a goate.
>>> print(str)
He had a wife.
```
> The characters between 'w' and 'f' have been replaced with 'goat'.  
> The new string is saved in new_str  



#### Using subpatterns in the replacement

Sometimes you want to find a pattern and use it in the replacement. 
```python
>>> str = "Who's afraid of the big bad wolf?"
>>> new_str = re.sub(r"(\w+) (\w+) wolf" , r"\2 \1 wolf" , str)
>>> print(new_str)
Who's afraid of the bad big wolf?
```
> We found two words before 'wolf' and swapped the order.
> \\2 refers to the second subpattern
> \\1 refers to the first subpattern

__Let' Try It__  
![try it](images/Try-It-Now.jpg)

1. How would you use regular expressions to find all occurrences of 'ATG' and replace with '-M-' in this sequence 'GCAGAGGTGATGGACTCCGTAATGGCCAAATGACACGT'? 

#### Regular Expression Option Modifiers

| Modifier               | Description                              |
| ---------------------- | ---------------------------------------- |
| `re.I` `re.IGNORECASE` | Performs case-insensitive matching.      |
| `re.M` `re.MULTILINE`  | Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string). |
| `re.S` `re.DOTALL`     | Makes a period (dot) match any character, including a newline. |
| `re.U`                 | Interprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B. |
| `re.X` `VERBOSE`       | This flag allows you to write regular expressions that look nicer and are more readable by allowing you to visually separate logical sections of the pattern and add comments. Whitespace within the pattern is ignored, except when in a character class or when preceded by an unescaped backslash. When a line contains a # that is not in a character class and is not preceded by an unescaped backslash, all characters from the leftmost such # through the end of the line are ignored. |

```python
>>> dna = "atgcgtaatggc"
>>> re.search(r"ATG",dna)
>>>
>>> re.search(r"ATG",dna , re.I)
<_sre.SRE_Match object; span=(0, 3), match='atg'>
>>>
```
> We can make our search case insensitive by using the `re.I` or `re.IGNORECASE` flag.


You can use more than one flag by concatenating them with `|`.  `re.search(r"ATG",dna , re.I|re.M)`


### Helpful Regex tools

There are a lot of online tools for actually seeing what is happening in your regular expression. Search for `Python Regular Expression Tester` 

 - [regex101](https://regex101.com/)  
 - [pyregex](http://www.pyregex.com/)
 - [pythex](https://pythex.org/)

---


### [Link to Python 7 Problem Set](problemsets/Python_07_problemset.md)


## Python 8




### Data Structures


Sometimes a _simple_ list or dictionary just doesn't do what you want. Sometimes you need to organize data in a more _complex_ way.  You can nest any data type inside any other type. This lets you build multidimensional data tables easily.


#### List of lists

List of lists, often called a matrix are important for organizing and accessing data


Here's a way to make a 3 x 3 table of values.

```python
>>> M = [[1,2,3], [4,5,6],[7,8,9]]
>>> M[1] # second row (starts with index 0)
[4,5,6]
>>>M[1][2] # second row, third element
6
```

Here's a way to store sequence alignment data:

Four sequences aligned:
```
AT-TG
AATAG
T-TTG
AA-TA
```

The alignment in a list of lists.
```python
aln = [
['A', 'T', '-', 'T', 'G'],
['A', 'A', 'T', 'A', 'G'],
['T', '-', 'T', 'T', 'G'],
['A', 'A', '-', 'T', 'A']
]
```

Get the full length of one sequence:
```python
>>> seq = aln[2]
>>> seq
['T', '-', 'T', 'T', 'G']
```
> Use the outermost index to access each sequence

Retrieve the nucleotide at a particular position in a sequence.
```python
>>> nt = aln[2][3]
>>> nt
'T'
```
> Use the outermost index to access the sequence of interest and the inner most index to access the position


Get every nucleotide in a single column:
```python
>>> col = [seq[3] for seq in aln]
>>> col
['T', 'A', 'T', 'T']
```
> Retrieve each sequence from the aln list then the 4th column for each sequence. 


#### Lists of dictionaries

You can nest dictionaries in lists as well:

```python
>>> records = [
... {'seq' : 'actgctagt', 'accession' : 'ABC123', 'genetic_code' : 1},
... {'seq' : 'ttaggttta', 'accession' : 'XYZ456', 'genetic_code' : 1},
... {'seq' : 'cgcgatcgt', 'accession' : 'HIJ789', 'genetic_code' : 5}
... ]
>>> records[0]['seq']
'actgctagt'
>>> records[0]['accession']
'ABC123'
>>> records[0]['genetic_code']
1
```
> Here you can retrieve the accession of one record at a time by using a combination of the outer index and the key 'accession'

#### Dictionaries of lists

And, if you haven't guessed, you can nest lists in dictionaries

Here is a dictionary of kmers. The key is the kmer and its values is a list of postions
```python
>>> kmers = {'ggaa': [4, 10], 'aatt': [0, 6, 12], 'gaat': [5, 11], 'tgga':
... [3, 9], 'attg': [1, 7, 13], 'ttgg': [2, 8]}
>>> kmers
{'tgga': [3, 9], 'ttgg': [2, 8], 'aatt': [0, 6, 12], 'attg': [1, 7, 13], 'ggaa': [4, 10], 'gaat': [5, 11]}
>>>
>>> kmers['ggaa']
[4, 10]
>>> len(kmers['ggaa'])
2
```
> Here we can get a list of the positions of a kmer by using the kmer as the key. We can also do things to the returned list, like determining its length. The length will be the total count of this kmers.

You can also use the `get()` method to retrieve records.
```python
>>> kmers['ggaa']
[4, 10]
>>> kmers.get('ggaa')
[4, 10]
```
> These two statements returns the same results, but if the key does not exist you will get nothing and not an error.

#### Dictionaries of dictionaries

Dictionaries of dictionaries is my favorite!! You can do so many useful things with this data structure. Here we are storing a gene name and some different types of information about that gene, such as its, sequence, length, description, nucleotide composition and length.

```python
>>> genes = {
... 'gene1' : {
...     'seq' : "TATGCC",
...    'desc' : 'something',
...     'len' : 6,
... 'nt_comp' : {
...             'A' : 1,
...             'T' : 2,
...             'G' : 1,
...             'C' : 2,
...            }
...   },
...
... 'gene2' : {
...     'seq' : "CAAATG",
...    'desc' : 'something',
...     'len' : 6,
... 'nt_comp' : {
...           'A' : 3,
...           'T' : 1,
...           'G' : 1,
...           'C' : 1,
...           }
...       }
... }
>>> genes
{'gene1': {'nt_comp': {'C': 2, 'G': 1, 'A': 1, 'T': 2}, 'desc': 'something', 'len': 6, 'seq': 'TATGCC'}, 'gene2': {'nt_comp': {'C': 1, 'G': 1, 'A': 3, 'T': 1}, 'desc': 'something', 'len': 6, 'seq': 'CAAATG'}}
>>> genes['gene2']['nt_comp']
{'C': 1, 'G': 1, 'A': 3, 'T': 1}
```
> Here we store a gene name as the outermost key, with a second level of keys for qualities of the gene, like sequence, length, nucleotide composition. We can retrieve a quality by using the gene name and quality in conjunction.

To retrieve just one gene's nucleotide composition
```python
>>> genes['gene1']['nt_comp']
{'C': 2, 'G': 1, 'A': 1, 'T': 2}
```

Alter one gene's nucleotide count with `=` assignment operator:
```python
>>> genes['gene1']['nt_comp']
{'C': 2, 'G': 1, 'A': 1, 'T': 2}
>>>
>>> genes['gene1']['nt_comp']['T']=6
>>> genes['gene1']['nt_comp']
{'C': 2, 'G': 1, 'A': 1, 'T': 6}
```

Alter one gene's nucleotide count with `+=` assignment operator:
```python
>>> genes['gene1']['nt_comp']
{'C': 2, 'G': 1, 'A': 1, 'T': 6}
>>>
>>> genes['gene1']['nt_comp']['A']+=1
>>>
>>> genes['gene1']['nt_comp']
{'C': 2, 'G': 1, 'A': 2, 'T': 6}
>>>
>>>
```

To retrieve the A composition of every gene use a for loop.
```python
>>> for gene in sorted(genes):
...   A_comp = genes[gene]['nt_comp']['A']
...   print(gene+":","As=", A_comp)
...
gene1: As= 2
gene2: As= 3
```



#### Building Complex Datastructures

Below is an example of building a list with a mixed collection of value types. Remember that all elements inside a list or dictionary should be the same type. In other words, the values in a list should all be lists or dictonaries or scalar values. This allows you to loop over the data structure.

The dictionary which is a list value has a key that has a dictionary as a value.

```
[{'gene1' : {'sequence' : [1, 2, 3], [4, 5, 6], [7,8,9]]
```

Just spaced differently:
```
[
   [1, 2, 3], 
   [4, 5, 6], 
   {
       'key': 'value',
       'key2': 
            {
                'something_new': 'Yay'
            }
    }
 ]
```

Building this data structure in the interpreter:

```python
>>> new_data = []
>>> new_data
[]
>>> new_data.append([1,2,3])
>>> new_data
[[1, 2, 3]]
>>> new_data[0]
[1, 2, 3]
>>> new_data.append([4,5,6])
>>> new_data
[[1, 2, 3], [4, 5, 6]]
>>> new_data[1]
[4, 5, 6]
>>> new_data[1][2]
6
>>> new_data.append({})
>>> new_data
[[1, 2, 3], [4, 5, 6], {}]
>>> new_data[2]['key']='value'
>>> new_data
[[1, 2, 3], [4, 5, 6], {'key': 'value'}]
>>> new_data[2]['key2']={}
>>> new_data
[[1, 2, 3], [4, 5, 6], {'key2': {}, 'key': 'value'}]
>>> new_data[2]['key2']['something_new']='Yay'
>>> new_data
[[1, 2, 3], [4, 5, 6], {'key2': {'something_new': 'Yay'}, 'key': 'value'}]
>>>
```

Same example in a script file: [Building Complex Datastructures](scripts/building_datastructures.py)

__Course T-shirt Organization and Counting__

We have a spreadsheet of everyone's style, size, color. We want to know how many of each unique combination of style-size-color we need to order

[shirts.txt](files/shirts.txt) 
```
mens	small	heather seafoam
womens	medium	Heather Purple
womens	medium	berry
mens 	medium 	heather coral silk
womens	Small	Kiwi
Mens	large	Graphite Heather
mens	large	sport grey
mens	small	Carolina Blue
```

We want something like this:

```
womens	small	antique heliconia	2
womens	xs	heather orange	1
womens	medium	kiwi	2
womens	medium	royal heather	1
```

[shirts.py](scripts/shirts.py)
```python
#!/usr/bin/env python3

shirts = {}
with open("shirts.txt","r") as file_object:
  for line in file_object:
    line = line.rstrip()
    [style, size, color] = line.split("\t")
    style = style.lower()
    size = size.lower()
    color = color.lower()
    if style not in shirts:
        shirts[style] = {}
    if size not in shirts[style]:
        shirts[style][size] = {}
    if color not in shirts[style][size]:
        shirts[style][size][color] = 0

    shirts[style][size][color] += 1

for style in shirts:
  for size in shirts[style]:
    for color in shirts[style][size]:
      count = shirts[style][size][color]
      print(style,size,color,count,sep="\t")

```

Output:
```
sro$ python3 shirts.py
mens	small	heather maroon	1
mens	small	royal blue	1
mens	small	olive	1
mens	large	graphite heather	1
womens	medium	heather purple	3
womens	medium	berry	2
womens	medium	royal heather	1
womens	medium	kiwi	2
...
```

This is what the data structure we just built looks likes
```python
{
  'mens': 
    {
      'small': 
        {
           'heather seafoam': 1, 
           'carolina blue': 1, 
           'cornsilk': 1, 
           'dark heather': 1, 
           'heather maroon': 1, 
           'royal blue': 1, 
           'olive': 1
        }, 
      'large': 
        {
          'graphite heather': 1, 
          'sport grey': 1, 
          'heather purple': 1, 
          'heather coral silk': 1, 
          'heather irish': 1, 
          'heather royal': 1, 
          'carolina blue': 1
        }, 
      'medium': 
        {
          'heather coral silk': 1,
          'heather royal': 2, 
          'heather galapagos blue': 1, 
          'heather forest': 1, 
          'gold': 1, 
          'heather military green': 1, 
          'dark heather': 1, 
          'carolina blue': 1, 
          'iris': 1
        }, 
      'xs': 
        {
          'white': 1
        }, 
      'xl': 
        {
          'heather cardinal': 1, 
          'indigo blue': 1
        }
          }, 
  'womens': 
    {
      'medium': 
        {
          'heather purple': 3, 
          'berry': 2, 
          'royal heather': 1, 
          'kiwi': 2, 
          'carolina blue': 1
        }, 
      'small': 
        {
          'kiwi': 1, 
          'berry': 1, 
          'antique heliconia': 2
        }, 
      'large': 
        {
          'kiwi': 1
        }, 
      'xs': 
        {
          'heather orange': 1
        }
    },
  'child': 
    {
      '4t': 
        {
          'green': 2
        }, 
      '3t': 
        {
          'pink': 1
        }, 
      '2t': 
        {
          'orange': 1
        }, 
      '6t': 
        {
          'pink': 1
        }
    }
}

```



There are also specific data table and frame handling libraries like [Pandas](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html).

Here is a [intro](https://pandas.pydata.org/pandas-docs/stable/dsintro.html) to data structures in Panda.

Here is a very nice [interactive tutorial](https://www.learnpython.org/en/Pandas_Basics)

---
### [Link to Python 8 Problem Set](problemsets/Python_08_problemset.md)

## Python 9
### Exceptions


There are a few different types of errors when coding. Syntax errors, logic errors, and exceptions. You have probably encountered all three. Syntax and logic errors are issues you need to deal with while coding. An exception is a special type of error that can be informative and used to write code to respond to this type of error. This is especially relavent when dealing with user input. What if they don't give you any, or it is the wrong kind of input. We want our code to be able to detect these types of errors and respond accordingly.

```python
#!/usr/bin/env python3

import sys
file = sys.argv[1]

print("User provided file:" , file)
```
> This code takes user provided input and prints it

Run it.
```
$ python scripts/exceptions.py test.txt
User provided file: test.txt
```

What happens if the user does not provide any input and we try to print it? 
```bash
$ python scripts/exceptions.py
Traceback (most recent call last):
  File "scripts/exceptions.py", line 4, in <module>
    file = sys.argv[1]
IndexError: list index out of range 
```
> We get an **IndexError** exception, which is raised when an index is not found in a sequence.


We have already seen quite a few exceptions throughout the lecture notes, here are some:   
  - ValueError: math domain error
  - AttributeError: 'list' object has no attribute 'rstrip'
  - SyntaxError: EOL while scanning string literal
  - NameError: name 'GGTCTAC' is not defined
  - SyntaxError: Missing parentheses in call to 'print'
  - AttributeError: 'int' object has no attribute 'lower'
  - IndexError: list assignment index out of range
  - NameError: name 'HDAC' is not defined

[Link to Python Documentation of built in types of exceptions](https://www.tutorialspoint.com/python3/python_exceptions.htm)

We can use the exception to our advantage to help the people who are running the script. We can use a try/except condition like an if/else block to look for exceptions and to execute specific code if we **do not have** an exception and do something different if we **do have** an exception.

```python
#!/usr/bin/env python3
import sys

file = ''
try:
  file = sys.argv[1]
  print("User provided file:" , file)
except:
  print("Please provide a file name")
```
> We need to "try" to get a user provided argument. If we are successful then we can print it out. If we try and fail, we execute the code in the except portion of our try/except and print that we need a file name. 

Let's run it WITH user input
```bash
$ python3 scripts/exceptions_try.py test.txt
User provided file: test.txt
```
> It runs as expected

Let's run it WITHOUT user input
```bash
$ python scripts/exceptions_try.py
Please provide a file name
```
> Yeah, the user is informed that they need to provide a file name to the script


What if the user provides input but it is not a valid file or the path is incorrect? Or if you want to check to see if the user provided input as well as if it can open the input.  


We can add multiple exception tests, like if/elif block. Each except statement can specify what kind of exception it is waiting to recieve. If that kind of exception occures, that block of code will be executed.
```python
import sys

file = ''
try:
  file = sys.argv[1]
  print("User provided file name:" , file)
  FASTA = open(file, "r")
  for line in FASTA:
    line = line.rstrip()
    print(line)
except IndexError: 
  print("Please provide a file name")
except IOError:    
  print("Can't find file:" , file)
```
> Here we test for an IndexError: Raised when an index is not found in a sequence.
> The IndexError occurs when we try to access a list element that does not exists. 
> And we test for a IOError: Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.   
> The IOError happens when we try to access a file that does not exist.

Let's run it with a file that does not exist.
```
$ python scripts/exceptions_try_files.py test.txt
User provided file name: test.txt
Can't find file: test.txt
```
> This informs the user that they did provide input but that the file listed can not be found.

Let's run it with no input
```bash
$ python scripts/exceptions_try_files.py
Please provide a file name
```
> This informs the user that they need to provide a file.

#### try/except/else/finally

Lets summarize what we have covered and add on `else` and `finally`.

```
try:
  # try block is executed until an exception is raised
except _ExceptionType_:
  # if there is an exception of "ExceptionType" this block will be executed
  # there can be more than one except block, just like an elif
except:
  # if there are any exceptions that are not of "ExceptionType" this except block will be executed
else: 
  # the else block is executed after the try block has been completed, which means there were no exceptions raised
finally:
  # the finally block is executed if exceptions are or are not raised (no matter what happens)
```

#### Getting more information about an exception

Some exceptions can be thrown for multiple reasons, for example, ErrorIO will occur if the file does not exist as well as if you don't have permissions to read it. We can get more information by viewing the contents of our Exception Object. Yes, an exception is an object too! The system errors get stored in the exception object.  To access the object use `as` and supply a variable name, like 'ex'

```python
file = ''
try:
  file = sys.argv[1]
  print("User provided file name:" , file)
  FASTA = open(file, "r")
  for line in FASTA:
    line = line.rstrip()
    print(line)
except IndexError:
  print("Please provide a file name")
except IOError as ex:
  print("Can't find file:" , file , ': ' , ex.strerror  ) 
```
> Here we added `except IOError as ex` and now we can get the 'strerror' message from ex.

Run it.
```bash
$ python scripts/exceptions_try_files_as.py  test.txt
User provided file name: test.txt
Can't find file: test.txt :  No such file or directory
```
> Now we know that this file name or path is not valid


#### Raising an Exception

We can call or raise exceptions too!! This is accomplished by using a `raise` statement. 

1. First, create a new Exception Object, i.e., `ValueError()`
2. Use the Exception Object in a Raise statment `raise ValueError('your message')`


Let's raise an exception if the file name does not end in 'fa'
```python
import sys

file = ''
try:
  file = sys.argv[1]
  print("User provided file name:" , file)
  if not file.endswith('.fa'):
    raise ValueError("Not a FASTA file")
  FASTA = open(file, "r")
  for line in FASTA:
    print(line)
except IndexError:
  print("Please provide a file name")
except IOError as ex:
  print("Can't find file:" , file , ': ' , ex.strerror  )
```
> Here we raise a known exception, 'ValueError', if the file does not end with (uses `endswith()` method). 

Let's run it.
``` bash
$ python scripts/exceptions_try_files_raise.py test.txt
User provided file name: test.txt
Traceback (most recent call last):
  File "scripts/exceptions_try_files_raise.py", line 10, in <module>
    raise ValueError("Not a FASTA file")
ValueError: Not a FASTA file
```
> Our exception get's raised, now lets do something with it.

```python
import sys

file = ''
try:
  file = sys.argv[1]
  print("User provided file name:" , file)
  if not file.endswith('.fa'):
    raise ValueError("Not a FASTA file")
  FASTA = open(file, "r")
  for line in FASTA:
    print(line)
except IndexError:
  print("Please provide a file name")
except ValueError:
  print("File needs to be a FASTA file and end with .fa")
except IOError as ex:
  print("Can't find file:" , file , ': ' , ex.strerror  )
```
> Here we created an exception to catch any ValueError

Let's Run it.
```bash
$ python scripts/exceptions_try_files_raise_value.py test.txt
User provided file name: test.txt
File needs to be a FASTA file and end with .fa
```
> We get a great error message now.

But what if there is another ValueError, how can we tell if has anything to do with the FASTA file extension or not? Answer: the message will be different.

#### Creating Custom Exceptions

We can create our own custom exception. We will need to create a new class of exception. Below is the syntax to do this.

```python
import sys

class NotFASTAError(Exception):
  pass


file = ''
try:
  file = sys.argv[1]
  print("User provided file name:" , file)
  if not file.endswith('.fa'):
    raise NotFASTAError("Not a FASTA file")
  FASTA = open(file, "r")
  for line in FASTA:
    print(line)
except IndexError:
  print("Please provide a file name")
except NotFASTAError:
  print("File needs to be a FASTA file and end with .fa")
except IOError as ex:
  print("Can't find file:" , file , ': ' , ex.strerror  )
```
> Here we created a new class of exception called 'NotFASTAError'. Then we raised this new exception.

Let's Run it.
```bash
$ python scripts/exceptions_try_files_raise_try.py test.txt
User provided file name: test.txt
File needs to be a FASTA file and end with .fa
```
> Our new class of exception, NotFASTAError, works just like the built in exceptions.



---

### [Link to Python 9 Problem Set](problemsets/Python_09_problemset.md)



---
## Python 10

### Functions

Functions consist of several lines of code that do something useful and that you want to run more than once. There are built-in functions in python. You can also write your own. You also give your function a name so you can refer to it in your code. This avoids copying and pasting the same code to many places in your script and makes your code easier to read.

Let's see some examples.

Python has built-in functions

```python
>>> print('Hello world!')
Hello world!
>>> len('AGGCT')
5
```

You can define your own functions with  `def` Let's write a function that calculates the GC content. Let's define this as the fraction of nucleotides in a DNA sequence that are G or C. It can vary from 0 to 1.

First we can look at the code that makes the calculation, then we can convert those lines of code into a function.

Code to find GC content:
```python
dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCT'
c_count = dna.count('C')  # count is a string method
g_count = dna.count('G')
dna_len = len(dna) # len is a function
gc_content = (c_count + g_count) / dna_len # fraction from 0 to 1
print(gc_content)
```
#### Defining a Function that calculates GC Content

We use `def` do define our own function. It is followed by the name of the function (`gc_content`) and parameters it will take in parentheses. A colon is the last character on the `def` line. The parameter variables will be available for your code inside the function to use.

```python
def gc_content(dna):   # give our function a name and parameter 'dna'
   c_count = dna.count('C')
   g_count = dna.count('G')
   dna_len = len(dna)
   gc_content = (c_count + g_count) / dna_len
   return gc_content # return the value to the code that called this function
```
> Here is a custom function that you can use like a built in Python function

#### Using your function to calculate GC content

This is just like any other python function. You write the name of the function with any variables you want to pass to the function in parentheses. In the example below the contents of `dna_string` get passed into `gc_content()`. Inside the function this data is passed to the variable `dna`.

```python
dna_string = "GTACCTTGATTTCGTATTCTGAGAGGCTGCT"
print(gc_content(dna_string))
```
This code will print 0.45161290322580644 to the screen. You can save this value in a variable to use later in your code like this

```python
dna_gc = gc_content('GTACCTTGATTTCGTATTCTGAGAGGCTGCT')
```

As you can see we can write a nice clear line of python to call this function and because the function has a name that describes what it does it's easy to understand how the code works. Don't give your functions names like this `def my_function(a):`!

How could you convert the GC fraction to % GC. Use `format()`.

```python
dna_string = "GTACCTTGATTTCGTATTCTGAGAGGCTGCT"
dna_gc = gc_content(dna_string)
pc_gc = '{:.2%}'.format(dna_gc)
print('This sequence is' , pc_gc , 'GC')
```

Here's the output

```python
This sequence is 45.16% GC
```

#### The details

1. You define a function with `def`.  You need to define a function before you can call it.
2. The function must have a name. This name should clearly describe what the function does. Here is our example `gc_content`
3. You can pass variables to functions but you don't have to. In the definition line, you place variables your function needs inside parentheses like this `(dna)`. This variable only exists inside the function.
4. The first line of the function must end with a `:` so the complete function definition line looks like this ```def gc_content(dna):```
5. The next lines of code, the function body, need to be indented. This code comprises what the function does.
6. You can return a value as the last line of the function, but this is not required. This line `return gc_content` at the end of our function definition passes the value of gc_content back to the code that called the function in your main script.


#### Naming Arguments

You can name your argument variables anything you want, but the name should describe the data contained. The name needs to be consistent within your function. 

#### Keyword Arguments

Arguments can be named and these names can be used when the function is called. This name is called a 'keyword' 

```python
>>> dna_string = "GTACCTTGATTTCGTATTCTGAGAGGCTGCT"
>>> print(gc_content(dna_string))
0.45161290322580644
>>> print(gc_content(dna=dna_string)
0.45161290322580644

```
> The keyword must be the same as the defined function argument. If a function has multiple arguments, using the keyword allows for calling the function with the arguments in any order.

#### Default Values for Arguments

As defined above, our function is expecting an argument (`dna`) in the definition. You get an error if you call the function without any parameters.

```python
>>> gc_content()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: gc_content() missing 1 required positional argument: 'dna'

```

You can define default values for arguments when you define your function.

```python
def gc_content(dna='N'):   # give our function a name and parameter 'dna'
   c_count = dna.count('C')
   g_count = dna.count('G')
   dna_len = len(dna)
   gc_content = (c_count + g_count) / dna_len
   return gc_content # return the value to the code that called this function

```
> If you call the function with no arguments, the default will be used. In this case a default is pretty useless, and the function will return '0' if called without providing a DNA sequence.

#### Lambda expressions

Lambda expressions can be used to define simple (one-line) functions. There are some uses for lambda which we won't go into here. We are showing it to you because sometimes you will come across it.

Here is a one line custom function, like the functions we have already talked about:
```python
def get_first_codon(dna):
  return dna[0:3]

print(get_first_codon('ATGTTT'))
```
> This will print `ATG`

Here is the same function written as a lambda
```python
get_first_codon = lambda dna : dna[0:3]
print(get_first_codon('ATGTTT'))
```
> This also prints `ATG`. lambdas can only contain one line and there is no `return` statement.

List comprehensions can often be used instead of lambdas and may be easier to read. You can read more about `lambda`, particularly in relation to `map` which will perform an operation on a list, but generally  a `for` loop is easier to read.

### Scope

Almost all python variables are global. This means they are available everywhere in your code.  Remember that python blocks are defined as code at the same level of indentation.

```python
#!/usr/bin/env python3
print('Before if block')
x = 100
print('x=',x)
if True:  # this if condition will always be True 
  # we want to make sure the block gets executed
  # so we can show you what happens
  print('Inside if block')
  x = 30
  y = 10
  print("x=", x)
  print("y=", y)

print('After if block')
print("x=", x)
print("y=", y)


```

Let's Run it:
```bash
$ python3 scripts/scope.py
Before if block
x= 100
Inside if block
x= 30
y= 10
After if block
x= 30
y= 10

```

The most important exception to variables being global is that variables that are defined in **functions** are **local** i.e. they only exist inside their function. Inside a function, global variables are visible, but it's better to pass variables to a function as arguments

```python
def show_n():
  print(n)
n = 5
show_n()
```

The output is this `5` as you would expect, but the example below is better programming practice. Why? We'll see a little later.

```python3
def show_n(n):
  print(n)
n = 5
show_n(n)
```



#### Local Variables

Variables inside functions are local and therefore can only been accessed from within the function block. This applies to arguments as well as variables defined inside a function.


```python
#!/usr/bin/end python3

def set_local_x_to_five(x):
  print('Inside def')
  x = 5 # local to set_local_x_to_five()
  y=5   # also local
  print("x =",x)
  print("y = ",y)

print('After def')
x = 100 # global x
y = 100 # global
print('x=',x)
print('y=',y)

set_local_x_to_five(500)
print('After function call')
print('x=',x)
print('y=',y)

```
> Here we have added a function `set_local_x_to_five` with an argument named 'x'. This variable exists only within the function where is replaces any variable with the same name outside the `def`. Inside the `def` we also initialize a variable `y` that also replaces any global `y` within the `def`

Let's run it:
```bash
$ python3 scope_w_function.py
After def
x= 100
y= 100
Inside def
x = 5
y =  5
After function call
x= 100
y= 100



```
> There is a global variable, `x` = 100, but when the function is called, it makes a new local variable, also called `x` with value = 5. This variable disappears after the function finishes and we go back to using the global variable `x` = 100. Same for `y`

#### Global

You can make a local variable global with the statement `global`. Now a variable you use in a function is the same variable as in the rest of the code. It is best not to define any variables as global until you know you need to because you might modify the contents of a variable without meaning to.

Here is an example use of `global`. 

```python
#!/usr/bin/env python3

def set_global_variable():
  global greeting  # make greeting global
  greeting = "I say hello"


greeting = 'Good morning'
print('Before function call')
print('greeting =',greeting)

#make call to function
set_global_variable()
print('After function call')
print('greeting =',greeting)

```
Let's look at the output


```bash
$ python3 scripts/scope_global.py
Before function call
greeting = Good morning
After function call
greeting = I say hello

```
> Note that the function has changed the value of the global variable. You might not want to do this. 

By creating new local variables inside function definitions, python stops variables with the same name from over-writing each other by mistake.

### Modules

Python comes with some core functions and methods. There are many useful modules that you will want to use. `import` is the statement for telling your script you want to use code in a module. As we've already seen with regular expresions, you can bring in code that handles regular expressions with `import re`

#### Getting information about modules with `pydoc`

How do you find out information about a module? Python has help pages built into the command line, like `man` we met earlier in the unix lecture. Online information may be more up to date. Search at https://docs.python.org/3.6/. But if you don't have internet access, you can always use `pydoc`.
To find out about the `re` module, type `pydoc re` on the command line. The last line in the output tells you where the python module is actually installed.

```bash
% pydoc re
Help on module re:

NAME
    re - Support for regular expressions (RE).

MODULE REFERENCE
    https://docs.python.org/3.6/library/re
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides regular expression matching operations similar to
    those found in Perl.  It supports both 8-bit and Unicode strings; both
    the pattern and the strings being processed can contain null bytes and
    characters outside the US ASCII range.
    
    Regular expressions can contain both special and ordinary characters.
    Most ordinary characters, like "A", "a", or "0", are the simplest
    regular expressions; they simply match themselves.  You can
    concatenate ordinary characters, so last matches the string 'last'.
...
FILE
    /anaconda3/lib/python3.6/glob.py

```

Here are some of the most common and useful modules, along with their methods and objects. It's a lightning tour. 

#### os.path

`os.path` has common utilities for working file paths (filenames and directories). A path is either a relative or absolute list of directories (often ending with a filename) that tells you where to find a file or directory.

| function               | description                              |
| ---------------------- | ---------------------------------------- |
| os.path.basename(path) | what's the last element of the path? Note `/home/tmp/` returns `''`, rather than `tmp` |
| os.path.dirname(path)  | what's the directory the file is in?     |
| os.path.exists(path)   | does the path exist?                     |
| os.path.getsize(path)  | returns path (file) size in bytes or error |
| os.path.isfile(path)   | does the path point to a file?           |
| os.path.isdir(path)    | does the path point to a directory?      |
| os.path.splitext(path) | splits before and after the file extension (e.g. '.txt') |



#### os.system

Replaced by subprocess.



#### subprocess

This is the current module for running command lines from python scripts


```python
import subprocess
subprocess.run(["ls","-l"])  # same as running ls -l on the command line
```

more complex than `os.system()`. You need to specify where input and output go. Let's look at this in some more detail. 

##### Capturing output from a shell pipeline

Let's say we want to find all the files that have user amanda (or in the filename)

`ls -l | grep amanda`

becomes this 'shortcut' which will capture the output of the two unix commands in the variable `output`

```python
import subprocess
output = subprocess.check_output('ls -l | grep amanda', shell = True)
```

This is better than alternatives with `subprocess.run()`. This is equivalent to the unix backtick quoted string.

`output` contains a bytes object (more or less a string of ASCII character encodings)

```python
b'-rw-r--r--  1 amanda  staff       161952 Oct  2 18:03 test.subreads.fa\n-rw-r--r--  1 amanda  staff          126 Oct  2 13:23 test.txt\n'
```

You can covert by decoding the bytes object into a string 

```python3
>>>output.decode('utf-8')
'-rw-r--r--  1 amanda  staff       161952 Oct  2 18:03 test.subreads.fa\n-rw-r--r--  1 amanda  staff          126 Oct  2 13:23 test.txt\n'
```

##### Capturing output the long way (for a single command)


Let's assume that `ls -l` generates some output something like this

```
total 112
-rw-r--r--  1 amanda  staff           69 Jun 14 17:41 data.cfg
-rw-r--r--  1 amanda  staff       161952 Oct  2 18:03 test.subreads.fa
-rw-r--r--  1 amanda  staff          126 Oct  2 13:23 test.txt
```

How do we run `ls -l` in Python and capture the output (stdout)?

```python3
import subprocess
rtn = subprocess.run(['ls','-l'], stdout=subprocess.PIPE )  # specify you want to capture STDOUT
bytes = rtn.stdout
stdout = bytes.decode('utf-8')
# something like
lines = stdout.splitlines()
```

`lines` now contains elements from every line of the `ls -l` output, including the header line, which is not a file

```python3
>>> lines[0]
'total 112'
>>> lines[1]
'-rw-r--r--  1 amanda  staff     69 Jun 14 17:41 data.cfg'
```



##### Check the exit status of a command

To run a command and check the exit status (really to check the exit status was ok or zero), use 

```python
oops = subprocess.check_call(['ls', '-l'])
# or, simpler...
oops = subprocess.check_call('ls -l', shell=True)
```

##### Run a command with that redirects stdout to a file using python subprocess

You can't write `ls -l > listing.txt`  to redirect stdout in the subprocess method, so use this instead

```python
 tmp_file = 'listing.txt'
 with open(tmp_file,'w') as ofh:
     oops = subprocess.check_call(['ls', '-l'], stdout=ofh )
```



#### sys


A couple of useful variables for beginners. Many more advanced system parameters and settings that we are not covering here.

| function | description                          |
| -------- | ------------------------------------ |
| sys.argv | list of command line parameters      |
| sys.path | where Python should look for modules |



#### re

See notes on regular expressions

#### collections

Better lists etc.

`from collections import deque`

#### copy
`copy.copy()`

and 

`copy.deepcopy()`

[Link to more info for more on deep vs shallow copying](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/)

#### math


| function            | description |
| ------------------- | ----------- |
| math.exp()          | e**x        |
| math.log2()         | log base 2  |
| math.log10()        | log base 10 |
| math.sqrt()         | square root |
| math.sin()          | sine        |
| math.pi(), math.e() | constants   |
| etc                 |             |

see also numpy

#### random
Random numbers generated by computers are not truly random, so python calls these pseudo-random. 

| example                 | description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| random.seed(1)          | set starting seed for random sequence to 1 to enable reproducibility |
| random.randrange(9)     | integer between 0 and 8                                      |
| random.randint(1,5)     | integer between 1 and 5                                      |
| random.random()         | float between 0 and 1                                        |
| random.uniform(1,2)     | float between 1 and 2                                        |
| random.choice(my_genes) | return a random element of the sequence                      |

To get a random index from an element of `list` use `i=random.randrange(len(list))`

#### statistics

Typical statistical quantities

| example                         | description                              |
| ------------------------------- | ---------------------------------------- |
| statistics.mean([1,2,3,4,5])    | mean or average                          |
| statistics.median([ 2,3,4,5])   | median = 3.5                             |
| statistics.stdev([1,2,3,4,5])   | standard deviation of sample (square root of sample variance) |
| statistics.pstdev([1,2,3,4,5])q | estimate of population standard deviation |

#### glob

Does unix-like wildcard file path expansion.

```python
>>> import glob
>>> glob.glob('pdfs/*.pdf')
['pdfs/python1.pdf', 'pdfs/python2.pdf', 'pdfs/python3.pdf', 'pdfs/python4.pdf', 'pdfs/python6.pdf', 'pdfs/python8.pdf', 'pdfs/unix1.pdf', 'pdfs/unix2.pdf']
>>> fasta_files = glob.glob('sequences/*.fa')
>>> 
```


#### argparse

Great (if quite complicated) tool for parsing command line arguments and automatically generating help messages for scripts (very handy!). Here's a simple script that explains a little of what it does.

```python
#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser(description="A test program that reads in some number of lines from an input file. The output can be screen or an output file")
# we want the first argument to be the filename
parser.add_argument("file", help="path to input fasta filename")
# second argument will be line number
# default type is string, need to specify if expecting an int
parser.add_argument("lines", type=int, help ="how many lines to print")
# optional outfile argument specified with -o or --out
parser.add_argument("-o","--outfile", help = "optional: supply output filename, otherwise write to screen", dest = 'out')
args = parser.parse_args()
# arguments appear in args
filename = args.file
lines = args.lines
if args.out:
  print("writing output to", args.out)
```

With this module, -h help comes for free. --outfile type arguments are optional unless you write 'required=True' like this

```
parser.add_argument('-f', "-fasta", required=True, help='Output fasta filename', dest='outfile')

```





### Many more modules that do many things

time, HTML, XML, email, CGI, sockets, audio, GUIs with Tk, debugging, testing, unix utils

Also, non-core: BioPython for bioinformatics, Numpy for mathematics, statistics, pandas for data, scikitlearn for machine learning.

---

### [Link to Python 10 Problem Set](problemsets/Python_10_problemset.md)

---


## Python 11

### Classes

The advantages of writing classes and writing functions are very similar. 

When we write functions we group core Python functions and methods to create a unique collection statements that occur in a specific order. 

These new functions make our code easier to read and to write, especially if you will use the function many times.

A conceptual difference between a function and a class is that a function usually does one thing, while a class will do many related things to help solve a problem.

What is a class really, what does it do? A class doesn't really do anything except for setting a list of rules for creating a new custom object. Every time you use the class you are creating an instance of a type of object.   

#### You have been using classes to create objects

You have already been using classes to create objects. Here we are using the `open` function to create two instances of a file object. One instance holds information about a FASTA file while the other holds information about a GFF file.
```python
fa_input = open("somedata.fa")
gff_input = open("somedata.gff")
```


#### attributes and methods

Classes create objects, these objects will have attributes and methods associated with them.



__methods__

Methods are functions which belong to objects of a particular class.



__attributes__

Attributes are variables that are associated with an object of a particular class.

 

#### Creating a Class

Defining a class is straightforward. 

The first step is to decide what attributes and what methods it will have. 



__Create a DNARecord Class.__

When we create a class, we are really setting up a series of rules that a DNARecord object must follow.

DNARecord Rules:
1. DNARecord must have a sequence [attribute]
2. DNARecord must have a name [attribute]
3. DNARecord must have an organism [attribute]
4. DNARecord will be able to calculate AT content [method]
5. DNARecord will be able to calculate the reverse complement [method]



Here is the first, but not final draft of our class. We will go through each section of this code below:

```python
class DNARecord(object):
  # define class attributes
  sequence = 'ACGTAGCTGACGATC' 
  gene_name = 'ABC1'
  species_name = 'Drosophila melanogaster'
  
  # define methods
  def reverse_complement(self): 
    replacement1 = self.sequence.replace('A', 't') 
    replacement2 = replacement1.replace('T', 'a')
    replacement3 = replacement2.replace('C', 'g')
    replacement4 = replacement3.replace('G', 'c') 
    reverse_comp = replacement4[::-1]
    return reverse_comp.upper()
  
  def get_AT(self): 
    length = len(self.sequence)
    a_count = self.sequence.count('A') 
    t_count = self.sequence.count('T') 
    at_content = (a_count + t_count) / length 
    return at_content

## create a new DNARecord Object
dna_rec_obj = DNARecord() 

## Use New DNARecord object
print('Created a record for ' + dna_rec_obj.gene_name + ' from ' + dna_rec_obj.species_name) 
print('AT is ' + str(dna_rec_obj.get_AT()))
print('complement is ' + dna_rec_obj.reverse_complement())
```

Now let's go through each section: 

We start with the keyword `class`, followed by the name of our class `DNARecord` with
the name of the base class in parentheses `object`.  

```python
class DNARecord(object):
```



Then we define class attributes. These are variables with data that belongs to the class, and therefore to any object that is created using this class

```python
  # define class attributes
  sequence = 'ACGTAGCTGACGATC' 
  gene_name = 'ABC1'
  species_name = 'Drosophila melanogaster' 
```



Next, we define our class methods:

```python
  # define methods
  def reverse_complement(self): 
    replacement1 = self.sequence.replace('A', 't') 
    replacement2 = replacement1.replace('T', 'a')
    replacement3 = replacement2.replace('C', 'g')
    replacement4 = replacement3.replace('G', 'c') 
    reverse_comp = replacement4[::-1]
    return reverse_comp.upper()
  
  def get_AT(self): 
    length = len(self.sequence)
    a_count = self.sequence.count('A') 
    t_count = self.sequence.count('T') 
    at_content = (a_count + t_count) / length 
    return at_content
```

The methods are using an argument called `self`, i.e., `length = len(self.sequence)`. This is a special variable that you use inside a class. With it you can access all the data that is contained inside the object when it is created.

Use `self.attribute` format to retrieve the value of variables created within the class. Here we use `self.sequence` to retrieve the information stored in our attribute named `sequence`.

```python
replacement1 = self.sequence.replace('A', 't') 
```

#### Creating a DNARecord Object


The above class is a set of rules that need to be followed when creating a new DNARecord object. 
Now let's create a new DNARecord object:

```python
  dna_rec_obj = DNARecord() 
```

`dna_rec_obj` is our new DNARecord object that was creating using the rules we put into place in the class definition.


#### Retrieving attribute values

Now that a new DNARecord object has been created, and assigned to the variable `dna_rec_obj`, we can access its attributes using the following format, `object.attribute_name` 

To get the gene name of the object we created, we simply write `dna_rec_obj.gene_name`. 

This is possible because within our class definition we create a `gene_name` variable.

Let's try it:

```python
>>> dna_rec_obj.gene_name
'ABC1'
>>> dna_rec_obj.sequence
'ACGTAGCTGACGATC'

```



#### Using class methods

To call a method associated with our new object, we use a similar format `object.method_name`.

So to call the `get_AT()` method, we would use `dna_rec_obj.get_AT() `. This should look familiar, you have done used class methods over and over again: `some_string.count('A')` 

Let's try it with our `dna_rec_obj`:  


```python
>>> dna_rec_obj.sequence
'ACGTAGCTGACGATC'
>>> dna_rec_obj.get_AT()
0.4666666666666667

```


Now let's use the `reverse_complement()` method
```python
>>> dna_rec_obj.sequence
'ACGTAGCTGACGATC'
>>> dna_rec_obj.reverse_complement()
GATCGTCAGCTACGT
```
Wow!! Getting the reverse complement in one line is pretty nice!


#### Getting data into a new instance of our class

Great!!! 

We can now create a DNARecord object and retrieve the object attributes and use the cool methods we created.

But..... It always contains the same gene_name, sequence, and species information 😟 

Let's make our class more generic, or in other words, make it so that a user can provide a new gene name, gene sequence, and source organism everytime a DNARecord object is created.



##### __\_\_init\_\___

To do this we need to add an `__init__` function to our Object Rules, or Class. 

The `init` function will automatically get called when you create an object. 

It contains specific instructions for creating a new DNARecord Object. 

It specifies how many pieces of data we want to collect from the creator of a DNARecord object to use within a DNARecord object.

Below our __\_\_init\_\___ instructions indicate that we want to create object attributes called `sequence`, `gene_name`, and `species_name` and to set them with the values provided as arguments when the object was created.

Here is our new class definition and new object creation when using the  __\_\_init\_\___  function:

```python
#!/usr/bin/env python3
class DNARecord(object):
  
  # define class attributes
  def __init__(self, sequence, gene_name, species_name): ## note that '__init__' is wrapped with two underscores
    #sequence = 'ACGTAGCTGACGATC'
    #gene_name = 'ABC1'
    #species_name = 'Drosophila melanogaster'
    self.sequence = sequence
    self.gene_name = gene_name
    self.species_name = species_name

  # define methods
  def reverse_complement(self):
    replacement1 = self.sequence.replace('A', 't')
    replacement2 = replacement1.replace('T', 'a')
    replacement3 = replacement2.replace('C', 'g')
    replacement4 = replacement3.replace('G', 'c')
    reverse_comp = replacement4[::-1]
    return reverse_comp.upper()

  def get_AT(self):
    length = len(self.sequence)
    a_count = self.sequence.count('A')
    t_count = self.sequence.count('T')
    at_content = (a_count + t_count) / length
    return at_content

## Create new DNARecord Objects with user defined data
dna_rec_obj_1 = DNARecord('ACTGATCGTTACGTACGAGT', 'ABC1', 'Drosophila melanogaster')
dna_rec_obj_2 = DNARecord('ATATATTATTATATTATA', 'COX1', 'Homo sapiens')

for d in [ dna_rec_obj_1, dna_rec_obj_2 ]:
  print('name:' , d.gene_name , ' ' , 'seq:' , d.sequence)
```

Output:

```bash
$ python3 dnaRecord_init.py
name: ABC1   seq: ACTGATCGTTACGTACGAGT
name: COX1   seq: ATATATTATTATATTATA
```

Now you can create as many DNASequence Objects as you like, each can contain information about a different sequence.



---

### [Link to Python 11 Problem Set](problemsets/Python_11_problemset.md)

---



