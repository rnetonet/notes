# The Quick Python Book 3rd - Naomi Ceder

## Sobre Python

### Pontos fortes

* Fácil de usar
* Expressiva:

```python
# Swap entre duas variáveis
a = 10
b = 20
a, b = b, a
```

* Legível
* Tem (bibliotecas) baterias incluídas
* Multi-plataforma

### Pontos fracos

* Não tão rápida quanto C
* Tem menos bibliotecas - em alguns nichos - do que linguagens como C, Java...
* Não há verificação de tipos em *compile time*
* Não tem bom suporte em mobile
* GIL atrapalha concorrência

### Python em 10 minutos ou menos

#### Tipos numéricos

```python
# Inteiros
a = 3
b = -10

# O tamanho dos inteiros é limitado apenas pela memória disponível
c = 300102020101020120021 ^ 10

# Pontos Flutuantes
pi = 3.14

# Booleanos
t = True
z = False
```

#### Operações com tipos numéricos

* Com inteiros:

```python
>>> # Operacoes
>>> x = 5 + 2 - 10 + 35
>>> x
32
>>> 
>>> # Divisao normal
... 5 / 2
2.5
>>> 
>>> # Divisao descaranto a parte decimal
... 5 // 2
2
>>> # Resto da divisao
... 5 % 2
1
>>> # Resultado e resto da divisao
... divmod(5, 2)
(2, 1)
>> # Exponenciação
>>> 2 ** 8
256
>>> 100 ** 100
100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
>>> 
```

* Com pontos flutuantes:

```python
>>> x = 4.23 * 7.15
>>> x
30.244500000000006
>>> 
>>> 15.67 - 19.8
-4.130000000000001
>>> 
>>> 3.45 ** 5.6
1027.5120705982902
>>> 
```

* Algums funções *built-in* e do módulo *math*:

```python
>>> x = 3.49
>>> round(x) # built-in, sempre disponível, não precisa importar nada
3
>>> 
>>> import math
>>> math.ceil(x)
4
>>> 
>>> math.floor(x)
3
```

* Todo arquivo Python é um módulo. Os atributos definidos no módulo podem ser acessados a partir de outro módulo através de `import`. Feito o *import*, você pode acessar os atributos através da sintaxe: `module.function(arguments)`.

* Booleans:

```python
>>> x = True
>>> y = False
>>> 
>>> # Negando usando "not"
>>> not x
False
>>> 
>>> not y
True
>>> 
>>> # Booleans são nomes para os inteiros 0 e 1
>>> # True == 1, False == 0
... 
>>> x + x
2
>>> x + y
1
>>> y + y
0
>>> 
```

* Listas

```python
>>> # Lista vazia
... l1 = []
>>> 
>>> # Podem conter qualque tipo
... l2 = [1, 3.4, "aloha", [7, 6, 5]]
>>> l2 = [1, 3.4, "aloha", [7, 6, 5]]
>>> 
>>> # Indexando da esquerda pra direita (começa em 0)
... l2[0]
1
>>> l2[1]
3.4
>>> 
>>> # Indexando da direita pra esquerda (começa em -1)
... l2[-1]
[7, 6, 5]
>>> l2[-2]
'aloha'
>>> 

>>> # Slices. A primeira posição é inclusiva, a segunda não. 
>>> # l2[0:2] = l2[0], l2[1]...
... l2[0:2]
[1, 3.4]
>>> l2[1:3]
[3.4, 'aloha']
>>> l2[3:4]
[[7, 6, 5]]
>>> 

# Se omitir o primeiro índice, o slice começa do primeiro objeto
>>> l2[:3]
[1, 3.4, 'aloha']
>>> 

# Se omitir o segundo índice, o slice irá até o final
>>> l2[1:]
[3.4, 'aloha', [7, 6, 5]]
>>> l2[2:]
['aloha', [7, 6, 5]]
>>> 
```