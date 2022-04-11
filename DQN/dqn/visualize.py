import matplotlib.pyplot as plt


episodes = []
durations = []
with open('records/record_episode_2_3.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        items = line.split('\t')
        if len(items) < 2:
            print(items)
            continue
        episode = items[0].split('=')
        episode = episode[1]

        duration = items[2].split('=')
        duration = duration[1]

        episodes.append(episode)
        durations.append(duration)

plt.title('Training...')
plt.xlabel('Episode')
plt.ylabel('Duration')
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
plt.plot(episodes, durations)
plt.show()

