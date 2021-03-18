
# 采用国际单位制
# 数值优先取自维基百科
from math import *

mass = {
'proton':1.6726219e-27,
'electron':9.10938356e-31,
'neutron':1.674927471e-27
}

h = 6.62607015e-34		# J*s, 是定义值。
h_bar = h/2/pi
c = 2.99792458e8
k_B = 1.38e-23
k_e = 8.9875517873681764e9	# N*m2*C-2
e0 = 1.602176634e-19	# 元电荷

g = 9.80665		# 标准重力加速度, m*s-2

b = 2.898e-3 		# wein位移定律, m*K
sigma = 5.678e-8 		# Stefan-Boltzman定律 W*m-2*K-4
a1_bohr = 5.2917706e-11 	# 玻尔半径(氢原子)
v1_bohr = k_e*e0**2/h_bar	# 氢原子第一玻尔速度
alpha_bohr = v1_bohr/c	# 精细结构常数
E1_bohr = -k_e**2*mass['electron']*e**4/2/h_bar**2 # 氢原子基态能量, J
R_H = 2*pi**2*(e0**4)*(k_e**2)*mass['electron']/(h**3)/c # 里德伯常数(氢原子) m-1

eV = 1.6e-19		# 电子伏特, J
u = 1.660539040e-27	# 相对原子质量，kg
year = 365*24*3600		# 年,s
atm = 101.325e3		# 标准大气压, Pa

ly = light_year = c*year	# 光年, m

lambda_compton = h/mass['electron']/c # 电子的康普顿波长

stevan_boltzmannConstant = 5.670374419184429453e-8 #Stevab-Boltzmann constant, W*m-2*K-4
