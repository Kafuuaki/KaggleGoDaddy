import numpy as np

def smape(y_reals, y_predicts):
    smp = np.zeros(len(y_reals))

    nom = np.abs(y_reals - y_predicts)
    den = (np.abs(y_reals) + np.abs(y_predicts)) / 2
    effective_index = (y_reals != 0) & (y_predicts != 0)
    smp[effective_index] = nom[effective_index] / den[effective_index]

    return 1 / 100 * np.mean(smp)