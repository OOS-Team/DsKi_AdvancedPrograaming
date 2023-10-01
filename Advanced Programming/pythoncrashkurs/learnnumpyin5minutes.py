# tw, 17.5.2022
# -------------

# https://www.youtube.com/watch?v=xECXZ3tyONo

# Wir arbeiten mit Anaconda in vscode(+ Python-Plugin und Jupyter-Plugin)

import numpy as np

a = np.zeros(3)
a
type(a)
type(a[0])


z = np.zeros(10)
z


z.shape


z.shape = (10,1)
z


z = np.ones(10)
z
type(z[0])


z = np.empty(3)
z


z = np.linspace(2, 10, 5)
z
type(z[1])


z = np.array([10, 20])
z


a_list = [1,2,3,4,5,6,7]
z = np.array(a_list)
z
type(z)


b_list = [[9, 8, 7, 6, 5, 4, 3], [1, 2, 3, 4, 5, 6, 7]]
z = np.array(b_list)
z


z.shape
?z.shape


np.random.seed(0)
z1 = np.random.randint(10, size=6)
z1


z1[0]
z1[0:2]
z1[-1]


from skimage import io 
photo = io.imread('york_minster.jpg')
type(photo)


photo.shape


import matplotlib.pyplot as plt
plt.imshow(photo)


plt.imshow(photo[::-1])

plt.imshow(photo[:, ::-1])

plt.imshow(photo[50:150, 150:280])

plt.imshow(photo[::2, ::2])


photo
photo_sin = np.sin(photo)
photo_sin


print(np.sum(photo))
print(np.prod(photo))
print(np.mean(photo))
print(np.std(photo))
print(np.var(photo))
print(np.min(photo))
print(np.max(photo))
print(np.argmin(photo))
print(np.argmax(photo))


z = np.array([1, 2, 3, 4, 5])
z


z<3

z>3

z[z<3]


photo_masked = np.where(photo>100, 255, 0)
plt.imshow(photo_masked)


a_array = np.array([1, 2, 3, 4, 5])
b_array = np.array([6, 7, 8, 9, 10])

a_array + b_array

a_array + 30

a_array * b_array

a_array * 10

a_array @ b_array


plt.imshow(photo[:, :, 0].T)


x = np.array([2,1,4,3,5])
np.sort(x)


#########################################
#FINIS








