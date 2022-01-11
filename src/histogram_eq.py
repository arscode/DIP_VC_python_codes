import cv2
import numpy as np
from matplotlib import pyplot as plt

src_img = cv2.imread('./img/wiki.jpg', 0)

hist,bins = np.histogram(src_img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(src_img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()