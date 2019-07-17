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

