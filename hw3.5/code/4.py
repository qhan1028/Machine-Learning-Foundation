import math as m

ETA = 0.01
e = m.e

# E(u, v)
E = lambda u, v : e**u + e**(2*v) + e**(u*v) + u**2 - 2*u*v + 2*v**2 - 3*u - 2*v
# gradient of E(u, v)
GE = lambda u, v : (e**u + v*e**(u*v) + 2*u - 2*v - 3, 2*e**(2*v) + u*e**(u*v) - 2*u + 4*v - 2)

u = v = 0
print('E(u0, v0) =', E(u, v))
for i in range(5):
	g = GE(u, v)
	u -= ETA * g[0]
	v -= ETA * g[1]
	print ('E(u', i+1, ', v', i+1, ') = ', E(u, v), sep='')
