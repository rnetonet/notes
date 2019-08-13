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

- **Funções** podem ser definidas com o comando `def`.

A sintaxe de definição do `def` requer o nome da função, seus parâmetros (entre parênteses) - se algum for necessário, `:` e o bloco de código a ser executado:

```python
>>> def quadrado(numero):
...     """ Retorna o quadrado do numero """
...     return numero ** 2
...
```

É de bom tom a primeira linha de uma função ser um comentário, *docstring*, explicando brevemente o que é feito.

Após declaração, a função pode ser utilizada múltiplas vezes e com diferentes parâmetros.

```python
>>> quadrado(2)
4
>>> quadrado(3)
9
>>>
```

O comando `return` devolve um valor da função para quem a chamou, na função acima, o quadrado do número passado.

Se uma função não contém um comando `return`, ela implicitamente retorna `None`:

```python
>>> def inutil1():
...     print("inutil1")
...
>>>
>>> valor = inutil1()
inutil1
>>> print(valor)
None
```

Também é possível incluir um `return` sem valor algum ou retornando o próprio `None` explicitamente na função:

```python
>>> def inutil2():
...     print("Inutil 2")
...     return
...
>>> valor = inutil2()
Inutil 2
>>> print(valor)
None
>>>
```

```python
>>> def inutil3():
...     print("Inutil 3")
...     return None
...
>>>
>>> valor = inutil3()
Inutil 3
>>> print(valor)
None
```

- Os parâmetros passados e as variáveis definidas são locais ao escopo da função, **enquanto estiver em execução**.

Os parâmetros passados e variáveis declaradas no corpo da função tem escopo local e só existem durante a execução da função, não sendo possível referenciá-las *de fora*.

```python
>>> def soma(a, b):
...     resultado = a + b
...     return resultado
...
>>>
>>> soma(10, 20)
30
>>>
>>> a
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-63-3f786850e387> in <module>
----> 1 a

NameError: name 'a' is not defined
>>> b
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-64-89e6c98d9288> in <module>
----> 1 b

NameError: name 'b' is not defined
>>> resultado
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-65-b2c5c9eb7548> in <module>
----> 1 resultado

NameError: name 'resultado' is not defined
>>>
```

- Funções podem receber mais de um parâmetro:

```python
>>> def maximum(a, b, c):
...     if a > b and a > c:
...         return a
...     elif b > a and b > c:
...         return b
...     else:
...         return c
...
>>>
>>> maximum(1, 2, 3)
3
>>> maximum(3, 2, 1)
3
>>> maximum(1, 3, 2)
3
>>> maximum(2, 3, 1)
3
>>>
```

Inclusive, por existir tipagem dinâmica, tipos distintos podem ser passados e se a interface for compatível, a função atuará sem maiores problemas:

```python
>>> maximum(1.5, 3.1, 2.2)
3.1
>>> maximum("a", "bc", "defg")
'defg'
>>>
```

- Python contém muitas funcionalidades pré-carregadas, inclusive a identificação de máximos (`max()`) e mínimo (`min()`).

A função `maximum()` declarada acima, poderia ser substituida por uma chamada a função *builtin* `max()`:

```python
>>> max(1, 2, 3)
3
>>> max(45, 12, 11)
45
>>>
```

A função contrária, `min()`, pode ser utilizada para encontrar o menor valor:

```python
>>> min(12, 44, 3, 11, 1292)
3
>>>
```

- Inteiros grandes podem ser separados por `_` para facilitar a leitura:

```python
>>> valor = 6_000_000_000
>>> valor
6000000000
>>>
```

- Funções podem retornar múltiplos valores ao mesmo tempo, através de um objeto *container*, tipo uma **tupla**:

```python
>>> def maiuscula_minuscula(palavra):
...     return (palavra.upper(), palavra.lower())
...
>>>
>>> maiuscula_minuscula("Spam")
('SPAM', 'spam')
>>>
```

- É possível definir valores padrão para parte ou todos parâmetros de uma função:

```python
>>> def area_retangulo(largura=2, altura=3):
...     return largura * altura
...
>>>
```

Se todos parâmetros tiverem valores padrão, é possível chamar a função sem nenhum parâmetro:

```python
>>> area_retangulo()
6
>>>
```

Ou passá-los posicionalmente:

```python
>>> area_retangulo(5)
15
>>>
>>> area_retangulo(5, 10)
50
>>>
```

**Importante:** Paramêtros posicionais devem vir antes de parâmetros com valores padrão:

```python
>>> def mensagem_customizada(mensagem, n_repeticoes=3):
...     while n_repeticoes:
...         print(mensagem)
...         n_repeticoes -= 1
...
>>>
>>> mensagem_customizada("Teste")
Teste
Teste
Teste
>>>
```

É possível alterar a ordem dos parâmetros se todos argumentos forem passados com os nomes:

```python
>>> mensagem_customizada(n_repeticoes=4, mensagem="Spam!")
Spam!
Spam!
Spam!
Spam!
>>>
```

- `*args` permite criar funções com uma lista de argumentos arbitrária

Para tornar flexível a passagem de argumentos, podemos usar a sintaxe `*args` que indica que todos os parâmetros que forem passados dali em diante devem ser agrupados em uma tupla chamada `args`:

```python
>>> def average(*args):
...     print(args)
...     print(type(args))
...     return sum(args) / len(args)
...
>>>
>>> average(1, 5, 10, 20, 45, 99)
(1, 5, 10, 20, 45, 99)
<class 'tuple'>
30.0
>>>
```

Convenciona-se usar `args`, mas pode ser qualquer identificador:

```python
>>> def average(*tpl):
...     print(tpl)
...     print(type(tpl))
...     return sum(tpl) / len(tpl)
...
>>> average(1, 5, 10, 20, 45, 99)
(1, 5, 10, 20, 45, 99)
<class 'tuple'>
30.0
>>>
```

Se houverem outros parâmetros posicionais, `*args` deve estar após estes:

```python
>>> def imprime_perfil(nome, idade, *caracteristicas):
...     print(f"Nome: {nome}")
...     print(f"Idade: {idade}")
...     for caracteristica in caracteristicas:
...         print(f"- {caracteristica:>10}")
...
>>>
>>> imprime_perfil("Rui", 31, "divertido", "nerd", "humano")
Nome: Rui
Idade: 31
-  divertido
-       nerd
-     humano
>>>
```

- *Unpacking* de sequências para argumentos

O operador `*` pode ser utilizado também para expandir uma sequência em argumentos para uma função:

```python
>>> argumentos = (1, 2, 3, 4, 5)
>>>
>>> def soma(*args):
...     total = 0
...     for arg in args:
...         total += arg
...     return total
...
>>>
>>> soma(argumentos) # ops! nao deve-se passar uma tupla
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-10-19031880e71f> in <module>
----> 1 soma(argumentos) # ops! nao deve-se passar uma tupla

<ipython-input-9-958a3120e127> in soma(*args)
      2     total = 0
      3     for arg in args:
----> 4         total += arg
      5     return total
      6

TypeError: unsupported operand type(s) for +=: 'int' and 'tuple'
>>>
>>> # Agora sim
>>> soma(*argumentos) # equivale a soma(1, 2, 3, 4, 5)
15
>>>
```

- Métodos são funções vinculadas a classes ou objetos.

O tipo básico `str` apresenta divesos métodos que produzem novas strings, modificadas, sem, contudo, alterar a original:

```python
>>> s = "Hello World"
>>>
>>> s.upper()
'HELLO WORLD'
>>>
>>> s
'Hello World'
>>>
>>> s.lower()
'hello world'
>>>
>>> s
'Hello World'
>>>
```

- Variáveis locais, definidas dentro de uma função ou passadas como argumento, só existem dentro e durante a execução da função.

```python
>>> def soma(a, b):
...     resultado = a + b
...     return resultado
...
>>> soma( 3, 5 )
8
>>>
>>> a
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-20-3f786850e387> in <module>
----> 1 a

NameError: name 'a' is not defined
>>> b
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-21-89e6c98d9288> in <module>
----> 1 b

NameError: name 'b' is not defined
>>> resultado
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-22-b2c5c9eb7548> in <module>
----> 1 resultado

NameError: name 'resultado' is not defined
>>>
```

- Variáveis criadas fora da função, no corpo do script (*do módulo*) são ditas **globais**.

Estas funções podem ser lidas de dentro das funções:

```python
>>> N_INDENTACAO = 4
>>>
>>> def imprimir_perfil(nome, idade):
...     print(" " * N_INDENTACAO, nome, idade)
...
>>>
>>> imprime_perfil("Joao", 45)
Nome: Joao
Idade: 45
>>>
```

Contudo, ao tentar modificar uma variável global no escopo da função, uma nova variável local é criada (sobrepondo-se à variável global):

```python
>>> X = 42
>>>
>>> def modificar():
...     X = 99
...
>>>
>>> modificar()
>>> X
42
>>>
```

Para realizar tal modificação, deve-se explicitamente indicar que a variável é `global` no início da função:

```python
>>> X = 42
>>>
>>> def modificar():
...     global X
...     X = 99
...
>>>
>>> modificar()
>>>
>>> X
99
>>>
```

- Variáveis definidas dentro de uma função ou passadas como parâmetro/argumento têm escopo local, não existem após a execução da função ou fora da função.

- Variáveis declaradas no corpo do módulo, do script, **sem estar dentro de uma função**, são **globais**. E estão acessíveis em todo o módulo, inclusive nas funções. Contudo, para modificá-las de dentro de funções, deve-se indicar explicitamente com `global`.

- Os módulos/scripts são lidos do início ao fim pelo interpretador. Comandos no nível do módulo são interpretados e executados imediatamente.
Comandos dentro de funções são executados apenas quandoa função é chamada.

- `import` permite algumas sintaxes adicionais.

Importar múltiplos nomes:

```python
>>> from math import ceil, sqrt
>>>
>>> ceil(3.14)
4
>>>
>>> sqrt(9)
3.0
>>>
```

Se forem de fato muitos nomes a importar, pode-se colocá-los entre parênteses e quebrar a linha:

```python
>>> from math import (
...     ceil,
...     sqrt,
...     e,
...     pi
... )
>>>
>>> ceil(3.14)
4
>>> sqrt(9)
3.0
>>>
>>> e
2.718281828459045
>>>
>>> pi
3.141592653589793
>>>
```

Também é possível criar um apelido para o módulo durante sua importação, usando `import as`:

```python
>>> import statistics as stats
>>>
>>> lista = [10, 3, 44, 192, 9]
>>> stats.mean(lista)
51.6
>>>
```

- A passagem de parâmetros em Python é *pass-by-object-reference*.

Uma cópia da referência do objeto é passada como parâmetro. **Não o objeto em si**.

```python
>>> a = 10
>>> b = 20
>>>
>>> def soma(a, b):
        # inteiros são imutáveis, as operações abaixo produzem novos objetos e novas variáveis locais, que sobrescrevem os argumentos
...     a -= 1
...     b -= 1
...     return a + b
...
>>> # Passa cópia das referências de 'a' e 'b'
>>> soma(a, b)
28
>>> # seguem inalterados
>>> a, b
(10, 20)
>>>
```

Contudo, para objetos **mutáveis** a passagem *by object reference* pode causar efeitos colaterais:

```python
>>> lista = [1, 2, 3]
>>>
>>> def modificar(l):
...     l[1] = 42
...
>>>
>>> outra_referencia_lista = lista # faz uma copia da referencia! lembre-se. da referencia!, continua havendo apenas um unico objeto
>>>
>>> modificar(lista)
>>>
>>> lista
[1, 42, 3]
>>>
>>> outra_referencia_lista
[1, 42, 3]
>>>
```

- Para quem já estudou C, variáveis em Python são ponteiros para objetos. Ao serem utilizadas em comandos ou expressões, esses ponteiros são dereferenciados implicitamente.

- É possível comprovar a passagem de parâmetros *pass-by-object-reference* utilizando a função *builtin* `id(objeto)`, que retorna um número representando a **identidade** única de um objeto:

```python
>>> numero = 7
>>>
>>> def quadrado(valor):
...     print(f"id(valor): {id(valor)}")
...     return valor * valor
...
>>> id(numero)
10968992
>>>
>>> quadrado(numero)
id(valor): 10968992
49
>>>
```

- Você pode comparar se duas referências apontam para o mesmo objeto comparando seus `id()` ou com o operador `is`:

```python
>>> a = 42
>>> b = a
>>>
>>> id(a) == id(b)
True
>>>
>>> a is b
True
>>>
```

**Importante:** `is` é mais restrito que uma comparação de igualdade. O `is` compara se as referências apontam para o mesmo espaço de memória. Não leva em conta o **valor** de fato dos objetos:

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>>
>>> a == b
True
>>>
>>> a is b
False
>>>
```

- Referências para objetos imutáveis não permitem alterar o valor do objeto:

```python
>>> numero = 12
>>>
>>> def quadrado(valor):
...     print(f"antes -> id(valor): {id(valor)}")
...     valor *= 2
...     print(f"depois -> id(valor): {id(valor)}")
...
>>>
>>> id(numero)
10969152
>>>
>>> quadrado(numero)
antes -> id(valor): 10969152
depois -> id(valor): 10969536
>>>
>>> id(numero)
10969152
>>>
```

Ao tentar alterar um objeto imutável, um novo objeto é criado, com uma nova identidade.
O objeto original permanece inalterado.

- Recursão consiste em quebrar um problema em pedaços menores para resolvé-lo.

Funções recursivas conhecem apenas os resultados de **casos bases**.

Ao receber um caso mais complexo, a função quebra-o e lança uma nova execução da função para o caso mais simples (**recursion step**).
A função original, que recebeu o caso complexo, continua ativa, aguardando as chamadas subsequentes terminarem.
Essas funções terminam quando há convergência em um caso base. Daí os resultados vão sendo retornados, subindo a pilha.

Logo, **toda função recursiva deve ter um caso base**, do contrário não há convergência.

Exemplo de fatorial recursivo:

```python
>>> def fatorial(n):
...     if n == 1: return 1
...     return n * fatorial(n - 1)
...
>>> fatorial(5)
120
>>> fatorial(4)
24
>>>
```

- Python fornece mecanismos para programação funcional.

Programação funcional foca em imutabilidade, evitando modificar variáveis.

**Programação declarativa** é dizer o que você quer feito, ao invés de escrever como fazer.

**Funções puras** dependem apenas dos parâmetros que recebe, sempre retornam o mesmo resultado para um mesmo conjunto de parâmetros e não têm efeitos colaterais (não modificam nenhuma variável externa ou os parâmetros passados).

Um bom exemplo, é a própria função `sum()`:

```python
>>> lista = [1, 2, 3]
>>>
>>> sum(lista)
6
>>> sum(lista)
6
>>> sum(lista)
6
>>>
>>> lista
[1, 2, 3]
>>>
```

- Listas

Permite conter dados homogêneos (mesmo tipo) ou heterogêneos:

```python
>>> l_a = [1, 2, 3, 4, 5]
>>> l_b = ["John", "Doe", 15, 2019]
>>>
```

Elementos são acessíveis por indexação, que começa em `0`:

```python
>>> lista = ["a", "b", "c"]
>>> lista[0]
'a'
>>> lista[1]
'b'
>>> lista[2]
'c'
>>>
```

A função `len()` retorna o tamanho:

```python
>>> len(lista)
3
>>>
```

A indexação pode ocorrer de trás para frente usando índices negativos, o último elemento da lista tem índice negativo `-1`, o penúltimo `-2`:

```python
>>> lista = ["a", "b", "c"]
>>> lista[-1]
'c'
>>> lista[-2]
'b'
>>> lista[-3]
'a'
>>>
```

Índices devem ser inteiros ou expressões que produzam inteiros:

```python
>>> lista
['a', 'b', 'c']
>>> lista[ len(lista) - 1 ]
'c'
>>>
```

Índices inexistentes produzem exceções:

```python
>>> lista
['a', 'b', 'c']
>>>
>>> lista[5]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-18-cf0236d70f2a> in <module>
----> 1 lista[5]

IndexError: list index out of range
>>>
```

Elementos de listas podem ser alterados por indexação e atribuição:

```python
>>> lista = ["a", "b", "c"]
>>> lista
['a', 'b', 'c']
>>>
>>> lista[1] = 42
>>> lista
['a', 42, 'c']
>>>
>>>
```

Mas, cuidado, sequências como tuplas ou strings são imutáveis. Os elementos individuais podem ser lidos, mas não alterados:

```python
>>> t = ("a", "b", "c")
>>> t[1]
'b'
>>> t[1] = 42
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-31-adb5cf76b0f0> in <module>
----> 1 t[1] = 42

TypeError: 'tuple' object does not support item assignment
>>>
```

```python
>>> palavra = "bacon"
>>> palavra[0]
'b'
>>>
>>> palavra[0] = "x"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-34-50084dc939bc> in <module>
----> 1 palavra[0] = "x"

TypeError: 'str' object does not support item assignment
>>>
```

Os items da lista podem ser usados individualmente em expressões. Lembre-se: são objetos também!

```python
>>> lista = ["a", "b", "c"]
>>>
>>> lista[0].upper()
'A'
>>>
```

Você pode extender uma lista usando o operador `+=`:

```python
>>> lista = []
>>> lista += [1]
>>> lista
[1]
>>>
>>> lista += [1, 2, 3]
>>> lista
[1, 1, 2, 3]
>>>
```

Cuidado, o lado direito **deve** conter uma sequência também. Cada elemento dessa sequência será adicionado à lista na esquerda:

```python
>>> lista = []
>>>
>>> lista += [1]
>>> lista
[1]
>>>

>>> lista += [1, 2, 3]
>>> lista
[1, 1, 2, 3]

>>> lista += "Python"
>>> lista
[1, 1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n']
>>>
```

Se tentar concatenar com um objeto simples, uma exceção é produzida:

```python
>>> lista += 10
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-48-689f38fbfb69> in <module>
----> 1 lista += 10

TypeError: 'int' object is not iterable
>>>
```

Mas com uma string de um caractere funciona, pois é uma sequência contendo apenas um item:

```python
>>> lista += "X"
>>> lista
[1, 1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n', 'X']
>>>
```

Sequências (listas, tuplas e strings) podem ser concatenadas com `+`:

```python
>>> [1, 2, 3] + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>>
>>> (1, 2, 3) + (4, 5, 6)
(1, 2, 3, 4, 5, 6)
>>>
>>> "abc" + "def"
'abcdef'
>>>
```

Mas não é possível concatenar tipos diferentes de sequências:

```python
>>> [1, 2, 3] + (4, 5, 6)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-54-7296224f6977> in <module>
----> 1 [1, 2, 3] + (4, 5, 6)

TypeError: can only concatenate list (not "tuple") to list
>>>
>>> [1, 2, 3] + "spam"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-55-6c39e239b46e> in <module>
----> 1 [1, 2, 3] + "spam"

TypeError: can only concatenate list (not "str") to list
>>>
```

Listas podem ser comparadas, elemento a elemento:

```python
>>> [1, 2, 3] == [1, 2, 3]
True
>>>
>>> [10, 20, 30] > [1, 2, 3]
True
>>>
>>> [0, 1, 2] < [10, 30, 40]
True
>>>
```

- Tuplas

São muito similares às listas, mas são imutáveis.

Criando tuplas:

```python
>>> tpl_vazia = ()
>>> tpl_vazia
()
>>>
>>> tpl_unica = (42, ) # virgula necessaria
>>> tpl_unica
(42,)
>>>
>>> tpl = (1, 2, 3, 4, 5)
>>> tpl
(1, 2, 3, 4, 5)
>>>
>>> tpl_flat = 1, 2, 3, 4, 5 # paresentes sao opcionais, mas sao recomendados
>>> tpl_flat
(1, 2, 3, 4, 5)
>>>
>>>
```

Tuplas são acessadas e respondem a quase todas operações que as listas:

```python
>>> tpl = (10, 20, 30)
>>>
>>> len(tpl)
3
>>>
>>> tpl + (10, 20, 30)
(10, 20, 30, 10, 20, 30)
>>>
>>> tpl[0], tpl[-1]
(10, 30)
>>>
>>> tpl += (25, 50) # nova tupla e criada
>>> tpl
(10, 20, 30, 25, 50)
>>>
>>>
```

Tuplas, apesar de imutáveis, podem conter objetos mutáveis:

```python
>>> tpl = (1, 2, ["a", "b", "c"])
>>> tpl[2][0] = "X"
>>> tpl
(1, 2, ['X', 'b', 'c'])
>>>
```

- Decompondo uma sequência em variáveis

```python
>>> tpl = (1, 2, 3)
>>>
>>> a, b, c = tpl
>>> a
1
>>> b
2
>>> c
3
>>>
```

Se o número de variáveis for diferente (para maior ou menor) do tamanho da sequência, uma exceção é gerada:

```python
>>> a, b = tpl
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-7-352fb1238ad4> in <module>
----> 1 a, b = tpl

ValueError: too many values to unpack (expected 2)
>>>
```

```python
>>> a, b, c, d = tpl
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-6-6b50c620d7a3> in <module>
----> 1 a, b, c, d = tpl

ValueError: not enough values to unpack (expected 4, got 3)
```

- *swap* de variáveis através de *unpacking*

```python
>>> a = 10
>>> b = 20
>>>
>>> a, b = b, a
>>>
>>> a
20
>>> b
10
>>>
```

- Iterando sobre uma sequência com informação de índice - `enumerate(seq)`

```python
>>> lista = ["a", "b", "c", "d", "e"]
>>> for indice, valor in enumerate(lista):
...     print(f"{indice:<5}: {valor}")
...
0    : a
1    : b
2    : c
3    : d
4    : e
>>>
```

- Slices permitem referênciar partes de sequências

Slices têm o formato: `seq[inicio:fim]` ou, opcionalmente, passando um *step* `seq[inicio:fim:step]`

`fim` não é incluído no resultado.

```python
>>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> lista[0:5] # retorna os indices 0, 1, 2, 3, 4
[1, 2, 3, 4, 5]
>>>
```

`inicio` assume, se omitido, o valor `0`.
`fim` assume, se omitido, o tamanho (`len()`) da sequência.
`step` por padrão `= 1`.

```python
>>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> lista[5:]
[6, 7, 8, 9]
>>>
>>> lista[:5]
[1, 2, 3, 4, 5]
>>>
>>> lista[::2] # 2 em 2
[1, 3, 5, 7, 9]
>>>
>>> lista[:] # nova lista, copiando as variaveis da anterior (shallow copy)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
```

Índices negativos podem ser utilizados em slices, mas é um pouco confuso:

```python
>>> lista = ["a", "b", "c", "d", "e"]
>>>
>>> lista[::-1]
['e', 'd', 'c', 'b', 'a']
>>>
>>> lista[-4:-1]
['b', 'c', 'd']
>>>
```

Modificar listas via *slices*:

```python
>>> lista = ["a", "b", "c", "d", "e"]
>>>
>>> lista[0:3] = [1, 2, 3]
>>> lista
[1, 2, 3, 'd', 'e']
>>>
>>> lista[4:] = []
>>> lista
[1, 2, 3, 'd']
>>>
>>> lista[3:] = [10, 20, 30]
>>> lista
[1, 2, 3, 10, 20, 30]
>>>
```

Zerar lista com slices:

```python
>>> lista
[1, 2, 3, 10, 20, 30]
>>>
>>> lista[:] = []
>>>
>>> lista
[]
>>>
```

- Deletando com `del`

Em listas:

```python
>>> lista = ["a", "b", "c", "d", "e"]
>>>
>>> del lista[4]
>>>
>>> lista
['a', 'b', 'c', 'd']
>>>
>>> del lista[2:5]
>>>
>>> lista
['a', 'b']
>>>
>>> del lista[:]
>>> lista
[]
>>>
```

Deletando variáveis:

```python
>>> valor = 42
>>>
>>> del valor
>>>
>>> valor
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-24-57d0d821be24> in <module>
----> 1 valor

NameError: name 'valor' is not defined
>>>
```

- Ordenar lista  `sort()`, *in-place*

```python
>>> numeros = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
>>> numeros.sort()
>>>
>>> numeros
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>>
```

- Ordenar de forma reversa `sort()`, *in-place*

```python
>>> numeros.sort(reverse=True)
>>> numeros
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>>
```

- Ordenar, mas sem alterar o original (cópia) `sorted(lst)`

```python
>>> numeros = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
>>>
>>> sorted(numeros)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>>
>>> sorted(numeros, reverse=True)
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>>
>>> numeros
[10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
>>>
```

- Obter o índice de um valor em uma lista `index()`

Retorna o primeiro índice encontrado:

```python
>>> lista = ["pato", "galinha", "cachorro", "cisne", "ganso", "rato"]
>>> lista.index("cachorro")
2
>>>
>>> lista.index("pato", 3) # busque a partir do indice 3
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-37-f3f9bc37610e> in <module>
----> 1 lista.index("pato", 3) # busque a partir do indice 3

ValueError: 'pato' is not in list
>>>
>>> lista.index("pato", 0, 3) # busque entre os indices 0 e 2 (3 não é incluído)
0
>>>
>>>
```

- Verificando presença com `in` e ausência com `not in`:

```python
>>> lista = ["pato", "galinha", "cachorro", "cisne", "ganso", "rato"]
>>>
>>> "pato" in lista
True
>>>
>>> "gato" not in lista
True
>>>
```

- `in` pode ser utilizado para evitar exceções, ao tentar acessar algo que não está presente:

```python
>>> lista = ["pato", "galinha", "cachorro", "cisne", "ganso", "rato"]
>>>
>>> busca = input("Qual valor deseja buscar ? ")
Qual valor deseja buscar ? gato
>>>
>>> if busca  in lista:
...     print(f"{busca} encontrado na posicao {lista.index(busca)}")
... else:
...     print("nao encontrado")
...
nao encontrado
>>>
```

- Funções `any` e `all`

`any` retorna `True` se algum elemento da sequência for `True`, basta um:

```python
>>> lista = [0, 0, 0, 0, 1]
>>> any(lista)
True
>>>
>>> lista = [0, 0, 0, ""]
>>> any(lista)
False
>>>
```

`all` retorna `True` apenas se todos elementos da lista forem `True`

```python
>>> lista = [1, 1, 1, 1, 1]
>>> all(lista)
True
>>>
>>> lista = [1, 1, 1, 1, 0]
>>> all(lista)
False
>>>
```

- Outros métodos de listas

Inserir um objeto antes de determinada posição, `insert`:

```python
>>> lista = ["vermelho", "azul", "verde"]
>>>
>>> lista.insert(0, "branco")
>>> lista
['branco', 'vermelho', 'azul', 'verde']
>>>
```

Adicionar ao final `append`:

```python
>>> lista.append("roxo")
>>> lista
['branco', 'vermelho', 'azul', 'verde', 'roxo']
>>>
```

Adicionando todos elementos de uma outra sequência ao final da lista, `extend` ou `+=`:

```python
>>> lista
['branco', 'vermelho', 'azul', 'verde', 'roxo']
>>>
>>> lista.extend(["rosa", "laranja"])
>>> lista
['branco', 'vermelho', 'azul', 'verde', 'roxo', 'rosa', 'laranja']
>>>
```

Removendo a primeira ocorrência por valor:

```python
>>> lista = [1, 2, 3, 10, 2, 33]
>>> lista.remove(2)
>>>
>>> lista
[1, 3, 10, 2, 33]
>>>
```

Cuidado, uma exceção é gerada se não for possível remover:

```python
>>> lista = [1, 2, 3, 10, 2, 33]
>>> lista.remove(42)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-67-c64630808f10> in <module>
----> 1 lista.remove(42)

ValueError: list.remove(x): x not in list
>>>
```

Limpe uma lista com `clear`:

```python
>>> lista = [1, 2, 3]
>>> lista.clear()
>>> lista
[]
>>>
```

Conte número de ocorrências com `count`:

```python
>>> lista = [0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1]
>>>
>>> lista.count(0)
6
>>> lista.count(1)
5
>>>
```

Invertendo a ordem de uma lista `reverse`:

```python
>>> lst = [1, 2, 4, 3, 6, 5]
>>> lst.reverse()
>>> lst
[5, 6, 3, 4, 2, 1]
>>>
```

Cópia *shallow* de uma lista `copy`:

```python
>>> l_a = [1, 2, 3]
>>> l_b = l_a
>>> l_c = l_a.copy()
>>>
>>> l_a[1] = "X"
>>>
>>> l_a
[1, 'X', 3]
>>>
>>> l_b
[1, 'X', 3]
>>>
>>> l_c
[1, 2, 3]
>>>
```

- Para simular uma pilha com uma lista, use `append` e `pop`

```python
>>> pilha = []
>>>
>>> pilha.append(10)
>>> pilha.append(15)
>>> pilha.append(30)
>>>
>>> # LIFO
>>> pilha.pop()
30
>>> pilha.pop()
15
>>>
```

Cuidado, `pop()` gera exceção se a lista estiver vazio:

```python
>>> pilha.pop()
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-10-1091ca38982e> in <module>
----> 1 pilha.pop()

IndexError: pop from empty list
>>>
```

- *List comprehensions* permitem criar novas listas a partir da iteração sobre sequências existentes

*Mapping*: produzir uma lista de mesmo tamanho mas com o resultado de uma expressão para cada item da sequência original:

```python
>>> lista = [1, 2, 3, 4, 5]
>>>
>>> dobrados = [item * item for item in lista]
>>> dobrados
[1, 4, 9, 16, 25]
>>>
```

É possível adicionar condicionais para filtrar os items processados e, consequentemente, o resultado gerado:

```python
>>> lista = [1, 2, 3, 4, 5]
>>> nums_par_dobrados = [item * item for item in lista if item % 2 == 0]
>>> nums_par_dobrados
[4, 16]
>>>
```

Pode atuar inclusive sobre outras listas:

```python
>>> lista = [1, 2, 3, 4, 5]
>>> processado = [item + 5 for item in lista]
>>> processado
[6, 7, 8, 9, 10]
>>>
```

Inclusive, dá para iterar sobre listas aninhadas:

```python
>>> matriz = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>>
>>> matriz_flat = [valor for linha in matriz for valor in linha]
>>> matriz_flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
```

Note que dentro da *list comprehension* a ordem está meio que invertida. O exemplo acima é interpretado:

```python
>>> matriz = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>>
>>> matriz_flat = []
>>> for linha in matriz:
...     for valor in linha:
...         matriz_flat.append( valor )
...
>>>
>>> matriz_flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
```

- *Generator expressions* são como *list comprehensions*, mas ao invés de produzir a lista toda me memória de vez, eles produzem um valor por vez. Cada vez que são *chamados*. Isto permite economizar bastante memória (*lazy evaluation*).

```python
>>> matriz = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>>
>>> gerador = (valor for linha in matriz for valor in linha if valor % 2 == 0)
>>> gerador
<generator object <genexpr> at 0x7fd6a748fa40>
>>>
>>> for item in gerador:
...     print(item)
...
2
4
6
8
>>>
```

- `filter()`, `map()`, `reduce()` - funções que auxiliam na programação funcional

`filter(fx, seq)` aplica `fx` a cada item da sequência `seq`, e retorna uma lista contendo apenas os items de `seq` em que `fx` retornou `True`:

```python
>>> def eh_par(valor):
...     if valor % 2 == 0: return True
...     return False
...
>>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>

# Retorna um iterador (similar a um generator)
>>> pares = filter(eh_par, lista)
>>> pares
<filter at 0x7fd6a741c550>
>>>
# Valores so sao produzidos quando a iteracao ocorre
>>> for par in pares:
...     print(par)
...
2
4
6
8
>>>
```

Funções em Python são objetos de primeira ordem, podendo ser atribuídos, passados como parâmetros, etc.

O exemplo acima poderia ser reduzido através da utilização de funções anônimas, criadas com `lambda`:

```python
>>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> pares = filter(lambda valor: valor % 2 == 0, lista)
>>> pares
<filter at 0x7fd6a741c278>
>>>
>>> for par in pares: print(par)
2
4
6
8
>>>
```

- Funções anônimas tem o formato:

`lambda parametros: expressao`

Implicitamente a função retorna o valor de `expressao`.

- `map(fx, seq)` aplica `fx` a cada item de `seq` e retorna um iterador com os resultados gerados:

```python
>>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> dobrados = map(lambda numero: numero * numero, lista)
>>> dobrados
<map at 0x7fd6a736e860>
>>>
>>> for valor in dobrados:
...     print(valor)
...
1
4
9
16
25
36
49
64
81
>>>
```

`filter` e `map` podem ser combinados:

dobrando apenas os números pares:

```python
>>> lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> pares_dobrados = map(lambda x: x * x, filter(lambda y: y % 2 == 0, lista))
>>> print( list(pares_dobrados) )
[4, 16, 36, 64]
>>>
```

O módulo `functools` traz uma série de funções que auxiliam na programação funcional.
Uma, bastante útil, é a função `reduce` que permite transformar uma sequência em um valor único:

```python

>>> from functools import reduce
>>>
>>>
>>> lista = [1, 2, 3, 4, 5]
>>> reduce(lambda x, y: x + y, lista, 0)
15
>>>
```

No exemplo acima:

`lambda x, y: x + y` é a função executada para cada item de `lista`.
`x` é o valor acumulado, `y` é o valor da vez na `lista`.
`x + y` a expressão retornada.

`lista` é a sequência percorrida.

`0` é o valor inicial do acumulador.

- `min` e `max` permitem a passagem do parâmetro `key`, que define uma função a ser aplicada em cada elemento ser processado.
O resultado dessa função é utilizado então.

```python
>>> lista = ['Blue', 'green', 'orange', 'Red', 'Yellow']
>>>
>>> min(lista)
'Blue'
>>>
>>> min(lista, key=lambda x: x.lower())
'Blue'
>>>
>>> max(lista)
'orange'
>>>
>>> max(lista, key=lambda x: x.lower())
'Yellow'
>>>
```

- `reversed()` permite iterar no sentido contrário sobre qualquer sequência:

```python
>>> lista = [1, 2, 3, 4, 5]
>>>
>>> for item in reversed(lista): print(item)
5
4
3
2
1
>>>
```

- `zip()` combina sequências, permitindo iterar sobre mais de uma seq ao mesmo tempo

```python
>>> alunos = ["joao", "maria", "paula", "pedro", "ana carina"]
>>> notas  = [8.49,   3.1,     9.9,     5.0,     7.4         ]
>>>
>>> for aluno, nota in zip(alunos, notas):
...     print(f"{aluno:<10} - {nota:>10.2f}")
...
joao       -       8.49
maria      -       3.10
paula      -       9.90
pedro      -       5.00
ana carina -       7.40
>>>
```

- Matrizes podem ser criadas aninhando listas em listas

```python
>>> matriz = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>>
>>> for linha in matriz:
...     print(linha)
...
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
>>>
>>> matriz[0][2] # primeira linha, terceira coluna (indices comecam em zero)
3
>>>
```

- Dicionários e `sets`

Dicionários são coleções que vinculam chaves imutáveis a valores (de qualquer tipo).
`Sets` são conjuntos de valores imutáveis únicos.
Ambas coleções não apresentam ordem.

As chaves dos dicionários devem ser de tipos imutáveis (`strings`, `int`, `float`, `tuple`) e não podem se repetir. Os valores associados, podem se repetir.

```python
>>> dic_vazio = {}
>>>
>>> paises_abbr = {
...     "Finland": "fi",
...     "South Africa": "za",
...     "Nepal": "np"
... }
>>> paises_abbr
{'Finland': 'fi', 'South Africa': 'za', 'Nepal': 'np'}
>>>
```

`len` retorna o número de pares de um dicionário:

```python
>>> len(paises_abbr)
3
>>>
```

Dicionários, listas e qualquer outra sequência de Python, quando vazias têm valor lógico `False`. Se tiver pelo menos um item, é `True`:

```python
>>> dic = {"a": 1, "b": 2, "c": 3}
>>> len(dic)
3
>>>
>>> bool( dic )
True
>>>
>>> dic.clear()
>>> len(dic)
0
>>>
>>> bool( dic )
False
>>>
```

- Formas de iteração sobre um dicionário:

Iterando sobre as chaves implicitamente:

```python
>>> dic = {"a": 1, "b": 2, "c": 3}
>>>
>>> for chave in dic:
...     print(chave)
...
a
b
c
>>>
```

Iterando sobre as chaves explicitamente `.keys()`:

```python
>>> dic = {"a": 1, "b": 2, "c": 3}
>>> for chave in dic.keys():
...     print(chave)
...
...
a
b
c
>>>
```

Iterando sobre os valores `.values()`:

```python
>>> dic = {"a": 1, "b": 2, "c": 3}
>>> for valor in dic.values():
...     print(valor)
...
...
...
1
2
3
```

Iterando sobre os pares chave e valor `.items()`:

```python
>>> dic = {"a": 1, "b": 2, "c": 3}
>>> for chave, valor in dic.items():
...     print(f"{chave}:{valor:>10}")
...
a:         1
b:         2
c:         3
>>>
>>>
```

- Principais operações com dicionários

Declaração:

```python
# X propositalmente errado
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
```

Acessando um valor por indexação:

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
>>> numeros_romanos['I']
1
>>>
>>> numeros_romanos["V"]
5
>>>
```

Alterando um valor:

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
>>>
>>> numeros_romanos["X"] = 10
>>>
>>> numeros_romanos
{'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}
>>>
```

Adicionar novo par:

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}
>>>
>>> numeros_romanos["L"] = 50
>>>
>>> numeros_romanos
{'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 10, 'L': 50}
>>>
```

Removendo um par `del`:

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}
>>>
>>> del numeros_romanos["II"]
>>>
>>> numeros_romanos
{'I': 1, 'III': 3, 'V': 5, 'X': 10}
>>>
```

Removendo um par e guardando o valor removido `pop()`:

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}
>>>
>>> removido = numeros_romanos.pop("II")
>>>
>>> removido
2
>>>
>>> numeros_romanos
{'I': 1, 'III': 3, 'V': 5, 'X': 10}
>>>
```

Acesso a chaves que não existem geram a exceção `KeyError`:

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}
>>>
>>> numeros_romanos["Z"]
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-37-3e69e720dd74> in <module>
----> 1 numeros_romanos["Z"]

KeyError: 'Z'
>>>
```

A exceção pode ser evitada usando o método `.get`, que retorna `None`, caso não exista:

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}
>>>
>>> print( numeros_romanos.get("Z") )
None
>>>
```

`.get` aceita um segundo parâmetro, que é o valor a ser retornado caso a chave não seja encontrada, no lugar de `None`:

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}
>>> print( numeros_romanos.get("Z", "ops") )
ops
>>>
```

Os operadores `in` e `not in` permitem verificar se um chave está presente ou não em um dicionário:

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}
>>>
>>> if "I" in numeros_romanos:
...     print(numeros_romanos["I"])
...
1
>>>
>>> if "L" not in numeros_romanos:
...     numeros_romanos["L"] = 50
...
>>> print(numeros_romanos)
{'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 10, 'L': 50}
>>>
```

- Os objetos retornados por `.keys()`, `.values()` e `.items()` são visualizações do dicionário, referências. **Não são cópias.**

Por isso, é possível criar uma `view`, alterar o dicionário e a `view` se manterá coerente:

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}
>>>
>>> chaves = numeros_romanos.keys()
>>> chaves
dict_keys(['I', 'II', 'III', 'V', 'X'])
>>>
>>> numeros_romanos["L"] = 50
>>>
>>> chaves
dict_keys(['I', 'II', 'III', 'V', 'X', 'L'])
>>>
```

Por isso mesmo, evite alterar um dicionário enquanto itera sobre uma `view` deste.

Para iterar sobre um dicionário de forma ordenada, use `sorted()` e `keys()`:

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}
>>>
>>> for chave in sorted(numeros_romanos.keys()):
...     print(chave)
...
I
II
III
V
X
>>>
```

- `==` e `!=` podem ser utilizados para comparar dicionários.

A comparação verifica se os dois dicionários têm os mesmos pares `chave: valor`, independente da ordem.

```python
>>> d1 = {"a": 10, "b": 20}
>>> d2 = {"b": 20, "a": 10}
>>>
>>> d1 == d2
True
>>>
>>> d3 = {"a": 1, "b": 20}
>>>
>>> d1 == d3
False
>>>
>>> d1 != d3
True
>>>
```

- Módulo `collections`

É possível contar as ocorrências em uma sequência com a classe `collections.Counter`:

```python
>>> texto = "Minha fé é no desconhecido, em tudo que não podemos compreender por meio da razão. Creio que o que está acima do nosso entendimento é apenas um
... fato em outras dimensões e que no reino do desconhecido há uma infinita reserva de poder."
>>>
>>> from collections import Counter
>>>
>>> counter_texto = Counter(texto.split(" "))
>>> counter_texto
Counter({'Minha': 1,
         'fé': 1,
         'é': 2,
         'no': 2,
         'desconhecido,': 1,
         'em': 2,
         'tudo': 1,
         'que': 4,
         'não': 1,
         'podemos': 1,
         'compreender': 1,
         'por': 1,
         'meio': 1,
         'da': 1,
         'razão.': 1,
         'Creio': 1,
         'o': 1,
         'está': 1,
         'acima': 1,
         'do': 2,
         'nosso': 1,
         'entendimento': 1,
         'apenas': 1,
         'um': 1,
         'fato': 1,
         'outras': 1,
         'dimensões': 1,
         'e': 1,
         'reino': 1,
         'desconhecido': 1,
         'há': 1,
         'uma': 1,
         'infinita': 1,
         'reserva': 1,
         'de': 1,
         'poder.': 1})
>>>

>>> for token, total in counter_texto.items():
...     print(f"{token}:{total:>5}")
...
Minha:    1
fé:    1
é:    2
no:    2
desconhecido,:    1
em:    2
tudo:    1
que:    4
não:    1
podemos:    1
compreender:    1
por:    1
meio:    1
da:    1
razão.:    1
Creio:    1
o:    1
está:    1
acima:    1
do:    2
nosso:    1
entendimento:    1
apenas:    1
um:    1
fato:    1
outras:    1
dimensões:    1
e:    1
reino:    1
desconhecido:    1
há:    1
uma:    1
infinita:    1
reserva:    1
de:    1
poder.:    1
>>>
```

Neste último exemplo, poderíamos ordenar as tuplas retornadas por `items()` com a função `sorted()` que ordena as tuplas comparando seus primeiros elementos. Se forem iguais, compara o segundo, e assim por diante:

```python
>>> for token, total in counter_texto.items():
...     print(f"{token}:{total:>5}")
...
Minha:    1
fé:    1
é:    2
no:    2
desconhecido,:    1
em:    2
tudo:    1
que:    4
não:    1
podemos:    1
compreender:    1
por:    1
meio:    1
da:    1
razão.:    1
Creio:    1
o:    1
está:    1
acima:    1
do:    2
nosso:    1
entendimento:    1
apenas:    1
um:    1
fato:    1
outras:    1
dimensões:    1
e:    1
reino:    1
desconhecido:    1
há:    1
uma:    1
infinita:    1
reserva:    1
de:    1
poder.:    1
>>>
Do you really want to exit ([y]/n)? ^[n
Do you really want to exit ([y]/n)? n
>>> for token, total in sorted(counter_texto.items()):
...     print(f"{token}:{total:>5}")
...
...
Creio:    1
Minha:    1
acima:    1
apenas:    1
compreender:    1
da:    1
de:    1
desconhecido:    1
desconhecido,:    1
dimensões:    1
do:    2
e:    1
em:    2
entendimento:    1
está:    1
fato:    1
fé:    1
há:    1
infinita:    1
meio:    1
no:    2
nosso:    1
não:    1
o:    1
outras:    1
podemos:    1
poder.:    1
por:    1
que:    4
razão.:    1
reino:    1
reserva:    1
tudo:    1
um:    1
uma:    1
é:    2
>>>
```

- Atualizando dicionário com o método `update()`

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
>>>
>>> numeros_romanos.update(X=10)
>>> numeros_romanos
{'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 10}
```

```python
>>> # ou, a partir de outro dicionario
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
>>>
>>> dic_atualizacao = {"X": 10, "L": 50}
>>>
>>> numeros_romanos.update(dic_atualizacao)
>>> numeros_romanos
{'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 10, 'L': 50}
>>>
```

ou uma sequência de tuplas:

```python
>>> numeros_romanos = {'I':   1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
>>>
>>> numeros_romanos.update( [("X", 10), ("L", 50)] )
>>> numeros_romanos
{'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 10, 'L': 50}
>>>
```

- *dict comprehensions*

```python
>>> notas = {"joao": [10, 9.4, 7.7], "maria": [3.5, 4.4, 9.0]}
>>>
>>> medias = {aluno: sum(notas) / len(notas) for aluno, notas in notas.items()}
>>>
>>> medias
{'joao': 9.033333333333333, 'maria': 5.633333333333333}
>>>
```


Se no *dict comprehension* uma chave se repetir, ela é atualizada:

```python
>>> matriculas = {"joao": 2019001, "maria": 2019002, "pedro": 2019003, "paulo": 2019003} # repetido os valores de pedro e paulo
>>>
>>> matriculas_invertidas = {matricula: nome for nome, matricula in matriculas.items()}
>>> matriculas_invertidas
{2019001: 'joao', 2019002: 'maria', 2019003: 'paulo'} # paulo veio depois e atualizou
>>>
```

- `sets`

Um `set` é uma coleção não ordenada de valores únicos.

`sets` podem conter apenas objetos imutáveis.

`sets` não podem ser indexados, mas podem ser iterados.

declaração:

```python
>>> cores = {"vermelho", "azul", "verde", "preto", "vermelho"}
>>> cores
{'azul', 'preto', 'verde', 'vermelho'}
>>>
```

Note que valores duplicados (`"vermelho"`) são suprimidos de forma implícita e sem gerar exceções.

Este é um dos principais usos para `sets`, remover duplicatas:

```python
>>> lista = [1, 2, 3, 4, 1, 2, 15, 3, 3, 3]
>>>
>>> lista_unicos = set(lista)
>>> lista_unicos
{1, 2, 3, 4, 15}
>>>
```


- Operações com `sets`

Tamanho `len()`:

```python
>>> s = {1, 3, 4, 3, 6, 7}
>>> s
{1, 3, 4, 6, 7}
>>>
>>> len(s)
5
>>>
```

Presença `in`:

```python
>>> s = {"vermelho", "azul", "roxo"}
>>>
>>> "roxo" in s
True
>>>
>>> "verde" not in s
True
>>>
```

Iteração `for`:

```python
>>> for cor in s:
...     print(cor)
...
vermelho
azul
roxo
>>>
```

Além da expressão, é possível usar a função `set()` para criar a partir de outras sequências:

```python
>>> lista = [1, 3, 4, 3, 3, 2, 7, 9]
>>>
>>> s_lista = set(lista)
>>> s_lista
{1, 2, 3, 4, 7, 9}
>>>
```

- Para criar um `set` vazio, use `set()`. `{}` produz um dicionário vazio.

```python
>>> dic_vazio = {}
>>>
>>> set_vazio = set()
>>>
>>> dic_vazio
{}
>>>
>>> set_vazio
set()
>>>
```

- Adicionando elementos a um `set()` com `add()`:

```python
>>> s = {12, 13, 14}
>>> s.add(15)
>>> s
{12, 13, 14, 15}
>>>
```

- Removendo com `remove(valor)`

```python
>>> s = {12, 13, 14}
>>> s.add(15)
>>> s
{12, 13, 14, 15}
>>>
>>> s.remove(15)
>>> s
{12, 13, 14}
>>>
```

Lembre-se: apesar de serem mutáveis, `set()` só podem conter elementos imutáveis. Ou seja, um `set()` não pode conter outro `set()`:

```python
>>> s_in_s = {1, 2, 3, {4, 5, 6}}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-112-3bdd54200959> in <module>
----> 1 s_in_s = {1, 2, 3, {4, 5, 6}}

TypeError: unhashable type: 'set'
>>>
```

- `frozenset`, os `sets` imutáveis e `hashable`


A função `frozenset()` cria `frozenset` a partir de qualquer sequência, ou `frozenset` vazios:

```python
>>> fset_vazio = frozenset()
>>>
>>> lista = [1, 2, 1, 3, 4, 4]
>>> fset_lista = frozenset(lista)
>>> fset_lista
frozenset({1, 2, 3, 4})
>>>
```

`frozenset` também removem duplicatas.

- Operações com `set`

Comparação e diferença:

```python
>>> {1, 3, 5} == {3, 1, 5}
True
>>>
>>> {1, 3, 4} != {4, 5, 1}
True
>>>
```

Teste se o da esquerda é um *subset* do da direita com `<`:

```python
>>> {1, 3, 5} < {1, 2, 3, 4, 5}
True
>>>
```

E pode-se verificar se o da esquerda é um *superset* do da direita com `>`:

```python
>>> {1, 2, 3, 4, 5} > {1, 3, 4}
True
>>>
```

Estas operações podem ser feitas pelos métodos `issubset()` e `issuperset()`:

```python
>>> {1, 2, 3}.issubset({1, 2, 3, 4, 5})
True
>>>
>>> {1, 2, 3, 4, 5}.issuperset({1, 2, 3})
True
>>>
```

- Operações matemáticas com conjuntos

Obs: Os operadores requerem que os dois objetos envolvidos sejam `set()`.
Os métodos, entretanto, suportam quaisquer sequências, que são convertidas em `set()` antes da operação:

União: `|` ou `.union()`. Tudo dos dois conjuntos.

```python
>>> {1, 2, 3} | {4, 5, 6}
{1, 2, 3, 4, 5, 6}
>>>
>>> {1, 2, 3}.union({4, 5, 6})
{1, 2, 3, 4, 5, 6}
>>>
>>> {1, 2, 3}.union([10, 20, 30])
{1, 2, 3, 10, 20, 30}
>>>
```

Intersecção: `&` ou `.intersection()`. Apenas o que é comum entre os conjuntos.

```python
>>> {1, 2, 3} & {3, 4, 5}
{3}
>>>
>>> {1, 2, 3}.intersection([3, 4, 5])
{3}
>>>
```

Diferença: `-` ou `.difference()`. Todos que estão no conjunto da esquerda mas **não** estão no da direita.

```python
>>> {1, 2, 3} - {3, 4, 5}
{1, 2}
>>> {1, 2, 3}.difference((3, 4, 5))
{1, 2}
>>>
```

Diferença simétrica: `^` ou `.symmetric_difference`. Apenas os elementos que são exclusivos de cada conjunto.

```python
>>> {1, 2, 3} ^ {3, 4, 5}
{1, 2, 4, 5}
>>> {1, 2, 3}.symmetric_difference((3, 4, 5))
{1, 2, 4, 5}
>>>
```

Dois conjuntos são **disjuntos** se eles **não** contêm nenhum elemento em comum. A intersecção é vazia.

Verifica-se com `.isdisjoint()`:

```python
>>> a = {1, 2, 3}
>>> b = {4, 5, 6}
>>>
>>> a & b
set()
>>>
>>> a.isdisjoint(b)
True
>>>
```

Esses operadores podem ser usados com atribuições.

União com atribuição ou `.update()`:

```python
>>> a = {1, 2, 3}
>>>
>>> a |= {4, 5, 6}
>>> a
{1, 2, 3, 4, 5, 6}
>>>

>>> a = {1, 2, 3}
>>> a.update([4, 5, 6])
>>> a
{1, 2, 3, 4, 5, 6}
>>>
```

Outros operadores com atribuição são:

Intersecção: `&=` ou `.intersection_update()`:

```python
>>> a = {1, 2, 3}
>>> b = {3, 4, 5}
>>>
>>> a &= b
>>> a
{3}

>>> a = {1, 2, 3}
>>> b = {3, 4, 5}
>>>
>>> a.intersection_update(b)
>>> a
{3}
>>>
```

Diferença: `-=` ou `.difference_update()`

```python
>>> a = {1, 2, 3}
>>> b = {3, 4, 5}
>>>
>>> a -= b
>>> a
{1, 2}

>>> a = {1, 2, 3}
>>> b = {3, 4, 5}
>>> a.difference_update(b)
>>> a
{1, 2}
>>>
```

Diferença simétrica `^=`  ou `.symmetric_difference_update()`:

```python
>>> a = {1, 2, 3}
>>> b = {3, 4, 5}
>>>
>>> a ^= b
>>> a
{1, 2, 4, 5}

>>> a = {1, 2, 3}
>>> b = {3, 4, 5}
>>> a.symmetric_difference_update(b)
>>> a
{1, 2, 4, 5}
>>>
```

- Métodos para adicionar e remover items de `sets`

Adicionar `add(valor)`

```python
>>> s = {1, 2}
>>> s.add(3)
>>> s
{1, 2, 3}
>>>
```

Remover `remove(valor)`:

```python
>>> s = {1, 2, 3}
>>> s.remove(2)
>>> s
{1, 3}
>>>
```

Contudo, `remove` gera exceção se o valor não estiver presente:

```python
>>> s = {1, 2, 3}
>>> s.remove(2)
>>> s
{1, 3}
>>> s.remove(4)
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-57-758cf2d329e6> in <module>
----> 1 s.remove(4)

KeyError: 4
>>>
```

Para remover sem risco de produzir exceções, use `discard(valor)`:

```python
>>> s = {1, 2, 3}
>>>
>>> s.discard(2)
>>> s
{1, 3}
>>>
>>> s.discard(2)
>>> s
{1, 3}
>>>
```

Retornar um elemento do início do `set` com `pop()`:

```python
>>> s = {1, 3, 4, 5, 2, 7, 9, 8}
>>> s.pop()
1
>>> s.pop()
2
>>> s.pop()
3
>>>
```

Por fim, `.clear()` limpa o `set`:

```python
>>> s = {1, 2, 3}
>>> s.clear()
>>> s
set()
>>>
```

- *Set comprehensions*

```python
>>> palavras = "bacon", "spam", "eggs", "yaki!", "knight", "boom", "bacon", "bacon", "spam"
>>>
>>> set_palavras_grandes = {palavra for palavra in palavras if len(palavra) >= 5}
>>> set_palavras_grandes
{'bacon', 'knight', 'yaki!'}
>>>
```

- Formatando strings

Nas *f-strings* os *placeholders* são convertidos para `str` por padrão.

Às vezes é necessário definir o tipo, exemplo: formatação de `floats`:

```python
>>> import math
>>>
>>> math.pi
3.141592653589793
>>>
>>> math.e
2.718281828459045
>>>
>>> print(f"{math.pi:.2f}")
3.14
>>> print(f"{math.e:.2f}")
2.72
>>>
```

A definição do tipo é necessária, pois a definição do número de casas decimais `.2` só é possível para `floats` e `Decimals`.

Outras definições de tipo incluem:

`d`, para inteiros:

```python
>>> print(f"{10:d}")
10
```

É possível usar os tipos `b` para representar inteiros em binário:

```python
>>> print(f"{10:b}")
1010
>>>
```

Ou `o` para octal e `x` para hexadecimal:

```python
>>> print(f"{10:o}")
12
>>> print(f"{10:x}")
a
>>>
```

E `c` formata um inteiro como o caractere correspondente:

```python
>>> print(f"{99:c}")
c
>>>
```

Se você usar a representação `s`, de `str`, a expressão tem que retornar uma string:

```python
>>> nome = "John"
>>> print(f"{nome:s}")
John
>>>
```

Não há conversão automática:

```python
>>> idade = 15
>>> print(f"{idade:s}")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-19-23c592b5549d> in <module>
----> 1 print(f"{idade:s}")

ValueError: Unknown format code 's' for object of type 'int'
>>>
```

Essa conversão só existe se você **não** especificar:

```python
>>> idade = 15
>>> print(f"{idade}")
15
>>>
```

- Alinhamento

Em *f-strings* números são, por padrão, alinhados a direita e todo o resto à esquerda:

```python
>>> inteiro = 15
>>> print(f"[{inteiro:20}]")
[                  15]
>>>

>>> numero = 3.14
>>> print(f"[{numero:20}]")
[                3.14]

>>> texto = "bacon"
>>> print(f"[{texto:20}]")
[bacon               ]
>>>
```

Você pode usar `<` e `>` para indicar o alinhamento desejado:

```python
>>> from math import pi
>>> print(f"[{pi:>30}]")
[             3.141592653589793]
>>> print(f"[{pi:<30}]")
[3.141592653589793             ]
```

E `^` para centralizar:

```python
>>> print(f"[{pi:^30}]")
[      3.141592653589793       ]
>>>
```

- Formatação numérica

Use `+` para forçar a presença do sinal em números positivos:

```python
>>> valor = 100
>>>
>>> print(f"{valor:+}")
+100
>>>
```

Caso queira que ao invés do `+` um espaço apareça para números positivos (para alinharem iguais aos negativos), use um espaço no lugar do `+`:

```python
>>> positivo = 10
>>> negativo = -10
>>> print(f"[{negativo}]")
[-10]
>>> print(f"[{positivo: d}]")
[ 10]
>>>
```


Para preencher os espaços com zeros, adicionar um `0` antes da formatação:

```python
>>> from math import pi
>>>
>>> print(f"[{pi:>030}]")
[00000000000003.141592653589793]
>>>
```

Por fim, para incluir separador de milhar (`,`) use `:,d`:

```python
>>> valor = 1_234_567
>>> print(f"{valor:,d}")
1,234,567
>>>
```

Separando milhares e parte decimal:

```python
>>> valor = 1_234_567.89
>>>
>>> print(f"{valor:,.3f}")
1,234,567.890
>>>
```

- Concatenar `+` e repetir strings `*`

```python
>>> a = "spam"
>>> b = "bacon"
>>>
>>> c = a + b
>>> c
'spambacon'
>>>
>>> d = a * 3
>>> d
'spamspamspam'
>>>
```

- Remova espaços dos dois lados das strings com `strip()`:

```python
>>> mensagem = "  spam bacon eggs  "
>>>
>>> mensagem_limpa = mensagem.strip()
>>> mensagem_limpa
'spam bacon eggs'
>>>
```

Removendo só da esquerda com `lstrip()` ou da direita com `rstrip()`:

```python
>>> mensagem = "  spam bacon eggs  "
>>>
>>> mensagem.lstrip()
'spam bacon eggs  '
>>>
>>> mensagem.rstrip()
'  spam bacon eggs'
>>>
>>>
```

- Capitalizar `.capitalize()` e formatar em título com `.title()`:

```python
>>> msg = "i believe i can fly"
>>>
>>> msg.capitalize()
'I believe i can fly'
>>>
>>> msg.title()
'I Believe I Can Fly'
>>>
```

- Buscando por substrings

Contando ocorrências com `.count()`:

```python
>>> sentenca = "As aguias voam alto singrando todo o ceu"
>>> sentenca.count("as")
1
>>> sentenca.count("a")
5
>>>
```

Você pode delimitar o *range* de busca:

```python
>>> sentenca = "As aguias voam alto singrando todo o ceu"
>>> sentenca.count("a", 5, 10)
1
>>>
```

Ache o primeiro índice em que uma substring inicia:

```python
>>> sentenca = "As aguias voam alto singrando todo o ceu"
>>>
>>> indice = sentenca.index("voam")
>>> indice
10
>>>
>>> sentenca[indice:]
'voam alto singrando todo o ceu'
>>>
```

Mas, se não encontrar, gera exceção:

```python
>>> indice = sentenca.index("xxx")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-86-b1aa2828ab61> in <module>
----> 1 indice = sentenca.index("xxx")

ValueError: substring not found
>>>
```

Você pode buscar em sentido contrário (encontrando o índice da última ocorrência da substring) usando `rindex`:

```python
>>> sentenca = "As aguias voam alto singrando todo o ceu"
>>>
>>> sentenca.rindex("o")
35
>>>
```

Os métodos `find()` e `rfind()` fazem a mesma coisa, mas ao invés de gerarem exceção quando não encontram, retornam `-1`:

```python
>>> sentenca = "As aguias voam alto singrando todo o ceu"
>>>
>>> sentenca.find("voam")
10
>>> sentenca.find("xxx")
-1
>>>
>>> sentenca.rfind("o")
35
>>> sentenca.rfind("xxx")
-1
>>>
```

- Para verificar presença de uma substring, use `in`, e ausência `not in`

```python
>>> "s" in "spam"
True
>>>
>>> "x" not in "spam"
True
>>>
```

- Se quiser verificar se começa com algo ou termina, `startswith()` ou `endswith()`:

```python
>>> text = "spam eggs bacon"
>>>
>>> text.startswith("spam")
True
>>>
>>> text.endswith("bacon")
True
>>>
```

- Para substituir substrings, use `replace()`

```python
>>> text = "spam eggs bacon"
>>>
>>> text = text.replace("spam", "bacon")
>>> text
'bacon eggs bacon'
>>>
```

- Dividindo e juntando strings

Divida com `split()`:

```python
>>> letras = "A, B, C, D"
>>> letras = letras.split(", ")
>>> letras
['A', 'B', 'C', 'D']
>>>
```

Por padrão, a quebra é por espaços em branco:

```python
>>> letras = "A B C D"
>>> letras = letras.split()
>>> letras
['A', 'B', 'C', 'D']
>>>
```

Um segundo parâmetro o máximo de pedaçõs a serem formados:

```python
>>> letras = "A, B, C, D"
>>> letras = letras.split(", ", 2)
>>> letras
['A', 'B', 'C, D']
>>>
```

Para unir, use `.join()`:

```python
>>> letras = "A, B, C, D"
>>> letras = letras.split(", ")
>>> letras
['A', 'B', 'C', 'D']
>>>
>>> " ".join(letras)
'A B C D'
>>> "-".join(letras)
'A-B-C-D'
>>>
>>>
```

- O método `partition()` permite quebrar uma string em uma tupla com três elementos: `(antes_token, token, depois_token)`. Útil para strings mais complexas:

```python
>>> text = "Amanda: 85, 93, 13"
>>> splitted = text.partition(":")
>>> splitted
('Amanda', ':', ' 85, 93, 13')
>>>
```

A busca pode ser feita da direita para esqueda com `rpartition`:

```python
>>> text = "Name: Amanda Grades: 85, 93, 13"
>>> text.rpartition(":")
('Name: Amanda Grades', ':', ' 85, 93, 13')
>>>
```

Para quebrar as linhas, use `splitlines()`:

```python
>>> msg = """
... Roses are red
... Violets are blue
... I can´t make music
... """
>>>
>>> msg.splitlines()
['', 'Roses are red', 'Violets are blue', 'I can´t make music']
>>>
```

Para quebrar e ainda sim manter as quebras de linha, passe `True` para `splitlines()`:

```python
>>> msg.splitlines(True)
['\n', 'Roses are red\n', 'Violets are blue\n', 'I can´t make music\n']
>>>
```

