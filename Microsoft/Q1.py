class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        opmap = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.itruediv}
        stack = []
        for t in tokens:
            if t.isdigit() or t[1:].isdigit():
                stack.append(int(t))
            else:
                a, b = stack.pop(), stack.pop()
                # for case 1/-22, in python it returns -1, here use itruediv to get a float then apply int() to get 0
                stack.append(int(opmap[t](b, a)))
        return stack[0]
