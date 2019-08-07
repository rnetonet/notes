# Python for Programmers, First Edition

- Os exemplos abaixo usam o **REPL** do Python. [Clique aqui para ver o tutorial oficial sobre uso do REPL](https://docs.python.org/3/tutorial/interpreter.html).

- **Expressões** retornam valores:

```python
>>> 4 + 7
11
>>> "exemplo"
'exemplo'
>>>
```

- Os **valores** retornados por expressões podem ser armazenados em **variáveis**:

```python
>>> resposta = 40 + 2
>>> resposta
42
>>>
```

- O exemplo acima, responsável por criar a **variável** `resposta`, pode ser chamado de *comando* ou *instrução*.

*Comandos* não produzem valores, mas, sim, especificam ações a serem realizadas.

No exemplo, o *comando* define que a variável `resposta` deve passar a representar o resultado da expressão `40 + 2`.

- As **variáveis**, depois de criadas, podem ser utilizadas em qualquer parte do programa. Quando o interpretador as encontra, substitui por seus respectivos valores-referenciados:

```python
>>> resposta = 40 + 2
>>> resposta
42
>>> outra_resposta = 98 + 1
>>> outra_resposta
99
>>> resposta + outra_resposta
141
>>>
```

- A atribuição (`=`) **não** é um operador. O lado direito é sempre executado primeiro, então este resultado passa a ser referenciado pelo lado esquerdo.

- Os nomes das variáveis em Python, os **identificadores**, podem começar com letra ou *underline*, mas nunca com um número.

Também não podem conter espaços (use *underline* no lugar).

Python diferencia minúsculas e maiúsculas.

```python
>>> identificador = 1
>>> _identificador = 2
>>> um_identificador = 3
```

- **Tudo** é **objeto** em Python. E todo objeto tem um **tipo**. Este tipo identifica as informações armazenadas e as ações possíveis em um objeto. Para identificar o tipo de um objeto, use a função `type(obj)`:

```python
>>> resposta = 42
>>> type(resposta)
int
>>>
```

Também podem ser aplicados a *literals* - expressões simplificadas que produzem objetos:

```python
>>> type(3.14) # pi
float
>>>
```

- Python dispõe das principais operações matemáticas nativamente. Algumas, contudo, com símbolos um pouco diferentes:

**Multiplicação**  - `*`

```python
>>> 12 * 3
36
```

**Exponenciação** - `**`

```python
>>> 2 ** 2
4
>>> 2 ** 3
8
>>> 2 ** 4
16
>>> 2 ** 10
1024
>>>
```

**Divisão real** - `/` - Retorna um `float`

```python
>>> 10 / 3
3.3333333333333335
>>>
>>> 4 / 5
0.8
>>>
```

**Divisão arredondada** - `//` - Retorna um `int`. Despreza a parte decimal e retorna o inteiro mais próximo, menor do que o resultado real.

```python
>>> 10 // 3
3
>>>
>>> 4 // 5
0
>>>
>>> -13 // 4 # aproxima para -4
-4
>>> -13 / 4 # resultado real
-3.25
>>>
```

**Operador de resto** - `%` - Retorna o resto de uma divisão

```python
>>> 10 % 7
3
>>> 15 % 3.4
1.4000000000000004
>>>
```

- Expressões matemáticas podem ser agrupadas usando parênteses, o que aumenta a sua prioridade de resolução:

```python
>>> 2 * 4 + 1
9
>>> 2 * (4 + 1)
10
>>>
```

- A ordem de resolução das expressões numéricas em Python é:

1. Parênteses (do mais interno para o mais externo);
2. Exponenciação;
3. Multiplicação, divisão e resto;
4. Adição e subtração.

*Lembre-se que se duas operações, de mesma prioridade, estão juntas, elas são resolvidas da esquerda para direita.*

- Operações com mesma prioridade são implicitamente agrupadas, da esqueda para direita:

```python
>>> 2 + 3 - 4
1

# Equivale a
>>> (2 + 3) - 4
1
>>>
```

Parênteses sem função, apenas para dar mais claridade, podem ser utilizados, conforme a segunda expressão.

- O lançamento de objetos **exceção** são a forma de Python indicar que ocorreram erros.

Um tipo comum, ao lidar com operações aritméticas, é a divisão por zero:

```python
>>> 10 / 0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-24-cd759d3fcf39> in <module>
----> 1 10 / 0

ZeroDivisionError: division by zero
>>>
>>> 15 // 0
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-25-e47b7636fa8a> in <module>
----> 1 15 // 0

ZeroDivisionError: integer division or modulo by zero
>>>
```

Outro erro, também comum, ocorre ao referenciar uma variável inexistente:

```python
>>> x = 10
>>> y = 35
>>>
>>> x + y + z
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-28-b5bd3aae62b8> in <module>
----> 1 x + y + z

NameError: name 'z' is not defined
>>>
```

- É possível imprimir para saída padrão, normalmente o próprio console, usando a função *built-in* `print(arg)`:

```python
>>> print('Hello World!')
Hello World!
>>>
```

O argumento deste exemplo, `'Hello World'`, é uma expressão literal que produz uma **string**. **Strings** também podem ser descritas usando aspas duplas:

```python
>>> print("Hello World")
Hello World
>>>
```

`print(arg1, arg2, arg...)` também permite imprimir uma sequência de objetos separados por espaço:

```python
>>> print("Hello", "World")
Hello World
>>>
```

- Em strings, o caractere `\` junto com o caractere seguinte formam uma **sequência escape** e produzem caracteres especiais.

Para produzir uma quebra de linha dentro da string, use `\n`:

```python
>>> print("Hello\nWorld")
Hello
World
```

Outras sequências escape comuns incluem:

```python
>>> print("Hello\tWorld")
Hello   World
>>> print("Hello\\World")
Hello\World
>>> print("Hello\"World")
Hello"World
>>> print("Hello\'World")
Hello'World
```

- É possível *escapar* uma quebra de linha, permitindo dividir um comando extenso em duas ou mais linhas:

```python
>>> print("Hello \
... Darkness \
... My \
... Old \
... Friend")
Hello Darkness My Old Friend
>>>
```

- Expressões podem ser passadas como parâmetros para a função `print()`. Seus valores serão calculados e só então impressos:

```python
>>> print("Result: ", 42 + 13)
Result:  55
>>>
```

- Strings podem ser criadas com três aspas simples ou duplas, permitindo a quebra em várias linhas. Útil para comentar, criar docstrings.

```python
>>> msg = """
... What goes around
... Comes aroung
... """
>>>
>>> print(msg)

What goes around
Comes aroung

>>> msg
'\nWhat goes around\nComes aroung\n'
>>>
```

- Aspas dentro de aspas.

Pode-se incluir aspas simples dentro de strings formadas por aspas duplas, sem necessidade de *escape*.

```python
>>> print(" d'ior ")
 d'ior
```

E vice-verca, é possível incluir aspas duplas dentro de strings delimitadas por aspas simples, sem precisar *escape*:

```python
>>> print(' he said "hello!" ')
 he said "hello!"
>>>
```

Por fim, é possível escapar ambos tipos de aspas:

```python
>>> print(" alo\"ha alo\'ha ")
 alo"ha alo'ha
>>> print(' alo\"ha alo\'ha ')
 alo"ha alo'ha
>>>
```

E dentro de strings triplas (simples ou duplas), pode-se incluir qualquer tipo simples ou duplo, desde que não tripla:

```python
>>> print(""" "teste" 'teste' """)
 "teste" 'teste'
>>> print(''' "teste" 'teste' ''')
 "teste" 'teste'
>>>
```

- Lendo dados do usuário: `input(prompt)`

```python
>>> print(""" "teste" 'teste' """)
 "teste" 'teste'
>>> print(''' "teste" 'teste' ''')
 "teste" 'teste'
>>>
```

- `input(prompt)` sempre retorna strings. Para ler um inteiro, convert com `int()`:

```python
>>> idade = input("Qual a sua idade ? ")
Qual a sua idade ? 25
>>> idade = int(idade)
>>> idade
25

>>> # Ou, diretamente
>>> idade = int(input("Qual sua idade? "))
Qual sua idade? 31
>>> idade
31
```

Caso queira um ponto flutuante, use `float()` no lugar de `int()`:

```python
>>> valor_pi = input(" Qual o valor de pi ? ")
 Qual o valor de pi ? 3.14
>>> valor_pi = float(valor_pi)
>>> valor_pi
3.14
>>>
>>> # Ou, diretamente
>>> valor_pi = float(input(" Qual o valor de pi ? "))
 Qual o valor de pi ? 3.14
>>> valor_pi
3.14
>>>
```

- Condições

**Condições** são *expressões* que retornam `True` ou `False`.

Exemplos:

```python
>>> 7 > 14
False
>>>
>>> 7 < 14
True
>>>
>>> 11 == 11
True
>>>
>>> 16 - 2 == 14
True
>>>
```

- Comentários, *docstrings*

*Comentários* começam com `#` e vão até o final da linha. Todo comentário é ignorado.

*docstrings* são strings que documentam módulos, classes e funções. Devem ser a primeira coisa em cada um destes. São implicitamentes atribuídas ao atributo `__doc__` de cada um destes objetos e vistas com `help(objeto)`.
Normalmente são strings *triplas*.

- Quebrando longas linhas

Comandos grandes podem ser quebrados em múltiplas linhas com *escape* - `\`:

```python
>>> print("Hello" + \
... "World")
HelloWorld
>>>
```

Ou, sendo postas entre parênteses, sem necessidade de *escape*. **Este é o método recomendado:**

```python
>>> soma = (
...     10 +
...     20 +
...     30 +
...     40
... )
>>> soma
100
>>>
```

- Condições são utilizadas em blocos `if`

Blocos `if` permitem condicionar a execução de blocos de código conforme o valor de uma condição/expressão.

Lembre-se, `input("Mensagem:")` pede e retorna uma string para o usuário.

```python
>>> valor = input("Digite o valor: ")
Digite o valor: 15
>>>
>>> valor = int(valor) # precisa converter, vem como string
>>>
>>> if valor % 2 == 0:
...     print("Eh par!")
...
>>> if valor > 10:
...     print("Maior que 10")
... elif valor == 15:
...     print("Eh 15!")
... else:
...     print("Nao eh nenhuma das condicoes acima")
...
Maior que 10
>>>
```

Blocos de `if`, `elif` e `else` serão testados em sequência. O primeiro que produzir uma condição válida, será executado, concluindo a sequência de checagens.

Atente-se, apenas um bloco é executado. Se nenhum for, o `else`, se presente, será executado:

```python
>>> valor = int( input("Entre com valor: ") )
Entre com valor: 10
>>>
>>> if valor > 5:
...     print(" > 5 ")
... elif valor == 10:
...     print(" == 10 ")
...
 > 5
>>>
```

- Comparações poder sem encadeadas

Comparações podem ser encadeadas, facilitando a verificação de limites:

```python
>>> valor = int( input("Entre com valor: ") )
Entre com valor: 15
>>>
>>> if 10 < valor < 20:
...     print("Valor esta entre 10 e 20")
...
Valor esta entre 10 e 20
>>>
>>>
```

O bloco de código acima é, implicitamente, traduzido para:

```python
>>> if 10 < valor and valor < 20:
...     print("Valor esta entre 10 e 20")
...
Valor esta entre 10 e 20
>>>
```

- Objetos têm valor lógico.

Nem sempre é necessário escrever uma condição completa.
Os principais objetos de Python têm valor lógico implícito.

Esse valor é verificável através da função `bool(objeto)`.

Números com valor zero, são considerados `False`.
Conjuntos vazios também são considerados `False`.
`None` é considerado `False`.

```python
>>> bool( 0.0 )
False
>>> bool( 0 )
False
>>> bool( [] ) # lista vazia
False
>>> bool( {} ) # dic vazio
False
>>> t = ()
>>> t
()
>>> bool( () ) # tupla vazia
False
>>>
>>> bool( None )
False
>>>
>>> bool( "" )
False
>>>
```

Todo o resto é tido como `True`.

```python
>>> bool( 1 )
True
>>> bool( 1.0 )
True
>>> bool( "x" )
True
>>> bool( [1, 2, 3] )
True
>>> bool( (1, 2, 3) )
True
>>> bool( {"chave": 42} )
True
>>>
```

- Expressões condicionais concisas (expressões ternárias)

É possível abreviar um `if` em um comando de apenas uma linha. Muito útil para atribuir um valor a uma variável conforme o valor de outra:

```python
>>> nota = 87
>>>
>>> resultado = "aprovado" if nota >= 75 else "reprovado"
>>> resultado
'aprovado'
>>>
>>> nota = 54
>>> resultado = "aprovado" if nota >= 75 else "reprovado"
>>> resultado
'reprovado'
>>>
```

É boa prática usar parênteses nesses casos:

```python
>>> nota = 100
>>> resultado = ("aprovado" if nota >= 75 else "reprovado")
>>> resultado
'aprovado'
>>>
```

- Objetos e tipagem dinâmica

Lembre-se: **tudo em Python é objeto**.

Todo objeto tem um tipo, identificável via `type(objeto)`, e um valor, que está contido no objeto (*não há tipos primitivos*).

Os tipos *"primitivos"* são:

```python
>>> a = 10
>>> type(a)
int
>>>
>>> b = 3.14
>>> type(b)
float
>>>
>>> c = "spam"
>>> type(c)
str
>>>
```

- Variáveis apontam para objetos

Variáveis apontam para objetos:

```python
>>> a = "aloha"
>>>
>>> type(a)
str
>>>
>>>
```

As variáveis são substituídas pelo objeto que referenciam:

```python
>>> a.upper()
'ALOHA'
>>>
```

Variáveis podem passar a apontar para novos objetos, esquecendo o antigo:

```python
>>> a = "spam"
>>> a.upper()
'SPAM'
>>>
```

Contudo, alterar a referência de uma variável não altera o objeto em si:

```python
>>> a = "spam"
>>> b = a
>>>
>>> a = a.upper()
>>>
>>> a
'SPAM'
>>> b
'spam'
>>>
```

Cuidado! Objetos mutáveis podem se modificar, logo, alterações em uma variável, referência, terão efeito em outras cópias.

```python
>>> a = [1, 2, 3]
>>> b = a
>>>
>>> a[1] = 99
>>>
>>> a
[1, 99, 3]
>>>
>>> b
[1, 99, 3]
>>>
```

- Existem duas estruturas de repetição: `while` e `for`.

`while` repete um conjunto de comandos até uma condição se tornar falsa:

```python
>>> contador = 10
>>> while contador > 0:
...     print(contador)
...     contador = contador - 1
...
10
9
8
7
6
5
4
3
2
1
>>>
```

O `for` executa um conjunto de instruções para cada item de uma sequência:

```python
>>> palavra = "spam"
>>> for letra in palavra:
...     print(letra)
...
s
p
a
m
>>>
```

- Parâmetros da função `print()`

A função `print()` admite dois parâmetros nomeados:

`sep` define o caractere a ser utilizado entre as strings passadas, por padrão um espaço.

`end` determina o caractere a ser utilizada após o último valor passado, por padrão uma quebra de linha `\n`.

```python
print("spam", "eggs", "bacon", sep="_", end="***")
```

- Iteráveis, listas e iteradores

O comando `for` atua sobre objetos que são *iteráveis*. Todas sequências, incluindo *strings*, são iteráveis em Python.

Um tipo iterável bastante comum é a **lista**:

```python
>>> lista = [10, 20, 30]
>>> for valor in lista:
...     print(valor)
...
10
20
30
>>>
```

As sequências encapsulam um objeto **iterador** que é utilizado *por debaixo dos panos*. Este objeto mantém controle de qual foi o último objeto retornado, o próximo a ser retornado e quando a sequência finda.

- A função `range(inicio, fim, [incremento])` permite produzir sequências numéricas.

A função `range(inicio, fim, [incremento])` produz iteradores que retornam números sequenciais. Os números produzidos vão de `inicio` (incluído) até antes de `fim` (não incluído). Os números produzidos são
incrementados por `incremento`, que por padrão é `1`.

```python
>>> for numero in range(10, 22, 2): # gere um iterador de 10 ate 21, saltando de 2 em 2
...     print(numero)
...
10
12
14
16
18
20
>>>
```

Em sua versão mais simples, `range(fim)` requer apenas o parâmetro `fim`, usando como `inicio` o valor `0` e `incremento` o valor `1`:

```python
>>> for i in range(10):
...     print(i)
...
0
1
2
3
4
5
6
7
8
9
>>>
```

**Lembre-se:** o valor `fim` **não é incluído**.

A função é bastante flexível, permitindo, por exemplo, gerar sequências de forma decrescente:

```python
>>> for numero in range(10, -1, -1):
...     print(numero)
...
10
9
8
7
6
5
4
3
2
1
0
>>>
```

- Atribuições aprimoradas.

Atribuições em que a variável aparece tanto do lado esquerdo quanto do direito podem ser abreviadas.

Este código:

```python
>>> total = 0
>>> for numero in range(0, 11):
...     total = total + numero
...
>>> total
55
>>>
```

Pode ser abreviado para:

```python
>>> total = 0
>>> for numero in range(0, 11):
...     total += numero
...
>>> total
55
>>>
```

Todas operações permitem essa abreviação:

```python
>>> valor = 10
>>>
>>> valor *= 3
>>> valor
30
>>>
>>> valor /= 3
>>> valor
10.0
>>>
>>> valor **= 2
>>> valor
100.0
>>>
>>>
>>> valor -= 1
>>> valor
99.0
>>>
>>> valor += 1
>>> valor
100.0
>>>
```

- Strings formatadas

Ao prefixar uma string com um `f`, ela é transformada numa **f-string**, o que permite interpolar variáveis e expressões através de `{}` (chaves).

Substituir uma variável:

```python
>>> soma = 33
>>>
>>> print(f"A soma deu {soma}")
A soma deu 33
>>>
```

Uma expressão:

```python
>>> nome = "joao"
>>>
>>> print(f"O nome eh {nome.upper()}")
O nome eh JOAO
>>>
```

As variáveis/expressões dentro das chaves são chamadas de *placeholders*. Elas são processadas e o seu resultado convertido em string, para então serem substituídos na string de fato.

Formatando números decimais com duas casas decimais:

```python
>>> valor = 11 / 3
>>> valor
3.6666666666666665
>>>
>>> print(f"{valor:.2f}")
3.67
>>>
```

Se o número só tiver uma casa decimal e você formatar com duas, zeros são adicionados:

```python
>>> limite = 9.9
>>> print(f"limiar = {limite:.2f}")
limiar = 9.90
>>>
```

- Se precisão é importante, utilize `Decimal`. Evite `float`.

Números do tipo `float` são armazenados em binário de forma aproximada:

```python
>>> valor = 121.3
>>> valor
121.3
```

Parece que está certinho, preciso. Mas, se aumentamos a precisão, percebe-se que trata-se de uma aproximação:

```python
>>> print(f"{valor:.20f}")
121.29999999999999715783
>>>
```

E isso pode impactar em algumas comparações:

```python
>>> 11 / 3
3.6666666666666665
>>>
>>> 11 / 3 == 3.6
False
>>>
```

Ou seja, se quer precisão, use o tipo `Decimal`. Se vai mexer com dinheiro, use `Decimal`.

Para usar `Decimal` você pode importar todo o módulo `decimal`:

```python
>>> import decimal
>>>
>>> valor = decimal.Decimal('3.14')
>>> valor
Decimal('3.14')
>>>
```

Ou carregar todo o módulo, mas trazer para sua aplicação apenas a classe `Decimal`:

```python
>>> from decimal import Decimal
>>>
>>> valor = Decimal('3.14')
>>> valor
Decimal('3.14')
>>>
```

Os tipos `Decimal` podem ser criados a partir de strings e permitem executar operações entre `Decimal` e de `Decimal` com `int`. **Não permite misturar `Decimal` com `float`.**

```python
>>> x = Decimal("10.5")
>>> y = Decimal("2")
>>>
>>> z = x + y
>>> z
Decimal('12.5')
>>>
>>> x / y
Decimal('5.25')
>>>
>>> x * y
Decimal('21.0')
>>>
>>> x += y
>>> x
Decimal('12.5')
>>>
>>> y += 100
>>> y
Decimal('102')
>>>
>>> x -= 5
>>> x
Decimal('7.5')
>>>
```

Para calcular o redimento de uma aplicação de `1000` ao longo de `10` ano a juros de `0.05`, podemos fazer:

```python
>>> principal = Decimal("1000.00")
>>> interest  = Decimal("0.05")
>>>
>>> for ano in range(1, 11):
...     print(f"ano={ano}, acumulado={principal * (1 + interest) ** ano}")
...
ano=1, acumulado=1050.0000
ano=2, acumulado=1102.500000
ano=3, acumulado=1157.62500000
ano=4, acumulado=1215.5062500000
ano=5, acumulado=1276.281562500000
ano=6, acumulado=1340.09564062500000
ano=7, acumulado=1407.1004226562500000
ano=8, acumulado=1477.455443789062500000
ano=9, acumulado=1551.32821597851562500000
ano=10, acumulado=1628.8946267774414062500000
>>>
```

Podemos deixar o resultado mais simpático com as opções de formatação das *f-string*:

```python
>>> montante = Decimal('1_000')
>>> taxa = Decimal('0.05')
>>> for ano in range(1, 11):
...     print(f"ano = {ano:<2} / acumulado = {montante * (1 + taxa) ** ano:>10.2f}")
...
...
ano = 1  / acumulado =    1050.00
ano = 2  / acumulado =    1102.50
ano = 3  / acumulado =    1157.62
ano = 4  / acumulado =    1215.51
ano = 5  / acumulado =    1276.28
ano = 6  / acumulado =    1340.10
ano = 7  / acumulado =    1407.10
ano = 8  / acumulado =    1477.46
ano = 9  / acumulado =    1551.33
ano = 10 / acumulado =    1628.89
>>>
```

O formato a ser aplicado vem depois do `:`.
`<` ou `>` indicam o alinhamento. Após estes, deve a quantidade de *espaços* a serem utilizados. Este tamanho pode ser precedido por um `0`, caso queira preencher os espaços sobressalentes com `0`. Por fim, pode vir o `.`, o número de casas decimais e o formato numérico, geralmente um `f`.

São muitas opções, de fato. Exemplos ajudam:

```python
>>> print(f"{123:>10}") # alinhado a direita, ocupando 10 espaços
       123
>>> print(f"{123:>010}") # alinhado a direita, ocupando 10 espaços, preenchendo com zero
0000000123
>>>
>>> print(f"{123:<10}") # alinhado a esquerda, ocupando 10 espaços
123
>>> print(f"{123:<010}") # alinhado a esquerda, ocupando 10 espaços, preenchendo com zero
1230000000
>>> print(f"{3.1418391231:>10.2f}") # alinhado a direita, 10 espaços, duas casas decimais
      3.14
>>>
```

- É possível interromper um loop com `break` ou pular para a próxima iteração com `continue`.

Para sair antecipadamente de um loop, seja `while` ou `for`, utilize o comando `break`:

```python
>>> contador = 0
>>> while contador <= 100:
...     print(contador)
...     if contador == 10:
...         break
...     contador += 1
...
0
1
2
3
4
5
6
7
8
9
10
>>>
```

Após um `break`, a próxima instrução, fora do loop, é executada.

Pode-se utilizar `break` em `for` também:

```python
>>> palavra = "bacon"
>>> for letra in palavra:
...     print(letra)
...     if letra == "o":
...         break
...
b
a
c
o
>>>
```

Caso se deseje *pular* a iteração corrente e ir para a próxima, utilize `continue`.

O exemplo abaixo pula o `5`:

```python
>>> contador = 0
>>> while contador <= 10:
...     contador += 1
...     if contador == 5:
...         continue
...     print(contador)
...
1
2
3
4
6
7
8
9
10
11
>>>
```

Neste, pulamos o `c`:

```python
>>> palavra = "bacon"
>>> for letra in palavra:
...     if letra == "c":
...         continue
...     print(letra)
...
b
a
o
n
>>>
```

Tanto o loop `while` quanto o `for` suportam uma claúsula `else`, que só executada quando **nenhum** comando `break` é executado, ou seja, o loop termina naturalmente:

```python
>>> contador = 0
>>> while contador <= 10:
...     if contador == 999:
...         break
...     print(contador)
...     contador += 1
... else:
...     print("break NÃO foi executado")
...
0
1
2
3
4
5
6
7
8
9
10
break NÃO foi executado
>>>
```

Um exemplo de `else` com `for`:

```python
>>> palavra = "bacon"
>>> for letra in palavra:
...     if letra == "z":
...         break
...     print(letra)
... else:
...     print("break NÃO foi executado")
...     print("letra 'z' não está presente")
...
b
a
c
o
n
break NÃO foi executado
letra 'z' não está presente
>>>
```

Lembre-se: o bloco `else` só não é chamado se algum `break` for executado. Pode executar `continue` à vontade, o `else` continua sendo chamado:

```python
>>> palavra = "bacon"
>>> for letra in palavra:
...     if letra == "a":
...         continue
...     print(letra)
... else:
...     print("break NÃO foi executado")
...     print("letra 'z' não está presente")
...
b
c
o
n
break NÃO foi executado
letra 'z' não está presente
>>>
```

- Os operadores lógicos `and`, `or` e `not` permitem construir condições mais complexas.

Use `and` para combinar duas condições simples, a combinação só resultará em `True` se todas condições envolvidas forem `True`. Basta uma ser `False` para toda a condição se tornar `False`:

```python
>>> gender = "Male"
>>> age = 45
>>>
>>> gender == "Male" and age > 40
True
>>> gender == "Male" and age > 50
False
>>>
```

Utilize parênteses para deixar ainda mais claro:

```python
>>> (gender == "Male") and (age > 50)
False
>>>
```

**Importante:** o `and` só executa a segunda condição se necessário. Se a primeira for `False`, ele já retorna `False` e nem analisa a segunda. Este comportamento se chama *short-circuit*.

O operador `or` no entanto, precisa que apenas uma das duas condições simples seja `True`, para retornar `True`. Ou seja, só retorna `False` se as duas forem `False`:

```python
>>> (gender == "Male") or (age > 50)
True
>>>
```

**Importante:** assim como o `and` o `or` também atua em *short-circuit*, se a primeira condição for `True`, ele já retorna `True` e sequer avalia a segunda.

**Performance:** ao usar o operador `and` coloque à esquerda expressões que têm maior tendência de ser `False`. E ao utilizar o operador `or`, coloque à esquerda expressões que tenham maior tendência de ser `True`. A ideia é aproveitar o *short-circuit*.

Por fim, o `not` nega o valor lógico de uma condição. Ele é um operador unário e deve ser posto logo antes de uma condição:

```python
>>> gender = "Male"
>>>
>>> not gender == "Female"
True
>>>
>>> not gender == "Male"
False
>>>
```