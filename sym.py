print(0)
from sympy import symbols, integrate, pi, cos, sqrt,plot
# from sympy.plotting import plot
import matplotlib.pyplot as plt

nb = 5
x = symbols('x')
t = []
for i in range(0, nb):
    t.append(x**i)
print("t: ", t)
b = []
# b.append(t[0])
for i in range(0, nb):
    tmp = t[i]
    for j in range(0, i):
        tmp -= integrate(t[i]*b[j], (x, -pi, pi))/integrate(b[j]*b[j], (x, -pi, pi))*b[j]
    tmp2 = tmp / sqrt(integrate(tmp*tmp, (x, -pi, pi)))
    b.append(tmp2)
print("b: ", b)
Pu = 0
for i in range(0, nb):
    Pu += integrate(b[i] * cos(x), (x, -pi, pi)) * b[i]
print("Pu: ", Pu)

p1 = plot(cos(x), show=False, ylim=(-1.5, 1.5), xlim=(-pi, pi),line_color='r',label='cos(x)')
p2 = plot(Pu, show = False,line_color='y',label='Px')
p3 = plot(1 - x**2 / 2 + x**4 / 24, show = False,line_color='b',label='Taloy')
# p1.append(p2[0])
# p1.append(p3[0])
# p1[0].legend()
# p1.show()

x1,y1 = p1[0].get_points()
x2,y2 = p2[0].get_points()
x3,y3 = p3[0].get_points()
plt.plot(x1, y1,'-',label='y = cos(x)')
plt.plot(x2, y2,'--',label=r'$y = a_0+a_1x+a_2x^2+a_3x^3+a_4x^4$')
plt.plot(x3, y3,'-.',label=r'$y = 1-\frac{x^{2} }{2!} +\frac{x^{4} }{4!} \ (Taylor)$')
plt.xlim((-3.14, 3.14))
plt.ylim((-1.5, 1.5))
plt.legend()
plt.show()  