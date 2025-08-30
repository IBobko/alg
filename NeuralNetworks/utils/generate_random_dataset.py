"""Utilities for generating synthetic datasets."""
from sklearn.datasets import make_classification


def generate_dataset(n_samples: int = 1000,
                     n_features: int = 10,
                     n_classes: int = 2,
                     random_state: int = 42):
    """Generate a random classification dataset.

    Args:
        n_samples: Number of samples to generate.
        n_features: Number of features for each sample.
        n_classes: Number of target classes.
        random_state: Seed for reproducibility.

    Returns:
        Tuple of feature matrix ``X`` and label vector ``y``.
    """
    return make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_classes=n_classes,
        random_state=random_state,
    )
