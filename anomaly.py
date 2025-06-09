
import numpy as np

def zscore_anomaly(data, threshold=3.0):
    mu = np.mean(data)
    sigma = np.std(data)
    if sigma == 0:
        return np.zeros(len(data), dtype=bool)
    zscores = np.abs((data - mu) / sigma)
    return zscores > threshold

def iqr_anomaly(data):
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    return (data < q1 - 1.5 * iqr) | (data > q3 + 1.5 * iqr)
