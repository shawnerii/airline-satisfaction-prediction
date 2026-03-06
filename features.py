
import numpy as np

def variance_ranking(X):
    variances = np.var(X, axis=0)
    return np.argsort(variances)[::-1]

def correlation_with_target(X, y):
    corrs = [abs(np.corrcoef(X[:, i], y)[0, 1]) for i in range(X.shape[1])]
    return np.argsort(corrs)[::-1]

import numpy as np

def top_k_features(importances, feature_names, k=10):
    idx = np.argsort(importances)[::-1][:k]
    return [(feature_names[i], importances[i]) for i in idx]

def normalize_importances(importances):
    total = sum(importances)
    if total == 0:
        return importances
    return [v / total for v in importances]

import numpy as np

def variance_ranking(X):
    variances = np.var(X, axis=0)
    return np.argsort(variances)[::-1]

def correlation_with_target(X, y):
    corrs = [abs(np.corrcoef(X[:, i], y)[0, 1]) for i in range(X.shape[1])]
    return np.argsort(corrs)[::-1]

import numpy as np

def top_k_features(importances, feature_names, k=10):
    idx = np.argsort(importances)[::-1][:k]
    return [(feature_names[i], importances[i]) for i in idx]

def normalize_importances(importances):
    total = sum(importances)
    if total == 0:
        return importances
    return [v / total for v in importances]

import numpy as np

def variance_ranking(X):
    variances = np.var(X, axis=0)
    return np.argsort(variances)[::-1]

def correlation_with_target(X, y):
    corrs = [abs(np.corrcoef(X[:, i], y)[0, 1]) for i in range(X.shape[1])]
    return np.argsort(corrs)[::-1]

import numpy as np

def top_k_features(importances, feature_names, k=10):
    idx = np.argsort(importances)[::-1][:k]
    return [(feature_names[i], importances[i]) for i in idx]

def normalize_importances(importances):
    total = sum(importances)
    if total == 0:
        return importances
    return [v / total for v in importances]

import numpy as np

def variance_ranking(X):
    variances = np.var(X, axis=0)
    return np.argsort(variances)[::-1]

def correlation_with_target(X, y):
    corrs = [abs(np.corrcoef(X[:, i], y)[0, 1]) for i in range(X.shape[1])]
    return np.argsort(corrs)[::-1]

import numpy as np

def top_k_features(importances, feature_names, k=10):
    idx = np.argsort(importances)[::-1][:k]
    return [(feature_names[i], importances[i]) for i in idx]

def normalize_importances(importances):
    total = sum(importances)
    if total == 0:
        return importances
    return [v / total for v in importances]

import numpy as np

def variance_ranking(X):
    variances = np.var(X, axis=0)
    return np.argsort(variances)[::-1]

def correlation_with_target(X, y):
    corrs = [abs(np.corrcoef(X[:, i], y)[0, 1]) for i in range(X.shape[1])]
    return np.argsort(corrs)[::-1]
