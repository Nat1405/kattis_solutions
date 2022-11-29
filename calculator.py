import sys
import re

"""
Pretty cool problem: https://open.kattis.com/problems/calculator
Lots of fun roads to go down with it, like implementing your own
calculator or computer from basic hardware. It's a really cool
example of some fundamental problems and algorithms in CS,
like the shunting yard algorithm.

My first idea was to try to build an abstract syntax tree then
evaluate that, maybe using something like recursive descent. The
problem though seemed to be left associativity; see this page. https://www.engr.mun.ca/~theo/Misc/exp_parsing.htm

The simplest solution, as also suggested by the wikipedia pages
for both reverse polish notation (rpn) and the shunting yard algorithm,
seemed to be to first convert to rpn then evaluate that using a stack.
Cool problem!
"""

class Stack:
    def __init__(self):
        self.storage = []
    
    def push(self, x):
        self.storage.append(x)

    def pop(self):
        # Note; this can throw if empty!
        return self.storage.pop()

    def peek(self):
        # Fine for simple immutable tokens
        return self.storage[-1]

    def empty(self):
        return not len(self.storage)

    def __str__(self):
        return ' '.join([str(x) for x in self.storage])


class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, x):
        self.storage.append(x)

    def dequeue(self):
        return self.storage.pop(0)

    def empty(self):
        return not len(self.storage)

    def __str__(self):
        return ' '.join([str(x) for x in self.storage])


def operand(t):
    return (not operator(t)) and t != '(' and t != ')'

def operator(t):
    return t=='m' or t=='+' or t=='-' or t=='*' or t=='/'

def precedence(o):
    if o == 'm':
        return 5
    elif o == '*' or o == '/':
        return 4
    elif o == '+' or o == '-':
        return 3
    elif o == '(' or o == ')':
        return 2


def RPN(token_list):
    """eg. (3+1/2)/3 ==> 3 1 2 / + 3 /
    Uses shunting yard algorithm.
    """

    s_operators = Stack()
    q_output = Queue()

    for t in token_list:
        # Operands go directly on output queue
        #print(f"Operators: {s_operators}")
        #print(f"Operands:  {q_output}")
        if operand(t):
            q_output.enqueue(t)

        elif operator(t):
            # Can't put operator of low precedence
            # on stack while operator of higher precedence
            # is on top

            # m is right associative, all others left associative
            if t == 'm':
                while (not s_operators.empty()) and \
                        precedence(s_operators.peek()) > precedence(t):
                    q_output.enqueue(s_operators.pop())
                s_operators.push(t)
            else:
                while (not s_operators.empty()) and \
                        precedence(s_operators.peek()) >= precedence(t):
                    q_output.enqueue(s_operators.pop())
                s_operators.push(t)

        elif t == '(':
            s_operators.push(t)

        elif t == ')':
            while s_operators.peek() != '(':
                q_output.enqueue(s_operators.pop())
            # Discard the '('
            s_operators.pop()

        #print(f"Operators: {s_operators}")
        #print(f"Operands:  {q_output}")

    # Empty the operands stack
    while not s_operators.empty():
        q_output.enqueue(s_operators.pop())

    output = []
    while not q_output.empty():
        output.append(q_output.dequeue())

    return output


def evaluate(rpn):
    """Evaluates an expression from a list of tokens
    in rpn format."""

    s_eval = Stack()

    for t in rpn:
        if operand(t):
            s_eval.push(t)

        elif operator(t):
            if t == 'm':
                s_eval.push(
                        -1 * float(s_eval.pop())
                    )
            else:
                # Must be a binary operator
                a = float(s_eval.pop())
                b = float(s_eval.pop())

                if t == '+':
                    s_eval.push(b + a)
                elif t == '-':
                    s_eval.push(b - a)
                elif t == '*':
                    s_eval.push(b * a)
                elif t == '/':
                    s_eval.push(b / a)



    if s_eval.empty():
        return None
    else:
        return s_eval.pop()






if __name__ == "__main__":
    for line in sys.stdin:
        if line == '\n':
            continue

        # Tokenization
        line = line.rstrip('\n')
        line = line.replace(' ', '') # Strip whitespace
        # Unary negation gets seperate character
        line = re.sub(r"^-|-(?<=--|\+-|\*-|\/-|\(-)", 'm', line)

        token_list = re.findall(r"\+|-|\*|\/|m|\(|\)|[0-9]+", line)

        # print(' '.join(token_list))

        # Convert in-fix tokens to reverse polish notation
        rpn = RPN(token_list)

        # print(' '.join(rpn))

        # evaluate and print result
        print(f"{evaluate(rpn):.2f}")



