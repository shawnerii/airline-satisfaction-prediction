
import numpy as np

def variance_ranking(X):
    variances = np.var(X, axis=0)
    return np.argsort(variances)[::-1]

def correlation_with_target(X, y):
    corrs = [abs(np.corrcoef(X[:, i], y)[0, 1]) for i in range(X.shape[1])]
    return np.argsort(corrs)[::-1]
