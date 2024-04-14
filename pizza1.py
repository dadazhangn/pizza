import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import linear_model

# 生成一些随机数据作为示例

X = np.array([2014, 1015, 1016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]).reshape(-1, 1)
y = [340,330,345,355,340,320,360,335,355,340]

# 使用线性回归模型拟合数据
# lin_reg = LinearRegression()
# lin_reg.fit(X, y)
lin_reg = linear_model.LinearRegression()
lin_reg.fit(X, y)
# 打印模型的参数
print("Intercept:", lin_reg.intercept_)
print("Coefficient:", lin_reg.coef_)

# 绘制数据和拟合线
x_shap = [2014, 1015, 1016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
plt.scatter(x_shap, y)
plt.plot(X, lin_reg.predict(X), color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression Example')
plt.show()
