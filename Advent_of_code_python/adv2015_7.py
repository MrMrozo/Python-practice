input = open("Advent_of_code_python/advdata2015_7.txt").read().strip().splitlines()

def instructions(input):
    wires = {}
    
    for line in input:
        parts = line.split(" -> ")
        expression = parts[0]
        wire = parts[1]
        wires[wire] = expression
    
    def evaluate(wire):
        if wire.isdigit():
            return int(wire)
        if wire in memo:
            return memo[wire]
        
        expression = wires[wire]
        if "AND" in expression:
            left, right = expression.split(" AND ")
            result = evaluate(left) & evaluate(right)
        elif "OR" in expression:
            left, right = expression.split(" OR ")
            result = evaluate(left) | evaluate(right)
        elif "LSHIFT" in expression:
            left, right = expression.split(" LSHIFT ")
            result = evaluate(left) << int(right)
        elif "RSHIFT" in expression:
            left, right = expression.split(" RSHIFT ")
            result = evaluate(left) >> int(right)
        elif "NOT" in expression:
            operand = expression.split(" ")[1]
            result = ~evaluate(operand) & 0xFFFF
        else:
            result = evaluate(expression)
        
        memo[wire] = result
        return result
    
    memo = {}
    return evaluate("a")

print(instructions(input))

def instructions2(input):
    wires = {}
    
    for line in input:
        parts = line.split(" -> ")
        expression = parts[0]
        wire = parts[1]
        wires[wire] = expression
    
    def evaluate(wire):
        if wire.isdigit():
            return int(wire)
        if wire in memo:
            return memo[wire]
        
        expression = wires[wire]
        if "AND" in expression:
            left, right = expression.split(" AND ")
            result = evaluate(left) & evaluate(right)
        elif "OR" in expression:
            left, right = expression.split(" OR ")
            result = evaluate(left) | evaluate(right)
        elif "LSHIFT" in expression:
            left, right = expression.split(" LSHIFT ")
            result = evaluate(left) << int(right)
        elif "RSHIFT" in expression:
            left, right = expression.split(" RSHIFT ")
            result = evaluate(left) >> int(right)
        elif "NOT" in expression:
            operand = expression.split(" ")[1]
            result = ~evaluate(operand) & 0xFFFF
        else:
            result = evaluate(expression)
        
        memo[wire] = result
        return result
    
    memo = {}
    a_value = evaluate("a")
    memo.clear()
    wires["b"] = str(a_value)
    return evaluate("a")

print(instructions2(input))