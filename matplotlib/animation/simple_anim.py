import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.rcParams['animation.ffmpeg_path'] = 'D:/dev/tools/ffmpeg-4.3.2-2021-02-02-full_build/bin/ffmpeg.exe'

fig, ax = plt.subplots()
x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,


anim = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

# unzip ffmpeg-release-full.7z from https://www.gyan.dev/ffmpeg/builds/ and add bin folder containing ffmpeg.exe to your path. For some reason, I still ahd to add path explicitly above
# x264 codec can be embedded in html5
# writer = animation.FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# anim.save('simple_anim.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
