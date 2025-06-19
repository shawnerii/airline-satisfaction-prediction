
import numpy as np
from scipy import stats

def ab_test(control, treatment, alpha=0.05):
    t_stat, p_value = stats.ttest_ind(control, treatment)
    return {
        'control_mean': np.mean(control),
        'treatment_mean': np.mean(treatment),
        'lift': (np.mean(treatment) - np.mean(control)) / np.mean(control),
        'p_value': p_value,
        'significant': p_value < alpha
    }
