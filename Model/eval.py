import matplotlib.pyplot as plt
from pathlib import Path

#display metric
print("\n=== Evaluation Metrics ===")
print(metrics.__dict__) 


def safe_get(metric_obj, attr, default='N/A'):
    return getattr(metric_obj, attr, default)

print(f"Top-1 Accuracy : {safe_get(metrics, 'top1', 0):.4f}")
print(f"Top-5 Accuracy : {safe_get(metrics, 'top5', 0):.4f}")
print(f"Precision      : {safe_get(metrics, 'precision', 0):.4f}")
print(f"Recall         : {safe_get(metrics, 'recall', 0):.4f}")
print(f"F1 Score       : {safe_get(metrics, 'f1', 0):.4f}")


# plot 
red = Path(
