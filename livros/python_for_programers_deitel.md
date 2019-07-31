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

