import random

# code contribution from ffmu aka banjo (big thanks)
def meth_quests():
  num1 = random.randint(0, 10)
  num2 = random.randint(0, 10)
  oper = random.choice(["+", "-", "*"])
  mafs = f"{num1} {oper} {num2}"
  result = eval(mafs)

  return result, f"**amogus quest:\nSolve the mathsfs problem: {mafs} = ?"
