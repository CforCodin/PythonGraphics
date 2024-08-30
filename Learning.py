from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5,6,7,8,9]).reshape(-1, 1)
y = np.array([1,3,2,5,7,8,8,9,10,12])

model = LinearRegression()
model.fit(x, y)

m = model.coef_[0]
c = model.intercept_
y_pred = m*x + c

plt.scatter(x, y, color = "blue", label = "data points" )
plt.plot(x, y_pred, color = "red", label = f"Fitted Line: y = {m:.2f}x + {c:.2f}")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.legend()
plt.show()


print(f"Slope (m): {m}")
print(f"Intercept (c): {c}")


#predicting value of y:
X_new = np.array([12]).reshape(-1,1)
y_predd = model.predict(X_new)

print(X_new.flatten())
print(y_predd)