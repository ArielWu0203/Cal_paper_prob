import click
import math
import matplotlib.pyplot as plt

@click.command()
@click.option('-m', help='the length of bloom filter', type=click.INT)
@click.option('-k', help='the # of hash functions', type=click.INT)
@click.option('-n', help='the # of input items', type=click.INT)
def cal_bloom_prob(m, k, n):
    f=open('result_cal_bloom_prob.txt', 'w+')
    lst_x=list()
    lst_y=list()
    for N in range(1, n+1):
        x=-1.0*k*N/m
        fr=math.pow(1-math.exp(x), k)
        f.write("%d %f\n" %(N, fr))
        lst_x.append(N)
        lst_y.append(fr)
    plot_result(lst_x, lst_y)

def plot_result(x, y):
    # print(lst_x, lst_y)
    fig_1 = plt.figure(figsize=(10,5))
    ax_1 = fig_1.add_subplot(1, 1, 1)
    ax_1.set_xlabel("the number of input items in BF")
    ax_1.set_ylabel("false postive rate")
    ax_1.plot(x, y)
    fig_1.savefig("./cal_bloom_prob.png")

if __name__ == '__main__':
    cal_bloom_prob()