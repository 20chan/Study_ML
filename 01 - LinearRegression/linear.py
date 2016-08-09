import random

input = [1, 2, 3, 4, 5]
output = [100, 200, 300, 400, 500]
m = len(input)

def cost(w):
    return sum([(w * input[i] - output[i]) ** 2 for i in range(m)]) / m

def derivative(w):
    return sum([(w * input[i] - output[i]) * input[i] for i in range(m)]) / m

def eval(n):
    return W * n

W = random.random()

for i in range(100):
    c = cost(W)
    delta = derivative(W)

    W -= 0.1 * delta

print('1 : ', eval(1))
print('2 : ', eval(2))
print('3 : ', eval(3))
print('4 : ', eval(4))
print('5 : ', eval(5))
print('10 : ', eval(10))