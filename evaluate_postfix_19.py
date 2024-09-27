def evaluate_postfix(exp):
    exp_list = exp.split(" ")
    res = []
    for i in exp_list:
        if(i not in "+-*/"):
            res.append(i)
        else:
            op1 = res.pop()
            op2 = res.pop()
            res.append(str(eval(op2+i+op1)))
    if(len(res)!= 1):
        return False
    else:
        return int(float(res.pop()))
exp = "5"
print(evaluate_postfix(exp))