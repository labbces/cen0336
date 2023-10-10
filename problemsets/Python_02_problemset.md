Python 2 Problem Set -- Operadores, Verdadeiro/Falso, Lógica 
===================

1. Use o Interpretador Interativo para testar se você pode achar um ['ATG'](https://github.com/prog4biol/pfb2019#membership-operators) na seguinte fita simples de DNA:

```
GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA
```

2. E que tal 'TTT'?

3. Se você ainda não salvou a cadeia de DNA em uma variável, faça isso e refaça os [passos 1 e 2](https://github.com/prog4biol/pfb2019#membership-operators).

4. No interpretador, utilize bool para testar uma variedade de valores como '', 0, 0.0, FALSE, false, True, true, 'True', 'False' para ver se eles avaliam como True ou False.

5. Usando um editor de texto, escreva um código que:
    - Atribua um valor a uma variável;
    - Possua uma instrução [if/else](https://github.com/prog4biol/pfb2019#logic-control-statements) na qual:
       - Print uma confirmação de verdade se o valor for verdadeiro.
       - Print "Not True" se o valor não for verdadeiro 

6. Certifique-se de fazer commit das suas alterações ao longo do caminho. Você pode esperar até o final para enviá-las para o repositório remoto, se preferir, ou pode fazê-lo agora.

7. Crie um script que tenha a instrução [if/else](https://github.com/prog4biol/pfb2019#if-statement) que (lembre-se de escrever um pouco de cada vez e testar)
    - Teste para ver se um número é positivo e negativo
    - Print "positivo" se for positivo
    - Print "negativo" se for negativo
    - Salve e execute.
8. Adicione um [elif](https://github.com/prog4biol/pfb2019#ifelif) para testar se o número é igual a 0. Salve e execute.

9. Adicione testes aninhados ao seu último scrpit:
    - Se for positivo, além de imprimir "positivo"
    - Teste se é menor que 50
    - Salve e execute 
            
10. Adicione mais testes aninhados ao seu scrpit:.
    - Se for menor que 50
    - Teste se o número é par
    - Se for menor que 50 e par, imprima "é um número par menor que 50"
    - Salve e execute
         
11. Adicione mais testes aninhados.  
    -  Se for maior que 50,  
    -  Teste se o número é divisível por 3  
    -  Se o número for maior que 50 e divisível por 3, imprima "é maior que 50 e divisível por 3" 
    -  Salve e execute

12. Nos seus loops aninhados anteriores, teste o número 50. O que é impresso na tela? É a resposta correta? Se não, você tem um erro semântico e precisa alterar seu código para estar correto com qualquer número.  

13. Escreva um novo script que realiza todos os testes de 7 a 11, mas obtém o valor a ser testado a partir da linha de comando e o armazena em uma variável. Adicione uma instrução de impressão que lembra ao usuário qual número está sendo testado. [Lembre-se de 'sys' nas notas](pfb2019#command-line-parameters-a-special-built-in-list). 

14. ADD/COMMIT/PUSH

15. Escreva um novo script que teste se um ano é bissexto. De acordo com a [Wikipedia](https://en.wikipedia.org/wiki/Leap_year), um ano bissexto é um ano especial que tem um dia extra (366 dias em um ano). Um ano pode ser bissexto se for exatamente divisível por 4, mas não divisível por 100. Um ano também é bissexto se for exatamente divisível por 400.

16. ADD/COMMIT/PUSH

