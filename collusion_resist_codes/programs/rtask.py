# This program evaluates the remaining task ratio.

import random
import math
import time
from copy import deepcopy
# Let there be 1000 users.
n = 1000
# Let the upper bound of the users' unit costs be 10.
k_max = 10.0
# Remaining tasks number is 1000.
rt = 1000
# the maximum payment to each user is 100.
Pm = 100
# Total budget of the platform is 10000.
R = 1000
# Platform utility
u_p = R
# The outputs will be stored in the text file loss_truthful_dis.txt
f = open('rtask.txt', 'w')
# Test samples 1000
n_test = 1000;

class SensingUser:
	'''the class for a user participating in sensing.'''
	k = 0;	# the unit cost
	upper_k = 0;	# the upper cost bound
	lower_k = 0;	# the lower cost bound
	s = 0;	# the user strategy
	n_tasks = 0;	# sensing task number of this user
	p = 0;	# payment to this user
	u = 0;	# user utility
	def __init__(self):
		# The initial s_i = kappa_i
		self.s = self.k = random.uniform(0.01, k_max)
		# additionally we have the cost bounds
		self.upper_k = self.k + random.uniform(0.01, k_max/2.0)
		self.lower_k = self.k - random.uniform(0.01, k_max/2.0)
		if self.upper_k > k_max:
			self.upper_k = k_max
		if self.lower_k < 0:
			self.lower_k = 0.01

n=100;	# Initially we have 500 participating users.
R = 0	# budget
while R<10000:	# 1000 to 10000..
	R = R + 1000;	# with step of 1000.
	
	# our mechanism
	Pm = R/n
	
	ratio = 0
	sq_ratio = 0
	for i in range(n_test):
		remaining = rt	# remaining tasks
		# Initialize the users.
		users = []
		for i in range(n):
			users.append(SensingUser())

		# Compute the d.
		d = k_max
		for user in users:
			if user.upper_k - user.lower_k < 2*d:
				d = (user.upper_k - user.lower_k)/2

		# Compute the m.
		m = 1
		while (m+1)*(m+2)*d < 2*Pm:
			m = m+1

		# Recorrect the d
		if m*d > k_max:
			d = k_max / m

		# Let us compute the sensing time and the payment for each user.
		# Also we calculate each user utility and the platform utility.
		nsum = 0
		for user in users:
			user.n_tasks = m - math.floor(user.s / d)
			if user.n_tasks > remaining:
				user.n_tasks = 0
			if user.n_tasks < 0:
				user.n_tasks = 0
			user.p = d * user.n_tasks * (2*m + 1 - user.n_tasks) / 2.0
			user.u = user.p - user.k * user.n_tasks
			u_p = u_p - user.p	
			remaining = remaining - user.n_tasks
			nsum = nsum + user.n_tasks
		
		immr = float(nsum)/rt
		ratio = ratio + immr
		sq_ratio = sq_ratio + immr*immr
	
	# Output the statistical results.
	result = ratio/n_test
	f.write('{0:f} {1:f} {2:f} \n'.format(R, result, sq_ratio/n_test - (ratio/n_test)*(ratio/n_test))) #ms
	
f.close()
