import scipy.stats as stats


# 1)
n = 10
p = 0.5
x_values = [7,8,9,10]
sum_prob = 0
for x in x_values:
    sum_prob += stats.binom.pmf(x, n, p)
print(f'1) {sum_prob:.6f}')
print(50*"=")


# =============================================================================
# 2-1)
n = 5
p = 2/3
probability1 = stats.binom.pmf(5, n, p)
print(f'2.1) {probability1:.6f}')
# 2-2)
x_values = [3,4,5]
sum_prob = 0
for x in x_values:
    sum_prob += stats.binom.pmf(x, n, p)
print(f'2.2) {sum_prob:.6f}')
# 2-3)
probability2 = stats.binom.pmf(2, n, p)
print(f'2.3) {probability2:.6f}')
print(50*"=")


# =============================================================================
# 3)
p = 0.04
x = 6
probability3 = stats.geom.pmf(x,p)
print(f'3) {probability3:.6f}')
print(50*"=")


# =============================================================================
# 4)
lam = 1

prob_a = stats.poisson.pmf(k=0, mu=lam)
prob_b = stats.poisson.pmf(k=1, mu=lam)
prob_c = stats.poisson.pmf(k=2, mu=lam)
prob_d = stats.poisson.pmf(k=3, mu=lam)

print(f'4.1) {prob_a:.6f}\n4.2) {prob_b:.6f}\n4.3) {prob_c:.6f}\n4.4) {prob_d:.6f}\n')
