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

- 