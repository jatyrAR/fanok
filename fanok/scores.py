import numpy as np


def selection_bool_fdr(mask: np.ndarray, true_mask: np.ndarray, q: float = 0) -> float:
    return (mask & ~true_mask).sum() / max(mask.sum() + (0 if q == 0 else 1 / q), 1)


def selection_fdr(a: np.ndarray, b: np.ndarray, q: float = 0) -> float:
    """
    Computes the false discovery proportion (FDP) of the subset
    of selected features.
    """
    return selection_bool_fdr(a.astype(bool), b.astype(bool), q=q)


def selection_bool_power(mask: np.ndarray, true_mask: np.ndarray) -> float:
    return (mask & true_mask).sum() / max(true_mask.sum(), 1)


def selection_power(a: np.ndarray, b: np.ndarray) -> float:
    """
    Computes the statistical power of the subset of selected features.
    """
    return selection_bool_power(a.astype(bool), b.astype(bool))