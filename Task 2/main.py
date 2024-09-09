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

print(f"Variation:\n\tV(X_A) = {v_x_a}\n\tV(X_B) = {v_x_b}\n")

s_x_a = math.sqrt(v_x_a)
s_x_b = math.sqrt(v_x_b)

cv_x_a = s_x_a / m_x_a
cv_x_b = s_x_b / m_x_a

print(f"Coefficient of Variation:\n\tCV(X_A) = {cv_x_a}\n\tCV(X_B) = {cv_x_b}\n")

ssv_x_a = round(math.sqrt((0.5 * ((a_profit_1 - m_x_a) * 100) ** 2))) / 100
ssv_x_b = round(math.sqrt((0.5 * ((b_profit_2 - m_x_b) * 100) ** 2))) / 100

print(f"Semi-Squared Variation:\n\tSSV(X_A) = ${ssv_x_a}\n\tSSV(X_B) = ${ssv_x_b}\n")

csv_x_a = ssv_x_a / m_x_a
csv_x_b = ssv_x_b / m_x_b

print(f"Coefficient of Semi-Variation:\n\tCSV(X_A) = {csv_x_a}\n\tCSV(X_B) = {csv_x_b}\n")

if csv_x_a > csv_x_b:
  print('A risk-prone person is more likely to choose share package A, whilst a risk-averse person is likely to choose share package B.')
else:
  print('A risk-prone person is more likely to choose share package B, whilst a risk-averse person is likely to choose share package A.')
