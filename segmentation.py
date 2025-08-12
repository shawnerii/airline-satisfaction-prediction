
import numpy as np

def kmeans_simple(X, k=3, max_iter=100, seed=42):
    rng = np.random.RandomState(seed)
    centers = X[rng.choice(len(X), k, replace=False)]
    for _ in range(max_iter):
        dists = np.array([[np.linalg.norm(x - c) for c in centers] for x in X])
        labels = np.argmin(dists, axis=1)
        new_centers = np.array([X[labels == i].mean(axis=0) if (labels == i).any() else centers[i] for i in range(k)])
        if np.allclose(centers, new_centers):
            break
        centers = new_centers
    return labels, centers

import numpy as np

def segment_satisfaction(df, segment_col, target_col='satisfaction'):
    segments = df[segment_col].unique()
    profiles = {}
    for seg in segments:
        subset = df[df[segment_col] == seg]
        profiles[seg] = {
            'count': len(subset),
            'satisfaction_rate': (subset[target_col] == 1).mean()
        }
    return profiles

import numpy as np

def kmeans_simple(X, k=3, max_iter=100, seed=42):
    rng = np.random.RandomState(seed)
    centers = X[rng.choice(len(X), k, replace=False)]
    for _ in range(max_iter):
        dists = np.array([[np.linalg.norm(x - c) for c in centers] for x in X])
        labels = np.argmin(dists, axis=1)
        new_centers = np.array([X[labels == i].mean(axis=0) if (labels == i).any() else centers[i] for i in range(k)])
        if np.allclose(centers, new_centers):
            break
        centers = new_centers
    return labels, centers
