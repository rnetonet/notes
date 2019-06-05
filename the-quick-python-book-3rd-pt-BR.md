# The Quick Python - Third Edition - Naomi Ceder

## Survey Python

Python tem 4 tipos numéricos principais:

- Inteiros ```-3, 42, 888888888888888``` (limitados apenas pela memória disponível)

- Pontos Flutuantes ```3.14, -2.14```

- Números Complexos ```-3 + 2j```

- Booleanos ```True, False```

As seguintes operações são suportadas: ```+, -, *, /, //, **, %```.

Exemplos com inteiros:

```python
>>> 10 + 3
13
>>> 
>>> 4 - 1
3
>>> 
>>> 13 / 4  # Divisão com resultado decimal
3.25
>>> 
>>> 13 // 4 # Divisão com resultado inteiro (truncado)
3
>>> 
>>> 2 ** 3  # Exponenciação
8
>>> 
>>> 13 % 2  # Resto da divisão
1
>>> 
```

Alguns exemplos com pontos flutuantes (baseados no tipo `double` do C):

```python
>>> 35.1 + 1.2
36.300000000000004
>>> 
>>> 33.0 - 13
20.0
>>> 
>>> 17.3 / 1.3
13.307692307692308
>>> 
>>> 17.3 // 1.3
13.0
>>> 
>>> 2.5 ** 3
15.625
>>> 
>>> 19 % 3.1
0.39999999999999947
>>> 
```

Existem diversas funções matemáticas aplicáveis. Algumas nativas, outras a partir de bibliotecas (acessíveis usando `
import`):

```python
>>> round(3.14)
3
>>> import math
>>> math.ceil(3.14)
4
>>> math.floor(3.14)
3
```

Exemplo de ```Booleans```:

```python
>>> x = False
>>> 
>>> x
False
>>> 
>>> not x
True
>>> 
>>> y = True
>>> y 
True
>>> not y
False
>>> 
>>> y * 2 # True == 1, False == 0
2
>>> False ** 4
0
>>> 
```

Python tem um tipo ```lista``` bastante poderoso que pode hospedar qualquer tipo de objeto, inclusive outras listas:

```python
>>> lst = [1, 3.14, "spam", ["a", "b", "c"]]
>>> lst
[1, 3.14, 'spam', ['a', 'b', 'c']]
```

Suportam indexação por deslocamento (*offset*) ou segmentos (*slices*):

```python

```