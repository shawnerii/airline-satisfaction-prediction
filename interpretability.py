
import numpy as np

def permutation_importance(model_func, X, y, n_repeats=5, seed=42):
    rng = np.random.RandomState(seed)
    baseline = model_func(X, y)
    importances = []
    for col in range(X.shape[1]):
        scores = []
        for _ in range(n_repeats):
            X_perm = X.copy()
            X_perm[:, col] = rng.permutation(X_perm[:, col])
            scores.append(baseline - model_func(X_perm, y))
        importances.append(np.mean(scores))
    return np.array(importances)

import numpy as np

def permutation_importance(model_func, X, y, n_repeats=5, seed=42):
    rng = np.random.RandomState(seed)
    baseline = model_func(X, y)
    importances = []
    for col in range(X.shape[1]):
        scores = []
        for _ in range(n_repeats):
            X_perm = X.copy()
            X_perm[:, col] = rng.permutation(X_perm[:, col])
            scores.append(baseline - model_func(X_perm, y))
        importances.append(np.mean(scores))
    return np.array(importances)

import numpy as np

def permutation_importance(model_func, X, y, n_repeats=5, seed=42):
    rng = np.random.RandomState(seed)
    baseline = model_func(X, y)
    importances = []
    for col in range(X.shape[1]):
        scores = []
        for _ in range(n_repeats):
            X_perm = X.copy()
            X_perm[:, col] = rng.permutation(X_perm[:, col])
            scores.append(baseline - model_func(X_perm, y))
        importances.append(np.mean(scores))
    return np.array(importances)
