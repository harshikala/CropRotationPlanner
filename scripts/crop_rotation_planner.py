import pulp

def crop_rotation_planner(Ci, si, ti, Ei, Yi, Di, Bi, Wi, W, crop_data):
    crops = list(Ci.keys())
    time_periods = range(1, 13)
    plots = crop_data['Location'].unique().tolist()
    X = pulp.LpVariable.dicts("X", ((i, j, l) for i in crops for j in time_periods for l in plots), cat='Binary')
    prob = pulp.LpProblem("Crop_Rotation_Problem", pulp.LpMaximize)
    prob += pulp.lpSum(Ci[i] * X[i, j, l] for i in crops for j in time_periods for l in plots)

    for j in time_periods:
        for l in plots:
            prob += pulp.lpSum(X[i, j, l] for i in crops) <= 1

    prob += pulp.lpSum(Wi[i] * X[i, j, l] for i in crops for j in time_periods for l in plots) <= W

    for i in crops:
        prob += pulp.lpSum(Yi[i] * X[i, j, l] for j in time_periods for l in plots) >= Di[i]

    for i in crops:
        for l in plots:
            prob += pulp.lpSum(X[i, j, l] for j in time_periods) <= Bi[i]

    prob.solve()
    results = {v.name: v.varValue for v in prob.variables() if v.varValue > 0}
    total_profit = pulp.value(prob.objective)
    return results, total_profit

if __name__ == "__main__":
    from load_data import load_and_process_data
    from define_parameters import define_parameters

    file_path = '../Data/Database.csv'
    crop_data = load_and_process_data(file_path)
    parameters = define_parameters(crop_data)
    results, total_profit = crop_rotation_planner(*parameters, crop_data)
    print("Results:", results)
    print("Total Profit:", total_profit)
