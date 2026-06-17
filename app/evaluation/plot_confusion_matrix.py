import pandas as pd
import matplotlib.pyplot as plt

cm = pd.read_csv(
    "reports/confusion_matrix.csv",
    index_col=0
)

plt.figure(figsize=(6,4))

plt.imshow(cm)

plt.colorbar()

plt.xticks(
    range(len(cm.columns)),
    cm.columns,
    rotation=45
)

plt.yticks(
    range(len(cm.index)),
    cm.index
)

plt.tight_layout()

plt.savefig(
    "reports/confusion_matrix.png"
)

plt.show()