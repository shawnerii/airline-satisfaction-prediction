
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

import numpy as np
from scipy import stats

def required_sample_size(baseline_rate, min_effect=0.05, alpha=0.05, power=0.8):
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(power)
    p1 = baseline_rate
    p2 = baseline_rate + min_effect
    p_bar = (p1 + p2) / 2
    n = (z_alpha * np.sqrt(2 * p_bar * (1 - p_bar)) + z_beta * np.sqrt(p1*(1-p1) + p2*(1-p2)))**2 / (p2-p1)**2
    return int(np.ceil(n))

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

import numpy as np
from scipy import stats

def required_sample_size(baseline_rate, min_effect=0.05, alpha=0.05, power=0.8):
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(power)
    p1 = baseline_rate
    p2 = baseline_rate + min_effect
    p_bar = (p1 + p2) / 2
    n = (z_alpha * np.sqrt(2 * p_bar * (1 - p_bar)) + z_beta * np.sqrt(p1*(1-p1) + p2*(1-p2)))**2 / (p2-p1)**2
    return int(np.ceil(n))

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

import numpy as np
from scipy import stats

def required_sample_size(baseline_rate, min_effect=0.05, alpha=0.05, power=0.8):
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(power)
    p1 = baseline_rate
    p2 = baseline_rate + min_effect
    p_bar = (p1 + p2) / 2
    n = (z_alpha * np.sqrt(2 * p_bar * (1 - p_bar)) + z_beta * np.sqrt(p1*(1-p1) + p2*(1-p2)))**2 / (p2-p1)**2
    return int(np.ceil(n))

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

import numpy as np
from scipy import stats

def required_sample_size(baseline_rate, min_effect=0.05, alpha=0.05, power=0.8):
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(power)
    p1 = baseline_rate
    p2 = baseline_rate + min_effect
    p_bar = (p1 + p2) / 2
    n = (z_alpha * np.sqrt(2 * p_bar * (1 - p_bar)) + z_beta * np.sqrt(p1*(1-p1) + p2*(1-p2)))**2 / (p2-p1)**2
    return int(np.ceil(n))
