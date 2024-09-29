from sympy import symbols, Eq, solve

err_1 = 0.1
err_2 = 0.2
err_3 = 0.5

ssv_1 = 0.02
ssv_2 = 0.1
ssv_3 = 0.2

cc_12 = 0
cc_13 = 0
cc_23 = -0.6

print(f"Акції Виду А\u2081:\n\tСподівана Норма Прибутку: {err_1 * 100}%\n\tСередньоквадратичне Відхилення: {ssv_1 * 100}%\n\tКоефіцієнти Кореляції: \u03C1\u2081\u2082 = {cc_12}, \u03C1\u2081\u2083 = {cc_13}\n\nАкції Виду А\u2082:\n\tСподівана Норма Прибутку: {err_2 * 100}%\n\tСередньоквадратичне Відхилення: {ssv_2 * 100}%\n\tКоефіцієнти Кореляції: \u03C1\u2081\u2082 = {cc_12}, \u03C1\u2082\u2083 = {cc_23}\n\nАкції Виду А\u2083:\n\tСподівана Норма Прибутку: {err_3 * 100}%\n\tСередньоквадратичне Відхилення: {ssv_3 * 100}%\n\tКоефіцієнти Кореляції: \u03C1\u2081\u2083 = {cc_13}, \u03C1\u2082\u2083 = {cc_23}\n\n")

x1, x2, x3, lambd = symbols('x1 x2 x3 lambd')

sigma_squared = (ssv_1 ** 2) * (x1 ** 2) + (ssv_2 ** 2) * (x2 ** 2) + (ssv_3 ** 2) * (x3 ** 2) + 2 * ssv_1 * ssv_2 * x1 * x2 * cc_12 + 2 * ssv_1 * ssv_3 * x1 * x3 * cc_13 + 2 * ssv_2 * ssv_3 * x2 * x3 * cc_23

constraint = x1 + x2 + x3 - 1

def minimize_risk():
  L = sigma_squared + lambd * constraint
  dl_dx1 = L.diff(x1)
  dl_dx2 = L.diff(x2)
  dl_dx3 = L.diff(x3)
  dl_dlambd = L.diff(lambd)

  equations = [Eq(dl_dx1, 0), Eq(dl_dx2, 0), Eq(dl_dx3, 0), Eq(dl_dlambd, 0)]
  solution = solve(equations, (x1, x2, x3, lambd))

  return solution

min_risk = minimize_risk()

print(min_risk)
