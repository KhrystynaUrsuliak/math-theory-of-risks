import math

def u(x):
  return math.log(x + 30)

def expected_return(x1, p, x2):
  return (x1 + x2) * p

print('U(x) = ln(x + 30), x > -30\n\nL1(-20; 0.5; -10)\nL2(-25; 0.5; -15)\nL3(-29; 0.5; -19)\n')

x1 = -20
x2 = -10
x3 = -25
x4 = -15
x5 = -29
x6 = -19

p1 = p2 = p3 = 0.5

expected_return_1 = expected_return(x1, p1, x2)
expected_return_2 = expected_return(x3, p2, x4)
expected_return_3 = expected_return(x5, p3, x6)

print(f"Expected Return 1 = {expected_return_1}\nExpected Return 2 = {expected_return_2}\nExpected Return 3 = {expected_return_3}\n")

expected_efficiency_1 = p1 * (u(x1) + u(x2))
expected_efficiency_2 = p2 * (u(x3) + u(x4))
expected_efficiency_3 = p3 * (u(x5) + u(x6))

print(f"Expected Efficiency 1 = {expected_efficiency_1}\nExpected Efficiency 2 = {expected_efficiency_2}\nExpected Efficiency 3 = {expected_efficiency_3}\n")

de1 = math.e**expected_efficiency_1 - 30
de2 = math.e**expected_efficiency_2 - 30
de3 = math.e**expected_efficiency_3 - 30

print(f"Deterministic Equivalent 1 = {de1}\nDeterministic Equivalent 2 = {de2}\nDeterministic Equivalent 3 = {de3}\n")

risk_premium_1 = expected_return_1 - de1
risk_premium_2 = expected_return_2 - de2
risk_premium_3 = expected_return_3 - de3

print(f"Risk Premium 1 = {risk_premium_1}\nRisk Premium 2 = {risk_premium_2}\nRisk Premium 3 = {risk_premium_3}\n")
