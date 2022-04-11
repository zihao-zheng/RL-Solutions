import random
import matplotlib.pyplot as plt

# 检验状态 S 下能否采取动作 a
def check_action(width, height, S, a):
    S_ = (S[0]+a[0], S[1]+a[1])
    if S_[0] < 0 or S_[0] > height-1 or S_[1] < 0 or S_[1] > width-1:
        return False
    return True


# 计算状态 S 下采取动作 a 后的状态 S'
def move(width, height, S, a, wind, rand_move=False):
    x, y = S[0]+a[0], S[1]+a[1]
    x = max(x-wind[S[1]], 0)
    if rand_move:
        r = random.randint(1, 3)
        if r == 1:
            x = max(x-1, 0)
        elif r == 2:
            x = min(x+1, height-1)
    return (x, y)


# epsilon-贪心策略
def eps_greedy(width, height, S, action_all, eps, Q):
    actions = [a for a in action_all if check_action(width, height, S, a)]
    p = [eps/len(actions) for a in actions]
    q = [Q[S, a] for a in actions]
    p[q.index(max(q))] += 1-eps
    sum_p = 0
    random_value = random.random()
    for a, i in zip(actions, p):
        sum_p += i
        if sum_p >= random_value:
            return a


# Sarsa 算法
def Sarsa(alpha, gamma, eps, width, height, wind, action_all, G, S_start, iterations, rand_move=False):
    Q = {}
    for i in range(height):
        for j in range(width):
            actions = [a for a in action_all if check_action(
                width, height, (i, j), a)]
            for a in actions:
                if (i, j) == G:
                    Q[(i, j), a] = 0
                else:
                    Q[(i, j), a] = random.random()
    step_list = [0]
    for it in range(iterations):
        S = S_start
        step = 0
        while True:
            if step == 0:
                A = eps_greedy(width, height, S, action_all, eps, Q)
            S_ = move(width, height, S, A, wind, rand_move)
            R = -1
            A_ = eps_greedy(width, height, S_, action_all, eps, Q)
            Q[(S, A)] = Q[(S, A)]+alpha*(R+gamma*Q[(S_, A_)]-Q[(S, A)])
            S, A = S_, A_
            step += 1
            if S == G:
                break
        step_list.append(step_list[-1]+step)
    return step_list

if __name__=="__main__":
    # 6.9
    # wind = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]
    # G = (3, 7)
    # S_start = (3, 0)
    # iterations = 300
    #
    # action_all = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # step_list = Sarsa(0.5, 1, 0.1, 10, 7, wind, action_all, G, S_start, iterations)
    # plt.plot(step_list, list(range(iterations+1)), label="example6.5 directions=4")
    #
    # action_all = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    # step_list = Sarsa(0.5, 1, 0.1, 10, 7, wind, action_all, G, S_start, iterations)
    # plt.plot(step_list, list(range(iterations+1)), label="exercise6.9 directions=8")
    #
    # action_all = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]
    # step_list = Sarsa(0.5, 1, 0.1, 10, 7, wind, action_all, G, S_start, iterations)
    # plt.plot(step_list, list(range(iterations+1)), label="exercise6.9 directions=9")
    #
    # plt.xlabel("Time steps")
    # plt.ylabel("Episodes")
    # plt.legend()
    # plt.show()

    # 6.10
    wind = [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]
    G = (3, 7)
    S_start = (3, 0)
    iterations = 1000

    action_all = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    step_list = Sarsa(0.5, 1, 0.1, 10, 7, wind, action_all, G, S_start, iterations)
    plt.plot(step_list, list(range(iterations + 1)), label="example6.5 directions=4")

    action_all = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    step_list = Sarsa(0.5, 1, 0.1, 10, 7, wind, action_all, G, S_start, iterations)
    plt.plot(step_list, list(range(iterations + 1)), label="exercise6.9 directions=8")

    action_all = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 0)]
    step_list = Sarsa(0.5, 1, 0.1, 10, 7, wind, action_all, G, S_start, iterations)
    plt.plot(step_list, list(range(iterations + 1)), label="exercise6.9 directions=9")

    action_all = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    step_list = Sarsa(0.5, 1, 0.1, 10, 7, wind, action_all, G, S_start, iterations, rand_move=True)
    plt.plot(step_list, list(range(iterations + 1)), label="exercise6.10 directions=8")

    plt.xlabel("Time steps")
    plt.ylabel("Episodes")
    plt.legend()
    plt.show()


