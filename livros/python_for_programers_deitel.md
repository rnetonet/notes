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