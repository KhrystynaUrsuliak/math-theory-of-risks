import numpy as np
import pandas as pd

err_1, err_2, err_3 = 10, 20, 50  
ssv_1, ssv_2, ssv_3 = 2, 10, 20   
cc_12, cc_13, cc_23 = 0, 0, -0.6  

portfolios = {
    "A": {"A1": 0.896358543417367, "A2": 0.0728291316526611, "A3": 0.0308123249299720},
    "B": {"A1": 1.48670926604630, "A2": 0.306633786122049, "A3": 0.160919383626034},
    "C": {"A1": 3.17426902710791, "A2": -1.69693209029153, "A3": -0.477336936816380}
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
        "Expected Return (%)": exp_return,
        "Risk (Standard Deviation %)": portfolio_risk
    }

results_df = pd.DataFrame(results).T
print(results_df)
