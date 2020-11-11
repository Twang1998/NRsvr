import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVR
from sklearn.metrics import r2_score

np.random.seed(0)

x = np.random.randn(80, 2)
y = x[:, 0] + 2*x[:, 1] + np.random.randn(80)

clf = SVR(kernel='linear', C=1.25)
x_tran,x_test,y_train,y_test = train_test_split(x, y, test_size=0.25)
clf.fit(x_tran, y_train)
y_hat = clf.predict(x_test)

print("得分:", r2_score(y_test, y_hat))

r = len(x_test) + 1
print(y_hat.shape)
plt.plot(np.arange(1,r), y_hat, 'go-', label="predict")
plt.plot(np.arange(1,r), y_test, 'co-', label="real")
plt.legend()
plt.show()