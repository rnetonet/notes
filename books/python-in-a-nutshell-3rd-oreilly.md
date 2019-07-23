# Python in a Nutshell, 3rd Edition

### Interpretador

- Python tem um interpretador, `python`, que realiza interpretação e compilação (módulos importados).
- Em versões mais recentes, na plataforma Windows, há o launcher `py.exe`, que é incluído ao PATH.
- O interpretador é afetado por algumas variáveis de ambientes. As principais:
    - `PYTHONHOME` - Local de instalação do Python que deve conter um diretório `lib`, com as bibliotecas padrão do Python. Se não setada, heurísticas são aplicadas para encontrar o diretório.
    - `PYTHONPATH` - Lista de pasta em que o interpretador irá buscar por módulos. Separadas por vírgulas em ambientes UNIX e pontos-virgúla em ambientes Windows. Estende o valor de `sys.path`.
    - `PYTHONSTARTUP` - Nome ou caminho de um script a ser executado antes de uma sessão **interativa** do interpretador.
    - `PYTHONDONTWRITEBYTECODE` - Evita que o interpretador salve bytecodes em disco.

- Opções de linha de comando do interpretador:
    - `-B` - não gera bytecode
    - `-c "..."` - executa a linha de comando passada nas aspas e encerra
    - `-i` - abre uma sessão interativa ao final do script, mesmo que haja erro. A sessão tem acesso às variáveis globais definidas pelo script.
    - `-m module` - especifica um módulo, procurado em `PYTHONPATH`, para ser executado como script/main.
    - `-t` ou `-tt`, respectivamente, emitem warning/erro para indentação errada.
    - `-v` - mostra imports e cleanup de forma verbosa

- O interpretador suporta caminhos de arquivo separados por `/`, mesmo no Windows. Neste, também existe suporte para `\`.

- Apenas módulos importados são compilados e armazenados (cache). Em Python 2, salvos como `.pyc`, em Python 3, dentro de `__pycache__`, no mesmo *path* que o arquivo `.py` do módulo.

- Em ambientes UNIX, é possível tornar um script Python executável dando-o permissão de leitura e execução, `r+x`, e incluindo uma linha *shebang* em seu início:

```python
#!/usr/bin/env python
```

### A linguagem Python

- Programas Python são feitos de linhas lógicas, que podem ter uma ou mais linhas físicas.

- *Blank lines* são ignoradas por Python

- Comentários `# texto`, podem ocorrer em uma linha própria ou no final de outras linhas. Tudo após o `#` é ignorado por Python.

- Não precisar terminar comandos com `;`. O final da linha física faz esse papel.

- Se o comando for muito grande, Python permite quebrá-lo usando: `\` no final de cada linha, exceto a última:

```python
print("Meu nome é " + \
"John!")
```

- Linhas físicas dentro de chaves `{}`, colchetes `[]` ou parênteses `()`. Nesses casos, a indentação é relevante apenas para primeira linha:

```python
In [1]: print( "a",
   ...: "b",
   ...: "c")
a b c

In [3]: [1,
   ...: 2,
   ...: 3,
   ...: 4,
   ...: 5]
Out[3]: [1, 2, 3, 4, 5]

In [4]:

In [4]: {"a": 1,
   ...: "b": 2,
   ...: "c": 3,
   ...: "d": 4,
   ...: "e": 5}
Out[4]: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

- Python usa indentação para delimitar blocos. Cada bloco é uma sequência de linhas lógicas indentadas com a mesma quantidade de espaços.

- Versão 2 do Python susbstitui tabs por 8 espaços.

- Não use tabs. Use sempre 4 espaços, é o padrão.

- Em v2, use a opção `-tt` para evitar misturar tabs e espaços. v3, não permite isso.

- Em v3, o encoding dos arquivos `.py` é por padrão, `utf-8`. Em v2, é `ascii`. Em ambos pode-se definir explicitamente, através de um comentário especial:

```python
# coding: iso-8859-1
...
```

- Recomenda-se sempre usar `utf-8`.

- Identificadores são tokens que dão nomes a variáveis, módulos, funções, classes, etc. Devem começar com uma letra ou `_` e não podem ter espaços.

- A versão 3 suporta unicode em identificadores, mas evite.

- Maiúsculas e minúsculas são **diferenciadas**.

- Sinais gráficos como: `#, @, $, !, etc` não são permitidos em identificadores.

- Algumas convenções utilizadas para identificadores em Python:
    - Apenas nomes de classes começam com letra **Maiúscula**, todos outros com minúscula.

    - Identificadores iniciados com um underscore, `_identificador`, são semanticamente **privados**. Já identificadores iniciados com **dois** underscores `__identificador` são semanticamente **fortemente privados**. Isso ocorre pois Python não impõe tal proteção, realizando apenas uma simples obfuscação dos nomes para torná-las *privados*.

    - Identificadores que iniciam e terminam com dois underscores, `__iden__`, são nomes especiais da linguagem.

- Em sessões interativas do interpretador, o identificar dor `_`, *single underscore*, guarda o valor do último comando interpretado.

- Todos valores em Python são objetos. Tudo é objeto.

- Todo objeto tem um **tipo**. O tipo define as ações realizáveis e os atributos alteráveis em um objeto. Além de dizer se ele é mutável ou imutável.

- `type(obj)` retorna o objeto-classe/tipo de qualquer objeto

- `isinstance(obj, type)` retorna `True` se `obj` é do tipo `type` ou uma subclasse

- Tipos numéricos:
    - `int`
    - `float`
    - `decimal`   * módulo
    - `fractions` * módulo

- Todos tipos numéricos são imutáveis. Operações produzem novos objetos.

- Os tipos numéricos não carregam sinal, qualquer sinal presente é uma operação.

- Formas de declarar **inteiro**:

```python
>>> 0b0101 # binário
5
>>> 0o1234 # octal
668
>>> 0x1112 # hex
4370
>>> 0x1EFF # hex
7935
```

- Números não podem começar com `0`. Isto é permitido apenas para os prefixos de binário, hex, etc:

```python
>>> 0123
  File "<input>", line 1
    0123
       ^
SyntaxError: invalid token
>>>
```

- Formas de declarar **ponto flutuante**:

```python
>>> .0
0.0
>>> .1
0.1
>>> 0.
0.0
>>> 1.
1.0
>>> 1.1
1.1
>>> 1.234
1.234
>>>
```

- **Pontos flutuantes** são implementados como `doubles` na implementação **CPython**. Os limites de precisão e tamanho podem ser vistos em `sys.float_info`:

```python
>>> import sys
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308,
min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
>>>
```

- A partir da versão **3.6**, é possível separar grupos de dígitos com `_` em números de Python:

```python
>>> 1_000_000
1000000
>>> 1.345_678
1.345678
>>> 123_456.789
123456.789
>>>
```

- Sequências são containers de objetos indexáveis através de índices. Python tem três tipos sequenciais: `string, tuple e list`.

- Todas sequências são iteráveis.

- Strings **str** são sequências (um posição por caractere). Também são imutáveis, toda operação produz uma nova string.

- Em Python 2 uma string sem prefixo é uma sequência de `bytes`.

- Em Python 3 uma string sem prefixo é uma sequência `unicode`, ou seja, texto.

-  **str** podem ser declaradas com aspas simples (mais pythonico) ou duplas:

```python
>>> 'ola mundo'
'ola mundo'
>>> "ola mundo"
'ola mundo'
>>>
>>> # Use \ para quebrar strings longas
>>> "ola \
... mundo"
'ola mundo'
>>>
>>> 'ola \
... mundo'
'ola mundo'
>>>
>>> # Use caracteres de escape, para quebra de linha, tabulação...
>>> 'ola \t mundo'
'ola \t mundo'
>>> print('ola \t mundo')
ola      mundo
>>> print('ola \n mundo')
ola
 mundo
>>> # Para evitar escape codes e preservar quebra de linhas, use aspas triplas
>>> print("""
... ola mundo
... banco spam eggs
... """)

ola mundo
banco spam eggs

>>> print("""ola mundo
... spam bacon eggs""")
ola mundo
spam bacon eggs
>>>
>>> # Para evitar uma diferenca de indentacao, comece a string tripla com \
>>> text = """\
... ola mundo
... spam bacon eggs"""
>>> text
'ola mundo\nspam bacon eggs'
>>>
>>> # Aspas triplas duplas são mais pythonico, mas é possível usar aspas simples também
>>> '''ola
... mundo'''
'ola\nmundo'
>>>
```

- String prefixadas com `r` (*raw strings*) permitem criar strings ignorando possíveis sequências escape. Útil para expressões regulares, paths:

```python
>>> print(r'ola \n mundo')
ola \n mundo
>>>
>>> print(r"""ola
... \n mundo
... spam bacon eggs""")
ola
\n mundo
spam bacon eggs
>>>
```

- *raw strings* são apenas um açúcar sintático. Elas produzem strings normais, não foram um tipo diferente.

- **strings** postas lado a lado e separadas apenas por um ou mais espaços são automagicamente concatenadas:

```python
>>> 'ola' " " 'mundo'
'ola mundo'
>>>
```

- **tuple** são sequência imutáveis. Podem incluir qualquer tipo, inclusive sequências mutáveis (*melhor evitar!*).

- Formas de criação de uma **tupla**:

```python
>>> tupla_vazia = ()
>>> tupla_vazia
()
>>>
>>> tupla_unitaria = (123,)
>>> tupla_unitaria
(123,)
>>>
>>> tupla_complexa = (1, 'oi', 3.14, ('a', 'b', 'c'))
>>> tupla_complexa
(1, 'oi', 3.14, ('a', 'b', 'c'))
>>>
>>> # Os parênteses podem ser omitidos, mas é melhor colocá-los sempre...
>>> tuple_sem_parentese = 1, 2, 3
>>> tuple_sem_parentese
(1, 2, 3)
>>>
>>> # É possível criar tuplas usando o tipo 'tuple'
>>> tuple('abc')
('a', 'b', 'c')
>>>
>>> tupla_vazia = tuple()
>>> tupla_vazia
()
```

- **list** são sequências **mutáveis** que podem conter qualquer tipo de objeto.
Suas principais formas de declaração são:

```python
>>> lista_vazia = []
>>> lista_unitaria = [1]
>>> lista_complexa = [1, 3.14, 'spam', ['a', 'b', 'c']]

>>> # Também pode-se utilizar o tipo, list()
>>> lista_vazia = list()
>>> lista = list('teste')
>>> lista
['t', 'e', 's', 't', 'e']
>>>
```

- `set` e `frozenset` são conjuntos de objetos de qualquer tipos.
Nestes conjuntos, cada objeto é único e não pode se repetir.
`set` é mutável. `frozenset` é imutável.

- `set` e `frozenset` não são, necessariamente, ordenados. Não se fie nisto.

- Todos objetos dentro de um `set` ou `frozent` set devem ser *hashable*, logo, imutáveis. Portanto, um `set` não pode conter outro `set`.

- Entretanto, um `set` pode conter um `frozenset`

- Formas de declarar um `set` ou `frozenset`:

```python
>>> set_vazio = set() # cuidado! {} cria um dicionário !
>>> set_vazio
set()
>>>
>>> set_unitario = {1} #
>>> set_unitario
{1}
>>>
>>> set_simples = set([1, 2, 3])
>>> set_simples
{1, 2, 3}
>>>
>>> set_literal = {1, 2, 3}
>>> set_literal
{1, 2, 3}
>>>
>>> fset = frozenset([1, 2, 3])
>>> fset
frozenset({1, 2, 3})
>>>
>>> # set() permite remover letras duplicadas de uma string
>>> set('abacaxi')
{'x', 'i', 'b', 'c', 'a'}
```

- `dict` são mapeamentos mutáveis de um objeto *chave* com um objeto *valor*.
`valor` pode ser de qualquer tipo. `chave` pode ser *quase* de qualquer tipo (tem que ser *hashable*).

- `dict` não são, necessariamente, ordenados. A partir da versão 3.6 passaram a ser. Mas tem uma implementação ordenada específica (`collections.OrderedDict`)

- cada item de um `dict` é o par `chave` e `valor`.

- formas de declarar um dicionário:

```python
>>> dic_vazio = {}
>>> dic_simples = {'nome': 'John'}
>>> dic_simples
{'nome': 'John'}

>>> dic_variado = {'nome': 'John', 'idade': 30}
>>> dic_variado
{'nome': 'John', 'idade': 30}
```

- se uma chave se repete, o último valor atribuido é o que vale:

```python
>>> dct = {'a': 1, 'a': 2, 'a': 3}
>>> dct
{'a': 3}
>>>
```

- o tipo `dict` também permite a criação de dicionários:

```python
>>> dic_vazio = dict()
>>> dic_simples = dict(a=1, b=2, c=3)
>>> dic_simples
{'a': 1, 'b': 2, 'c': 3}
>>>
>>> # Usando pairs - tuplas com dois valores
>>> dict([('a', 1), ('b', 2), ('c', 3)])
{'a': 1, 'b': 2, 'c': 3}
```

- tendo apenas a lista de chaves, é possível criar uma lista com um valor padrão:

```python
>>> lst = ['nome', 'sobrenome', 'apelido']
>>>
>>> # Valor atribuido = None, se nenhum parâmetro for passado
>>> dct = dict.fromkeys(lst)
>>> dct
{'nome': None, 'sobrenome': None, 'apelido': None}
>>>
>>> dct = dict.fromkeys(lst, 15)
>>> dct
{'nome': 15, 'sobrenome': 15, 'apelido': 15}
>>>
```

- `None` é o objeto nulo de Python. Não tem métodos ou atributos.

- Funções sem um `return` explícito retornam `None`

- `callables` em Python, são todos objetos que suportam a operação de chamada de função. Por padrão, funções e `generators` são `callable`.

- `types` (classes) também são `callable` e, geralmente, ao serem chamados, produzem um novo objeto daquele tipo

- os outros tipos de `callable` são os métodos (funções vinculadas a objetos) e instâncias de classes que implementam o método especial `__call__`

- todos valores de Python podem ser usados como indicador de `True` ou `False`. `0`, `0.0` e todo container vazio `[], {}, ()` é tido como `False`. todo resto é entendido como `True`:

```python
>>> bool(-1)
True
>>> bool(1)
True
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool(5.0)
True
>>> bool([1, 2, 3])
True
>>> bool([])
False
>>> bool({})
False
```

- Evite usar pontos flutuantes para lógicas booleanas. Pontos flutuantes são *imprecisos*.

- `True` e `False` são subclasses de `int`. `True` tem valor `1` e `False` tem valor `0`. Dá até pra fazer conta:

```python
>>> int(False)
0
>>> int(True)
1
>>> True + True
2
>>>
```

- O tipo `bool()` pode ser usado para converter qualquer objeto passado para `True` ou `False`:

```python
>>> bool(0)
False
>>> bool(1)
True
>>> bool('')
False
>>> bool('spam')
True
```

- Como todo objeto em Python tem um valor lógico implícito, você deve escrever expressões lógicas usando os objetos diretamente. Evite chamar o tipo ou comparar direto com os valores `True` ou `False`:

```python
# sim!
>>> valor = 10
>>> if valor: print('valor eh valido')
...
valor eh valido

# nao!
>>> if bool(valor) == True: print('valor eh valido')
...
valor eh valido
>>>
```

- Variáveis são criadas na primeira atribuição. Não há declaração:

```python
>>> a = 1
>>> b = 2
>>> a
1
>>> b
2
>>>
```

- Podem ser desvinculadas com o operador `del`:

```python
>>> a = 10
>>> b = 20
>>>
>>> del a
>>>
>>> a
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b
20
>>>
```

- Variáveis podem ser revinculadas, a um novo objeto. A revinculação não tem efeito no objeto que era referenciado. Entretanto, `objetos sem nenhuma referência são` *garbage collected*

```python
>>> var = 10
>>> print(var)
10
>>>
>>> var = 'spam'
>>> print(var)
spam
>>>
```

- Variáveis podem ser `global`, quando são declaradas no corpo de um módulo (lembre-se: todo arquivo `.py` é um módulo) ou `local`, quando declaradas no escopo de uma função

- Variáveis podem referenciar qualquer tipo: `functions, methods`. Lembre-se: tudo é objeto.

- Os bindings de variáveis podem ser feitos com diferentes targets:

    - um identificador. a atribuição é feita imediatamente:

    ```python
    >>> valor = 99
    >>> valor
    99
    >>>
    >>> valor = 10
    >>> valor
    10
    >>>
    ```

    - se for um atributo de um objeto ou o item de uma lista, a operação é `delegada` para o objeto ou container (vide `__setattr__, __setitem__`):

    ```python
    >>> lst = [1, 2, 3]
    >>> lst[0] = 100
    >>> lst
    [100, 2, 3]
    >>>
    >>> # implicitamente o objeto é chamado
    >>> lst.__setitem__(0, 999)
    >>> lst
    [999, 2, 3]
    >>>
    ```

- múltiplas variáveis podem ser atribuídas a um mesmo valor:

```python
# Cada variável vai referenciar o objeto a direito.
# a referencia 100, b referencia 100, c referencia 100
# a NÃO referencia b...
>>> a = b = c = 100
>>> c
100
>>> b
100
>>> a
100

# Apenas c mudará
>>> c = 101
>>> c
101
>>> b
100
>>> a
100
>>>
```

- múltiplas variáveis podem ser atribuídas para valores distintos, usando um container no `right side`. `unpacking assignment`:

```python
>>> # Cuidado: o número de variáveis deve ser igual ao tamanho do right side
>>> a, b, c = (1, 2, 3)
>>> a
1
>>> b
2
>>> c
3
>>>
```

- esse comportamento pode ser utilizado para realizar `swap` de variáveis, pois lembre-se que o `right side` é sempre resolvido antes da atribuição, e variáveis são substituidas por seus valores:

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

- a partir da versão 3, `um` dos identificadores do lado esquerdo pode ser prefixado com um asterisco `*` para que ele obtenha todos valores do lado direito que não foram diretamente mapeados:

```python
>>> first, *middle, last = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> first
1
>>> middle
[2, 3, 4, 5, 6, 7, 8]
>>> last
9
>>>
```

- `augmented assignments` permitem uma variável apenas, previamente existente, no lado esquerdo. Como em toda atribuição, o lado direito é avaliado primeiro, então a operação acontece e um dos argumentos é a variável do lado esquerdo:

```python
>>> a = 10
>>> a *= 2 # a = a * 2
>>> a
20
>>>
```

- Todo operador Python tem um método especial correspondente, ex: `+ -> __add__`.
Este método é chamado para realizar a operação e recebe o outro objeto da operação como parâmetro.

    - Quando o objeto implementa tais métodos os `augmented assignments` modificam o objeto do lado esquerdo, ao invés de simplesmente remapeá-lo:

    ```python
    >>> lst = [1, 2, 3]
    >>> lst += [4]
    >>> lst
    [1, 2, 3, 4]
    >>>
    ```

- `del` apenas deleta a referência que está sendo feita pela variável a um objeto, não deleta o objeto. A deleção é feita pelo GC quando não existem referências para tal objeto.

    - Em identificadores, variáveis simples, a referência é desfeita na hora.

    - Em container ou objetos complexos, que implementam os métodos especiais `__delitem__` ou `__delattr__`, a operação é delegada para tais métodos

- Comparações booleanas podem ser encadeadas. Um `and` é implicado:

```python
>>> a = 10
>>> b = 25
>>>
>>> if a < 18 <= b:
...     print('Can pass!')
...
...
Can pass!
>>>
>>> # O mesmo que
>>> if a < 18 and 18 <= b:
...     print('Can pass!')
...
...
Can pass!
>>>
```

- `and` e `or` em Python avaliam as expressões necessárias apenas. Exemplo: em `x and y`, se `x` for `False`, este valor é retornado e `y` sequer é executado.

- Outro operador `short-circuit` é o operador ternário:

```python
valor_se_verdadeiro if condicao else valor_se_falso
```

`condicao` é executada. Se o resultado for `True`, `valor_se_verdadeiro` é executado. Senão, `valor_se_falso` é executado.

- tipos numéricos (`int`, `float`) são imutáveis. operações produzem novos objetos. sinais (`+`, `-`) são operadores e não fazem partes das declarações literais de números

- se tipos numéricos diferentes (ex: `int` e `float`) forem usados na mesma expressão, todos são nivelados no tipo mais 'largo', `float`.

```python
>>> 2 + 3.14
5.140000000000001
>>>
```

- é possível conveter entre tipos usando os nomes dos tipos:

```python
>>> # int despreza a parte decimal
>>> int(3.14)
3
>>>
>>> # também é possível passar strings com literals para os tipos criarem objetos numéricos
>>> int('3')
3
>>> float('3.14')
3.14
>>> float('3')
3.0

>>> # int suporta uma base para ser usada na conversão
>>> int('101')
101
>>> int('101', 2)
5
>>>
```

- As operações aritméticas atuam de maneira natural. Vale mencionar apenas a divisão:

    - `/` divisão normal em v3, resultado é um ponto flutuante. em v2, use:

    ```python
    from __future__ import division
    ```

    - `//` retorna o resultado da divisão truncado:

    ```python
    >>> 3 // 2
    1
    >>>
    ```

    - `divmod` retorna o quociente e o resto:

    ```python
    >>> divmod(5, 2)
    (2, 1)
    >>>
    ```

- `sequences` são containers ordenados acessíveis por indexação ou slices.

- algumas funções aplicáveis a sequências:

    - `len()`, retorna o tamanho:
    ```python
    >>> a = [1, 2, 3]
    >>> b = "spam"
    >>>
    >>> len(a)
    3
    >>> len(b)
    4
    >>>
    ```

    - `max()` retorna o maior valor na sequência, ou o maior entre dois parâmetros:
    ```python
    >>> a = [15, 7, 10]
    >>> max(a)
    15
    >>>
    >>> max(5, 19)
    19
    >>>
    ```

    - `min()` retorna o valor mínimo de uma sequência ou o menor entre dois parâmetros:
    ```python
    >>> lst = [14, 2, 311]
    >>> min(lst)
    2
    >>>
    >>> min(13, 17)
    13
    >>>
    ```

    - `sum()` retorna o somatório de uma sequência:
    ```python
    >>> lst = [14, 21, 33]
    >>> sum(lst)
    68
    ```

- é possível converter sequências como `tuple` ou `list` passando os objetos para o construtor do tipo:

```python
>>> tpl = (10, 20, 30)
>>> lst = [1, 2, 3]
>>>
>>> tuple(lst)
(1, 2, 3)
>>>
>>> list(tpl)
[10, 20, 30]
>>>
```

- sequências do mesmo tipo podem ser concatenadas com `+`:

```python
>>> lst = [1, 2, 3]
>>>
>>> lst = lst + [10, 20, 30]
>>> lst
[1, 2, 3, 10, 20, 30]
>>>
```

- sequências podem ser repetidas, usando `*`:

```python
>>> lst = [1, 2, 3]
>>> lst = lst * 3
>>> lst
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>>
```

- o operador `in` permite testar pertencimento a uma sequência ou se o valor é chave de um dicionário ou se é substring de uma string maior:

```python
>>> valor = 'a'
>>> valor in [1, 2, 'a', 4, 5]
True
>>> valor in {'a': 10, 'b': 12}
True
>>> valor in 'spam'
True
>>>
```

- Indexação de sequências começa em zero e vai até `len(sequencia) - 1`.

```python
>>> lst = ['a', 'b', 'c', 'd', 'e']
>>> lst[0]
'a'
>>> lst[ len(lst) - 1 ]
'e'
>>>
>>> # negativo tambem pode. -1 e o ultimo. -2 penultimo.
... lst[-1]
'e'
>>> lst[-2]
'd'
>>>

>>> lst[10] # exceçao!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

###### Slicing

- Para obter um pedaço de uma sequência, use slices: `sequencia[inicio:fim]`, onde `inicio` e `fim` são índices, sendo `inicio` incluido no resultado e `fim` **não** incluído:

```python
>>> lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> lst[1:5] # 1 = 'b', 5 = 'f'
['b', 'c', 'd', 'e']
>>>
```

- `inicio` tem como valor padrão `0` e `fim`, `len(sequencia)`. Você pode omitir um, ou ambos:

```python
>>> lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> lst[0:len(lst)]
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> lst[:]
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> lst[0:]
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> lst[:len(lst)]
['a', 'b', 'c', 'd', 'e', 'f', 'g']
```

- Slices tem uma indexação `graciosa`. Ou seja, indexar a maior que `length` ou a menor (indexação negativa), não causam exceções. :

```python
>>> lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> lst[100:200]
[]
>>>
>>> lst[-100:0]
[]
>>> lst[-100:1]
['a']
>>>
>>> lst[1000:-123]
[]
>>>
```

- o parâmetro `stride` permite indicar a distância entre os índices gerados no slice:

```python
>>> lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>>
>>> lst[0:len(lst):-1]
[]
>>> lst[len(lst):0:-1] # vai de um em um, no sentido contrario
['g', 'f', 'e', 'd', 'c', 'b']
>>>
>>> lst[::2] # two in two
['a', 'c', 'e', 'g']
>>>
```

- `strings` são imutáveis. toda operação produz uma nova string, inclusive a indexação, que produz uma string de `length = 1`.

- contudo, em `v3`, o tipo `bytes` ao ser indexado, retorna um `int`.

- `tuples` são imutáveis. seus slices também são `tuples`. apresentam apenas dois métodos, `count` e `index`. Suportam qualquer tipo de objeto, inclusive mutáveis, mas não é recomendado:

```python
>>> t = ('a', 'b', 'c')
>>> t[0:2]
('a', 'b')
>>>
>>> t.count('a')
1
>>> t.index('c')
2
>>> t[2]
'c'
>>>
```

- `list` são mutáveis. Podendo ser alteradas por indexação ou atribuição em slices. Se alterada por slices, o lado direito deve ser um iterável:

```python
>>> lst = ['a', 'b', 'c', 'd', 'e']
>>> lst[0] = 'x'
>>> lst
['x', 'b', 'c', 'd', 'e']
>>>
>>> lst[0:3] = ['y', 'z', 'w']
>>> lst
['y', 'z', 'w', 'd', 'e']
>>>
>>> lst[0:3] = ['k']
>>> lst
['k', 'd', 'e']
>>>
```

- Algumas sintaxes comuns envolvendo listas e slices:

```python
>>> lst = ['a', 'b', 'c', 'd', 'e']
>>>
>>> # Copia
... lst_copy = lst[:]
>>> lst_copy
['a', 'b', 'c', 'd', 'e']
>>>
>>> # Excluir elementos. mesmo que del lst[0:3]...
... lst[0:3] = []
>>> lst
['d', 'e']
>>>

>>> # Inserir numa posiçao. Inclui elementos just before the position.
... lst
['d', 'e']
>>> lst[1:1] = ['f', 'g', 'h']
>>> lst
['d', 'f', 'g', 'h', 'e']
>>>

>>> # Substituir todo o conteudo
... lst = ['a', 'b', 'c']
>>> lst
['a', 'b', 'c']
>>>
>>> lst[:] = ['d', 'e', 'f']
>>> lst
['d', 'e', 'f']
>>>
```

- Além da deleção por slices, `del` também permite excluir um objeto ou um slice de objetos:

```python
>>> lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>>
>>> del lst[3]
>>> lst
['a', 'b', 'c', 'e', 'f', 'g']
>>>
>>> del lst[0:3]
>>> lst
['e', 'f', 'g']
>>>
```

- Listas permitem algumas operações inplace:

```python
>>> # Concatenaçao
>>> lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>>
>>> lst += ['h', 'i']
>>> lst
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
>>>
>>> # o mesmo que o metodo extend()
...
>>> lst.extend(['j', 'l'])
>>> lst
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l']
>>>
>>> # repetiçao com *
... lst = ['a', 'b']
>>> lst *= 2
>>> lst
['a', 'b', 'a', 'b']
>>>
>>> # Multiplicar por um valor negativo esvazia:
... lst = ['a', 'b']
>>> lst *= 10
>>> lst
['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
>>>
>>> lst *= -5
>>> lst
[]
>>>
```

- `list` tem métodos modificadores e não-modificadores. Apenas dois métodos, `count()` e `index()`, não modificam as listas:

```python
>>> lst = ['a', 'b', 'c', 'a']
>>> lst.count('a')
2
>>>
>>> lst.index('b')
1
>>> lst[1]
'b'
>>>
```

- Métodos que modificam:

```python
>>> lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>>
>>> lst += ['h', 'i']
>>> lst
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
>>>
>>> # o mesmo que o metodo extend()
...
>>> lst.extend(['j', 'l'])
>>> lst
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l']
>>>
>>> # repetiçao com *
... lst = ['a', 'b']
>>> lst = ['a', 'b', 'c']
>>> lst.append('d')
>>> lst
['a', 'b', 'c', 'd']
>>>
>>> lst.extend(['e', 'f', 'g'])
>>> lst
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>>
>>>
>>> lst.insert(1, 'x')
>>> lst
['a', 'x', 'b', 'c', 'd', 'e', 'f', 'g']
>>>
>>>
>>> lst.remove('x')
>>>
>>> lst
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>>
>>> lst.pop()
'g'
>>> lst
['a', 'b', 'c', 'd', 'e', 'f']
>>>
>>> lst.sort()
>>> lst
['a', 'b', 'c', 'd', 'e', 'f']
>>>
>>> lst.reverse()
>>> lst
['f', 'e', 'd', 'c', 'b', 'a']
>>>
>>>
```

- Ordenando listas:

```python
>>> lst
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>>
>>> # inplace, usando .sort()
... lst = ['d', 'a', 'e', 'f']
>>> lst.sort()
>>> lst
['a', 'd', 'e', 'f']
>>>
>>> # inplace, invertido
... lst.sort(reverse=True)
>>> lst
['f', 'e', 'd', 'a']
>>>
>>> # criando novo objeto, usando o builtin sorted()
... lst_sorted = sorted(lst)
>>> lst_sorted
['a', 'd', 'e', 'f']
>>>
>>> lst
['f', 'e', 'd', 'a']
>>>
>>>
>>> # tambem e possivel utilizar uma funcao key, que sera executada em cada objeto antes da comparacao
... lst = ['Plone', 'javascript', 'Zope', 'ASP']
>>>
>>> lst.sort(key=str.lower)
KeyboardInterrupt
>>> lst.sort()
>>> lst
['ASP', 'Plone', 'Zope', 'javascript']
>>>
>>> lst.sort(key=str.lower)
>>> lst
['ASP', 'javascript', 'Plone', 'Zope']
>>>
```

- Em Python 3 o parâmetro `cmp`, que permitia definir uma função e comparação personalizada deixou de existir. Contudo, você pode usar `functools.cmp_to_key` e o parâmetro `key=` para obter o mesmo resultado.

- O módulo `operator` fornece os métodos `attrgetter` e `itemgetter` que retornam funções personalizadas para buscar itens específicos em sequências:

```python
>>> import operator
>>>
>>> lst = ['python', 'perl', 'javascript', 'java', 'bash']
>>>
>>> # ordenando pelo ultimo caractere
... lst.sort(key=operator.itemgetter(-1))
>>> lst
['java', 'bash', 'perl', 'python', 'javascript']
>>>
```

###### Operações com `set`

- As operações com `set` a seguir não modificam, mas sim, produzem novos `sets`. Logo, são aplicáveis a `frozenset` também:

```python
>>> sA = {1, 3, 4, 5, 12, 33, 98}
>>> sB = {2, 4, 5, 87, 88, 89}
>>>
>>> # diferenca todos em sA que nao estao em sB
... sA.difference(sB)
{1, 98, 3, 33, 12}
>>>
>>> # intersecao: todos em sA e em sB
... sA.intersection(sB)
{4, 5}
>>>
>>> # subset: todos de sA estao em sB
... sA.issubset(sB)
False
>>>
>>> # superset: todos de sB estao em sA ?
... sA.issuperset(sB)
False
>>>
>>> # symmetric_difference: todos que estao apenas em sA ou apenas em sB
... sA.symmetric_difference(sB)
{1, 2, 3, 12, 87, 88, 89, 33, 98}
>>>
>>> # uniao
... sA.union(sB)
{1, 33, 3, 4, 5, 98, 2, 12, 87, 88, 89}
>>>
```

- Métodos que alteram o `set`. Não são aplicáveis a `frozensets`:

```python
>>> s = {'a', 'b', 'c'}
>>>
>>> # Adicione item ao set
>>> s.add('d')
>>> s
{'d', 'c', 'b', 'a'}
>>> # Tente remover. Se não existir, não gera exceção.
>>> s.discard('c')
>>> s
{'d', 'b', 'a'}
>>>
>>> # remove o último inserido
>>> s.pop() # retorna e remove um item qualquer do conjunto
'd'
>>>
>>> s
{'b', 'a'}
>>>
>>> # Remove o elemento. Se não existir, gera KeyError
>>> s.remove('b')
>>> s
{'a'}
>>> s.remove('x')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'x'
>>>
```

- Você pode fazer um loop destrutivo usando `pop()`, inclusive modificando o conjunto. Com um for convencional, isto não é possível:

```python
>>> while s:
...     print(s.pop())
...
c
b
a
>>>

>>> s = {'a', 'b', 'c'}
>>> for elem in a:
...     a.insert('x')
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>>
```

- `sets` tem outros métodos mutáveis, como `symmetric_difference_update`, `difference_update` (todos terminam com `_update`) que realizam a operação mas modificam o `inplace`:

```python
>>> s1 = {'a', 'b', 'c'}
>>> s2 = {'c', 'd', 'e'}
>>>
>>> s1.symmetric_difference_update(s2)
>>> s1
{'b', 'e', 'a', 'd'}
>>>

>>> s1 = {'a', 'b', 'c'}
>>> s2 = {'c', 'd', 'e'}
>>> s1.intersection_update(s2)
>>> s1
{'c'}
>>>
```

- Os métodos de `sets` podem ser aplicados com qualquer sequência, pois esta será convertida para um `set(sequencia)`. Já os `operadores`, só podem ser aplicados entre `sets` ou `sets` e `frozensets`:

```python
>>> s1 = {'a', 'b', 'c'}
>>> s2 = {'c', 'd', 'e'}
>>>
>>> s1 & s2
{'c'}
>>> s1 | s2
{'e', 'b', 'a', 'd', 'c'}
>>> s1 - s2
{'b', 'a'}
>>> s1 + s2
```

### Operações com dicionários

- Métodos que modificam:

```python
>>> d = {'a': 10, 'b': 2, 'c': 30}
>>>
>>> # copy() retorna uma copia 'shallow' (nao cria copia dos objetos contidos)
... d2 = d.copy()
>>> d2
{'a': 10, 'b': 2, 'c': 30}
>>>
>>> # dict(d) tem o mesmo efeito que d.copy():
... d3 = dict(d)
>>> d3
{'a': 10, 'b': 2, 'c': 30}
>>>
>>> # se voce indexar um dicionario com uma chave inexistente uma excecao e produzida
... # para evitar isso, utilize o metodo .get(chave), que retorna None
... # se None nao for um bom valor, voce pode passar um segundo parametro que sera o retorno padrao
...
>>> d.get('x')
>>> print( d.get('x') )
None
>>> print( d.get('x', 0) )
0
>>>
>>> # .items() retorna um iterable dict_items
... d.items()
dict_items([('a', 10), ('b', 2), ('c', 30)])
>>>
>>> # .keys() retornas as chaves presentes no dicionario
... d.keys()
dict_keys(['a', 'b', 'c'])
>>>
>>> # .values() retorna os valores
... d.values()
dict_values([10, 2, 30])
>>>
>>>
```

- Métodos que **não** modificam:

```python
>>> d = {'a': 10, 'b': 2, 'c': 30}
>>>
>>> # copy() retorna uma copia 'shallow' (nao cria copia dos objetos contidos)
... d2 = d.copy()
>>> d2
{'a': 10, 'b': 2, 'c': 30}
>>>
>>> # dict(d) tem o mesmo efeito que d.copy():
... d3 = dict(d)
>>> d3
{'a': 10, 'b': 2, 'c': 30}
>>>
>>> # se voce indexar um dicionario com uma chave inexistente uma excecao e produzida
... # para evitar isso, utilize o metodo .get(chave), que retorna None
... # se None nao for um bom valor, voce pode passar um segundo parametro que sera o retorno padrao
...
>>> d.get('x')
>>> print( d.get('x') )
None
>>> print( d.get('x', 0) )
0
>>>
>>> # .items() retorna um iterable dict_items
... d.items()
dict_items([('a', 10), ('b', 2), ('c', 30)])
>>>
>>> # .keys() retornas as chaves presentes no dicionario
... d.keys()
dict_keys(['a', 'b', 'c'])
>>>
>>> # .values() retorna os valores
... d.values()
dict_values([10, 2, 30])
>>>
>>>
```

> Nunca modifique um dicionário enquanto itera sobre ele.

- Se você iterar diretamente sobre o dicionário, sem especificar um método, o método `.keys()` é utilizado:

```python
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for chave in d:
...     print(chave)
...
a
b
c
>>>
```

- Evite usar o método `setdefault`. Dê preferência a coleção `collections.defaultdict`.

- Use o método `popitem()` em conjunto com um loop `while` para consumir um dicionário de maneira destrutiva:

```python
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> bool(d)
True
>>> while d:
...     print( d.popitem() )
...
...
('c', 3)
('b', 2)
('a', 1)
>>> d
{}
>>>
```

- O método `update()` também suporta uma lista com pares `chave, valor` ou parâmetros nomeados:

```python
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>>
>>> d.update([ ('a', 10), ('d', 99) ])
>>> d
{'a': 10, 'b': 2, 'c': 3, 'd': 99}
>>>
>>> d.update(b=35, f=50)
>>> d
{'a': 10, 'b': 35, 'c': 3, 'd': 99, 'f': 50}
>>>
```

### Fluxos de controle

- `if`, `elif` e `else`. São opcionais: `elif` e `else`. Não há `switch`, use um conjunto de `elif` para essa finalidade.

```python
>>> num = int( input('enter the num:') )
enter the num: 25
>>> if num < 0:
...     print('negative')
... elif num % 2:
...     print('positivo e par')
... else:
...     print('positivo e impar')
...
...
positivo e par
```

- `while`. Repete até uma condição se tornar `False`.

```python
>>> x = 5
>>> while x:
...     print(x)
...     x -= 1
...
...
5
4
3
2
1
>>>
```

- Pode conter um bloco `else`, executado quando o loop termina **sem** ser interrompido por um `break`:

```python
>>> x = 5
>>> while x:
...     print(x)
...     x -= 1
... else:
...     print('x e zero!')
...
...
5
4
3
2
1
x e zero!
>>>
```

- `continue` e `break` podem ser utilizados:

```python
>>> x = 10
>>> while x:
...     if x % 2 == 0:
...         print(x)
...         x -= 1
...         continue
...     elif x == 5:
...         print(x)
...         break
...     else:
...         x -= 1
... else:
...     print('* Loop terminou sem interrupcoes')
...
...
10
8
6
5
>>>
```

- Loops `while` terminam quando a condição é avaliada para `False` ou quando a função em que está inserido executa um `return`.


- `for` itera sobre uma sequência.

```python
>>> for letra in 'abcdef':
...     print(letra)
...
a
b
c
d
e
f
>>>
```

Pode conter claúsulas `break`, `continue` e o `else`:

```python
>>> for letra in 'abcdef':
...     if letra == 'c':
...             continue
...     elif letra == 'e':
...             break
...     else:
...             print(letra)
... else:
...     print('Loop concluido sem nenhuma interrupcao')
...
a
b
d
>>>
```

- `for` pode iterar sobre sequências com mais de um item por vez:

```python
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for chave, valor in d.items():
...     print(chave, ' -> ', valor)
...
a  ->  1
b  ->  2
c  ->  3
>>>
```

- o identificar que é atribuído em cada iteração do `for` pode ser qualquer identificador de atribuição (lado esquerdo) válido:

```python
>>> lst = ['a', 999]
>>> for lst[1] in ('b', 'c', 'd', 'e', 'f'):
...     print(lst)
...
['a', 'b']
['a', 'c']
['a', 'd']
['a', 'e']
['a', 'f']
>>>
```

- **Não altere o objeto sendo iterado durante o** `for`.

- O identificador só é atribuído se houver pelo menos uma execução do loop, ou seja, a sequência tiver pelo menos um item. Esse identificar fica disponível no escopo após a execução do loop:

```python
>>> lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for par in lista[0::2]:
...     print(par)
...
0
2
4
6
8
>>> print('Ultimo par na sequencia: ', par)
Ultimo par na sequencia:  8
>>>
```

entenda como:

```python
>>> lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> par = None
>>> for par in lista[0::2]:
...     print(par)
...
0
2
4
6
8
>>> print('Ultimo par na sequencia: ', par)
Ultimo par na sequencia:  8
>>>
```

Mas lembre-se: `par` só existirá se o loop for executado pelo menos uma vez.

### Iterators

- `iterators` são objetos que podem ser usados na função `next(iterator)`. Estes objetos retornam um objeto cada vez que são chamados e produzem uma exceção `StopIteration` quando não existem mais objetos a serem retornados.

- A função `next(iterator)` também aceita um segundo parâmetro como valor `default`, `next(iterator, default)`. Neste caso, quando não existem mais objetos a serem retornados, não é gerada uma exceção, mas sim o valor `default` é retornado.

- Você pode tornar qualquer classe um iterator, bastando implementar nela um método `__next__(self)` que retorna um próximo objeto ou lança a exceção `StopIteration` quando termina.

- A maioria dos iterators são produzidos através de chamadas implícitas ou explícitas a função `iter`:

```python
>>> # Chamando de forma explicita
... lst = [1, 2, 3]
>>> lst_iterator = iter(lst)
>>> next(lst_iterator)
1
>>> next(lst_iterator)
2
>>> next(lst_iterator)
3
>>> next(lst_iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
```

O loop `for` chama `iter` implicitamente:

```python
>>> for el in [1, 2, 3]:
...     print(el)
...
1
2
3
>>>
```

- Muitos padrões e funções conveniente para lidar com iteradores encontram-se no módulo `itertools`.

### `range()`

É comum precisar iterar sobre uma lista de números, para gerar essa sequência Python provê uma função denominada `range()`.

Seus parâmetros são equivalentes ao de um slice. Existindo, portanto, três formas de chamá-la:

```python
>>> list( range(3) )
[0, 1, 2]
>>>
>>> list( range(1, 3) )
[1, 2]
>>>
>>> list( range(0, 7, 2) )
[0, 2, 4, 6]
>>>
```

A partir de `v3`, `range()` sempre retorna um objeto especializado. Para obter uma lista sequencial comum, use `list( range(...) )`.

### Comprehensions

É muito comum criar novas listas através do processamento de listas existente. Isto pode ser feito de forma simplificada com `list comprehensions`:

```python
>>> lst = [1, 2, 3]
>>> n_lst = [i * 10 for i in lst] # sem clausulas, apenas expressao e iteracao
>>> n_lst
[10, 20, 30]
>>>
```

Este tipo de expressão também permite condicionais, `if`:

```python
>>> lst = [1, 2, 3, 4, 5]
>>> pares = [i for i in lst if i % 2 == 0]
>>> pares
[2, 4]
>>>
```

Também é possível fazer `for` aninhados:

```python
>>> matrix = [
...     [1, 2, 3],
...     [4, 5, 6],
...     [7, 8, 9]
... ]
>>>
>>> flat = [y for row in matrix for y in row]
>>> flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> # mesmo que
... flat = []
>>> for row in matrix:
...     for y in row:
...             flat.append(y)
...
>>> flat
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
```

Os condicionais `if` podem ser usados com cada `for`. Mas evite, vai ficando cada vez mais complexo:

```python
>>> flat = [y for row in matrix if row[1] == 5 for y in row]
>>> flat
[4, 5, 6]
>>> flat = [y for row in matrix if row[1] == 5 for y in row if y == 6]
>>> flat
[6]
>>>
```

Lembre-se: os `for` consecutivos são considerados aninhados ao `for` anterior.

`set` também podem ser criados a partir de comprehensions, basta usar chaves ao invés de colchetes:

```python
>>> lst = [1, 2, 3, 4, 1, 5, 1, 6]
>>> s = {x for x in lst}
>>> s
{1, 2, 3, 4, 5, 6}
>>>
```

Os dicionários também podem ser criados dessa maneira:

```python
>>> lst = range(6)
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
>>> dct = {i:letters[i] for i in lst}
>>> dct
{0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}
>>>
```

### break

- Permitido dentro de loops. Pausa apenas o loop no qual está inserido. Caso esteja aninhado a um loop superior, este não é impactado.

```python
>>> x = 10
>>> while x:
...     print(x)
...     x -= 1
...     if x == 4: break
...
10
9
8
7
6
5
>>>
```

### continue

- Pula para próxima iteração do loop, ignorando o restante do bloco.

- Assim como o `break`, tem efeito apenas no loop em que está contido.

```python
>>> x = 10
>>> while x:
...     x -= 1
...     if x % 2 == 0: continue
...     else: print(x)
...
9
7
5
3
1
>>>
```

- Por vezes, o `continue` permite implementar uma estrutura mais `flat`, logo mais Pythonica. Pois permite substituir um `if` em alguns casos:

```python
>>> lst = [1, 3, 45, 89, 3, 33, 45, 98]
>>> for n in lst:
...     if n > 50: continue
...     print(n)
...
1
3
45
3
33
45
>>>
```

### `else` em loops

- `while` e `for` suportam uma clausula `else`, executada apenas quando o loop termina naturalmente (sem `break`, `return` ou `Exception`)

```python
>>> lst = [1, 2, 3, 4, 5]
>>> for n in lst:
...     if n > 10: break
...     print(n)
... else:
...     print('sem interrupcoes')
...
1
2
3
4
5
sem interrupcoes
>>>
>>> lst = [1, 2, 3, 100, 4, 5]
>>> for n in lst:
...     if n > 10: break
...     print(n)
... else:
...     print('sem interrupcoes')
...
1
2
3
>>>
```

### `pass`

- Algumas instruções de Python são compostas e requerem uma segunda instrução ou bloco de instruções. Quando isto é exigido e você não tem nada a executar de fato, você pode atender esse requisito com a instrução `pass`:

```python
>>> lst = [1, 2, 3]
>>> for n in lst:
...     if n == 1: print('um')
...     elif n == 2: pass
...     elif n == 3: print('tres')
...
um
tres
>>>
```

- Obs: funções `def` e classes não precisam de uma instrução `pass`, quando estão vazias. O ideal é colocar uma `docstring`:

```python
>>> def nada():
...     """ faz nada """
...
>>> class Nada:
...     """ Naaada """
...
>>>
```

## Funções

- Sempre que possível, encapsule seu código em funções ao invés de colocá-lo diretamente no corpo de um módulo. É mais rápido e fica mais organizado.

- Funções sempre retornam um valor, se não for utilizado o `return`,  `None` será retornado.

- Funções definidas no escopo de uma classe são chamadas de métodos (`bound functions`).

- Funções **são** objetos. Podem ser passadas como parâmetros, podem estar presentes em listas, dicionários, ser atribuídas a variáveis, etc.

Um exemplo disso é o mapeamento da inversa da função em um dicionário:

```python
>>> def soma(a, b):
...     return a + b
...
>>> def subtracao(a, b):
...     return a - b
...
>>> inversa = {soma: subtracao, subtracao: soma}
>>> inversa
{<function soma at 0x7f9f87a58d08>: <function subtracao at 0x7f9f87a58d90>, <function subtracao at 0x7f9f87a58d90>: <function soma at 0x7f9f87a58d08>}
>>>
>>> soma(10, 20), inversa[soma](10, 20)
(30, -10)
>>>
```

- Funções são declaradas usando `def` e podem aceitar parâmetros:

```python
>>> def nome_funcao(parametro1, parametro2):
...     # corpo. executado apenas quando a funcao é chamada.
...     pass
...
>>>
```

- Se houver parâmetros definidos, no momento da chamada da função estes devem ser fornecidos. No momento da chamada, esses valores são chamados de argumentos e são atribuídos a variáveis locais no escopo da função.

- Funções podem conter parâmetros obrigatórios, quando são listados apenas o identificador:

```python
>>> def soma(a, b):
...     return a + b
...
>>> soma(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: soma() missing 1 required positional argument: 'b'
>>>
>>> soma(10, 31)
41
>>>
```

- Parâmetros nomeados com valor padrão:

```python
>>> def soma(a, b=2):
...     return a + b
...
>>> soma(10, 31)
41
>>>
>>> soma(10)
12
>>>
```

- A expressão que representa o valor padrão de cada argumento é avaliada e salva entre os atributos do objeto função criado. Dessa forma, quando o argumento não é passado, esse valor é utilizado.

Cuidado: a expressão que define o valor padrão é executada apenas durante a declaração e a referência perdura durante toda a vida da função:

```python
>>> lst = [1, 2, 3, 4, 5]
>>> for n in lst:
...     if n > 10: break
...     print(n)
... else:
...     print('sem interrupcoes')
...
1
>>> def incluir(valor, lst=[]):
...     lst.append(valor)
...     return lst
...
>>> incluir(1)
[1]
>>> incluir(2)
[1, 2]
>>>
>>> nova_lst = []
>>> incluir(1, nova_lst)
[1]
>>> incluir(2, nova_lst)
[1, 2]
>>>
>>> # volta para referencia padrao. lembre-se que so eh amarrado durante a declaracao.
... incluir(3) # volta para lst criada na declaracao
[1, 2, 3]
>>>
>>> # nova_lst segue sem o 3
... nova_lst
[1, 2]
>>>
```

- Use o seguinte idioma para evitar parâmetros `default` mutáveis em funções:

```python
>>> def inserir(valor, lst=None):
...     if lst is None: lst = []
...     lst.append(valor)
...     return lst
...
>>> inserir(1)
[1]
>>> inserir(2)
[2]
>>>
>>> lista = []
>>> inserir(1, lista)
[1]
>>> inserir(2, lista)
[1, 2]
>>>
```

- Contudo, por vezes esse comportamento é útil. Exemplo: quando queremos fazer cache de alguma computação (memoization):

```python
>>> def fib(a, _cache={0: 1, 1: 1}):
...     print(_cache)
...     if a in _cache: return _cache[a]
...     _cache[a] = a + fib(a - 1)
...     return _cache[a]
...
>>> fib(10)
{0: 1, 1: 1}
{0: 1, 1: 1}
{0: 1, 1: 1}
{0: 1, 1: 1}
{0: 1, 1: 1}
{0: 1, 1: 1}
{0: 1, 1: 1}
{0: 1, 1: 1}
{0: 1, 1: 1}
{0: 1, 1: 1}
55
>>> fib(10)
{0: 1, 1: 1, 2: 3, 3: 6, 4: 10, 5: 15, 6: 21, 7: 28, 8: 36, 9: 45, 10: 55}
55
>>>
```

Contudo, é possível obter melhores resultados usando o decorador disponível no módulo `functools`: `functools.lru_cache`.

- `*args` e `**kwargs` permitem uma chamada de função flexível. `*args` recebe uma lista de argumentos posicionais e atribui como uma tupla em uma variável `args`. `**kwargs` permite que seja passada uma lista de argumentos nomeados (`argumento=valor, argumento2=valor2`) e os atribui na forma de dicionário à variável `kwargs`:

```python
>>> def exemplo(posicional, *args, **kwargs):
...     print(posicional)
...     print(args)
...     print(kwargs)
...
>>> exemplo('spam', 1, 2, 3, a=10, b=20, c=30)
spam
(1, 2, 3)
{'a': 10, 'b': 20, 'c': 30}
>>>
```

- Lembre-se: cada chamada de função cria um escopo próprio e os argumentos são atribuidos e existem apenas nesse escopo.

- A partir da versão 3 é possível definir argumentos obrigatoriamente nomeados. Eles devem vir entre `*args` e `**kwargs`. Se forem postos apenas como identificador `argumento`, são obrigatórios. Se forem postos como `argumento=valor_padrao` são opcionais:

```python
>>> def teste(a, *args, k1, k2='spam', **kwargs):
...     print(f'a={a}')
...     print(f'args={args}')
...     print(f'k1={k1}')
...     print(f'k2={k2}')
...     print(f'kwargs={kwargs}')
...
>>> teste(10, 33, 44, 55, k1=100)
a=10
args=(33, 44, 55)
k1=100
k2=spam
kwargs={}
>>>
```

- Se você não desejar flexibilidade para os argumentos posicionais, use um `*` puro no lugar de `*args`. Dessa maneira, apenas argumentos posicionais existentes na assinatura podem ser passados:

```python
>>> def teste(a, *, k1, k2='spam', **kwargs):
...     print(f'a={a}')
...     print(f'k1={k1}')
...     print(f'k2={k2}')
...     print(f'kwargs={kwargs}')
...
>>> teste(10, k1=100, k2='eggs', k3='bacon')
a=10
k1=100
k2=eggs
kwargs={'k3': 'bacon'}

>>> # Não pode passar mais posicionais do que o esperado
>>> teste(10, 20, 30,  k1=100, k2='eggs', k3='bacon')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: teste() takes 1 positional argument but 3 positional arguments (and 2 keyword-only arguments) were given
>>>
```

- `def` produz alguns atributos no objeto função definido:

`__name__` é o nome da função.

`__defaults__` é uma tupla com os valores `default` dos parâmetros:

```python
>>> def soma(a=2, b=5):
...     print(soma.__name__)
...     print(soma.__defaults__)
...
>>> soma()
soma
(2, 5)
>>>
```

- Outro atributo magicamente definido é o `__doc__` que recebe, caso a função seja iniciada com, uma docstring:

```python
>>> def soma(a, b):
...     """ soma a + b """
...     return a + b
...
>>> soma.__doc__
' soma a + b '
>>>
>>> help(soma) # chama .__doc__

>>>
```

- Funções, por serem objetos, podem manter diferentes atributos. Exemplo, contar quantas vezes foi chamada.

```python
>>> def counter():
...     counter.count += 1
...     print(counter.count)
...
>>> counter.count = 0
>>> counter()
1
>>> counter()
2
>>> counter()
3
>>>
```

Contudo, não é um idioma de programação comum. Se quer manter estado, utilize orientação a objetos.

### Anotação de funções

- Você pode anotar os parâmetros da função usando `:` e o retorno da função usando `->`. Qualquer objeto pode ser usado nessas anotações. Esse mapeamento fica salvo no atributo `__annotations__` do objeto da função:

```python
>>> def soma(a: 'inteiro', b: 'inteiro') -> 'inteiro':
...     return a + b
...
>>> soma.__annotations__
{'a': 'inteiro', 'b': 'inteiro', 'return': 'inteiro'}
>>>
```

- A partir de Python 3.6, é possível anotar variáveis também:

```python
>>> a:int = 10
>>> b:int = 20
```

- Para mais informações sobre anotações de tipo e sua análise, veja:

https://docs.python.org/3/library/typing.html

e

https://mypy.readthedocs.io/en/latest/

### Python é "passe por referência de objeto"

- Traduzindo: **referências dos objetos são passadas por valor**.

Para simplificar, entenda variáveis em Python como hyperlinks para os objetos. Quando acessadas, retornam o objeto referenciado.

Quando essas variáveis são passadas como argumentos, o hyperlink é copiado para o argumento e uma novo hyperlink é criado no escopo da função. Ambos hyperlinks, ambas variáveis, apontam para o mesmo objeto.

```python
>>> a = 10
>>> b = 20
>>>
>>> def exemplo(x, y):
...     print(id(x))
...     print(id(y))
...
>>> id(a)
10969088
>>> id(b)
10969408
>>>
>>> exemplo(a, b)
10969088
10969408
>>>
```

Contudo, dentro do escopo da função, o hyperlink-argumento criado pode ser alterado, sem afetar o hyperlink de fora:

```python
>>> x = 10
>>> id(x)
10969088
>>>
>>> def exemplo2(z):
...     z = 100
...     print(id(z))
...
>>> exemplo2(x)
10971968
>>>
>>> print(x, id(x)) # inalterado
10 10969088
>>>
```

Para objetos imutáveis (números, strings, tuplas), esse comportamento não traz surpresas. Mas para objetos modificáveis, é possível que uma operação através do escopo da função reflita em todo o sistema, pois o objeto é compartilhado:

```python
>>> lista = [1, 2, 3]
>>> print(lista, id(lista))
[1, 2, 3] 139632946475208
>>>
>>> def exemplo(l):
...     l.append(9)
...
>>> exemplo(lista)
>>> print(lista, id(lista))
[1, 2, 3, 9] 139632946475208
>>>
```

Por fim, se você reatribuir o link no escopo local para um novo objeto, o hyperlink original não é modificado:

```python
>>> lista = [1, 2, 3]
>>>
>>> def exemplo(l):
...     l = [14, 15, 16]
...     print(l, id(l))

>>> exemplo(lista)
[14, 15, 16] 139632886589064
>>>
>>> print(lista, id(lista))
[1, 2, 3] 139632946478792
>>>
```

- Em funções puramente Python, é possível alterar a ordem dos argumentos posicionais usando argumentos nomeados:

```python
>>> def subtrai(a, b):
...     return a - b
...
>>> print( subtrai(b=3, a=10) )
7
>>>
```

- É possível "desempactor" argumentos passados como `*args` ou `**kwargs` e passá-los para outras funções:

```python
>>> def soma(*, a, b):
...     return a + b
...
>>> def exemplo(*args, **kwargs):
...     print( *args ) # arg1, arg2, arg3...
...     print( soma(**kwargs) ) # soma(..=...)...
...
>>> exemplo(1, 2, 3, a=10, b=20)
1 2 3
30
>>>
```

### Namespaces

- Funções produzem um escopo local próprio, com as variáveis definidas em seu corpo e os argumentos passados.

- Variáveis fora do escopo de uma função são variáveis globais e são atributos do objeto do módulo em que foram declaradas.

- Se o escopo local tem uma variável com o nome igual de uma global, ela "esconde" a global.

```python
>>> valor = 10
>>>
>>> def soma(a, b):
...     valor = a + b
...     return valor
...
>>>
>>> soma(100, 100)
200
>>> valor
10
>>>
```

- Caso queira alterar de fato uma variável do escopo global, declare-a no início da função com a palavra-chave `global`:

```python
>>> valor = 10
>>>
>>> def soma(a, b):
...     global valor
...     valor = a + b
...     return valor
...
>>> soma(35, 39)
74
>>> valor
74
>>>
```

- Funções podem ser declaradas dentro de outras funções. A função interna, conhecida como `nested function` ou `inner function`. A função que engloba, é denominada `outer function`.

- As funções internas podem ler variáveis definidas na `outer function`, mas não alterá-las:

```python
>>> def create_incrementer(value):
...     def incrementer(parameter):
...             return parameter + value
...     return incrementer
...
>>> inc10 = create_incrementer(10)
>>> inc10(5)
15
>>>
>>> inc2 = create_incrementer(2)
>>> inc2(5)
7
>>>
```

As `nested function` que acessam variáveis do escopo superior são chamadas de `closures`.

- Ao invés de se valer do acesso ao escopo superior, é de bom tom passar as variáveis necessárias como parâmetro durante a definição da `inner function`:

```python
>>> def create_incrementer(value):
...     def incrementer(param, increment=value):
...             return param + increment
...     return incrementer
...
>>> inc10 = create_incrementer(10)
>>> inc10(2)
12
>>>
>>> inc2 = create_incrementer(2)
>>> inc2(5)
7
>>>
```

- Caso você queira alterar a variável do escopo da `outer function`, você deve declarar a variável com a palavra chave `nonlocal` logo no início da função:

```python
>>> def make_counter():
...     count = 0
...     def counter():
...             nonlocal count
...             count += 1
...             return count
...     return counter
...
>>> c1 = make_counter()
>>> c2 = make_counter()
>>>
>>> c1()
1
>>> c1()
2
>>> c2()
1
>>> c2()
2
>>>
```

Lembre-se que cada chamada de função tem um escopo próprio.

### Expressões lambda

- Permite criar funções anônimas de apenas uma linha. Não requer o uso de `return`, o resultado da expressão é o resultado da função:

```python
# Filtrando uma lista usando o builtin filter()
>>> lst = range(0, 11) # 0, 1, 2....10
>>> list( filter(lambda x: x % 2 == 0, lst) )
[0, 2, 4, 6, 8, 10]
>>>
```

### Generators

- Funções que usam `yield` são chamadas de `generators` e automagicamente encapsuladas em um iterator. Quando o `yield valor` é executado, a excução da função é pausada e `valor` retornado. Quando `next(generator)` é chamado novamente, a função resume sua execução de onde parou.

É possível chamar `yield` sem passar nenhum valor, o que equivale a passar `None`,  `yield None`:

```python
>>> def make_counter():
...     count = 0
...     def counter():
>>> def g():
...     for i in range(0, 11):
...             yield i
...
>>> g
<function g at 0x7ff182399400>
>>> for it in g():
...     print(it)
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
```

- Generators podem ser úteis para produzir sequências complexas:

```python
>>> def seq():
...     for i in range(0, 6):
...             yield i
...     for i in range(6, 0, -1):
...             yield i
...
>>> for i in seq():
...     print(i)
...
0
1
2
3
4
5
6
5
4
3
2
1
>>>
```

- A partir de v3 é possível realizar um `yield from iterator`, para que não seja necessário replicar um `yield`:

```python
>>> def seq():
...     yield from range(0, 6)
...     yield from range(5, -1, -1)
...
>>> list( seq() )
[0, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 0]
>>>
```

- É possível criar generators simples de forma similar as `list comprehensions`:

```python
>>> for double in (x * x for x in range(2, 11, 2)):
...     print(double)
...
4
16
36
64
100
>>>
```

São delimitadas por parênteses e apresentam um `yield` implícito.

As `generator expressions` ou `genexp` aceitam as mesmas construções das `list comprehensions`: vários `for`, `if`...

```python
>>> for num in (x * 2 for x in range(0, 11) if x % 2 == 0):
...     print(num)
...
0
4
8
12
16
20
>>>
```

### Generators como coroutines

- As funções generators podem ser utilizadas como corotinas. As chamadas `yield` são expressões, logo produzem um valor. Esse valor pode ser informado pelo `caller` do generator, utilizando o método `send(valor)` que funciona de forma similar ao `next(generator)`, mas passa um valor:

```python
>>> def repeater():
...     while True:
...             recv = yield
...             print(recv)
...
>>> rp = repeater() # cria o generator
>>> next(rp) # inicia a corotina
>>> rp.send('Oi!')
Oi!
>>> rp.send('Tchau!')
Tchau!
>>>
```

Outro exemplo, que sempre retorna o menor valor recebido:

```python
>>> def the_minimizer():
...     current = yield
...     while True:
...             new_value = yield current
...             current = min(current, new_value)
...
>>>
>>> g_the_minimizer = the_minimizer()
>>> next(g_the_minimizer) # inicializa, passo obrigatorio
>>> print( g_the_minimizer.send(1) )
1
>>> print( g_the_minimizer.send(3) )
1
>>> print( g_the_minimizer.send(123) )
1
>>> print( g_the_minimizer.send(-9) )
-9
>>>
```

### recursividade

- Python suporte recursividade. Mas tem um limite de aproximadamente 1.000 níveis. É possível alterar via `sys.setrecursionlimit`.

- Evite recursão com Python. Não há `tail-call optimization` e a quantidade de níveis é limitada, podendo, se extrapolada, causar um `hard crash` na sua aplicação (não será tratável via exceções)

## Orientação a Objetos

- Classes são tipos definidos pelo usuário.

- Classes podem ser instanciadas para criar novos objetos.

- O processo de instanciação é similar a uma chamada de função, só que o nome da classe é utilizado:

```python
objeto = Tipo()
```

- Classes podem conter atributos. Estes atributos podem ser modificados e referenciados:

```python
>>> class Ponto:
...     x = 0
...     y = 0
...
>>> Ponto.x
0
>>> Ponto.y
0
>>> Ponto.x = 10
>>> Ponto.y = 99
>>>
>>> Ponto.x
10
>>> Ponto.y
99
>>>
```

- Os atributos das classes podem ser funções. Nestes casos, elas são chamadas de métodos.

- Classes podem implementar diferentes métodos especiais, ex: `__init__` (chamado durante a criação da instância). Estes métodos são chamados durante diferentes operações aplicadas sobre o objeto.

```python
>>> class Ponto:
...     def __init__(self, x, y):
...             self.x = x
...             self.y = y
...             print(self.x, self.y)
...
>>>
>>> p = Ponto(3, 6)
3 6
>>>
```

- Classes podem herdar de outra classes, delegando para estas quando um atributo buscado não é encontrado:

```python
>>> class Cachorro:
...     barulho = "Huf huf"
...
>>> class Beagle(Cachorro):
...     def fazer_barulho(self):
...             print(self.barulho)
...
>>> b = Beagle()
>>> b.fazer_barulho()
Huf huf
>>>
>>> # Perceba que ele foi até a classe pai, buscando pelo atributo
>>> Cachorro.barulho = "Au au!"
>>> b.fazer_barulho()
Au au!
>>>
```

- Uma instância de uma class é um objeto Python e poder ter atributos, que podem ser modificados ou referenciados.

- Objetos delegam a busca de atributos não encontrados para a classe, que por sua vez pode delegar - caso não tenha o atributo - para classes pai:

```python
>>> class Pai:
...     atributo = 'bacon'
...
>>> class Filho(Pai):
...     pass
...
>>> instancia = Filho()
>>> print( instancia.atributo )
bacon
>>>
>>>
```

- E claro, classes são objetos! Ou seja, podem ser passadas como argumento, ser criadas e retornadas a partir de funções, vinculadas a variáveis, fazer parte de um container (lista, dicionário, etc)...

- A herança em Python é transitiva. Se `C` herda de `B` e `B` herda de `A`, então `C` também herda de `A`:

```python
>>> class A:
...     pass
...
>>> class B(A):
...     pass
...
>>> class C(B):
...     pass
...
```

- Você pode verificar a hierarquia usando `issubclass` ou `isinstance`:

```python
>>> # verifica a relaçao de herança
... issubclass(C, B)
True
>>> issubclass(C, A)
True
>>> isinstance(C(), B)
True
>>> isinstance(C(), A)
True
```

- O corpo identado da classe é executado e só então o nome da classe é vinculado como variável

- Lembre-se: `class` não cria nenhuma instância. Apenas define o `objeto tipo`, seus `atributos` (compartilhados entre todas instâncias) e métodos.

- No corpo da classe são definidos os atributos. Que podem ser objetos normais, funções (métodos) ou até outras classes (`nested classes`).

Você pode defini-los no corpo da classe:

```python
>>> class Ponto:
...     x = 0
...     y = 1
...
>>> print( Ponto.x, Ponto.y )
0 1
>>>
```

Inclusive, criá-los ou alterá-los de fora do corpo:

```python
>>> class Ponto: pass
...
>>> Ponto.x = 10
>>> Ponto.y = 99
>>>
>>> print( Ponto.x, Ponto.y )
10 99
```

- Os atributos da classe são `compartilhados` por todas instâncias.

- Ao declarar uma classe, alguns atributos são definidos implicitamente no objeto-tipo criado:

```python
>>> class Animal: pass
...
>>> class Mamifero:
...     amamentacao = True
...
>>> print(Mamifero.__name__, Mamifero.__bases__, Mamifero.__dict__)
Mamifero (<class 'object'>,) {'__module__': '__main__', 'amamentacao': True, '__dict__': <attribute '__dict__' of 'Mamifero' objects>, '__weakref__': <attribute '__weakref__' of '
Mamifero' objects>, '__doc__': None}
>>>
```

`__name__` é o nome de classe
`__bases__` são as superclasses
`__dict__` é o mapeamento dos atributos existentes na classe.

- Lembre-se que funções tem um escopo próprio e que podem se comunicar apenas com o escopo de uma outra `função` que a contenha. Pontanto, em métodos, `atributos de classe` devem SEMPRE ser qualificados:

```python
>>> class Teste:
...     atributo = 'spam'
...     def imprimir(self):
...             print( self.atributo )
...             print( Teste.atributo )
...             print( atributo ) # Ops! Sem qualificar
...
>>>
>>> t = Teste()
>>> t.imprimir()
spam
spam
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in imprimir
NameError: name 'atributo' is not defined
>>>
```

- Mas no corpo da classe, você pode referenciar sem qualificar.

```python
>>> class Teste:
...     atributo = 'spam'
...     atributo_maiusculo = atributo.upper()
...
>>> Teste.atributo
'spam'
>>> Teste.atributo_maiusculo
'SPAM'
>>>
```

- Inclusive, se você tentar qualificar no corpo da classe, vai gerar exceção, pois a classe só passa a existir ao final do bloco:

```python
>>> class Teste:
...     atributo = 'spam'
...     atributo_maiusculo = Teste.atributo.upper()
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in Teste
NameError: name 'Teste' is not defined
>>>
```

- O corpo das classes permite a declaração de funções / métodos usando `def`. Contudo, essas funções `devem` ter um primeiro parâmetro chamado (convencionalmente) de `self`:

```python
>>> class Test:
...     def hello(self):
...             print('Hello World')
...

>>> t = Test()
>>> t.hello()
Hello World

>>> # Implicitamente essa chamada equivale a:
>>> Test.hello(t)
Hello World
```

- Mas, por que obrigar um parâmetro `self` ? Pois funções têm um escopo próprio que não se comunica com o escopo da classe diretamente. Além disso, normalmente, métodos têm como objetivo alterar o estado do `objeto`, não da classe. Perceba:

```python
>>> class Exemplo:
...     atributo = 'Atributo da classe Exemplo'
...     def tornar_atributo_maiusculo(self):
...             self.atributo = self.atributo.upper()
...
>>> e = Exemplo()
>>> e.atributo
'Atributo da classe Exemplo'
>>>
>>> e.tornar_atributo_maiusculo()
>>> e.atributo # o metodo transformou em uma variavel da instancia, "sobreescrevendo" o atributo da classe, que permanece inalterado
'ATRIBUTO DA CLASSE EXEMPLO'
>>>
>>> Exemplo.atributo
'Atributo da classe Exemplo'
>>>
```

- Python não tem, nativamente, controle de acesso aos atributos das classes. Isto é feitos através de convenções, `name mangling`.

- Atributos prefixados com dois underline `__` são convertidos para `_NomeClase__atributo`, de forma a dificultar seu acesso externo.
No corpo da classe e em métodos dentro do corpo da classe, você pode referenciar a versão curta `__atributo` que o interpretador implicitamente substituirá pela versão extensa `_NomeClase__atributo`:

```python
>>> class Ponto:
...     __x = 0
...     __y = 0
...     def imprimir(self):
...             print(self.__x, self.__y)
...
>>> p = Ponto()
>>> p.imprimir()
0 0
>>> Ponto.__dict__
mappingproxy({'__module__': '__main__', '_Ponto__x': 0, '_Ponto__y': 0, 'imprimir': <function Ponto.imprimir at 0x7f764940a400>, '__dict__': <attribute '__dict__' of 'Ponto' objec
ts>, '__weakref__': <attribute '__weakref__' of 'Ponto' objects>, '__doc__': None})
>>>
```

- Atributos privados, pontanto devem - fora da classe original - ser acessados com o prefixo da classe em que são declarados:

```python
>>> class Pai:
...     __sobrenome = 'Silva'
...
>>> class Filho(Pai):
...     __nome = 'Joao'
...     def imprimir(self):
...             print(self.__nome, self._Pai__sobrenome) # A traducao so e feita na classe original. Objetivo e dificultar acesso.
...
>>> f = Filho()
>>> f.imprimir()
Joao Silva
>>>
```

- Por fim, identificadores de classe que começam com apenas um underscore devem ser considerados privados. Mas Python não muda nome, nem evita que sejam usados. O programador que deve ser responsável e não se basear neles.

- Assim como funções, se a primeira instrução de uma classe for uma string, ela é atribuída ao atributo `__doc__` e é considerada a `docstring` da classe:

```python
>>> class Teste:
...     """ Meu texto de ajuda """
...     pass
...

>>> Teste.__doc__
' Meu texto de ajuda '
>>>
```

- `Descritores` são objetos que sobreescrevem o comportamento padrão da leitura e escrita de seus atributos.

São utilizados para implementar métodos, métodos de classes, etc.

Existem dois tipos de descritor, `data` e `non-data`.
Os descritores `data` implementam `__set__(self, obj, value)` e `__get__(self, obj, type=None)`. Exemplo:

```python
>>> class Contante:
...     def __init__(self, v):
...             self.v = v
...     def __get__(self, instance, owner):
...             return self.v
...     def __set__(self, instance, value): # readonly descriptor
...             raise AttributeError()

>>> class Exemplo:
...     c = Constante(42)
...
>>> e = Exemplo()
>>> e.c
42
>>> e.c = 10 # Exception: AttributeError
```

Perceba que para criar um descritor `data` `readonly` bastou produzir uma exceção no método `__set__`.

Os descritores `non-data` implementam apenas o `__get__`:

```python
>>> class NDTeste:
...     def __get__(self, obj, type=None):
...         return 42
...
>>>
```

Agora quando os descritores são chamados ? Para utilizá-los, eles precisam ser uma instância-atributo de alguma outra classe.

```python
>>> class Constante:
...     def __get__(self, obj, type=None):
...         print(f'__get__(obj={obj}, type={type})')
...         return 42
...
...     def __set__(self, obj, value):
...         print(f'__set__(obj, value)')
...         raise AttributeError('readonly')
...
>>>
>>> class Exemplo:
...     atributo = Constante()
...
>>>
>>> e = Exemplo()
>>> e.atributo
__get__(obj=<__main__.Exemplo object at 0x7f3d8a69a978>, type=<class '__main__.Exemplo'>)
42
>>>
```

Por ser um descriptor do tipo `data`, ou seja, tem `__get__` e `__set__` ao ser chamado, ele toma precedência sobre o dict do objeto. Há uma inversão de controle:

A instância `Exemplo`, `e.atributo`, é identificada como descritor e tem seu método `__get__` chamado. Magicamente, Python passa como parâmetros a instância que o chamou (tá vendo como `self` é implementado?) e o tipo dessa instância.

E se fosse um descriptor `non-data` ?

```python
>>> class Constante:
...     def __get__(self, obj, type=None):
...         return 42
...
>>>
>>> class Exemplo:
...     c = Constante()
...
>>>
>>> e = Exemplo()
>>> e.c
42

# Se o descritor for 'non-data' (apenas implementar __get__)
# e o atributo estiver definido no __dict__ do objeto,
# o valor em __dict__ será retornado. O descritor só tem prioridade
# quando implementa __get__ e __set__ (é data)
>>> e.c = 100
>>> e.c
100
>>>
```

- Para criar novas instãncias, chame o tipo como se fosse uma função: `Tipo()`:

```python
>>> class Ponto: pass
>>> p = Ponto()
>>> p
<__main__.Ponto at 0x7fd518356da0>
>>>
```

- Para verificar se um objeto é uma instância de um determinado objeto, utilize o `builtin` `isinstance(objeto, classe)`. `isinstance` retorna `True` se `objeto` for uma instância de `classe` ou de uma possível `subclasse` de `classe`:

```python
>>> class Ponto: pass
>>>
>>> p1 = Ponto()
>>>
>>> isinstance(p1, Ponto)
True
>>>
```

- Você pode especializar a chamada de criação do objeto, definindo o método `__init__`. Este método deve apenas atribuir variáveis à instância sendo criada e não deve retornar nenhum valor que não seja `None`, senão produzirá exceção:

```python
>>> class Ponto:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...
>>>
>>> p = Ponto() # Não pode criar assim! Tem que respeitar o __init__...
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-522cb827c960> in <module>
----> 1 p = Ponto() # Não pode criar assim! Tem que respeitar o __init__...

TypeError: __init__() missing 2 required positional arguments: 'x' and 'y'
>>>
>>> p = Ponto(10, 34)
>>> p.x
10
>>> p.y
34
>>>
```

- Se `__init__()` não está presente, é possível criar a instância chamando apenas o tipo como uma função: `Tipo()`.
Nesse caso, a instância não terá nenhum atributo inicializado.

- Se `__init__()` está presente, deve-se respeitar a sua assinatura. O inicializador padrão `Tipo()` sem parâmetros deixa de existir,
a não ser que o método `__init__` seja construído para não precisar de nenhum argumento.

- Logicamente, atributos podem ser criados ou alterados depois da instância ter sido criada:

```python
>>> class Ponto: pass
>>>
>>> p = Ponto()
>>> p.x = 10
>>> p.y = 23
>>>
```

- Essa atribuição é interceptada pelo método `__setattr__`, se presente.

- Contudo, se o atributo sendo alterado for um descritor `data`, com `__get__` e `__set__`, ocorre a inversão de controle, e a chamada vira:

`p.atributo.__set__(p, valor)`.

- Toda instância tem, automaticamente, dois atributos `__class__` (que aponta para o tipo do objeto) e `__dict__` que guarda as variáveis atribuidas na instância:

```python
>>> class Ponto: pass
>>>
>>> p = Ponto()
>>> p.x = 10
>>> p.y = 23
>>>
>>> p.__class__
__main__.Ponto
>>>
>>> p.__dict__
{'x': 10, 'y': 23}
>>>
```

- Se não houver interceptação por um método `__setattr__` ou `__set__`, atribuit um valor a um objeto é o mesmo que adicionar um par chave valor ao `__dict__` desse objeto:

```python
>>> class Ponto: pass
>>>
>>> p = Ponto()
>>> p.x = 10
>>> p.y = 23
>>>
>>> p.__class__
__main__.Ponto
>>>
>>> p.__dict__
{'x': 10, 'y': 23}
>>>
>>> p.__dict__['x'] = 44
>>> p.__dict__['y'] = 91
>>>
>>> p
<__main__.Ponto at 0x7f858997ea90>
>>> p.__dict__
{'x': 44, 'y': 91}
>>>
>>>
```

- Por não permitir que se retorne valor ou objeto em seu `__init__`, o design pattern `factory` deve ser criado utilizando funções:

```python
>>> class Gato: pass
>>> class Cachorro: pass
>>>
>>> def animal_estimacao_factory(nome_em_ingle='dog'):
...     if nome_em_ingle == 'dog': return Cachorro()
...     elif nome_em_ingle == 'cat': return Gato()
...
>>>
>>> d = animal_estimacao_factory('dog')
>>> d
<__main__.Cachorro at 0x7f8190d0f550>
>>>
>>> c = animal_estimacao_factory('cat')
>>> c
<__main__.Gato at 0x7f8190cf0fd0>
>>>
```

- Mesma coisa para singletons:

```python
>>> class _Singleton:
...     pass
...
>>>
>>> def make_singleton():
...     if not hasattr(make_singleton, 'instance'):
...         make_singleton.instance = _Singleton()
...     return make_singleton.instance
...
>>>
>>> a = make_singleton()
>>> a
<__main__._Singleton at 0x7f510b644b70>
>>> id(a)
139986060200816
>>>
>>> b = make_singleton()
>>> b
<__main__._Singleton at 0x7f510b644b70>
>>> id(b)
139986060200816
>>>
```

- Toda `classe` tem um método de classe `__new__` que é chamado implicitamente durante a criação de uma instância.
Na verdade, este é o método responsável por retornar a instância. Depois de retornada, o método `__init__` dessa instância é executado.

```python
# O procedimento comum
>>> class Ponto:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...
>>> p = Ponto(10, 33)
>>> p.x
10
>>> p.y
33
>>>

>>> # Equivalente a:
>>> p2 = Ponto.__new__(Ponto) # classmethod
>>> p2
<__main__.Ponto at 0x7f510b638320>
>>> p2.__init__(55, 66)
>>> p2
<__main__.Ponto at 0x7f510b638320>
>>> p2.x
55
>>> p2.y
66
>>>
```

- A existência do `__new__` permite criar classes singleton de maneira mais robusta:

```python
>>> class Singleton:
...     __instance = None
...     def __new__(cls, *args, **kwargs):
...         if not cls.__instance:
...             cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
...         return cls.__instance
...
>>>
>>> s1 = Singleton()
>>> s1, id(s1)
(<__main__.Singleton at 0x7f919251c668>, 140263201818216)
>>>
>>> s2 = Singleton()
>>> s2, id(s2)
(<__main__.Singleton at 0x7f919251c668>, 140263201818216)
>>>
```

-