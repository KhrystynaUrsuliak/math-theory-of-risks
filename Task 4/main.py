from sympy import symbols, Eq, solve
import numpy as np

err_1 = 10
err_2 = 20
err_3 = 50

ssv_1 = 2
ssv_2 = 10
ssv_3 = 20

cc_12 = 0
cc_13 = 0
cc_23 = -0.6

print(f"Акції Виду А\u2081:\n\tСподівана Норма Прибутку: {err_1}%\n\tСередньоквадратичне Відхилення: {ssv_1}%\n\tКоефіцієнти Кореляції: \u03C1\u2081\u2082 = {cc_12}, \u03C1\u2081\u2083 = {cc_13}\n\nАкції Виду А\u2082:\n\tСподівана Норма Прибутку: {err_2}%\n\tСередньоквадратичне Відхилення: {ssv_2}%\n\tКоефіцієнти Кореляції: \u03C1\u2081\u2082 = {cc_12}, \u03C1\u2082\u2083 = {cc_23}\n\nАкції Виду А\u2083:\n\tСподівана Норма Прибутку: {err_3}%\n\tСередньоквадратичне Відхилення: {ssv_3}%\n\tКоефіцієнти Кореляції: \u03C1\u2081\u2083 = {cc_13}, \u03C1\u2082\u2083 = {cc_23}\n\n")

x1, x2, x3, lambd = symbols('x1 x2 x3 lambd')

sigma_squared = (ssv_1 ** 2) * (x1 ** 2) + (ssv_2 ** 2) * (x2 ** 2) + (ssv_3 ** 2) * (x3 ** 2) + 2 * ssv_1 * ssv_2 * x1 * x2 * cc_12 + 2 * ssv_1 * ssv_3 * x1 * x3 * cc_13 + 2 * ssv_2 * ssv_3 * x2 * x3 * cc_23

constraint = x1 + x2 + x3 - 1


def minimize_risk():
  L = sigma_squared + lambd * constraint
  dl_dx1 = L.diff(x1)
  dl_dx2 = L.diff(x2)
  dl_dx3 = L.diff(x3)
  dl_dlambd = L.diff(lambd)

  equations_1 = [Eq(dl_dx1, 0), Eq(dl_dx2, 0), Eq(dl_dx3, 0), Eq(dl_dlambd, 0)]
  solution = solve(equations_1, (x1, x2, x3, lambd))

  return solution


def maximize_return():
  expected_return_constraint = err_1 * x1 + err_2 * x2 + err_3 * x3 - 30
  L2 = sigma_squared + lambd * constraint + lambd * expected_return_constraint

  dl_dx1 = L2.diff(x1)
  dl_dx2 = L2.diff(x2)
  dl_dx3 = L2.diff(x3)
  dl_dlambd = L2.diff(lambd)

  equations_2 = [Eq(dl_dx1, 0), Eq(dl_dx2, 0), Eq(dl_dx3, 0), Eq(dl_dlambd, 0)]

  solution = solve(equations_2, (x1, x2, x3, lambd))

  return solution


def capital_growth():
  risk_constraint = sigma_squared - 15 ** 2 
  L3 = sigma_squared + lambd * constraint + lambd * risk_constraint

  dl_dx1 = L3.diff(x1)
  dl_dx2 = L3.diff(x2)
  dl_dx3 = L3.diff(x3)
  dl_dlambd = L3.diff(lambd)

  equations_3 = [Eq(dl_dx1, 0), Eq(dl_dx2, 0), Eq(dl_dx3, 0), Eq(dl_dlambd, 0)]
  solution = solve(equations_3, (x1, x2, x3, lambd))

  return solution

def calculate_return_and_risk(solution):
  w1, w2, w3 = solution[x1], solution[x2], solution[x3]

  expected_return = w1 * err_1 + w2 * err_2 + w3 * err_3

  weights = np.array([w1, w2, w3])
