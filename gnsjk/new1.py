a = ['tkinter', 'pynput', 'matplotlib']

b = ['print()', 'input()', 'int()']

c = ['if', 'else', 'elif', 'while', 'and']

d = ['+', '-', '*', '/', '=']


#内置函数		
func1 = ['abs()', 'divmod()', 'input()', 'open()', 'staticmethod()',
 'all()', 'enumerate()', 'int()', 'ord()', 'str()', 'any()',
 'eval()', 'isinstance()', 'pow()', 'sum()', 'basestring()',
 'execfile()', 'issubclass()', 'print()', 'super()', 'bin()',
 'file()', 'iter()', 'property()', 'tuple()', 'bool()', 'filter()',
 'len()', 'range()', 'type()', 'bytearray()', 'float()', 'list()',
 'raw()', 'unichr()', 'callable()', 'format()', 'locals()',
 'reduce()', 'unicode()', 'chr()', 'frozenset()', 'long()',
 'reload()', 'vars()', 'classmethod()', 'getattr()', 'map()',
 'repr()', 'xrange()', 'cmp()', 'globals()', 'max()', 'reverse()',
 'zip()', 'compile()', 'hasattr()', 'memoryview()', 'round()',
 '__import__()', 'complex()', 'hash()', 'min()', 'set()', 'delattr()',
 'help()', 'next()', 'setattr()', 'dict()', 'hex()', 'object()',
 'slice()', 'dir()', 'id()', 'oct()', 'sorted()']

func2 = ['__import__()', 'abs()', 'all()', 'any()', 'basestring()', 'bin()', 'bool()', 'bytearray()', 'callable()', 'chr()', 'classmethod()', 'cmp()', 'compile()', 'complex()', 'delattr()', 'dict()', 'dir()', 'divmod()', 'enumerate()', 'eval()', 'execfile()', 'file()', 'filter()', 'float()', 'format()', 'frozenset()', 'getattr()', 'globals()', 'hasattr()', 'hash()', 'help()', 'hex()', 'id()', 'input()', 'int()', 'isinstance()', 'issubclass()', 'iter()', 'len()', 'list()', 'locals()', 'long()', 'map()', 'max()', 'memoryview()', 'min()', 'next()', 'object()', 'oct()', 'open()', 'ord()', 'pow()', 'print()', 'property()', 'range()', 'raw()', 'reduce()', 'reload()', 'repr()', 'reverse()', 'round()', 'set()', 'setattr()', 'slice()', 'sorted()', 'staticmethod()', 'str()', 'sum()', 'super()', 'tuple()', 'type()', 'unichr()', 'unicode()', 'vars()', 'xrange()', 'zip()']

'''#单词排序
#w = [i for i in func1]  #依次将func1中的元素放入w[]中
#func1.sort()只可以作用于列表
func2 = sorted(func1)  #可以对所有可迭代对象使用
print(func2)'''


#运算符
operator1 = ['+', '-', '*', '/', '++', '--', '**', '%', '&',
 '@@', '||', '&&', '=', '<', '<=', '>', '>=', '==', '<>', '!=', '+=',
 '-=', '*=', '/=', '%=', '**=', '<<=', '>>=', '&=','^=', '|=']


operator2 = ['!=', '%', '%=', '&', '&&', '&=', '*', '**', '**=', '*=', '+', '++', '+=', '-', '--', '-=', '/', '/=', '<', '<<=', '<=', '<>', '=', '==', '>', '>=', '>>=', '@@', '^=', '|=', '||']


'''operator2 = sorted(operator1)  #可以对所有可迭代对象使用
print(operator2)'''


#关键字
keyword1 = ['False','None', 'True','and','as', 'assert','break',
 'class','continue', 'def','del','elif', 'else','except',
'finally', 'for', 'from','global','if','import','in','is',
'lambda', 'nonlocal','not','or','pass','raise', 'return',
'try','while','with','yield']


