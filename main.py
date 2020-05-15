from lib import calculator

def choose_operator(ops):
  print('Choose calculator operator (please type on of %s): ' % ops.keys())
  chosen_op = input('--> ')
  return ops[chosen_op]

def get_operands():
  a =int(input('1.st operand: '))
  b =int(input('2.nd operand: '))
  return a,b

def main():
  print(">>> Calculator example <<<")
  cal = calculator.Calculator()
  op = choose_operator(cal.operators())
  a, b = get_operands()
  # 1. either call directly
  print(op(a,b))
  # 2.call it using the name-attribute
  print(eval("cal.%s(%s,%s)" % (op.__name__, a,b)))


if __name__ == '__main__':
  main()