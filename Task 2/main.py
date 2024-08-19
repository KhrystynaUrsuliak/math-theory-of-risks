import math

a_profit_1 = 40000
a_profit_2 = 10000
b_profit_1 = 30000
b_profit_2 = 5000

p_a_1 = p_a_2 = p_b_1 = p_b_2 = 0.5

print(f"Share Package A:\nOptimistic:\n\tProbable Profit: ${a_profit_1}\n\tProbability: {p_a_1}\nPessimistic:\n\tProbable Profit: ${a_profit_2}\n\tProbability: {p_a_2}\n")

print(f"Share Package B:\nOptimistic:\n\tProbable Profit: ${b_profit_1}\n\tProbability: {p_b_1}\nPessimistic:\n\tProbable Profit: ${b_profit_2}\n\tProbability: {p_b_2}\n")

m_x_a = p_a_1 * a_profit_1 + p_a_2 * a_profit_2
m_x_b = p_b_1 * b_profit_1 + p_b_2 * b_profit_2

print(f"Expected Values:\n\tM(X_A) = ${m_x_a}\n\tM(X_B) = ${m_x_b}\n")

v_x_a = (0.5 * (a_profit_1 - m_x_a) ** 2) + (0.5 * (a_profit_2 - m_x_a) ** 2)
v_x_b = (0.5 * (b_profit_1 - m_x_b) ** 2) + (0.5 * (b_profit_2 - m_x_b) ** 2)

print(f"Variation:\n\tV(X_A) = {v_x_a}\n\tV(X_B) = {v_x_b}")

s_x_a = math.sqrt(v_x_a)
s_x_b = math.sqrt(v_x_b)


