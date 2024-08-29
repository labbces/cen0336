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

Python tem:
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

Python pode ser executado em uma linha por vez em um interpretador interativo. É como se usasse a linha de comando de Shell (que estudamos nas duas primeiras aulas/capítulos), mas agora com a linguagem Python. Para executar o interpretador, execute o seguinte código no seu terminal:  

`$ python3`

Nota: '$' indica o prompt de comando. Lembre-se do Unix 1 que cada computador tem seu próprio prompt!

Primeiros comandos em Python:

```python
>>> print("Olá, turma 2024!")
Olá, turma 2024!
```

> Nota: `print` é uma função. Nomes de funções precedem (); assim, de maneira formal, a função é `print()`


#### Scripts em Python são arquivos de texto

* O mesmo código acima é digitado em um arquivo usando um editor de texto.
* Scripts em Python são sempre salvos em arquivos cujos nomes têm a extensão '.py' (o nome do arquivo termina com '.py').
* Poderíamos executar o código `ola.py`

Conteúdos do arquivo:

```python
print("Olá, turma 2024!")
```

#### Rodando scripts em Python

Digitar o comando `python3` seguido do nome do script faz com que Python execute o código. Lembre-se que nós vimos que podemos também executar o código de forma interativa executando apenas `python3` (ou `python`) na linha de comando.

Execute o script desta forma (% representa o prompt):

```bash
% python3 ola.py 
```

Este procedimento gera o seguinte resultado no terminal:

```bash
Olá, turma 2024!
```

#### Uma forma mais rápida/melhor de rodar scripts em Python

Se você tornar script em um executável, você pode executá-lo sem precisar digitar `python3` antes. Use o comando `chmod` para alterar as permissões do script desta forma:

`chmod +x ola.py`

Você pode verificar as permissões assim:

```
% ls -l ola.py 
-rwxr-xr-x  1 sprochnik  staff  60 Oct 16 14:29 ola.py
```

Os primeiros 10 caracteres que aparecerem na tela possuem significados especiais. O primeiro (`-`) diz a você qual tipo de arquivo `ola.py` é. `-` significa um arquivo normal, 'd' um diretório, '1' um link. Os próximos nove caracteres aparecem em três sets de três. O primeiro set se refere às suas permissões, o segundo às permissões do grupo, e o último de quaisquer outros. Cada set de três caracteres mostra em ordem 'rwx' para leitura, escrita, execução. Se alguém não tem uma permissão, um `-` é mostrado ao invés de uma letra. Os três caracteres 'x' significam que qualquer um pode executar ou rodar o script.  

Nós também precisamos adicionar uma linha no começo do script que pede para o python3 interpretar o script. Essa linha começa com `#`, então aparece como um comentário para o python. O '!' é importante como o espaço entre `env` e `python3`. O programa `/usr/bin/env` procura por onde `python3` está instalado e roda o script com `python3`. Os detalhes podem parecer um pouco complexos, mas você pode apenas copiar e colar essa linha 'mágica'.

Esse arquivo ola.py agora se parece com isso

```python
#!/usr/bin/env python3
print("Olá, turma 2024!")
```

Agora você pode simplesmente digitar o símbolo para o diretório atual `.` seguido por um `/` e o nome do script para rodá-lo. Como isso: 

```
% ./ola.py
Olá, turma 2024!
```



### Sintaxe


#### Nomes de variável em Python

Um nome de variável em Python é o nome usado para identificar uma variável, função, classe, módulo ou outro objeto. Um nome de variável inicia com uma letra, de `A` a `Z` ou de `a` a `z`, ou então com um travessão (`_`), seguido de zero ou mais letras, travessões e dígitos (`0` a `9`).

Python não permite caracteres como `@`, `$` e `%` dentro do nome de variável. Python é uma linguagem "sensível a minúsculas e maiúsculas" (muitas vezes referido com o anglicismo "case sentitive"). Portanto, `seq_id` e `seq_ID` são dois nomes diferentes de variável em Python.

#### Convenções para nomeação de nomes de variável em Python

 * A primeira letra deve ser minúscula, exceto em nomes de classes. Classes devem começar com letra maiúscula (p.e. `Seq`).
 * Os nomes de variáveis privadas são iniciadas com sublinhado (ex. `_private`).
 * Os nomes de variáveis privadas fortes (verdadeiras) são iniciadas com dois sublinhados (ex. `__private`).
 * Nomes especiais de variáveis definidas pela linguagem começam e terminam com dois travessões (p.e. `__special__`).


Selecionar bons nomes de variáveis para objetos que você nomeia é muito importante. Não chame suas variáveis de `item` ou `minha_lista` ou `dados` ou `var`, exceto em casos que você esteja trabalhando com trechos de códigos muito simples (a título de testes) ou fazendo algum gráfico. Não dê `x` ou `y` como nome de variáveis. Todos estes nomes não são descritivos para o tipo de informação encontrado naquela variável ou objeto.

Uma escolha ainda pior é dar nomes de variáveis que contêm nomes de genes como `sequencias`. Por que é uma ideia ruim? Pense no que poderia acontecer se você encher seu carro de combustível em um comércio chamado "posto de gasolina" que vendesse limonada em vez de gasolina ou etanol combustível.

Em Ciência da Computação, os nomes devem sempre descrever de forma acurada os objetos aos quais estejam vinculados. Isso reduz a possibilidade de `bugs` no seu código, torna muito mais fácil o seu entendimento se você volta ao seis meses depois ou por pessoas com as quais compartilha seu código. Embora pensar em bons nomes para variáveis tome um pouco mais de tempo e esforço, isso previne problemas no futuro!

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

Python considera como um bloco de código linhas adjacentes que apresentam o mesmo nível de indentação. Isso mantém organizadas as linhas de código que são executadas de forma conjunta. Espaçamento e/ou indentação incorretos irão causar erros ou podem fazer com que seu código seja executado de uma forma que você não espera. Ambientes de Desenvolvimento Interativo (IDEs) e editores de texto podem ajudar a indentar códigos corretamente.

O número de espaços na indentação precisa ser consistente, mas este número não é específico. Todas as linhas de código ou sentenças dentro de um bloco precisam ser indentados com o mesmo número. Por exemplo, usando quatro espaços:


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
print("Olá, turma 2024!") # esta linha imprime o conteúdo na tela
```


#### Linhas em branco

Linhas em branco são importantes para aumentar a legibilidade do código. Você deve separar com uma linha em branco trechos de código que vão juntos, organizando em "parágrafos" de código. Linhas em branco são ignoradas pelo interpretador de Python.


### Tipos de dados e variáveis

Esta é a sua primeira oportunidade de olhar para variáveis e tipos de dados. Cada tipo será discutido em mais detalhes nas seções subsequentes.

O primeiro conceito a ser considerado é que os tipos de dados de Python podem ser ou não mutáveis. Números literais, strings e tuplas não podem ser alterados. Listas, dicionários e sets podem. Da mesma forma, variáveis individuais também podem ser alteradas. Você pode armazenar dados na memória por meio da atribuição de variáveis, o que pode ser feito usando o sinal "=".

#### Números e Strings

Números e strings são dois tipos comuns de dados. Números literais e strings como `5` ou `meu nome é` são imutáveis. No entanto, seus valores podem ser armazenados em variáveis, as quais podem ser alteradas.

Por exemplo:

```python
contagem_genes = 5
# alterando o valor de contagem_genes
contagem_genes = 10
```
>Lembre-se da seção anterior sobre nomes de variáveis e objetos (e variáveis são objetos em Python).

Diferentes tipos de dados podem ser atribuídos a variáveis, como inteiros (`1`,`2`,`3`), números de ponto flutuante (`3.1415`) e strings (`"texto"`).

Por exemplo:

```python
contagem = 10    # este é um inteiro
média = 2.531      # este é um número de ponto flutuante
mensagem = "Bem-vindo ao interpretador de Python" # isso é uma string
```

`10`, `2.531` e `"Bem-vindo ao interpretador de Python"` são peças de dados singulares (escalares) e cada um é armazenado em sua própria variável.

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

- Tuplas são similares a listas e contêm coleções de dados ordenados (indexados).
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

- Um sinal de dois pontos é colocado entre cada chave e valor. Vírgulas separam pares de chave:valor.


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
> Você pode acessar valores dos outros parâmetros pelos seus índices, começando com 1, então `sys.argv[1]` contém 'Maria' e `sys.argv[2]` contém 'Carlos'. Você acessa elementos em uma lista adicionando colchetes e o índice numérico depois do nome da lista.  
> Se você quisesse imprimir uma mensagem dizendo que estas duas pessoas são amigas, você poderia escrever um código como este


```python
#!/usr/bin/env python3
import sys
friend1 = sys.argv[1] # obtém o parâmetro do primeiro comando
friend2 = sys.argv[2] # obtém o parâmetro do segundo comando
# agora a mensagem será exibida na tela
print(friend1,'e',friend2,'são amigos')
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

Um operador em uma linguagem de programação é um símbolo que faz o cumpridor ou intérprete performar operações matemáticas, relativas ou lógicas e produzir um resultado. Aqui explicaremos o conceito de operadores. 

#### Operadores aritméticos  

Em Python nós podemos escrever declarações que performam cálculos matemáticos. Para fazer isso nós precisamos usar operadores que são específicos para este propósito. Aqui estão operadores aritméticos: 

| Operador | Descrição                                                    | Exemplo          | Resultado   |
| -------- | ------------------------------------------------------------ | ---------------- | ----------- |
| `+`      | Adição                                                       | `3+2`            | 5           |
| `-`      | Subtração                                                    | `3-2`            | 1           |
| `*`      | Multiplicação                                                | `3*2`            | 6           |
| `/`      | Divisão                                                      | `3/2`            | 1.5         |
| `%`      | Módulo (divide o operador da esquerda pelo da direita e retorna o resto) | `3%2`            | 1           |
| `**`     | Expoente                                                     | `3**2`           | 9           |
| `//`     | Divisão de piso (resultado é o quociente com os dígitos depois do ponto removidos). | `3//2`  `-11//3` | 1        -4 |


__Módulo__

![3 dividido por 2 é 1 com um restante de 1. Módulo retorna o restante](images/modulus.png)

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
| `==`     | Igual a              | `3 == 2` | Falso  |
| `!=`     | Diferente de             | `3 != 2` | Verdadeiro  |
| `>`      | Maior que          | `3 > 2`  | Verdadeiro  |
| `<`      | Menor que             | `3 < 2`  | Falso  |
| `>=`     | Maior ou igual que | `3 >= 2` | Verdadeiro  |
| `<=`     | Menor ou igual que    | `3 <= 2` | Falso  |



#### Operadores lógicos

Operadores lógicos permitem combinar dois ou mais conjuntos de comparações. Você pode combinar os resultados de diferentes formas. Por exemplo, você pode 1) querer que todas as declarações sejam verdadeiras, 2) que apenas uma declaração precise ser verdadeira, ou 3) que a declaração precise ser falsa.

| Operador | Descrição                                | Exemplo        | Resultado |
| -------- | ---------------------------------------- | -------------- | ------ |
| `and`    | Verdadeiro se o operador da esquerda e o da direita forem verdade | `3>=2 and 2<3` | Verdadeiro  |
| `or`     | Verdadeiro se o operador da esquerda ou o da direita forem verdade | `3==2 or 2>3`  | Falso   |
| `not`    | Inverte o status lógico           | `not False`    | Verdadeiro  |



#### Operadores de filiação   

Você pode testar para ver se o valor é incluído em uma string, tupla ou lista. Você pode também testar que o valor não está incluso na string, tupla ou lista. 

| Operador | Descrição                                |
| -------- | ---------------------------------------- |
| `in`     | Verdadeiro se o valor é incluso em uma lista, tupla ou string |
| `not in` | Verdadeiro se o valor é ausente em uma lista, tupla ou string |

Por Exemplo:  
```python
>>> frutas = ['maca', 'laranja', 'manga', 'tomate']
>>> 'manga' in frutas
True
>>>
>>> 'pera' in frutas
False
```

Outro exemplo:
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
| `~` `+` `-`                              | Complemento binário mais e menos (nomes de métodos que os dois últimos são +@ e -@) |
| `*` `/` `%` `//`                         | Multiplica, divide, módulo e divisão de piso |
| `+` `-`                                  | Adição e subtração                       |
| `>>` `<<`                                | Deslocamento binário parte por parte de direita e esquerda |
| `&`                                      | Deslocamento binário 'AND'                       |
| `^` `\|`                                 | Bitwise exclusivo 'OR' e regular 'OR'    |
| `<=` `<` `>` `>=`                        | Operadores de comparação                 |
| `<>` `==` `!=`                           | Operadores de igualdade ('<>' obsoleto no python 3)                  |
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


Declarações de controle são usadas para direcionar o fluxo do seu código e criar oportunidade para tomada de decisão. Os fundamentos das declarações de controle são construídas por expressões verdadeiras.

#### Declaração If

- Use a declaração `if` para testar a verdade e executar linhas do código caso seja verdade.  
- Quando a expressão é avaliada como verdadeira, cada uma das declarações recuadas abaixo da declaração `if`, também conhecidas como o bloco de declarações aninhadas, será executada.


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
Retorna:  
```
found AGC in your dna sequence
```

**else**

- A porção `if` da declaração if/else statement se comporta como antes. 
- O primeiro bloco recuado é executado se a condição é verdadeira.
- Se a condição for falsa, o segundo bloco else recuado é executado.

```python
dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
if 'ATG' in dna:
  print('found ATG in your dna sequence')
else:
  print('did not find ATG in your dna sequence')
```
Retorna:  
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
  message = "é menor que 0"
  print(count, message)
elif count < 50:
  message = "é menor que 50"
  print (count, message)
elif count > 50:
  message = "é maior que 50"
  print (count, message)
else:
  message = "deve ser 50"
  print(count, message)
```
Retorna:  
```
60 é maior que 50
```

Vamos mudar a contagem para 20, qual declaração será executada?   

```python
count = 20
if count < 0:
  message = "é menor que 0"
  print(count, message)
elif count < 50:
  message = "é menor que 50"
  print (count, message)
elif count > 50:
  message = "é maior que 50"
  print (count, message)
else:
  message = "deve ser 50"
  print(count, message)
```
Retorna:  
```
20 é menor que 50
```

O que acontece quando a contagem é 50?  

```python
count = 50
if count < 0:
  message = "é menor que 0"
  print(count, message)
elif count < 50:
  message = "é menor que 50"
  print (count, message)
elif count > 50:
  message = "é maior que 50"
  print (count, message)
else:
  message = "deve ser 50"
  print(count, message)
```
Retorna:  
```
50 deve ser 50
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

Às vezes um tipo de número precisa ser mudado por outro para a função poder trabalhar. Aqui está a lista de funções para converter tipos de números:

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
| `round(x,n)`   | x arredondado para n dígitos do ponto decimal. round() arredonda para um inteiro se o valor é exatamente entre dois inteiros, então round(0.5) é 0 e round(-0.5) é 0. round(1.5) é 2. **Arredondar para um número fixo de lugares decimais pode fornecer resultados imprevisíveis.** |
| `max(x1, x2,...)` | O maior argumento é retornado           |
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
>>> round(2.675, 2)  # Observe que este arredonda para baixo
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
| `math.floor(x)`  | retorna o maior inteiro menor ou igual que x |
| `math.exp(x)`    | O exponencial de x: e<sup>x</sup> é retornado |
| `math.log(x)`    | O logaritmo natural de x, para x > 0 é retornado |
| `math.log10(x)`  | O logaritmo de base 10 de x para x > 0 é retornado |
| `math.modf(x)`   | As partes fracionárias e inteiras de x são retornadas em uma tupla de dois itens |
| `math.pow(x,y)` | O valor de x criado pelo poder y é retornado |
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

Na próxima seção, nós iremos aprender sobre strings, tuplas, e listas. Todos estes são exemplos de sequências em python. uma sequência de caracteres `'ACGTGA'`, uma tupla `(0.23, 9.74, -8.17, 3.24, 0.16)`, e uma lista `['dog', 'cat', 'bird']` são sequências de diferentes tipos de dados. Veremos mais detalhes em breve.

Em Python, um tipo de objeto consegue operações que pertencem àquele tipo. Sequências têm operações sequenciais então as strings também podem usar operações sequenciais. Strings também possuem suas próprias operações específicas.

Você pode perguntar qual a extensão de qualquer sequência

```python
>>>len('ACGTGA') # extensão de uma string
6
>>>len( (0.23, 9.74, -8.17, 3.24, 0.16) )   # extensão de uma tupla, precisa de dois parênteses (( ))
5
>>>len(['dog', 'cat', 'bird'])  # extensão de uma lista
3
```

Você pode também usar funções de strings específicas, mas não em listas e vice-versa. Nós vamos aprender mais sobre isso posteriormente. `rstrip()` é um método de string ou função. Você obtém um erro se você tentar usar isso em uma lista.

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
parágrafo = """Isso é um parágrafo. Isso é feito de múltiplas linhas e sentenças. 
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

E se você não quiser suas strings separadas por um espaço? use o operador concatenação para concatenar as duas strings antes ou dentro da função `print()`. 
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
> Nós obtemos um 'NameError' quando a string literal não for incluída nas sentenças porque o Python está procurando uma variável com o nome GGTCTAC

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
| \\r              | Retorno de carro |
| \\t              | Tab             |


Vamos incluir alguns caracteres de escape em suas strings e funções `print()`.
```python
>>> string_with_newline = 'esta string possuí uma quebra de linha\nesta é a segunda linha'
>>> print(string_with_newline)
esta string possuí uma quebra de linha
esta é a segunda linha
```
> Nós imprimimos uma nova linha na tela

`print()` adiciona espaços entre argumentos e uma nova linha ao final. Você pode mudar isso com `sep=` e `end=`. Aqui está um exemplo:
`print('uma linha', 'segunda linha' , 'terceira linha', sep='\n', end = '')`

Uma forma mais limpa para fazer isso é expressar uma string de múltiplas linhas inclusa em aspas triplas (""").
```python
>>> print("""esta string possuí uma quebra de linha
... esta é a segunda linha""")
esta string possuí uma quebra de linha
esta é a segunda linha
```

Vamos imprimir um caractere tab (\t).
```python
>>> line = "valor1\tvalor2\tvalor3"
>>> print(line)
valor1	valor2	valor3
```
> Nós obtemos as três palavras separadas por caracteres tab. Um formato comum para dados é separar colunas com tabs como isso.

Você pode adicionar uma barra invertida antes de qualquer caractere para forçar de ser impresso como um literal. Isso é chamado 'escaping'. Só é realmente útil para imprimir sentenças literais ' e " 

```python
>>> print('esta é uma \'palavra\'')  # se você quiser imprimir um ' dentro: '...'
esta é uma 'palavra'
>>> print("esta é uma 'palavra'") # talvez mais claro para imprimir um ' dentro "..."
esta é uma 'palavra'
```
> Em ambos os casos a sentença atual única é impressa na tela 

Se você quiser todos caracteres em sua string para permanecer exatamente como são, declare sua string uma string crua literal com 'r' antes da primeira sentença. Isso parece feio, mas funciona.
```python
>>> line = r"valor1\tvalor2\tvalor3"
>>> print(line)
valor1\tvalor2\tvalor3
```
> Nossos caracteres de escape '\t' estão como nós digitamos, eles não são convertidos para caracteres tab de fato.

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
>>> print("The length of the DNA sequence:" , dna , "is" , dna_length)
The length of the DNA sequence: TAGCTATATAAAATCATAAT is 20
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
> Os conteúdos de 'dna' são transformados em minúsculos e transportados para a função `print()`.

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
> Todas as ocorrências de T são substituídas por U. A nova string é retornada. A string original não foi de fato alterada. Se você quiser reutilizar a nova string, armazene ela em uma variável.



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
> Os caracteres com índices 3, 4, 5 são retornados. Em outras palavras, todo caractere começando com o índice 3 e acima, mas não incluindo acima ou igual ao índice 6. 

Vamos retornar os primeiros 6 caracteres.
```python
>>> dna = 'ATTAAAGGGCCC'
>>> sub_dna = dna[0:6]
>>> print(sub_dna)
ATTAAA
```
> Todo caractere começando no índice 0 e acima, mas não incluindo o de índice 6 e acima, são retornados. Esse é o mesmo que dna[:6]

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
| `s.isdigit()`                  | testa se todos caracteres da string são numéricos. Retorna verdadeiro ou falso. |
| `s.startswith('other_string')` | testa se a string começa com a string fornecida como argumento. Retorna verdadeiro ou falso. |
| `s.endswith('other_string')`   | testa se a string termina com a string fornecida como argumento. Retorna verdadeiro ou falso. |
| `s.split('delim')`             | separa a string no delimitador exato fornecido. Retorna a lista de subtermos. Se o argumento é fornecido, a string será separada no espaço em branco. |
| `s.join(list)`                 | O oposto de `split()`. Os elementos de uma lista serão concatenados juntos usando a string armazenada em 's' como um delimitadoras. |


__split__
`split` é um método ou forma de partir uma string em um grupo de caracteres. O que é retornado é uma lista de elementos com caracteres que são usados para partir removidos. Veremos as listas com mais detalhes na próxima seção. Não se preocupe com isso.

Vamos olhar para essa string:
```
00000xx000xx000000000000xx0xx00
```
Vamos separar em 'xx' e obter uma lista dos 0's  

O que é o 's' em `s.split(delim)` ?

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

Aqui está outro exemplo. Vamos dividir em tabs para obter uma lista dos números em colunas separadas por tab.   
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


Vamos pegar uma lista de valores de expressão e criar uma string delimitada por tab que abrirá bem em uma planilha com cada valor em sua própria coluna:
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
>>> string = "Esta sequência: {} possui {} nucleotídeos e é encontrada em {}."
>>> string.format(dna,dna_len,gene_name)
'Esta sequência: TGAACATCTAAAAGATGAAGTTT possui 23 nucleotídeos e é encontrada em Brca1.'
>>> print(string) # string.format() não altera a string original
Esta sequência: {} possui {} nucleotídeos e é encontrada em {}.
>>> new_string = string.format(dna,dna_len,gene_name)
>>> print(new_string)
Esta sequência: TGAACATCTAAAAGATGAAGTTT possui 23 nucleotídeos e é encontrada em Brca1.
```
Nós colocamos juntamente três variáveis e strings literais em uma string única usando a função `format()`. A string original não é alterada, uma nova string é retornada e incorpora os argumentos. Você pode salvar o valor retornado em uma nova variável. Cada `{}` é um espaço reservado para a string que precisa ser inserida.  

Algo legal sobre `format()` é que você pode imprimir int e tipos variáveis de string sem converter primeiramente.

Você pode também chamar diretamente `format()` dentro de uma função `print()`. Aqui estão dois exemplos

```python
>>> string = "Esta sequência: {} possui {} nucleotídeos e é encontrada em {}."
>>> print(string.format(dna,dna_len,gene_name))
Esta sequência: TGAACATCTAAAAGATGAAGTTT possui 23 nucleotídeos e é encontrada em Brca1.
```
Ou use a função `format()` em uma string literal:
```python
>>> print( "Esta sequência: {} possui {} nucleotídeos e é encontrada em {}.".format(dna,dna_len,gene_name))
Esta sequência: TGAACATCTAAAAGATGAAGTTT possui 23 nucleotídeos e é encontrada em Brca1.
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
| `<`    | Força o campo para estar alinhado à esquerda com o espaço disponível (Isso é o padrão para a maioria dos objetos). |      |
| `>`    | Força o campo para estar alinhado à direita com o espaço disponível (Isso é o padrão para números). |      |
| `=`    | Força o campo para o preenchimento ser posto depois do sinal (se tiver) mas antes dos dígitos. Isso é usado para imprimir campos na forma ‘+000000120’. Essa opção de alinhamento é apenas válida para tipos numéricos. |      |
| `^`    | Força o campo para ser centralizado com o espaço disponível. |      |

>Aqui está um exemplo 
>
>`{  :    x  <  10   s}`
>
> preencher com `x`   
> justificar à esquerda `<`  
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


Muito pode ser feito com a função `format()`. Aqui está um último exemplo, mas não a última funcionalidade desta função, vamos arredondar um número de ponto de flutuação para algumas casas decimais, começando com muitos. (o padrão é 6). Note que a função arredonda para a casa decimal mais próxima, mas nem sempre exatamente da forma que você espera por conta da forma que os computadores representam decimais com 1s e 0s.

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


- Listas são usadas para armazenar uma coleção de dados de maneira ordenada e *indexada*.
- Valores são separados por vírgulas
- Valores são anexados entre colchetes '[]'
- Listas podem crescer e encolher
- Valores são mutáveis

```python
[ 'atg' , 'aaa' , 'agg' ]
```

#### Tuplas

- Tuplas são usadas para armazenar uma coleção de dados de maneira ordenada e indexada
- Valores são separados por vírgulas
- Valores são anexados entre parênteses '()'
- Tuplas **NÃO** podem crescer ou encolher
- Valores são imutáveis

```python
( 'Jan' , 'Fev' , 'Mar' , 'Abr' , 'Mai' , 'Jun' , 'Jul' , 'Ago' , 'Set' , 'Out' , 'Nov' , 'Dez' )
```

Muitas funções e métodos retornam tuplas: O `math.modf(x)`, por exemplo, retorna as partes fracionais e inteiras de `x` em uma tupla de dois itens. Aqui não existem motivos para mudar a sequência.

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

Outro exemplo com culturas:

```python
>>> culturas = ['soja', 'milho', 'algodao', 'arroz']
>>> print(culturas[0])
soja
>>> print(culturas[1])
milho
>>> print(culturas[3])
arroz
```
> Os 3 valores são acessados independentemente e impressos imediatamente. Eles não são armazenados em uma variável.


Mais um exemplo com números inteiros

```python
>>> producao = [3000, 8000, 2000, 3000]
>>> print(producao[2])
```

Mas nessa lista com inteiros, podemos fazer algumas operações, por exemplo, somar os valores armazenados nos índices 1 e 2:

```python
>>> producao[1] + producao[2]
>>> 10000
```


Se você deseja acessar os valores começando pelo fim da lista, use índices negativos.
```python
>>> codons = [ 'atg' , 'aaa' , 'agg' ]
>>> print(codons[-1])
agg
>>> print(codons[-2])
aaa
```

> Usar um índice negativo retornará os valores do final da lista. Por exemplo, -1 é o índice do último valor 'agg'. Esse valor também possui um índice de 2.

Ou com o exemplo das culturas

>>> print(culturas[-1])
arroz

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
> codon[5] não existe, e quando tentamos atribuir valor para esse índice ocorre um IndexError. Se você deseja adicionar novos elementos no final da lista use `codons.append('taa')` ou `codons.extend(list)`. Veja mais detalhes abaixo.

Vamos acrescentar mais uma cultura na nossa lista de culturas: mandioca.

```python
>>> culturas.append('mandioca')
print(culturas)
```

#### Extraindo um subconjunto de uma lista, ou Recortando

Isso funciona da mesma forma com as listas como com as strings. Isso é porque ambos são sequências, ou coleções ordenadas de dados com informação posicional. Lembre-se que Python conta as divisões entre os elementos, começando com 0.

| Índice | Valor |
| ----- | ----- |
| 0     | atg   |
| 1     | aaa   |
| 2     | agg   |
| 3     | aac   |
| 4     | cgc   |
| 5     | acg   |

use a sintaxe [start : end : step] para dividir sua sequência python 

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
> `codons[1:3]` retorna todo valor começando com o valor de codons[1] até, mas não incluindo, o codons[3]  
> `codons[3:]` retorna todo valor começando com o valor de codons[3] e todos os valores posteriores.  
> `codons[:3]` retorna todo valor até, mas não incluindo, codons[3]  
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
| `sorted(list, key=str.lower, reverse=False)`  | `str.lower()` faz com que os elementos minúsculos retornem antes na lista organizada | `sorted(['a','A','z'],key=str.lower)` retorna `['a', 'A', 'z']` |


#### Lista de métodos

Lembre-se que métodos são utilizados no seguinte formato list.method().   

Para esses exemplos utilize: `nums = [1,2,3]` e `codons = [ 'atg' , 'aaa' , 'agg' ]`

| Métodos                   | Descrição                                | Exemplo                                  |
| ------------------------- | ---------------------------------------- | ---------------------------------------- |
| `list.append(obj)`        | anexa um objeto no final de uma lista  | nums.append(9) ; print(nums) ; retorna [1,2,3,9] |
| `list.count(obj)`         | conta as ocorrências de um objeto em uma lista | nums.count(2) retorna 1                  |
| `list.index(obj)`         | retorna o menor índice em que o objeto fornecido é encontrado | nums.index(2) retorna 1                  |
| `list.pop()`              | remove e retorna o último valor de uma lista. A lista é agora um elemento mais curta | nums.pop() retorna 3                     |
| `list.insert(index, obj)` | insere um valor ao índice fornecido. Lembre-se de pensar sobre as divisões entre os elementos | nums.insert(0,100) ; print(nums) retorna [100, 1, 2, 3] |
| `list.extend(new_list)`   | anexa `new_list` ao final de `list`  | nums.extend([7, 8]) ; print(nums) retorna [1, 2, 3, 7,8] |
| `list.pop(index)`         | remove e retorna o valor do argumento indexado. A lista é agora um valor mais curta | nums.pop(0) retorna 1                    |
| `list.remove(obj)`        | encontra o menor índice do objeto fornecido e o remove da lista. A lista é agora um elemento mais curta | codons.remove('aaa') ; print(codons) retorna  [ 'atg' , 'agg' ] |
| `list.reverse()`          | inverte a ordem da lista          | nums.reverse() ; print(nums) retorna [3,2,1] |
| `list.copy()`             | Retorna uma cópia rasa da lista. Rasa vs [Deep](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/) apenas importa em estruturas de data multidimensionais. |                                          |
| `list.sort([func])`       | organiza uma lista utilizando a função fornecida. Não retorna uma lista. A lista foi alterada. A organização avançada de listas será coberta adiante na discussão sobre escrever suas próprias funções. | codons.sort() ; print(codons) retorna ['aaa', 'agg', 'atg'] |


Tome cuidado em como você faz uma cópia de sua lista
```python
>>> my_list=['a', 'um', 'dois']
>>> copy_list=my_list
>>> copy_list.append('1')
>>> print(my_list)
['a', 'um', 'dois', '1']
>>> print(copy_list)
['a', 'um', 'dois', '1']
```
> Não foi o que esperava?! Ambas listas foram alteradas porque nós apenas copiamos um ponteiro para a lista original quando escrevemos `copy_list=my_list`. 

Vamos copiar a lista utilizando o método `copy()`.
```python
>>> my_list=['a', 'um', 'dois']
>>> copy_list=my_list.copy()
>>> copy_list.append('1')
>>> print(my_list)
['a', 'um', 'dois']
```
> Agora sim, nós obtivemos o esperado desta vez!



#### Construindo uma lista um valor por vez

Agora que você já viu a função `append()` nós podemos ver como construir uma lista com um valor por vez.

```python
>>> words = []
>>> print(words)
[]
>>> words.append('um')
>>> words.append('dois')
>>> print(words)
['um', 'dois']
```
> Nós começamos com uma lista vazia chamada 'words'. Nós usamos `append()` para adicionar o valor 'um' depois o valor 'dois'. Finalizamos a lista com dois valores. Você pode adicionar uma lista inteira em outra lista com `words.extend(['três','quatro','cinco'])`



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
# código logo abaixo é executado depois que o while loop encerrar
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

Um loop infinito ocorre quando uma condição while é sempre verdadeira. Aqui está um exemplo de um loop infinito.

```python
#!/usr/bin/env python3

contagem = 0
while contagem < 5:            # isso é normalmente um bug!!
  print("contagem:" , contagem)   # esqueça de incrementar a contagem no loop!!
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

#### Sintaxe do For Loop

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

Esse próximo exemplo é utilizando um for loop para iterar em uma string. Lembre-se que uma string é uma sequência como uma lista. Cada caractere possui uma posição. Olhe novamente em "Extraindo uma substring, ou Recortando" na seção [Strings](#strings) para ver outras formas em que strings podem ser tratadas como listas.

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

Outro exemplo de iterar em uma lista de variáveis, estes números de tempo.

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

Python tem uma função chamada `range()` que retornará números que podem ser convertidos em uma lista. 
```python
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
```

A função `range()` pode ser utilizada em conjunto com um for loop para iterar em um faixa de números. A função `range()` também começa com 0 e opera sobre os espaços entre os números.  

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
| `break`           | Um loop é terminado quando uma declaração break é executada. Todas as linhas de código após o break, mas dentro do bloco de loop, não são executadas. Sem mais interações do loop sendo executadas |
| `continue`        | Uma única iteração de um loop é terminada quando a declaração continue é executada. A próxima iteração vai proceder normalmente. |

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
  print("Linha após o nosso continue")
print("Done")
```

Saída:
```
$ python continue.py
count: 0
Linha após o nosso continue
count: 1
Linha após o nosso continue
count: 2
count: 3
Linha após o nosso continue
count: 4
Linha após o nosso continue
Done
```
> Quando a contagem é igual a 3 o continue é executado. Isso faz com que todas as linhas contendo o bloco de loop sejam puladas. "Linha após o nosso continue" não é impresso quando a contagem é igual a 3. O próximo loop é executado normalmente.

#### Iteradores


Um iterável é qualquer tipo de dado que pode ser iterado, ou pode ser usado em uma iteração. Um iterável pode ser transformado em um iterador com a função `iter()`. Isso significa que você pode utilizar a função `next()`.

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
> Um iterador permite que você obtenha o próximo elemento no iterador até que não existam mais elementos. Se você quer ir através de cada elemento novamente, você precisará redefinir o iterador.

Exemplo de utilização de um iterador em um for loop:
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
> Isso é bom se você tem uma lista muito larga que você não deseja manter na memória. Um iterador permite que você vá através de cada elemento mas sem manter a lista completa na memória. Sem iteradores toda a lista permanece na memória.


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


### Dicionário


Dicionários são outra estrutura iterável, semelhante a uma string e uma lista. Ao contrário de strings e listas, os dicionários não são uma sequência, ou em outras palavras, eles são __não ordenados__ e a posição não é importante.

Dicionários são uma coleção de pares chave/valor. Em Python, cada chave é separada de seu valor por dois pontos (:), os itens são separados por vírgulas, e tudo é envolto por chaves. Um dicionário vazio sem itens é escrito apenas com duas chaves, assim: `{}`

Cada chave em um dicionário é única, enquanto os valores podem não ser. Os valores de um dicionário podem ser de qualquer tipo, mas as chaves devem ser de um tipo de dado imutável, como strings, números ou tuplas.

Dados apropriados para dicionários são duas informações que naturalmente estão relacionadas, como o nome de um gene e sua sequência.

| Chave | Valor                                    |
| ----- | ---------------------------------------- |
| TP53  | GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC |
| BRCA1 | GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA |

#### Criando um dicionário

```python
genes = { 'TP53' : 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC' , 'BRCA1' : 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' }
```

Dividir os pares chave/valor em várias linhas facilita a leitura.
```python
genes = { 
           'TP53' : 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC' , 
           'BRCA1' : 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' 
         }
```

#### Acessando os valores do dicionário

Para recuperar um único valor em um dicionário, use a chave do valor neste formato `dict[chave]`. Isso retornará o valor na chave especificada.

```python
>>> genes = { 'TP53' : 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC' , 'BRCA1' : 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' }
>>>
>>> genes['TP53']
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC
```
> A sequência do gene TP53 está armazenada como um valor da chave 'TP53'. Podemos acessar a sequência usando a chave neste formato dict[chave].

O valor pode ser acessado e passado diretamente para uma função ou armazenado em uma variável.

```python
>>> print(genes['TP53'])
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC
>>>
>>> seq = genes['TP53']
>>> print(seq)
GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC
```

Lembre-se da lista de culturas e produção acima. Vamos criar um dicionário com esses dados:

```python
>>> producao_por_cultura = {'soja': 3000, 'milho': 8000, 'algodao':2000 , 'arroz':3000}
>>> print(producao_por_cultura['milho'])
```

Também podemos criar um dicionario com um animal repreentativo de cada bioma brasileiro: 

```python
>>> animais_por_bioma={'Amazonia':'Arara-vermelha','Cerrado':'Lobo-guará','Mata Atlantica': 'Capivara','Pantanal': 'Onca','Pampa': 'Garça','Caatinga': 'Jiboia'}
>>> print(animais_por_bioma['Cerrado'])
```

#### Mudando os valores de um dicionário

Valores individuais podem ser alterados usando a chave e o operador de atribuição.

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
> O conteúdo do dicionário foi alterado.

Outros operadores de atribuição também podem ser usados para alterar um valor de uma chave de dicionário.
```python
>>> genes = { 'TP53' : 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC' , 'BRCA1' : 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA' }
>>>
>>> genes['TP53'] += 'TAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTG'
>>>
>>> print(genes)
{'BRCA1': 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA', 'TP53': 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTG'}
```
> Aqui, usamos o operador de atribuição de concatenação '+='. Isso é equivalente a  `genes['TP53'] = genes['TP53'] + 'TAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTG'`.

No dicionário de animais dos biomas brasileiros, vamos substituir a Capivara da Mata Atlântica pelo Tucano.

```python
>>> animais_por_bioma['Mata Atlantica']= 'Tucano'
>>> print(animais_por_bioma)
```

#### Acessando cada chave/valor do dicionário

Já que um dicionário é um objeto iterável, podemos percorrer os seus conteúdos.

Um loop for pode ser usado para recuperar cada chave de um dicionário de cada vez:
```python
>>> for gene in genes:
...   print(gene)
...
TP53
BRCA1
```

Depois de obter a chave, você pode recuperar o valor:
```python
>>> for gene in genes:
...   seq = genes[gene]
...   print(gene, seq[0:10])
...
TP53 GATGGGATTG
BRCA1 GTACCTTGAT
```

Vamos imprimir os animais representativos dos biomas brasileiros:


```python
>>> for bioma in animais_por_bioma:
...   animal=animais_por_bioma[bioma]
...   print(bioma, animal)
... 
Amazonia Arara-vermelha
Cerrado Lobo-guará
Mata Atlantica Tucano
Pantanal Onca
Pampa Garça
Caatinga Jiboia
```

#### Construir um dicionário uma chave/valor de cada vez

Construir um dicionário uma chave/valor de cada vez é semelhante ao que acabamos de ver quando alteramos o valor de uma chave. Normalmente, você não fará isso. Falaremos sobre maneiras de construir um dicionário a partir de um arquivo em uma palestra posterior.

```python
>>> genes = {}
>>> print(genes)
{}
>>> genes['Brca1'] = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
>>> genes['TP53'] = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC'
>>> print(genes)
{'Brca1': 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA', 'TP53': 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC'}
```
> Começamos criando um dicionário vazio. Em seguida, adicionamos cada par chave/valor usando a mesma sintaxe que usamos ao alterar um valor.  
> dict[key] = new_value  


#### Verificar se as Chaves do Dicionário Existem

Python gera um erro (NameError) se você tentar acessar uma chave que não existe. 

```python
>>> print(genes['HDAC'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'HDAC' is not defined
```

#### Operadores de dicionário

| Operador | Descrição                             |
| -------- | ---------------------------------------- |
| `in`     | `key in dict` retorna True se a chave existe no dicionário |
| `not in` | `key not in dict` retorna True se a chave não existe no dicionário |

Como o Python gera um NameError se você tentar usar uma chave que não existe no dicionário, é necessário verificar se uma chave existe antes de tentar usá-la.

A melhor maneira de verificar se uma chave existe é usando `in`.

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


#### Construindo um Dicionário com um Par de Chave/Valor de Cada Vez Usando um Loop

Agora temos todas as ferramentas para construir um dicionário com um par de chave/valor usando um loop for. Isso é como você construirá dicionários com mais frequência na vida real.

Aqui, vamos contar e armazenar contagens de nucleotídeos:  

```python
#!/usr/bin/env python3

# cria um dicionário vazio
nt_count={}

# exemplo de loop
dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
for nt in dna:

  # 'nt' está no dicionário?
  if nt in nt_count:
    # se sim, aumentamos a contagem
    previous_count = nt_count[nt]
    new_count = previous_count + 1
    nt_count[nt] = new_count
  else:
    # se não, adicionamos e contamos 1
    nt_count[nt] = 1;

print(nt_count)
```
> {'G': 20, 'T': 21, 'A': 13, 'C': 16}

Qual outra maneira podemos contar?

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
> lembre-se que `count=count+1` é o mesmo que `count+=1`



#### Ordenando chaves de dicionários

Se você deseja imprimir o conteúdo de um dicionário, deve classificar as chaves e, em seguida, iterar sobre as chaves com um loop for. Por que você gostaria de classificar as chaves?

```python
for gene_key in sorted(genes): # python permite que você use atalhos em um "for loop"
                               # você não precisa escrever genes.keys() em um for loop
                               # para iterar sobre as chaves
  print(gene_key, '=>' , genes[gene_key])
```
> Isso imprimirá as chaves na mesma ordem toda vez que você executar seu script. Dicionários são desordenados, então sem ordenação, você obterá uma ordem diferente cada vez que executar o script, o que pode ser confuso.

#### Função do dicionário

| Função           | Descrição                              |
| ---------------- | ---------------------------------------- |
| `len(dict)`      | retorna o número total de pares chave/valor |
| `str(dict)`      | retorna uma representação em string do dicionário |
| `type(variable)` | Retorna o tipo ou classe da variável passada para a função. Se a variável for um dicionário, ela retornará o tipo "dicionário". |

Essas funções também funcionam com vários outros tipos de dados!

#### Métodos de dicionário

| Métodos                                | Descrição                                |
| -------------------------------------- | ---------------------------------------- |
| `dict.clear()`                         | Remove todos os elementos do dicionário `dict`.  |
| `dict.copy()`                          | Retorna uma cópia rasa (shallow copy) do dicionário. [Shallow vs. deep](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/) A cópia só é relevante em estruturas de dados multidimensionais. |
| `dict.fromkeys(seq,value)`             | Crie um novo dicionário com chaves de seq (tipo de sequência Python) e valores definidos como valor. |
| `dict.items()`                         | Retorna uma lista de tuplas (chave, valor). |
| `dict.pop(key)`                        | Remove o par chave:valor e retorna o valor. |
| `dict.keys()`                          | Retorna uma lista de chaves                     |
| `dict.get(key, default = None)`        | Obtenha o valor de dict[key], use o padrão se não estiver presente. |
| `dict.setdefault(key, default = None)` | Semelhante a get(), mas definirá dict[key] = default se a chave ainda não estiver em dict. |
| `dict.update(dict2)`                   | Adiciona os pares chave-valor do dicionário dict2 ao dicionário dict. |
| `dict.values()`                        | Retorna uma lista dos valores do dicionário `dict`. |


### Conjuntos


Um conjunto é outro tipo de dado em Python. Essencialmente, é um dicionário com chaves, mas sem valores.

- Um conjunto é não ordenado.
- Um conjunto é uma coleção de dados sem elementos duplicados.
- Usos comuns incluem buscar diferenças e eliminar duplicatas em conjuntos de dados.

Chaves `{}` ou a função `set()` podem ser usadas para criar conjuntos.

> Observação: para criar um conjunto vazio, você precisa usar `set()`, não `{}`, este último cria um dicionário vazio.

```python
>>> basket = {'maçã', 'laranja', 'maçã', 'pera', 'laranja', 'banana'}
>>> print(basket)                     
{'laranja', 'banana', 'pera', 'maçã'}
```
> Veja, os duplicados foram removidos.

Testar se um valor está no conjunto.
```python
>>> 'laranja' in basket                 
True
>>> 'capim-colchão' in basket
False
```
> O operador `in` funciona da mesma forma com conjuntos como funciona com listas e dicionários.


União, interseção, diferença e diferença simétrica podem ser feitas com conjuntos.
```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                 
{'a', 'r', 'b', 'c', 'd'}
```
> Conjuntos contêm elementos únicos; portanto, mesmo que elementos duplicados sejam fornecidos, eles serão removidos.

#### Operadores de Conjuntos

**Diferença**

A diferença entre dois conjuntos são os elementos que são exclusivos do conjunto à esquerda do operador `-`, com duplicatas removidas..

![Diferença de Conjunto](images/set_difference.png)

```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a - b                             
{'r', 'd', 'b'}
```
> Isso resulta nas letras que estão em "a", mas não em "b".

**União**

A união entre dois conjuntos é uma sequência de todos os elementos de ambos os conjuntos combinados, com duplicatas removidas.

![União de Conjunto](images/set_union.png)

```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a | b                          
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
```
> Isso retorna as letras que estão em ambos os conjuntos a e b.

**Interseção**

A interseção entre dois conjuntos é uma sequência dos elementos que estão em ambos os conjuntos ao mesmo tempo, com duplicatas removidas.

![Interseção do Conjunto](images/set_intersection.png)

```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a & b                            
{'a', 'c'}
```
> Isso retorna as letras que estão em ambos os conjuntos `a` e `b`.


**Diferença simétrica**

A diferença simétrica é composta pelos elementos que estão apenas no primeiro conjunto, mais os elementos que estão apenas no segundo conjunto, com duplicatas removidas.

![Diferença simétrica de conjunto](images/set_symmetric_difference.png)

```python
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a ^ b                             
{'r', 'd', 'b', 'm', 'z', 'l'}
```
> Isso retorna as letras que estão em `a` ou `b`, mas não em ambos (também conhecido como ou exclusivo).

#### Funções de Conjunto

| Funções       | Descrição                              |
| ------------- | ---------------------------------------- |
| `all()`       | retorna `True` se todos os elementos do conjunto forem `True` (ou se o conjunto estiver vazio). |
| `any()`       | retorna `True` se algum elemento do conjunto for `True`. Se o conjunto estiver vazio, retorna `False`. |
| `enumerate()` | retorna um objeto `enumerate`. Ele contém o índice e o valor de todos os itens do conjunto como um par. |
| `len()`       | retorna o número de itens no conjunto.  |
| `max()`       | retorna o maior item no conjunto.     |
| `min()`       | retorna o menor item no conjunto.    |
| `sorted()`    | retorna uma nova lista ordenada a partir dos elementos no conjunto (não altera o conjunto original). |
| `sum()`       | retorna a soma de todos os elementos no conjunto. |



#### Métodos de conjunto

| Métodos                                 | Descrição                              |
| --------------------------------------- | ---------------------------------------- |
| `set.add(new)`                          | adiciona novos elementos                       |
| `set.clear()`                           | remove todos elementos                 |
| `set.copy()`                            | retorna uma cópia rasa de um conjunto          |
| `set.difference(set2)`                  | retorna a diferença entre o set e o set2   |
| `set.difference_update(set2)`           | remove todos os elementos de outro conjunto (set) deste conjunto (set2) |
| `set.discard(element)`                  | remove um elemento do conjunto se ele for encontrado no conjunto. (Não faz nada se o elemento não estiver no conjunto) |
| `set.intersection(sets)`                | retorna a interseção do conjunto com outros conjuntos fornecidos |
| `set.intersection_update(sets)`         | atualiza o conjunto com a interseção do conjunto (set) e os outros conjuntos fornecidos (sets). |
| `set.isdisjoint(set2)`                  | retorna Verdadeiro se o set e o set2 não têm interseção. |
| `set.issubset(set2)`                    | retorna Verdadeiro se o set2 contém o conjunto.        |
| `set.issuperset(set2)`                  | retorna Verdadeiro se o set contém o set2.       |
| `set.pop()`                             | remove e retorna um elemento arbitrário do conjunto. |
| `set.remove(element)`                   | remove um elemento de um conjunto.              |
| `set.symmetric_difference(set2)`        | retorna a diferença simétrica entre o set e o set2. |
| `set.symmetric_difference_update(set2)` | atualiza o conjunto com a diferença simétrica entre o set e o set2 |
| `set.union(sets)`                       | retorna a união do conjunto (set) e dos outros conjuntos fornecidos (sets). |
| `set.update(set2)`                      | atualiza o conjunto com a união do set e o set2. |





#### Construa um dicionário de contagens de NT usando um conjunto e loops.

Vamos dar uma reviravolta no nosso script de contagem de NT. Vamos usar um conjunto para encontrar todos os NTs únicos e, em seguida, usar o método `count()` da string para contar o nucleotídeo, em vez de incrementar a contagem como fizemos anteriormente.

Código:  


```python
#!/usr/bin/env python3

# crie um novo dicionário
nt_count = {}

# obtenha um conjunto de caracteres únicos em nossa sequência de DNA.

dna = 'GTACCNTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'
unique = set(dna)

print('unique nt: ', unique) ## {'C', 'A', 'G', 'T', 'N'}

# Itere através de cada nucleotídeo único.
for nt in unique:
  # Conte o número deste nucleotídeo único no DNA.
  count = dna.count(nt)

  # Adicione nossa contagem ao nosso dicionário.
  nt_count[nt] = count


print('nt count:', nt_count)

```


Output:  


```
unique nt:  {'N', 'C', 'T', 'G', 'A'}
nt count: {'G': 20, 'T': 21, 'A': 13, 'C': 16, 'N': 1}

```
> Temos a contagem para todos os NTs, até mesmo aqueles que talvez não esperássemos.

---

### [Link para o Python 5 Problem Set](problemsets/Python_05_problemset.md)


---
## Python 6


### I/O e Arquivos


I/O significa input/output. O "in" e "out" referem-se a obter dados dentro e fora do seu script. Pode ser um pouco surpreendente no início, mas escrever na tela, ler do teclado, ler de um arquivo e escrever em um arquivo são todos exemplos de I/O.


#### Escrevendo na tela

Você deve estar bem familiarizado com a escrita na tela. Temos usado a função `print()` para isso.  


```python
>>> print ("Olá, PFB2019!")
Olá, PFB2019!
```
> Lembra-se desse exemplo de uma das nossas primeiras lições?

#### Lendo a entrada do teclado

Isso é algo novo. Há uma função que imprime uma mensagem na tela e espera uma entrada do teclado. Essa entrada pode ser armazenada em uma variável. Ela sempre começa como uma string. Converta para int ou float se quiser um número. Quando terminar de digitar o texto, pressione a tecla Enter para encerrar a entrada. Um caractere de nova linha não está incluído na entrada.

```python
>>> user_input = input("Digite algo agora: ")
Digite algo agora: Oi
>>> print(user_input)
Oi
>>> type(user_input)
<class 'str'>
```
#### Lendo de um arquivo

A maioria dos dados com os quais lidaremos estará contida em arquivos.

O primeiro passo com um arquivo é abri-lo. Podemos fazer isso com a função `open()`. A função `open()` leva o nome do arquivo e o modo de acesso como argumentos e retorna um objeto de arquivo.

Os modos de acesso mais comuns são leitura (r) e escrita (w).

#### Abrir um arquivo

```python
>>> objeto_arquivo = open("seq.nt.txt", "r")
```
> 'objeto_arquivo' é o nome de uma variável. Pode ser qualquer coisa, mas faça um nome útil que descreva que tipo de arquivo você está abrindo.


#### Lendo o conteúdo de um arquivo

Agora que abrimos um arquivo e criamos um objeto de arquivo, podemos fazer coisas com ele, como ler. Vamos ler todo o conteúdo de uma vez.

Vamos para a linha de comando e use `cat` para ver o conteúdo do arquivo primeiro.

```bash
$ cat seq.nt.txt
ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAG
ACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG
$ 
```

Observe as novas linhas. Agora, vamos imprimir o conteúdo na tela com Python. Vamos usar `read()` para ler todo o conteúdo do arquivo em uma variável.

```python
>>> arquivo = open("seq.nt.txt", "r")
>>> conteudo = arquivo.read()
>>> print(conteudo)  # observe que os caracteres de nova linha fazem parte do arquivo!
ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAG
ACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG

>>> arquivo.close()
```
> O conteúdo completo pode ser obtido com o método `read()`. Observe que as novas linhas são mantidas quando o `conteudo` é impresso na tela. `print()` adiciona outra nova linha quando termina de imprimir.
> É uma boa prática fechar seu arquivo. Use o método `close()`.

Aqui está outra maneira de ler dados de um arquivo. Um loop `for` pode ser usado para iterar pelo arquivo uma linha de cada vez.

```python
#!/usr/bin/env python3

arquivo = open("seq.nt.txt", "r")
for linha in arquivo: # Magia do Python: lê uma linha do arquivo
  print(linha)
```

Output:
```
$ python3 file_for.py
ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAG

ACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG

```
> Observe a linha em branco após cada linha que imprimimos. `print()` adiciona uma nova linha e temos uma nova linha no final de cada linha em nosso arquivo. Use o método `rstrip()` para remover a nova linha de cada linha.

Vamos usar o método `rstrip()` para remover a nova linha da entrada do nosso arquivo.

```python
$ cat arquivo_for_rstrip.py
#!/usr/bin/env python3

arquivo_objeto = open("seq.nt.txt", "r")
for linha in arquivo_objeto:
  linha = linha.rstrip()
  print(linha)
```
> `rstrip()` sem nenhum parâmetro retorna uma string com espaços em branco removidos do final.

Output:
```
$ python3 file_for_rstrip.py
ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAG
ACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG
```

> De onde vêm as novas linhas na saída acima?

#### Abrindo um arquivo com `with open() as fh:`

Muitas pessoas adicionam isso porque ele fecha o arquivo automaticamente para você. Boa prática de programação. Seu código se limpará conforme ele é executado. Para codificação mais avançada, `with ... as ...` economiza recursos limitados, como identificadores de arquivo e conexões de banco de dados. Por enquanto, só precisamos saber que `with ... as ...:` faz o mesmo que `fh = open(...) ... fh.close()`. Portanto, aqui está como o código adaptado se parece:

```python
#!/usr/bin/env python3

with open("seq.nt.txt", "r") as objeto_arquivo: # limpa após sair do bloco 'with'
  for linha in objeto_arquivo:
    linha = linha.rstrip()
    print(linha)
# o arquivo é fechado para você aqui.
```

#### Escrevendo em um Arquivo

Escrever em um arquivo requer apenas abrir um arquivo para escrita e depois usar o método `write()`.

O método `write()` é como a função `print()`. A maior diferença é que ele escreve no objeto do seu arquivo em vez da tela. Ao contrário do `print()`, ele não adiciona uma nova linha por padrão. `write()` recebe um único argumento de string.

Vamos escrever algumas linhas em um arquivo chamado "writing.txt".

```python
#!/usr/bin/env python3

fo = open("writing.txt", "w")
fo.write("Uma linha.\n")
fo.write("Segunda linha.\n")
fo.write("Terceira linha" + " tem texto adicional\n")
alguma_var = 5
fo.write("Quarta linha tem " + str(alguma_var) + " palavras\n")
fo.close()
print("Escrito no arquivo 'writing.txt'") # é legal informar ao usuário que você escreveu um arquivo
```

Output:
```
$ python3 file_write.py
Escrito no arquivo 'writing.txt'
$ cat writing.txt
Uma linha.
Segunda linha.
Terceira linha tem texto adicional
Quarta linha tem 5 palavras
```

Agora, vamos ficar loucos! Vamos ler de um arquivo uma linha de cada vez. Faça algo com cada linha e escreva os resultados em um novo arquivo.

```python
#!/usr/bin/env python3

total_nts = 0
# abre dois objetos de arquivo, um para leitura e outro para escrita
with open("seq.nt.txt", "r") as seq_read, open("nt.counts.txt", "w") as seq_write:
  for linha in seq_read:
    linha = linha.rstrip()
    contagem_nt = len(linha)
    total_nts += contagem_nt
    seq_write.write(str(contagem_nt) + "\n")

  seq_write.write("Total: " + str(total_nts) + "\n")

print("Escrito 'nt.counts.txt'")
```

Output:
```
$ python3 file_read_write.py
$ cat nt.counts.txt
71
71
Total: 142
```
> O arquivo do qual estamos lendo é chamado de "seq.nt.txt"
> O arquivo para o qual estamos escrevendo é chamado de "nt.counts.txt"
> Lemos cada linha, calculamos o comprimento de cada linha e imprimimos o comprimento
> Também criamos uma variável para acompanhar a contagem total de nt
> No final, imprimimos o total de nt
> Finalmente, fechamos cada um dos arquivos 



#### Construindo um dicionário a partir de um arquivo

Esta é uma tarefa muito comum. Ela usará um loop, E/S de arquivo e um dicionário.

Suponha que temos um arquivo chamado "sequence_data.txt" que contém nomes de genes e sequências delimitadas por tabulação, que se parece com isto:

```
TP53    GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC
BRCA1   GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA
```

Como podemos ler todo este arquivo em um dicionário?

```python
#!/usr/bin/env python3

genes = {}
with open("sequence_data.txt", "r") as seq_read:
  for linha in seq_read:
    linha = linha.rstrip()
    gene_id, seq = linha.split() # dividir no espaço em branco
    genes[gene_id] = seq
print(genes)
```

Output:
```
{'TP53': 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTC', 'BRCA1': 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'}
```

---



### [Link para Python 6 Conjunto de Problemas](problemsets/Python_06_problemset.md)



---
## Python 7

### Expressões Regulares

Expressões regulares são uma linguagem para correspondência de padrões. Muitas linguagens de programação diferentes incorporam expressões regulares, assim como alguns comandos Unix, como grep e sed. Até agora, vimos algumas funções para encontrar correspondências exatas em strings, mas isso nem sempre é suficiente.

Funções que utilizam expressões regulares permitem a correspondência de padrões não exatos.

Essas funções especializadas não estão incluídas no núcleo do Python. Precisamos importá-las digitando
`import re`
no topo do seu script

```python 
#!/usr/bin/env python3

import re
```

Primeiro, veremos alguns exemplos e depois entraremos nos detalhes mecânicos com mais detalhes.

Vamos começar com algo simples e encontrar uma correspondência exata para o sítio de restrição EcoRI em uma string.
```python
>>> dna = 'ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG'
>>> if re.search(r"GAATTC",dna):
...   print("Um sítio de EcoRI foi encontrado!")
...
Um sítio de EcoRI foi encontrado!
>>>
```
> Como podemos pesquisar por caracteres de controle como um tab (\t), é bom criar o hábito de usar a função de string raw 
> `r`
> ao definir padrões.

> Aqui usamos a função `search()` com dois argumentos, 1) nosso padrão e 2) a string que queremos pesquisar.

Vamos descobrir o que é retornado pela função `search()`.
```python
>>> dna = 'ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG'
>>> found=re.search(r"GAATTC",dna)
>>> print(found)
<_sre.SRE_Match object; span=(70, 76), match='GAATTC'>
```
> As informações sobre a primeira correspondência são retornadas


E uma correspondência não exata? Vamos procurar por um sítio de metilação que deve corresponder aos seguintes critérios:
- G ou A
- seguido por C
- seguido por qualquer coisa ou nada
- seguido por um G

Isso pode corresponder a qualquer um destes: 
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

Podemos testar cada um desses ou usar expressões regulares. É exatamente isso que as expressões regulares podem fazer por nós.
```python
>>> dna = 'ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG'
>>> found=re.search(r"[GA]C.?G",dna)
>>> print(found)
<_sre.SRE_Match object; span=(7, 10), match='ACG'>
```
> Aqui você pode ver nas informações retornadas que ACG começa na posição da string 7 (nt 8).
>
> A primeira posição após o final da correspondência está na posição da string 10 (nt 11).

E outras correspondências potenciais em nossa string de DNA? Podemos usar a função `findall()` para encontrar todas as correspondências.

```python
>>> dna = 'ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG'
>>> found=re.findall(r"[GA]C.?G",dna)
>>> print(found)
['ACG', 'GCTG', 'ACTG', 'ACCG', 'ACAG', 'ACCG', 'ACAG']
```
> `findall()` retorna uma lista de todas as partes da string que correspondem ao regex.

Uma contagem rápida de todos os sítios correspondentes pode ser feita contando o comprimento da lista retornada.

```python
>>> len (re.findall(r"[GA]C.?G",dna))
7
```

> Existem 7 sítios de metilação.
>
> Aqui temos outro exemplo de aninhamento.
>
> Chamamos a função `findall()`, procurando todas as correspondências de um sítio de metilação.
>
> Esta função retorna uma lista, a lista é passada para a função `len()`, que por sua vez retorna o número de elementos na lista.


__Vamos tentar__  
![tente agora](images/Try-It-Now.jpg)

1. Se você quiser encontrar apenas a primeira ocorrência de um padrão, que método você usa?

2. Se você quiser encontrar todas as ocorrências de um padrão, que método você usa?

3. Que operador vimos que reportará se uma correspondência exata está em uma sequência (string, lista, etc.)?

4. Que método de string vimos que contará o número de ocorrências de uma correspondência exata em uma string?


Vamos falar um pouco mais sobre todos os novos caracteres que vemos no padrão.

O padrão é composto por átomos. Cada átomo representa **UM** caractere.

#### Caracteres Individuais

| Átomo                              | Descrição                              |
| ---------------------------------- | ---------------------------------------- |
| a-z, A-Z, 0-9 e algumas pontuações | São caracteres comuns que correspondem a si mesmos |
| "."                                | O ponto, ou período. Isso corresponde a qualquer caractere único, exceto a nova linha. |


#### Classes de Caracteres

Um grupo de caracteres que podem ser correspondidos uma vez. Existem algumas classes predefinidas, que são símbolos que significam uma série de caracteres.

| Átomo  | Descrição                              |
| ----- | ---------------------------------------- |
| `[ ]` | Uma lista entre colchetes de caracteres, como `[GA]`. Isso indica que um único caractere pode corresponder a qualquer caractere na lista entre colchetes. |
| `\d`  | Dígitos. Também pode ser escrito como `[0-9]`      |
| `\D`  | Não dígitos. Também pode ser escrito como `[^0-9]`  |
| `\w`  | Caractere de palavra. Também pode ser escrito como `[A-Za-z0-9_]`. Note que o sublinhado faz parte dessa classe |
| `\W`  | Não é um caractere de palavra, ou `[^A-Za-z0-9_]` |
| `\s`  | Caractere de espaço em branco. Também pode ser escrito como `[ \r\t\n]`. Note o caractere de espaço após o primeiro `[` |
| `\S`  | Não é um espaço em branco. Também pode ser escrito como `[^ \r\t\n]`       |
| `[^]` | Um acento circunflexo dentro de uma lista entre colchetes de caracteres indica qualquer coisa, exceto os caracteres que o seguem |

#### Âncoras

Um padrão pode ser ancorado a uma região na string:

| Átomo | Descrição                              |
| ---- | ---------------------------------------- |
| `^`  | Corresponde ao início da string      |
| `$`  | Corresponde ao final da string            |
| `\b` | Corresponde a um limite de palavra entre `\w` e `\W` |

Exemplos:

```
c...a
```
> corresponde a "cobra", "cabra" e "caçar uma cabra" (duas vezes)


<br><br> 
```
\d\d\d-\d\d\d\d
```
> corresponde a 867-5309 e 5867-5309, mas não a 8-67-5309.

<br><br> 

```
^\d\d\d-\d\d\d\d
```
>  corresponde a 867-5309 e 867-53091, mas não a 5867-5309.
<br><br> 
```
^\d\d\d-\d\d\d\d$
```
> corresponde apenas a 3 dígitos seguidos de um traço seguido de 4 dígitos, nenhum caractere extra é permitido em qualquer lugar
<br><br> 



#### Quantificadores

Os quantificadores quantificam quantos átomos devem ser encontrados. Por padrão, um átomo corresponde apenas uma vez. Esse comportamento pode ser modificado seguindo um átomo com um quantificador.

| Quantificador | Descrição                              |
| ---------- | ---------------------------------------- |
| `?`        | o átomo corresponde zero ou exatamente uma vez        |
| `*`        | o átomo corresponde zero ou mais vezes          |
| `+`        | o átomo corresponde uma ou mais vezes           |
| `{3}`      | o átomo corresponde exatamente 3 vezes             |
| `{2,4}`    | o átomo corresponde entre 2 e 4 vezes, inclusive |
| `{4,}`     | o átomo corresponde pelo menos 4 vezes            |

Exemplos:   

```
ca?bra
```
> corresponde a "cabra" e "cbra". Também qualquer texto que contenha essas palavras.

```
c.+a
```
>  corresponde a "cabra", "cobra" e "covabra", entre outros.

```
c.*a
```
>  corresponde a "ca", "cabra", "ceeba" e "covabra", entre outros.

```
^\d{3}-\d{4}$
```
>  corresponde a números de telefone dos EUA (nenhum texto extra é permitido).

__Vamos tentar__  
![tente agora](images/Try-It-Now.jpg)

1. Qual seria um padrão para reconhecer um endereço de e-mail?
2. Qual seria um padrão para reconhecer a parte de ID de um registro de sequência em um arquivo FASTA?


#### Variáveis e Padrões

Variáveis podem ser usadas para armazenar padrões.

```python
>>> padrao = r"[GA]C.?G"
>>> len(re.findall(padrao, dna))
7
```
> Neste exemplo, armazenamos nosso padrão de metilação na variável chamada 'padrao' e a utilizamos como primeiro argumento para `findall`.


#### Ou

Um pipe '|' pode ser usado para indicar que o padrão antes ou depois do '|' pode ser correspondido. Coloque as duas opções entre parênteses.

```
grande (lobo|porquinho) mau
```
> Este padrão deve corresponder a uma string que contém:
>
> - "grande" seguido de um espaço seguido por
> -  *ou* "lobo" ou "porquinho" seguido de
> -  um espaço seguido de
> - "mau"
> 
> Isso corresponderia a:
>
> - "grande lobo mau"
> - "grande porquinho mau"

__Vamos Tentar__  
![tente agora](images/Try-It-Now.jpg)

1. Qual seria um padrão para reconhecer 'ATG' seguido de C ou um T?

#### Subpadrões

Subpadrões, ou partes do padrão contidas entre parênteses, podem ser extraídos e armazenados para uso posterior.

```
Quem tem medo do grande mau lobo(.+)f
```
> Este padrão possui apenas um subpadrão (.+)

Você pode combinar parênteses e quantificadores para quantificar subpadrões inteiros.


```
Quem tem medo do grande (mau )?lobo\?
```
> Isto corresponde a:
>
> - "Quem tem medo do grande mau lobo?"
> - Bem como "Quem tem medo do grande lobo?".
>
> O 'mau ' é opcional, ele pode estar presente 0 ou 1 vez em nossa string.
>
> Isso também mostra como corresponder literalmente a caracteres especiais. Use um '\\' para escapá-los.

__Vamos Tentar__  
![tente agora](images/Try-It-Now.jpg)

1. Que padrão você usaria para capturar o ID em um registro de sequência de um arquivo FASTA em um subpadrão.

Exemplo de registro de sequência FASTA.

```
  >ID Descrição Opcional
  SEQUÊNCIA
  SEQUÊNCIA
  SEQUÊNCIA 
```





#### Usando Subpadrões Dentro da Correspondência de Expressão Regular

Isso é útil quando você deseja encontrar um subpadrão e, em seguida, corresponder ao conteúdo novamente. Eles podem ser usados dentro da chamada da função e depois dela.

__Subpadrões dentro da chamada da função__

Uma vez que um subpadrão corresponde, você pode se referir a ele dentro da mesma expressão regular. O primeiro subpadrão se torna \\1, o segundo \\2, o terceiro \\3 e assim por diante.

```
Quem tem medo do l(.)b\1 mau
```
> Isso corresponderia a:
>
> -  "Quem tem medo do lobo mau"
> -  "Quem tem medo do laba mau"
> -  "Quem tem medo do lebe mau"  
>
> Mas não a:
>
> -  "Quem tem medo do loba mau"
> -  "Quem tem medo do labe mau" 


Da mesma forma,
```
\b(\w+)s adoram comida de \1
```
> Este padrão irá corresponder a:
>
> - "cachorros adoram comida de cachorro"  
> - Mas não a "cachorros adoram comida de macaco".  
>
> Fomos capazes de usar o subpadrão dentro da expressão regular usando `\1`
>
> Se houvesse mais subpadrões, eles seriam `\2`, `\3`, `\4`, etc.



#### Usando Subpadrões Fora da Expressão Regular

Os subpadrões podem ser recuperados após a chamada da função `search()`, ou fora da expressão regular, usando o método `group()`. Este é um método e pertence ao objeto que é retornado pela função `search()`.

Os subpadrões são recuperados por um número. Este será o mesmo número que poderia ser usado dentro da expressão regular, ou seja,

  - `\1` dentro do subpadrão pode ser usado fora com `search_found_obj.group(1)`
  - `\2` dentro do subpadrão pode ser usado fora com `search_found_obj.group(2)`
  - `\3` dentro do subpadrão pode ser usado fora com `search_found_obj.group(3)`  
  - e assim por diante


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
> 1. Este padrão reconhecerá um sítio de início de transcrição de consenso (TATTAT) 
> 2. E armazenará os 50 pares de bases a montante do sítio 
> 3. E os 25 pares de bases a jusante do sítio


Se você quiser encontrar as sequências a montante e a jusante de TODOS os sítios 'TATTAT', use a função `findall()`.
```python
>>> dna="ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG"
>>> found = re.findall( r"(.{50})TATTAT(.{25})"  , dna )
>>> print(found)
[('TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA', 'CCGGTTTCCAAAGACAGTCTTCTAA'), ('TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA', 'CCGGTTTCCAAAGACAGTCTTCTAA')]
```
> Os subpadrões são armazenados em tuplas dentro de uma lista. Mais sobre esse tipo de estrutura de dados mais tarde.

Outra opção para recuperar os subpadrões a montante e a jusante é colocar o `findall()` em um loop for

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
> 1. Este código executa a função `findall()` uma vez 
> 2. Os objetos de tupla são retornados 
> 3. Os subpadrões são armazenados nas variáveis a montante e a jusante 
> 4. O bloco for é executado  
> 5. O `findall()` busca novamente  
> 6. Uma correspondência é encontrada 
> 7. Novos subpadrões são retornados e armazenados nas variáveis a montante e a jusante
> 8. O bloco for de código é executado novamente 
> 9. O `findall()` busca novamente, mas nenhuma correspondência é encontrada  
> 10. O loop for termina  



Outra maneira de fazer isso é com um iterador, usando a função `finditer()` em um loop for. Isso permite que você não armazene todas as correspondências na memória. `finditer()` também permite que você recupere a posição da correspondência.

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
1. Este código executa a função `finditer()` uma vez.
2. O objeto de correspondência é retornado. Um objeto de correspondência terá todas as informações sobre a correspondência.
3. No bloco for, chamamos o método `group()` no primeiro objeto de correspondência retornado.
4. Imprimimos o primeiro e o segundo subpadrão usando o método `group()`.
5. A função `finditer()` é executada uma segunda vez e uma correspondência é encontrada.
6. O segundo objeto de correspondência é retornado.
7. Os segundos subpadrões são obtidos do objeto de correspondência usando o método `group()`.
8. A função `finditer()` é executada novamente, mas não são encontradas correspondências, portanto o loop termina.

#### Obtenha a posição do subpadrão com `finditer()`

O objeto de correspondência contém informações sobre a correspondência que podem ser recuperadas com métodos de correspondência como `start()` e `end()`

```python
#!/usr/bin/env python3

import re

dna="ACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGACAAAATACGTTTTGTAAATGTTGTGCTGTTAACACTGCAAATAAACTTGGTAGCAAACACTTCCAAAAGGAATTCACCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGG"

for found in re.finditer(r"(.{50})TATTAT(.{25})"  , dna):
  whole    = found.group(0)
  up       = found.group(1)
  down     = found.group(2)
  up_start = found.start(1) + 1   # é necessário converter da notação 0 para 1 
  up_end   = found.end(1) 
  dn_start = found.start(2) + 1
  dn_end   = found.end(2)

  print( whole , up , up_start, up_end , down , dn_start , dn_end , sep="\t" )
```
> podemos usar esses métodos de objeto de correspondência `group()`, `start()`, `end()` para obter a string, a posição de início e a posição de fim de cada subpadrão.

```
$ python3 re.finditer.pos.py
TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAA	TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA	98	148	CCGGTTTCCAAAGACAGTCTTCTAA	154	179
TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGATATTATCCGGTTTCCAAAGACAGTCTTCTAA	TCTAATTCCTCATTAGTAATAAGTAAAATGTTTATTGTTGTAGCTCTGGA	320	370	CCGGTTTCCAAAGACAGTCTTCTAA	376	401
```



**FYI:** A função `match()` é outra função de expressão regular que procura padrões. É semelhante à `search`, mas ela olha apenas para o início da string em busca do padrão, enquanto `search` procura em toda a string. Geralmente, `finditer()`, `search()` e `findall()` serão mais úteis.


#### Subpadrões e Ganância

Por padrão, as expressões regulares são "gananciosas". Elas tentam corresponder o máximo possível. Use o quantificador '?' para tornar a correspondência não gananciosa. A correspondência não gananciosa é chamada de 'preguiçosa'

```python
>>> str = 'The fox ate my box of doughnuts'
>>> found = re.search(r"(f.+x)",str)
>>> print(found.group(1))
fox ate my box
```
> O padrão f.+x não corresponde ao que você pode esperar, ele corresponde a partir de 'fox' até 'fox ate my box'. O '.+' é ganancioso. Ele encontra o máximo possível de caracteres entre 'f' e 'x'.

Vamos tornar essa correspondência preguiçosa usando '?'
```python
>>> found = re.search(r"(f.+?x)",str)
>>> print(found.group(1))
fox
```
> A correspondência agora é preguiçosa e corresponderá apenas a 'fox'

```python
>>> str = 'Atrás da porta torta tem uma porca morta'
>>> found = re.search(r"(p.+a)",str)
>>> print(found.group(1))
porta torta tem uma porca morta
```
> O padrão p.+a não corresponde ao que você pode esperar, ele corresponde a partir de 'porta' até 'porta torta tem uma porca morta'. O '.+' é ganancioso. Ele encontra o máximo possível de caracteres entre 'p' e 'a'.

Vamos tornar essa correspondência preguiçosa usando '?'
```python
>>> found = re.search(r"(p.+?a)",str)
>>> print(found.group(1))
porta
```
> A correspondência agora é preguiçosa e corresponderá apenas a 'porta'

#### Exemplo prático: Códons

A extração de códons de uma sequência de DNA pode ser realizada usando um subpadrão em uma função `findall()`. Lembre-se de que a função `findall()` retornará uma lista das correspondências.

```python
>>> dna = 'GTTGCCTGAAATGGCGGAACCTTGAA'
>>> codons = re.findall(r"(.{3})",dna)
>>> print(codons)
['GTT', 'GCC', 'TGA', 'AAT', 'GGC', 'GGA', 'ACC', 'TTG']
```

Ou você pode usar um loop for para fazer algo com cada correspondência.
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
> `finditer()` também funcionaria neste loop for. Cada códon pode ser acessado usando o método `group()`.

  

#### Verdade e correspondências de expressões regulares

As funções `search()`, `match()`, `findall()` e `finditer()` podem ser usadas em testes condicionais. Se uma correspondência não for encontrada, uma lista vazia ou 'None' é retornada. Ambos são Falsos.

```python
>>> found=re.search( r"(.{50})TATTATZ(.{25})"  , dna )
>>> if found:
...    print("encontrado")
... else:
...    print("não encontrado")
...
não encontrado
>>> print(found)
None
```
> None é False, então o bloco else é executado

 e "não encontrado" é impresso.


Aninhe isso!
```python
>>> 
>>> if re.search( r"(.{50})TATTATZ(.{25})"  , dna ):
...    print("encontrado")
... else:
...    print("não encontrado")
...
não encontrado
>>> print(found)
None
```



#### Usando expressões regulares em substituições

Anteriormente, vimos como encontrar um **padrão exato** e substituí-lo usando o método `replace()`. Para encontrar um padrão, ou correspondência inexata, e fazer uma substituição, é usada a função de expressão regular `sub()`. Esta função recebe o padrão, a substituição, a string a ser pesquisada, o número de vezes que a substituição deve ser feita e as flags.

```python
>>> str = "Quem tem medo do lobo mau?"
>>> re.sub(r'l.+o' , 'porquinho', str)
"Quem tem medo do porquinho mau?"
>>> print(str)
Quem tem medo do lobo mau?
```
> A função `sub()` retorna "Quem tem medo do porquinho mau?"
> O valor da variável `str` não foi alterado
> A nova string pode ser armazenada em uma nova variável para uso posterior.

Vamos salvar a nova string que é retornada em uma variável
```python
>>> str = "Ele tinha uma noiva."
>>> new_str = re.sub(r'n.+i' , 'cabra', str)
>>> print(new_str)
Ele tinha uma cabrava.
>>> print(str)
Ele tinha uma noiva.
```
> Os caracteres entre 'n' e 'i' foram substituídos por 'cabra'.
> A nova string é salva em `new_str`



#### Usando subpadrões na substituição

Às vezes, você deseja encontrar um padrão e usá-lo na substituição.
```python
>>> str = "Quem tem medo do lobo mau?"
>>> new_str = re.sub(r" do (\w+) (\w+)" , r" do \2 \1" , str)
>>> print(new_str)
Quem tem medo do mau lobo?
```
> Encontramos duas palavras depois de 'do' e trocamos a ordem.
> \\2 refere-se ao segundo subpadrão
> \\1 refere-se ao primeiro subpadrão

__Vamos tentar__  
![tente agora](images/Try-It-Now.jpg)

1. Como você usaria expressões regulares para encontrar todas as ocorrências de 'ATG' e substituir por '-M-' nesta sequência 'GCAGAGGTGATGGACTCCGTAATGGCCAAATGACACGT'?

#### Modificadores de opções de expressão regular

| Modificador               | Descrição                              |
| ---------------------- | ---------------------------------------- |
| `re.I` `re.IGNORECASE` | Executa correspondência sem diferenciação entre maiúsculas e minúsculas.      |
| `re.M` `re.MULTILINE`  | Faz com que $ corresponda ao final de uma linha (não apenas ao final da string) e faz com que ^ corresponda ao início de qualquer linha (não apenas ao início da string). |
| `re.S` `re.DOTALL`     | Faz com que um ponto (.) corresponda a qualquer caractere, incluindo uma nova linha. |
| `re.U`                 | Interpreta letras de acordo com o conjunto de caracteres Unicode. Esta bandeira afeta o comportamento de \w, \W, \b, \B. |
| `re.X` `VERBOSE`       | Essa bandeira permite que você escreva expressões regulares que parecem mais bonitas e sejam mais legíveis, permitindo separar visualmente seções lógicas do padrão e adicionar comentários. Os espaços em branco dentro do padrão são ignorados, exceto quando estão em uma classe de caracteres ou quando precedidos por uma barra invertida não escapada. Quando uma linha contém um # que não está em uma classe de caracteres e não é precedido por uma barra invertida não escapada, todos os caracteres do # mais à esquerda até o final da linha são ignorados. |

```python
>>> dna = "atgcgtaatggc"
>>> re.search(r"ATG",dna)
>>>
>>> re.search(r"ATG",dna , re.I)
<_sre.SRE_Match object; span=(0, 3), match='atg'>
>>>
```
> Podemos tornar nossa pesquisa insensível a maiúsculas e minúsculas usando a bandeira `re.I` ou `re.IGNORECASE`.


Você pode usar mais de uma bandeira concatenando-as com `|`. `re.search(r"ATG",dna , re.I|re.M)`


### Ferramentas de Expressões Regulares Úteis

Existem muitas ferramentas online para realmente ver o que está acontecendo em sua expressão regular. Procure por `Python Regular Expression Tester`

 - [regex101](https://regex101.com/)  
 - [pyregex](http://www.pyregex.com/)
 - [pythex](https://pythex.org/)

---


### [Link para o Python 7 Conjunto de Problemas](problemsets/Python_07_problemset.md)


## Python 8




### Estruturas de Dados

Às vezes, uma lista ou dicionário simples simplesmente não faz o que você quer. Às vezes, é necessário organizar dados de maneira mais complexa. Você pode aninhar qualquer tipo de dado dentro de qualquer outro tipo. Isso permite que você construa facilmente tabelas de dados multidimensionais.

#### Lista de listas

Listas de listas, frequentemente chamadas de matrizes, são importantes para organizar e acessar dados.

Aqui está uma maneira de criar uma tabela 3 x 3 de valores.

```python
>>> M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> M[1]  # segunda linha (começa com índice 0)
[4, 5, 6]
>>> M[1][2]  # segunda linha, terceiro elemento
6
```

Aqui está uma maneira de armazenar dados de alinhamento de sequência:

Quatro sequências alinhadas:

```
AT-TG
AATAG
T-TTG
AA-TA
```

O alinhamento em uma lista de listas.

```python
aln = [
    ['A', 'T', '-', 'T', 'G'],
    ['A', 'A', 'T', 'A', 'G'],
    ['T', '-', 'T', 'T', 'G'],
    ['A', 'A', '-', 'T', 'A']
]
```

Obtenha o comprimento total de uma sequência:

```python
>>> seq = aln[2]
>>> seq
['T', '-', 'T', 'T', 'G']
```

> Use o índice mais externo para acessar cada sequência.

Recupere o nucleotídeo em uma posição específica em uma sequência.

```python
>>> nt = aln[2][3]
>>> nt
'T'
```

> Use o índice mais externo para acessar a sequência de interesse e o índice mais interno para acessar a posição.

Obtenha todos os nucleotídeos em uma única coluna:

```python
>>> col = [seq[3] for seq in aln]
>>> col
['T', 'A', 'T', 'T']
```

> Recupere cada sequência da lista `aln` e, em seguida, a quarta coluna para cada sequência.

#### Listas de dicionários

Você também pode aninhar dicionários em listas:

```python
>>> records = [
... {'seq': 'actgctagt', 'accession': 'ABC123', 'genetic_code': 1},
... {'seq': 'ttaggttta', 'accession': 'XYZ456', 'genetic_code': 1},
... {'seq': 'cgcgatcgt', 'accession': 'HIJ789', 'genetic_code': 5}
... ]
>>> records[0]['seq']
'actgctagt'
>>> records[0]['accession']
'ABC123'
>>> records[0]['genetic_code']
1
```

> Aqui você pode recuperar o acesso de um registro por vez usando uma combinação do índice externo e a chave 'accession'.

#### Dicionários de listas

E, se você não adivinhou, você pode aninhar listas em dicionários.

Aqui está um dicionário de kmers. A chave é o kmer e seus valores são uma lista de posições.

```python
>>> kmers = {'ggaa': [4, 10], 'aatt': [0, 6, 12], 'gaat': [5, 11], 'tgga': [3, 9], 'attg': [1, 7, 13], 'ttgg': [2, 8]}
>>> kmers
{'tgga': [3, 9], 'ttgg': [2, 8], 'aatt': [0, 6, 12], 'attg': [1, 7, 13], 'ggaa': [4, 10], 'gaat': [5, 11]}
>>>
>>> kmers['ggaa']
[4, 10]
>>> len(kmers['ggaa'])
2
```

> Aqui, podemos obter uma lista das posições de um kmer usando o kmer como chave. Também podemos fazer coisas com a lista retornada, como determinar seu comprimento. O comprimento será o total de contagens desse kmer.

Você também pode usar o método `get()` para recuperar registros.

```python
>>> kmers['ggaa']
[4, 10]
>>> kmers.get('ggaa')
[4, 10]
```

> Essas duas declarações retornam os mesmos resultados, mas se a chave não existir, você obterá nada e não um erro.

#### Dicionários de dicionários

Dicionários de dicionários são os meus favoritos!! Você pode fazer tantas coisas úteis com essa estrutura de dados. Aqui estamos armazenando um nome de gene e alguns tipos diferentes de informações sobre esse gene, como sua sequência, comprimento, descrição, composição de nucleotídeos e comprimento.

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

> Aqui, armazenamos um nome de gene como a chave mais externa, com um segundo nível de chaves para características do gene, como sequência, comprimento, composição de nucleotídeos. Podemos recuperar uma característica usando o nome do gene e a característica em conjunto.

Para recuperar apenas a composição de nucleotídeos de um gene:

```python
>>> genes['gene1']['nt_comp']
{'C': 2, 'G': 1, 'A': 1, 'T': 2}
```

Altere a contagem de nucleotídeos de um gene com o operador de atribuição `=`:

```python
>>> genes['gene1']['nt_comp']
{'C': 2, 'G': 1, 'A': 1, 'T': 2}
>>>
>>> genes['gene1']['nt_comp']['T'] = 6
>>> genes['gene1']['nt_comp']
{'C': 2, 'G': 1, 'A': 1, 'T': 6}
```

Altere a contagem de nucleotídeos de um gene com o operador de atribuição `+=`:

```python
>>> genes['gene1']['nt_comp']
{'C': 2, 'G': 1, 'A': 1, 'T': 6}
>>>
>>> genes['gene1']['nt_comp']['A'] += 1
>>>
>>> genes['gene1']['nt_comp']
{'C': 2, 'G': 1, 'A': 2, 'T': 6}
>>>
>>>
```

Para recuperar a composição de A de todos os genes, use um loop for.

```python
>>> for gene in sorted(genes):
...   A_comp = genes[gene]['nt_comp']['A']
...   print(gene + ":", "As =", A_comp)
...
gene1: As= 2
gene2: As= 3
```

#### Construindo Estruturas de Dados Complexas

A seguir, um exemplo de construção de uma lista com uma coleção mista de tipos de valores. Lembre-se de que todos os elementos dentro de uma lista ou dicionário devem ser do mesmo tipo. Em outras palavras, os valores em uma lista devem ser todos listas, dicionários ou valores escalares. Isso permite que você faça loop sobre a estrutura de dados.

O dicionário, que é um valor de lista, tem uma chave que tem um dicionário como valor.

```
[{'gene1' : {'sequence' : [1, 2, 3], [4, 5, 6], [7,8,9]]
```

Apenas espaçado de maneira diferente:

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

Construindo esta estrutura de dados no interpretador:

```python
>>> new_data = []
>>> new_data
[]
>>> new_data.append([1, 2, 3])
>>> new_data
[[1, 2, 3]]
>>> new_data[0]
[1, 2, 3]
>>> new_data.append([4, 5, 6])
>>> new_data
[[1, 2, 3], [4, 5, 6]]
>>> new_data[1]
[4, 5, 6]
>>> new_data[1][2]
6
>>> new_data.append({})
>>> new_data
[[1, 2, 3], [4, 5, 6], {}]
>>> new_data[2]['key'] = 'value'
>>> new_data
[[1, 2, 3], [4, 5, 6], {'key': 'value'}]
>>> new_data[2]['key2'] = {}
>>> new_data
[[1, 2, 3], [4, 5, 6], {'key2': {}, 'key': 'value'}]
>>> new_data[2]['key2']['something_new'] = 'Yay'
>>> new_data
[[1, 2, 3], [4, 5, 6], {'key2': {'something_new': 'Yay'}, 'key': 'value'}]
>>>
```

O mesmo exemplo em um arquivo de script: [Building Complex Datastructures](scripts/building_datastructures.py)

**Organização e Contagem de Camisetas do Curso**

Temos uma planilha com o estilo, tamanho e cor de todos. Queremos saber quantas de cada combinação única de estilo-tamanho-cor precisamos encomendar.

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

Queremos algo assim:

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
with open("shirts.txt", "r") as file_object:
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
      print(style, size, color, count, sep="\t")

```

Saída:
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

É assim que se parece a estrutura de dados que acabamos de construir.

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



Também existem bibliotecas específicas para manipulação de tabelas e quadros de dados, como o [Pandas](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html).

Aqui é uma [introdução](https://pandas.pydata.org/pandas-docs/stable/dsintro.html) às estruturas de dados no Pandas.

E também há um [tutorial interativo](https://www.learnpython.org/en/Pandas_Basics)

---
### [Link to Python 8 Problem Set](problemsets/Python_08_problemset.md)

## Python 9
### Exceções


Existem alguns diferentes tipos de erros enquanto estamos programando. Erros de sintaxe, erros de lógica e exceções. Você provavelmente já encontrou todos os três. Erros de sintaxe e lógica são problemas com os quais você precisa lidar enquanto está programando. Uma exceção é um tipo especial de erro que pode ser informativo e usado para escrever códigos para responder a esse tipo de erro. Isso é especialmente relevante ao lidar com a entrada do usuário. E se ele não lhe der nenhuma, ou é o tipo errado de entrada. Nós queremos que nosso código seja capaz de detectar esses tipos de erros e responda adequadamente.

```python
#!/usr/bin/env python3

import sys
file = sys.argv[1]

print("User provided file:" , file)
```
> Este código aceita uma entrada fornecida pelo usuário e a imprime.

Execute-o.

```
$ python scripts/exceptions.py test.txt
User provided file: test.txt
```

O que acontece se o usuário não fornecer nenhuma entrada e tentar imprimi-la?

```bash
$ python scripts/exceptions.py
Traceback (most recent call last):
  File "scripts/exceptions.py", line 4, in <module>
    file = sys.argv[1]
IndexError: list index out of range 
```
> Obtemos uma exceção **IndexError** exception, a qual é gerada quando o índice não é encontrado em uma sequência.


Já vimos várias exceções ao longo dos capítulos, aqui estão algumas:
  - ValueError: erro de domínio matemático
  - AttributeError: o objeto 'list' não tem o atributo 'rstrip'
  - SyntaxError: EOL ao analisar a string literal
  - NameError: o nome 'GGTCTAC' não está definido
  - SyntaxError: parênteses ausentes na chamada para 'print'
  - AttributeError: o objeto 'int' não tem atributo 'lower'
  - IndexError: índice de atribuição de lista fora de alcance
  - NameError: o nome 'HDAC' não está definido

[Link para a Documentação de Python sobre tipos de exceções integradas](https://www.tutorialspoint.com/python3/python_exceptions.htm)

Podemos usar a exceção à nosso favor para ajudar as pessoas que estão executando o código. Podemos usar a condição try/except como um bloco if/else para procurar exceções e executar um código específico se **não tivermos** uma exceção e fazer algo diferente se **tivermos** uma exceção.

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
> Precisamos "tentar" obter um argumento fornecido do usuário. Caso seja um sucesso então podemos imprimi-lá. Caso tentemos e falhemos, nós executamos o código na parte da "exceção" do nosso bloco try/except e imprimimos que precisamos do nome do arquivo.

Vamos executá-lo COM entrada do usuário
```bash
$ python3 scripts/exceptions_try.py test.txt
User provided file: test.txt
```
> Funciona como esperado

Vamos executá-lo SEM entrada do usuário
```bash
$ python scripts/exceptions_try.py
Please provide a file name
```
> Sim, o usuário é informado de que precisa fornecer um nome de arquivo para o script


E se o usuário fornecer uma entrada mas ela não é um arquivo válido ou o caminho está incorreto? Ou se você quer verificar se o usuário forneceu a entrada, e se é possível abrir a entrada.

Podemos adicionar múltiplos testes de exceção, como blocos if/elif. Cada declaração de "exceção" pode especificar que tipo de exceção está esperando para receber. Se esse tipo de exceção ocorrer, esse bloco do código será executado.
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
> Aqui testamos um IndexError: Gerado quando um índice não é encontrado em uma sequência.
> O IndexError ocorre quando tentamos acessar um elemento de lista que não existe.
> E testamos um IOError: Gerado quando uma operação de entrada/saída falha, como a instrução print ou a função open() ao tentar abrir um arquivo que não existe.
> O IOError ocorre quando tentamos acessar um arquivo que não existe.


Vamos executá-lo com um arquivo que não existe.
```
$ python scripts/exceptions_try_files.py test.txt
User provided file name: test.txt
Can't find file: test.txt
```
> Isso informa ao usuário que eles forneceram uma entrada, no entanto, que o arquivo listado não pode ser encontrado.


Vamos executá-lo sem nenhuma entrada
```bash
$ python scripts/exceptions_try_files.py
Please provide a file name
```
> Isso informa ao usuário que ele precisa fornecer um arquivo.

#### try/except/else/finally

Vamos resumir o que cobrimos e adicionar `else` e `finally`.

```
try:
  # o bloco try é executado até que uma exceção seja gerada
except _ExceptionType_:
  # se houver uma exceção do tipo "ExceptionType", este bloco será executado
  # pode haver mais de um bloco except, assim como um elif
except:
  # se houver exceções que não sejam do tipo "ExceptionType", este bloco except será executado
else: 
  # o bloco else é executado após a conclusão do bloco try, o que significa que nenhuma exceção foi gerada
finally:
  # o bloco finally é executado se exceções forem ou não geradas (não importa o que aconteça)
```

#### Obtendo mais informação sobre uma exceção

Algumas exceções podem ser lançadas por múltiplos motivos, por exemplo, ErrorIO ocorrerá se o arquivo não existir, assim como se você não tiver permissões para lê-lo. Podemos obter mais informação observando o conteúdo dos nosso Objetos de Exceção. Sim, uma exceção é um objeto também! Os erros do sistema são armazenados no objeto de exceção. Para acessar o objeto use `as` e forneça um nome de variável, como 'ex'.
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
> Aqui nós adicionamos `except IOError as ex` e agora nós obtemos a mensagem de 'strerror' de ex.

Execute.
```bash
$ python scripts/exceptions_try_files_as.py  test.txt
User provided file name: test.txt
Can't find file: test.txt :  No such file or directory
```
> Agora nós sabemos que esse nome de arquivo ou o caminho não é válido


#### Gerando uma Exceção

Nós podemos chamar ou gerar exceções também!! Isso é feito usando uma instrução `raise`

1. Primeiro, criamos um novo objeto de exceção, ou seja, `ValueError()`
2. Use o objeto de exceção em uma frase com "Raise" `raise ValueError('your message')`

Vamos gerar uma exceção se o nome do arquivo não terminar em 'fa'
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
> Aqui geramos uma exceção conhecida, 'ValueError', se o arquivo não terminar com (usamos o método `endswith()`). 

Vamos executá-lo.
``` bash
$ python scripts/exceptions_try_files_raise.py test.txt
User provided file name: test.txt
Traceback (most recent call last):
  File "scripts/exceptions_try_files_raise.py", line 10, in <module>
    raise ValueError("Not a FASTA file")
ValueError: Not a FASTA file
```
> Nossa exceção é gerada, agora vamos fazer algo com ela.

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
> Aqui criamos uma exceção para capturar qualquer ValueError.

Vamos executá-lo.
```bash
$ python scripts/exceptions_try_files_raise_value.py test.txt
User provided file name: test.txt
File needs to be a FASTA file and end with .fa
```
> Agora temos uma ótima mensagem de erro.

Mas e se houver outro ValueError, como podemos saber se tem algo a ver com a extensão do arquivo FASTA ou não? Resposta: a mensagem será diferente.

#### Criando Exceções Personalizadas

Podemos criar nossa própria exceção personalizada. Precisaremos criar uma nova classe de exceção. Abaixo está a sintaxe para fazer isso.

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
> Aqui criamos uma nova classe de exceção chamada 'NotFASTAError'. Em seguida, levantamos esta nova exceção.

Vamos executá-lo.
```bash
$ python scripts/exceptions_try_files_raise_try.py test.txt
User provided file name: test.txt
File needs to be a FASTA file and end with .fa
```
> Nossa nova classe de exceção, NotFASTAError, funciona da mesma forma que as exceções integradas.



---

### [Link para o Conjunto de Problemas Python 9](problemsets/Python_09_problemset.md)



---
## Python 10

### Funções

Funções consistem em várias linhas de código que fazem algo útil e que você deseja executar mais de uma vez. Existem funções integradas em Python. Você também pode escrever as suas próprias. Além disso, você dá um nome à sua função para poder se referir a ela em seu código. Isso evita copiar e colar o mesmo código em muitos lugares em seu script e torna seu código mais fácil de ler.

Vamos ver alguns exemplos.

Python tem funções integradas

```python
>>> print('Hello world!')
Hello world!
>>> len('AGGCT')
5
```

Você pode definir suas próprias funções com `def`. Vamos escrever uma função que calcula o conteúdo de GC. Vamos definir isso como a fração de nucleotídeos em uma sequência de DNA que são G ou C. Isso pode variar de 0 a 1.

Primeiro, podemos olhar para o código que faz o cálculo, depois podemos converter essas linhas de código em uma função.

Código para encontrar o conteúdo de GC:
```python
dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCT'
c_count = dna.count('C')  # count é um método de string
g_count = dna.count('G')
dna_len = len(dna) # len é uma função
gc_content = (c_count + g_count) / dna_len # fração de 0 a 1
print(gc_content)
```
#### Definindo uma Função que Calcula o Conteúdo de GC

Usamos `def` para definir nossa própria função. É seguido pelo nome da função (`gc_content`) e parâmetros que serão inseridos entre parênteses. Um dois pontos é o último caractere na linha `def`. As variáveis de parâmetro estarão disponíveis para o seu código dentro da função para usar.

```python
def gc_content(dna):   # dê um nome à nossa função e ao parâmetro 'dna'
   c_count = dna.count('C')
   g_count = dna.count('G')
   dna_len = len(dna)
   gc_content = (c_count + g_count) / dna_len
   return gc_content # retorna o valor para o código que chamou esta função
```
> Aqui está uma função personalizada que você pode usar como uma função integrada do Python

#### Usando sua função para calcular o conteúdo de GC

Isso é igual a qualquer outra função python. Você escreve o nome da função com quaisquer variáveis que deseja passar para a função entre parênteses. No exemplo abaixo, o conteúdo de `dna_string` é passado para `gc_content()`. Dentro da função, esses dados são passados para a variável `dna`.

```python
dna_string = "GTACCTTGATTTCGTATTCTGAGAGGCTGCT"
print(gc_content(dna_string))
```
Este código imprimirá 0,45161290322580644 na tela. Você pode salvar esse valor em uma variável para usar posteriormente em seu código, assim:

```python
dna_gc = gc_content('GTACCTTGATTTCGTATTCTGAGAGGCTGCT')
```

Como você pode ver, podemos escrever uma linha de código python clara e, como a função tem um nome que descreve o que ela faz, é fácil entender como o código funciona. Não dê nomes às suas funções como esta `def my_function(a):`!

Como você poderia converter a fração GC em % GC. Use `format()`.

```python
dna_string = "GTACCTTGATTTCGTATTCTGAGAGGCTGCT"
dna_gc = gc_content(dna_string)
pc_gc = '{:.2%}'.format(dna_gc)
print('This sequence is' , pc_gc , 'GC')
```

Aqui está a saída

```python
This sequence is 45.16% GC
```

#### Os detalhes

1. Você define uma função com `def`. Você precisa definir uma função antes de poder chamá-la.
2. A função deve ter um nome. Este nome deve descrever claramente o que a função faz. Aqui está o nosso exemplo `gc_content`.
3. Você pode passar variáveis para funções, mas não é obrigatório. Na linha de definição, você coloca as variáveis que sua função precisa entre parênteses, assim `(dna)`. Esta variável existe apenas dentro da função.
4. A primeira linha da função deve terminar com um `:` para que a linha completa de definição da função pareça com isso ```def gc_content(dna):```
5. As próximas linhas de código, o corpo da função, precisam estar indentadas. Este código compreende o que a função faz.
6. Você pode retornar um valor como a última linha da função, mas isso não é obrigatório. Esta linha `return gc_content` no final da definição de nossa função passa o valor de conteudo_gc de volta para o código que chamou a função em seu script principal.


#### Nomeando Argumentos

Você pode nomear suas variáveis de argumento como quiser, mas o nome deve descrever os dados contidos. O nome precisa ser consistente dentro de sua função.

#### Argumentos de Palavra-chave

Argumentos podem ser nomeados e esses nomes podem ser usados quando a função é chamada. Este nome é chamado de 'palavra-chave'

```python
>>> dna_string = "GTACCTTGATTTCGTATTCTGAGAGGCTGCT"
>>> print(gc_content(dna_string))
0.45161290322580644
>>> print(gc_content(dna=dna_string)
0.45161290322580644

```
> A palavra-chave deve ser a mesma que o argumento definido da função. Se uma função tiver múltiplos argumentos, usar a palavra-chave permite chamar a função com os argumentos em qualquer ordem.

#### Valores Padrão para Argumentos

Como definido acima, nossa função está esperando um argumento (`dna`) na definição. Você recebe um erro se chamar a função sem quaisquer parâmetros.

```python
>>> gc_content()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: gc_content() missing 1 required positional argument: 'dna'

```

Você pode definir valores padrão para argumentos quando definir sua função.

```python
def gc_content(dna='N'):   # dê um nome à nossa função e parâmetro 'dna'
   c_count = dna.count('C')
   g_count = dna.count('G')
   dna_len = len(dna)
   gc_content = (c_count + g_count) / dna_len
   return gc_content # retorna o valor para o código que chamou esta função

```
> Se você chamar a função sem argumentos, o padrão será usado. Neste caso, um padrão é bastante inútil, e a função retornará '0' se chamada sem fornecer uma sequência de DNA.

#### Expressões Lambda

Expressões Lambda podem ser usadas para definir funções simples (de uma linha). Existem alguns usos para lambda que não vamos discutir aqui. Estamos mostrando a você porque às vezes você vai encontrar.

Aqui está uma função personalizada de uma linha, como as funções sobre as quais já falamos:    
```python
def get_first_codon(dna):
  return dna[0:3]

print(get_first_codon('ATGTTT'))
```
> Isso imprimirá `ATG`

Aqui está a mesma função escrita como uma lambda
```python
get_first_codon = lambda dna : dna[0:3]
print(get_first_codon('ATGTTT'))
```
> Isso também imprime `ATG`. lambdas só podem conter uma linha e não há instrução de `return`.

Compreensões de lista frequentemente podem ser usadas em vez de lambdas e podem ser mais fáceis de ler. Você pode ler mais sobre `lambda`, particularmente em relação ao `map` que irá realizar uma operação em uma lista, mas geralmente um laço `for` é mais fácil de ler.

### Escopo

Quase todas as variáveis Python são globais. Isso significa que estão disponíveis em todo o seu código. Lembre-se de que os blocos Python são definidos como código no mesmo nível de indentação.

```python
#!/usr/bin/env python3
print('Antes do bloco if')
x = 100
print('x=',x)
if True:  # esta condição if será sempre Verdadeira     
  # queremos garantir que o bloco seja executado
  # para que possamos mostrar o que acontece
  print('Dentro do bloco if')
  x = 30
  y = 10
  print("x=", x)
  print("y=", y)

print('Após o bloco if')
print("x=", x)
print("y=", y)


```

Vamos executar:
```bash
$ python3 scripts/scope.py
Antes do bloco if
x= 100
Dentro do bloco if
x= 30
y= 10
Após o bloco if
x= 30
y= 10

```

A exceção mais importante às variáveis serem globais é que variáveis definidas em **funções** são **locais**, ou seja, existem apenas dentro de sua função. Dentro de uma função, as variáveis globais são visíveis, mas é melhor passar variáveis para uma função como argumentos.

```python
def show_n():
  print(n)
n = 5
show_n()
```

A saída é esta `5`, como você esperaria, mas o exemplo abaixo é uma prática de programação melhor. Por quê? Veremos um pouco mais tarde.

```python3
def show_n(n):
  print(n)
n = 5
show_n(n)
```



#### Variáveis Locais

Variáveis dentro de funções são locais e, portanto, só podem ser acessadas de dentro do bloco da função. Isso se aplica tanto a argumentos quanto a variáveis definidas dentro de uma função.


```python
#!/usr/bin/end python3

def set_local_x_to_five(x):
  print('Dentro de def')
  x = 5 # localmente para set_local_x_to_five()
  y=5   # também local
  print("x =",x)
  print("y = ",y)

print('Após def')
x = 100 # global x
y = 100 # global
print('x=',x)
print('y=',y)

set_local_x_to_five(500)
print('Após chamada da função')
print('x=',x)
print('y=',y)

```
Aqui adicionamos uma função `set_local_x_to_five` com um argumento chamado 'x'. Esta variável existe apenas dentro da função, onde substitui qualquer variável com o mesmo nome fora do `def`. Dentro do `def`, também inicializamos uma variável `y` que substitui qualquer `y` global dentro do `def`.

Vamos executá-lo:
```bash
$ python3 scope_w_function.py
Após def
x= 100
y= 100
Dentro de def
x = 5
y =  5
Após chamada da função
x= 100
y= 100



```
> Há uma variável global, `x` = 100, mas quando a função é chamada, ela cria uma nova variável local, também chamada `x`, com valor = 5. Esta variável desaparece depois que a função termina e voltamos a usar a variável global `x` = 100. O mesmo vale para `y`.

#### Global

Você pode tornar uma variável local global com a declaração `global`. Agora, uma variável que você usa em uma função é a mesma variável no restante do código. É melhor não definir nenhuma variável como global até que você saiba que precisa, porque você pode modificar o conteúdo de uma variável sem querer.

Aqui está um exemplo de uso do `global`.

```python
#!/usr/bin/env python3

def set_global_variable():
  global greeting  # torna a variável "greeting" global
  greeting = "Eu digo olá"


greeting = 'Bom dia'
print('Antes da chamada de função')
print('greeting =',greeting)

#fazendo a chamada da função
set_global_variable()
print('Após a chamada de função')
print('greeting =',greeting)

```
Vamos olhar a saída!


```bash
$ python3 scripts/scope_global.py
Antes da chamada de função
greeting = Bom dia
Após a chamada de função
greeting = Eu digo olá

```
> Observe que a função alterou o valor da variável global. Pode ser algo que você não queira fazer.

Ao criar novas variáveis locais dentro das definições de função, o Python impede que variáveis com o mesmo nome se sobreponham por engano.

### Módulos

O Python vem com algumas funções e métodos principais. Existem muitos módulos úteis que você desejará usar. `import` é a declaração para informar ao seu script que você deseja usar código em um módulo. Como já vimos com expressões regulares, você pode trazer código que manipula expressões regulares com `import re`.

#### Obtendo informações sobre módulos com `pydoc`

Como você obtém informações sobre um módulo? O Python possui páginas de ajuda incorporadas na linha de comando, como `man` que encontramos anteriormente na palestra sobre Unix. As informações online podem ser mais atualizadas. Pesquise em https://docs.python.org/3.6/. Mas se você não tiver acesso à internet, sempre pode usar `pydoc`. Para saber mais sobre o módulo `re`, digite `pydoc re` na linha de comando. A última linha na saída informa onde o módulo Python está instalado.

```bash
% pydoc re
Ajuda sobre o módulo re:

NOME
    re - Suporte para operações de correspondência de expressões regulares (RE).

REFERÊNCIA DO MÓDULO
    https://docs.python.org/3.6/library/re
    
    A seguinte documentação é gerada automaticamente dos arquivos-fonte do Python.
    Pode estar incompleta, incorreta ou incluir recursos considerados detalhes de implementação e que podem variar entre as implementações do Python.
    Em caso de dúvida, consulte a referência do módulo no local indicado acima.

DESCRIÇÃO
    Este módulo fornece operações de correspondência de expressões regulares semelhantes às encontradas em Perl. Ele oferece suporte a strings de 8 bits e Unicode; tanto o padrão quanto as strings processadas podem conter bytes nulos e caracteres fora da faixa ASCII dos EUA.
    
    As expressões regulares podem conter caracteres especiais e ordinários.
    A maioria dos caracteres comuns, como "A", "a" ou "0", são as expressões regulares mais simples; eles simplesmente correspondem a si mesmos. Você pode
    concatenar caracteres comuns, então o último corresponde à string 'last'.
...
ARQUIVO
    /anaconda3/lib/python3.6/glob.py

```

Aqui estão alguns dos módulos mais comuns e úteis, juntamente com seus métodos e objetos. É um tour rápido.

#### os.path

`os.path` possui utilitários comuns para trabalhar com caminhos de arquivos (nomes de arquivos e diretórios). Um caminho é uma lista de diretórios (geralmente terminando com um nome de arquivo) que diz onde encontrar um arquivo ou diretório.

| função                 | descrição                              |
| ---------------------- | -------------------------------------- |
| os.path.basename(path) | qual é o último elemento do caminho? Observe que `/home/tmp/` retorna `''`, em vez de `tmp` |
| os.path.dirname(path)  | qual é o diretório em que o arquivo está? |
| os.path.exists(path)   | o caminho existe?                       |
| os.path.getsize(path)  | retorna o tamanho do caminho (arquivo) em bytes ou erro |
| os.path.isfile(path)   | o caminho aponta para um arquivo?       |
| os.path.isdir(path)    | o caminho aponta para um diretório?     |
| os.path.splitext(path) | divide antes e depois da extensão do arquivo (por exemplo, '.txt') |



#### os.system

Substituído por subprocess.



#### subprocess

Este é o módulo atual para executar linhas de comando a partir de scripts Python


```python
import subprocess
subprocess.run(["ls","-l"])  # o mesmo que executar ls -l na linha de comando
```

Mais complexo que `os.system()`. Você precisa especificar onde a entrada e a saída vão. Vamos olhar sobre isso com mais mais detalhes

##### Capturando a saída de um pipeline de shell

Digamos que queremos encontrar todos os arquivos que têm o usuário amanda (ou no nome do arquivo)

`ls -l | grep amanda`

torna-se este 'atalho' que capturará a saída dos dois comandos unix na variável `output`

```python
import subprocess
output = subprocess.check_output('ls -l | grep amanda', shell = True)
```

Isso é melhor do que alternativas com `subprocess.run()`. Isso é equivalente à string unix citada com backtick.

`output` contém um objeto de bytes (mais ou menos uma string de codificações de caracteres ASCII)

```python
b'-rw-r--r--  1 amanda  staff       161952 Oct  2 18:03 test.subreads.fa\n-rw-r--r--  1 amanda  staff          126 Oct  2 13:23 test.txt\n'
```

Você pode converter decodificando o objeto de bytes em uma string

```python3
>>>output.decode('utf-8')
'-rw-r--r--  1 amanda  staff       161952 Oct  2 18:03 test.subreads.fa\n-rw-r--r--  1 amanda  staff          126 Oct  2 13:23 test.txt\n'
```

##### Capturando a saída do jeito longo (para um único comando)

Vamos supor que `ls -l` gera alguma saída algo assim

```
total 112
-rw-r--r--  1 amanda  staff           69 Jun 14 17:41 data.cfg
-rw-r--r--  1 amanda  staff       161952 Oct  2 18:03 test.subreads.fa
-rw-r--r--  1 amanda  staff          126 Oct  2 13:23 test.txt
```

Como nós executamos `ls -l` no Python e capturamos a saída (stdout)?

```python3
import subprocess
rtn = subprocess.run(['ls','-l'], stdout=subprocess.PIPE )  # especifique que você deseja capturar STDOUT
bytes = rtn.stdout
stdout = bytes.decode('utf-8')
# algo como
lines = stdout.splitlines()
```

`lines` agora contêm elementos de cada linha da saída de `ls -l`, incluído a linha do cabeçalho, que não é um arquivo

```python3
>>> lines[0]
'total 112'
>>> lines[1]
'-rw-r--r--  1 amanda  staff     69 Jun 14 17:41 data.cfg'
```



##### Verifique o status da saída do comando

Para executar um comando e verificar o status da saída (realmente para verificar se o status da saída foi ok ou zero) use

```python
oops = subprocess.check_call(['ls', '-l'])
# ou, simplesmente...
oops = subprocess.check_call('ls -l', shell=True)
```

##### Executar um comando que redireciona stdout para um arquivo usando subprocess do Python

Você não pode escrever `ls -l > listing.txt` para redirecionar stdout no método subprocess, então use isso

```python
 tmp_file = 'listing.txt'
 with open(tmp_file,'w') as ofh:
     oops = subprocess.check_call(['ls', '-l'], stdout=ofh )
```



#### sys


Algumas variáveis úteis para iniciantes. Muitos mais parâmetros e configurações avançadas do sistema que não estamos cobrindo aqui.

| função | descrição                            |
| ------ | ------------------------------------ |
| sys.argv | lista de parâmetros da linha de comando |
| sys.path | onde o Python deve procurar módulos |



#### re

Consulte as notas sobre expressões regulares

#### collections

Listas etc. melhores

`from collections import deque`

#### copy
`copy.copy()`

e

`copy.deepcopy()`

[Link para mais informações sobre cópia profunda vs. cópia rasa](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/)

#### math

| função            | descrição |
| ------------------- | ----------- |
| math.exp()          | e**x        |
| math.log2()         | log base 2  |
| math.log10()        | log base 10 |
| math.sqrt()         | raiz quadrada |
| math.sin()          | seno        |
| math.pi(), math.e() | constantes   |
| etc                 |             |

veja também numpy

#### random
Números aleatórios gerados por computadores não são verdadeiramente aleatórios, então o Python os chama de pseudo-aleatórios.

| exemplo                 | descrição                                                  |
| ----------------------- | ------------------------------------------------------------ |
| random.seed(1)          | define a semente inicial para a sequência pseudo-aleatória como 1 para possibilitar a reprodutibilidade |
| random.randrange(9)     | inteiro entre 0 e 8                                       |
| random.randint(1,5)     | inteiro entre 1 e 5                                       |
| random.random()         | float entre 0 e 1                                         |
| random.uniform(1,2)     | float entre 1 e 2                                         |
| random.choice(my_genes) | retorna um elemento aleatório da sequência                |

Para obter um índice aleatório de um elemento de `list`, use `i=random.randrange(len(list))`

#### statistics

Quantidades estatísticas típicas

| exemplo                         | descrição                              |
| ------------------------------- | ---------------------------------------- |
| statistics.mean([1,2,3,4,5])    | média ou média                          |
| statistics.median([ 2,3,4,5])   | mediana = 3,5                           |
| statistics.stdev([1,2,3,4,5])   | desvio padrão da amostra (raiz quadrada da variância da amostra) |
| statistics.pstdev([1,2,3,4,5]) | estimativa do desvio padrão da população |

#### glob

Realiza expansão de caminho de arquivo com curingas semelhantes ao Unix.

```python
>>> import glob
>>> glob.glob('pdfs/*.pdf')
['pdfs/python1.pdf', 'pdfs/python2.pdf', 'pdfs/python3.pdf', 'pdfs/python4.pdf', 'pdfs/python6.pdf', 'pdfs/python8.pdf', 'pdfs/unix1.pdf', 'pdfs/unix2.pdf']
>>> fasta_files = glob.glob('sequences/*.fa')
>>> 
```


#### argparse

Ferramenta excelente (embora bastante complicada) para analisar argumentos da linha de comando e gerar automaticamente mensagens de ajuda para scripts (muito útil!). Aqui está um script simples que explica um pouco do que ele faz.

```python
#!/usr/bin/env python3
import argparse
parser = argparse.ArgumentParser(description="A test program that reads in some number of lines from an input file. The output can be screen or an output file")
# queremos que o primeiro argumento seja o nome do arquivo
parser.add_argument("file", help="path to input fasta filename")
# segundo argumento será o número da linha
# o tipo padrão é string, precisa especificar se espera um inteiro
parser.add_argument("lines", type=int, help ="how many lines to print")
# argumento outfile opcional especificado com -o ou --out
parser.add_argument("-o","--outfile", help = "optional: supply output filename, otherwise write to screen", dest = 'out')
args = parser.parse_args()
# os argumentos aparece em args
filename = args.file
lines = args.lines
if args.out:
  print("writing output to", args.out)
```

Com este módulo, a ajuda -h vem de graça. Os argumentos --outfile são opcionais, a menos que você escreva 'required=True', assim

```
parser.add_argument('-f', "-fasta", required=True, help='Output fasta filename', dest='outfile')

```





### Muitos outros módulos que realizam diversas funções

Tempo, HTML, XML, e-mail, CGI, soquetes, áudio, interfaces gráficas de usuário com Tk, depuração, teste, utilitários Unix.

Além disso, são essenciais: BioPython para bioinformática, Numpy para matemática e estatísticas, pandas para dados, scikit-learn para aprendizado de máquina.

---

### [Link para o Conjunto de Problemas Python 10](problemsets/Python_10_problemset.md)

---


## Python 11

### Classes

As vantagens de escrever classes e escrever funções são muito semelhantes.

Quando escrevemos funções, agrupamos funções principais do Python e métodos para criar uma coleção única de instruções que ocorrem em uma ordem específica.

Essas novas funções tornam nosso código mais fácil de ler e escrever, especialmente se você for usar a função muitas vezes.

Uma diferença conceitual entre uma função e uma classe é que uma função geralmente faz uma coisa, enquanto uma classe fará muitas coisas relacionadas para ajudar a resolver um problema.

O que é uma classe de verdade, o que ela faz? Uma classe na verdade não faz nada, exceto definir uma lista de regras para criar um novo objeto personalizado. Toda vez que você usa a classe, está criando uma instância de um tipo de objeto.

#### Você tem usado classes para criar objetos

Você já tem usado classes para criar objetos. Aqui estamos usando a função `open` para criar duas instâncias de um objeto de arquivo. Uma instância contém informações sobre um arquivo FASTA enquanto a outra contém informações sobre um arquivo GFF.

```python
fa_input = open("somedata.fa")
gff_input = open("somedata.gff")
```


#### Atributos e Métodos

Classes criam objetos, e esses objetos terão atributos e métodos associados a eles.



__Métodos__

Métodos são funções que pertencem a objetos de uma classe específica.

__Atributos__

Atributos são variáveis que estão associadas a um objeto de uma classe específica.

 

#### Criando uma Classe

Definir uma classe é objetivo.

O primeiro passo é decidir quais atributos e quais métodos ela terá.



__Criar uma Classe DNARecord__

Quando criamos uma classe, na verdade estamos estabelecendo uma série de regras que um objeto DNARecord deve seguir.

Regras do DNARecord:
1. O DNARecord deve ter uma sequência [atributo]
2. O DNARecord deve ter um nome [atributo]
3. O DNARecord deve ter um organismo [atributo]
4. O DNARecord será capaz de calcular o conteúdo de AT [método]
5. O DNARecord será capaz de calcular o complemento reverso [método]


Aqui está o primeiro rascunho, mas não final, da nossa classe. Vamos passar por cada seção deste código abaixo:


```python
class DNARecord(object):
  # definir atributos da classe
  sequence = 'ACGTAGCTGACGATC' 
  gene_name = 'ABC1'
  species_name = 'Drosophila melanogaster'
  
  # definir métodos
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

## criar um novo objeto DNARecord
dna_rec_obj = DNARecord() 

## Use o novo objeto DNARecord
print('Um novo registro para ' + dna_rec_obj.gene_name + ' foi criado de ' + dna_rec_obj.species_name) 
print('AT é ' + str(dna_rec_obj.get_AT()))
print('A fita complementar é ' + dna_rec_obj.reverse_complement())
```

Agora vamos passar por cada seção:

Começamos com a palavra-chave `class`, seguida pelo nome da nossa classe `DNARecord` com o nome da classe base entre parênteses `object`.

```python
class DNARecord(object):
```



Em seguida, definimos os atributos da classe. Estas são variáveis com dados que pertencem à classe e, portanto, a qualquer objeto que seja criado usando esta classe.

```python
  # definir atributos da classe
  sequence = 'ACGTAGCTGACGATC' 
  gene_name = 'ABC1'
  species_name = 'Drosophila melanogaster' 
```


A seguir, definimos nossos métodos de classe:

```python
  # define métodos
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

Os métodos estão usando um argumento chamado `self`, ou seja, `length = len(self.sequence)`. Esta é uma variável especial que você usa dentro de uma classe. Com ela, você pode acessar todos os dados que estão contidos dentro do objeto quando ele é criado.

Use o formato `self.attribute` para recuperar o valor das variáveis criadas dentro da classe. Aqui usamos `self.sequence` para recuperar as informações armazenadas em nosso atributo chamado `sequence`.


```python
replacement1 = self.sequence.replace('A', 't') 
```


#### Criando um Objeto DNARecord

A classe acima é um conjunto de regras que precisam ser seguidas ao criar um novo objeto DNARecord.
Agora vamos criar um novo objeto DNARecord:

```python
  dna_rec_obj = DNARecord() 
```

`dna_rec_obj` é o nosso novo objeto DNARecord que foi criado usando as regras que estabelecemos na definição da classe.



#### Recuperando valores de atributos

Agora que um novo objeto DNARecord foi criado e atribuído à variável `dna_rec_obj`, podemos acessar seus atributos usando o seguinte formato, `objeto.nome_do_atributo`.

Para obter o nome do gene do objeto que criamos, simplesmente escrevemos `dna_rec_obj.gene_name`.

Isso é possível porque dentro da nossa definição de classe criamos uma variável `gene_name`.

Vamos tentar:

```python
>>> dna_rec_obj.gene_name
'ABC1'
>>> dna_rec_obj.sequence
'ACGTAGCTGACGATC'

```



#### Usando métodos de classe

Para chamar um método associado ao nosso novo objeto, usamos um formato similar, `objeto.nome_do_método`.

Então, para chamar

 o método `get_AT()`, usaríamos `dna_rec_obj.get_AT()`. Isso deve parecer familiar, você já usou métodos de classe várias vezes: `alguma_string.count('A')`.

Vamos tentar com nosso `dna_rec_obj`:


```python
>>> dna_rec_obj.sequence
'ACGTAGCTGACGATC'
>>> dna_rec_obj.get_AT()
0.4666666666666667

```


Agora vamos usar o método `reverse_complement()`
```python
>>> dna_rec_obj.sequence
'ACGTAGCTGACGATC'
>>> dna_rec_obj.reverse_complement()
GATCGTCAGCTACGT
```
Uau!! Obter o complemento reverso em uma linha é bem legal!


#### Obtendo dados em uma nova instância de nossa classe

Ótimo!!!

Agora podemos criar um objeto DNARecord e recuperar os atributos do objeto e usar os métodos legais que criamos.

Mas..... Ele sempre contém o mesmo nome de gene, sequência e informações de espécie 😟

Vamos tornar nossa classe mais genérica, ou em outras palavras, fazer com que um usuário possa fornecer um novo nome de gene, sequência de gene e organismo de origem toda vez que um objeto DNARecord for criado.



##### __\_\_init\_\___

Para fazer isso, precisamos adicionar uma função `__init__` à nossa Regra de Objeto, ou Classe.

A função `init` será chamada automaticamente quando você criar um objeto.

Ela contém instruções específicas para criar um novo Objeto DNARecord.

Ela especifica quantos dados queremos coletar do criador de um objeto DNARecord para usar dentro de um objeto DNARecord.

Abaixo, nossas instruções __\_\_init\_\___ indicam que queremos criar atributos de objeto chamados `sequence`, `gene_name` e `species_name` e defini-los com os valores fornecidos como argumentos quando o objeto foi criado.

Aqui está a definição da nossa nova classe e a criação de um novo objeto ao usar a função __\_\_init\_\___:

```python
#!/usr/bin/env python3
class DNARecord(object):
  
  # definir atributos da classe
  def __init__(self, sequence, gene_name, species_name): ## observe que '__init__' está envolto com dois sublinhados
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

## Criar novos Objetos DNARecord com dados definidos pelo usuário
dna_rec_obj_1 = DNARecord('ACTGATCGTTACGTACGAGT', 'ABC1', 'Drosophila melanogaster')
dna_rec_obj_2 = DNARecord('ATATATTATTATATTATA', 'COX1', 'Homo sapiens')

for d in [ dna_rec_obj_1, dna_rec_obj_2 ]:
  print('name:' , d.gene_name , ' ' , 'seq:' , d.sequence)
```

Saída:

```bash
$ python3 dnaRecord_init.py
name: ABC1   seq: ACTGATCGTTACGTACGAGT
name: COX1   seq: ATATATTATTATATTATA
```

Agora você pode criar tantos Objetos DNASequence quanto desejar, cada um pode conter informações sobre uma sequência diferente.



---

### [Link para o Conjunto de Problemas Python 11](problemsets/Python_11_problemset.md)

---



