import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# grid是一个32*32的numpy数组
# grid = np.array([[1,2,3],[4,5,6],[7,8,9]])

xs = np.arange(1, 100)
ys = np.arange(1, 100).reshape(99, 1)
m = xs * ys
df = pd.DataFrame(m)
# 使用seaborn画图而不是plt
sns.set()

# data:数据 square:是否是正方形 vmax:最大值 vmin:最小值 robust:排除极端值影响
sns.heatmap(data=df, square=True, vmax=300, vmin=0, robust=True)
# 标题
plt.title("test")

# 保存图片
plt.savefig("../grid.png")
# 显示图片
plt.show()
