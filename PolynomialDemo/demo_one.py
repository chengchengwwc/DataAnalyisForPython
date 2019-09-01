
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

x = np.random.uniform(-3,3,size=100)
X = x.reshape(-1,1)
y = 0.5 * x**2 +x + 2 + np.random.normal(0,1,size=100)
plt.scatter(x,y)
plt.show()

poly = PolynomialFeatures(degree=2)
poly.fit(X)
X2 = poly.transform(X)

line_reg2 = LinearRegression()
line_reg2.fit(X2,y)
y_predict2 = line_reg2.predict(X2)
plt.scatter(x,y)
plt.plot(np.sort(x),y_predict2[np.argsort(x)])
plt.show()

poly_reg = Pipeline(
    [('poly',PolynomialFeatures(degree=2)),
     ('std_scaler',StandardScaler()),
     ('lin_reg',LinearRegression())]
)

poly_reg.fit(X,y)
y_predict = poly_reg.predict(X)







