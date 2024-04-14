import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

# 输入数据
years = np.array([2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]).reshape(-1, 1)
scores = np.array([340, 330, 345, 355, 340, 320, 360, 335, 355, 340])

# 创建 SVR 模型并拟合数据
svr_reg = SVR(kernel='rbf')
svr_reg.fit(years, scores)

# 使用模型进行预测
prediction_2024 = svr_reg.predict([[2024]])

# 打印预测结果
print("Predicted score for 2024:", prediction_2024[0])

# 绘制原始数据和拟合曲线
plt.scatter(years, scores, color='blue', label='Original data')
plt.scatter(2024, prediction_2024, color='green', label='Prediction for 2024')
plt.xlabel('Year')
plt.ylabel('Score')
plt.title('Support Vector Regression Example')
plt.legend()
plt.grid(True)

plt.show()
