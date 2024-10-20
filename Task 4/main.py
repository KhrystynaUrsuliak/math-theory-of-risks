from math import sqrt
from sympy import symbols, Eq, solve
import numpy as np
import pandas as pd

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


def preserve_capital():
  L = sigma_squared + lambd * constraint
  dl_dx1 = L.diff(x1)
  dl_dx2 = L.diff(x2)
  dl_dx3 = L.diff(x3)
  dl_dlambd = L.diff(lambd)

  equations_1 = [Eq(dl_dx1, 0), Eq(dl_dx2, 0), Eq(dl_dx3, 0), Eq(dl_dlambd, 0)]
  solution = solve(equations_1, (x1, x2, x3, lambd))

  return solution


def get_desired_profit():
  expected_return_constraint = err_1 * x1 + err_2 * x2 + err_3 * x3 - 30
  L2 = sigma_squared + lambd * constraint + lambd * expected_return_constraint

  dl_dx1 = L2.diff(x1)
  dl_dx2 = L2.diff(x2)
  dl_dx3 = L2.diff(x3)
  dl_dlambd = L2.diff(lambd)

  equations_2 = [Eq(dl_dx1, 0), Eq(dl_dx2, 0), Eq(dl_dx3, 0), Eq(dl_dlambd, 0)]

  solution = solve(equations_2, (x1, x2, x3, lambd))

  return solution


def ensure_capital_growth():
  mu = symbols('mu')  
  risk_constraint = sigma_squared - 15 ** 2 
  L3 = sigma_squared + lambd * constraint + mu * risk_constraint  

  dl_dx1 = L3.diff(x1)
  dl_dx2 = L3.diff(x2)
  dl_dx3 = L3.diff(x3)
  dl_dlambd = L3.diff(lambd)
  dl_dmu = L3.diff(mu)

  equations_3 = [Eq(dl_dx1, 0), Eq(dl_dx2, 0), Eq(dl_dx3, 0), Eq(dl_dlambd, 0), Eq(dl_dmu, 0)]  
  solution = solve(equations_3, (x1, x2, x3, lambd, mu))  

  return solution


solution_1 = preserve_capital()
solution_2 = get_desired_profit()
solution_3 = ensure_capital_growth()

for i, sol in enumerate(solution_3):
    x1_val, x2_val, x3_val = sol[0], sol[1], sol[2]

print(f"A) Структура ПЦП щодо задачі збереження капіталу:\n\tА\u2081 = {solution_1[x1]} \n\tА\u2082 = {solution_1[x2]} \n\tА\u2083 = {solution_1[x3]}\n\n")

print(f"Б) Структура ПЦП щодо задачі одержання бажаного прибутку при m_П = 30%:\n\tА\u2081 = {solution_2[x1]} \n\tА\u2082 = {solution_2[x2]} \n\tА\u2083 = {solution_2[x3]}\n\n")

print(f"В) Структура ПЦП щодо задачі забезпечення зростання капіталу при σ_П = 15%:\n\tА\u2081 = {x1_val} \n\tА\u2082 = {x2_val} \n\tА\u2083 = {x3_val}\n\n")

portfolios = {
    "А\u2081": {"A1": 0.896358543417367, "A2": 0.0728291316526611, "A3": 0.0308123249299720},
    "А\u2082": {"A1": 1.48670926604630, "A2": 0.306633786122049, "A3": 0.160919383626034},
    "А\u2083": {"A1": 3.17426902710791, "A2": -1.69693209029153, "A3": -0.477336936816380}
}

def expected_return(portfolio):
    A1, A2, A3 = portfolio["A1"], portfolio["A2"], portfolio["A3"]
    return A1 * err_1 + A2 * err_2 + A3 * err_3

def risk(portfolio):
    A1, A2, A3 = portfolio["A1"], portfolio["A2"], portfolio["A3"]
    sigma_squared = (A1 ** 2) * (ssv_1 ** 2) + (A2 ** 2) * (ssv_2 ** 2) + (A3 ** 2) * (ssv_3 ** 2) \
                    + 2 * A1 * A2 * ssv_1 * ssv_2 * cc_12 + 2 * A1 * A3 * ssv_1 * ssv_3 * cc_13 \
                    + 2 * A2 * A3 * ssv_2 * ssv_3 * cc_23
    return np.sqrt(sigma_squared)

results = {}
for portfolio_name, portfolio_values in portfolios.items():
    exp_return = expected_return(portfolio_values)
    portfolio_risk = risk(portfolio_values)
    results[portfolio_name] = {
        "Сподівана Норма Прибутку (%)": exp_return,
        "Оцінка Ризику (%)": portfolio_risk
    }

results_df = pd.DataFrame(results).T
print('Г) Сподівана норма прибутку та оцінка ризику для кожного портфеля:')
print(results_df)
