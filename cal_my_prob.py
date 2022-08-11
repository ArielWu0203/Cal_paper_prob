import click
import math
import matplotlib.pyplot as plt

@click.command()
@click.option('-m', help='the # of slots', type=click.INT)
@click.option('-k', help='the # of hash functions', type=click.INT)
@click.option('-n', help='the # of input items', type=click.INT)
def cal_bloom_prob(m, k, n):
    f=open('result_cal_my_prob.txt', 'w+')
    lst_x=list()
    lst_y=list()
    for N in range(1, n+1):
        p=(math.comb(N-1, k)/math.comb(m, k)) # probability
        f.write("%d %f\n" %(N, p))
        lst_x.append(N)
        lst_y.append(p)
    plot_result(lst_x, lst_y)

def plot_result(x, y):
    # print(lst_x, lst_y)
    fig_1 = plt.figure(figsize=(10,5))
    ax_1 = fig_1.add_subplot(1, 1, 1)
    ax_1.set_xlabel("the number of input items in our hash table")
    ax_1.set_ylabel("the probablility of collision")
    ax_1.plot(x, y)
    fig_1.savefig("./cal_my_prob.png")

if __name__ == '__main__':
    cal_bloom_prob()