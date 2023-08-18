def add(x:int, y:int):
  return x + y

def sub(x:int, y:int):
  return x - y

def mul(x:int, y:int):
  return x * y

def div(x:int, y:int):
  return x / y

def mod(x:int, y:int):
  return x % y

def exp(x:int, y:int):
  return x ** y

def fdiv(x:int, y:int):
  return x // y

def coocoo(instr:str):
  import re
  operators = ['>', '^', '<', '<=', '>=', '+', '-', '*', '/', '%', '**', '//', '=', '+=', '-=', '==', '*=', '/=', '%=', '//=', '!=', '&=', '|=', '^=', '>>=', '<<=']
  r = re.compile( '|'.join( '(?:{})'.format(re.escape(o)) for o in sorted(operators, reverse=True, key=len)) )  
  temp = re.findall(r'\d+', instr)
  res = list(map(int, temp))
  opr = r.findall(instr)
  if opr[0] == '+':
    return add(res[0], res[1])
  if opr[0] == '-':
    return sub(res[0], res[1])
  if opr[0] == '*':
    return mul(res[0], res[1])
  if opr[0] == '/':
    return div(res[0], res[1])
  if opr[0] == '%':
    return mod(res[0], res[1])
  if opr[0] in ['**', '^']:
    return exp(res[0], res[1])
  if opr[0] == '//':
    return fdiv(res[0], res[1])
