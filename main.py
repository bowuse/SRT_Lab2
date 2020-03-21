import random
import math
import matplotlib.pyplot as plt
import time

N = 256
w = 900
n = 10
t = [i for i in range(N)]


def count_sin():
    res = []
    for i in range(n):
        A = random.random()
        fi = random.random() * 6.28
        res_i = [A * math.sin(w * t[i] * i + fi) for i in range(N)]
        res.append(res_i)
    return res


def count_x_t():
    #######
    # Випадковий сигнал
    #######
    res = count_sin()
    x_t = []
    for i in range(N):
        x = 0
        for j in range(n):
            x += res[j][i]
        x_t.append(x)
    return x_t


def count_m_x(signal):
    m_x = sum(signal) / len(signal)
    return m_x


def count_cor(z, w):
    ######
    # Розрахунок кореляційних функцій
    ######
    m_z = count_m_x(z)
    m_w = count_m_x(w)
    signal_z = z
    signal_w = w
    r_z_z = [(signal_z[i] - m_z) * (signal_z[2 * i] - m_z) / N / 2 for i in range(N // 2)]
    r_z_w = [(signal_z[i] - m_z) * (signal_w[2 * i] - m_w) / N / 2 for i in range(N // 2)]
    r_w_z = [(signal_w[i] - m_w) * (signal_z[2 * i] - m_z) / N / 2 for i in range(N // 2)]
    plt.plot([i for i in range(N // 2)], r_z_z, label='Rzz', color='blue')
    plt.plot([i for i in range(N // 2)], r_z_w, label='Rzw', color='green')
    plt.plot([i for i in range(N // 2)], r_w_z, label='Rwz', color='red')
    plt.legend()
    plt.grid(True)
    plt.show()


def write_res_in_file(param, value):
    file = open('res.txt', 'a+')
    file.write('\n' + param + ': ' + value)
    file.close()


def main():
    time_start = time.time()
    z = count_x_t()
    w = count_x_t()
    count_cor(z, w)
    time_end = time.time()
    write_res_in_file('Time', str(time_end - time_start))


if __name__ == '__main__':
    main()
