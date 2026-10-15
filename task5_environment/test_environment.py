import numpy as np
import pandas as pd
import matplotlib
import sklearn

print("===== AI ENVIRONMENT TEST =====")

print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("Matplotlib:", matplotlib.__version__)
print("Scikit-learn:", sklearn.__version__)


data = np.array([10, 20, 30, 40, 50])

print("\nTest NumPy:")
print("Data:", data)
print("Mean:", np.mean(data))

print("\nEnvironment setup successfully!")