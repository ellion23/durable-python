import glfw
import numpy as np
from OpenGL.GL import *
if not glfw.init():
    raise Exception("YOU PICKED THE WRONG HOUSE, FOOL.")
winda = glfw.create_window(1920, 1080, "GTA 6 FOR ANDROID MULTIPLAYER", None, None)
print('привет анон.')
if not winda:
    glfw.terminate()
    raise Exception("GTA 6 didn't made.")

def winda_resize(winda, width, height):
    glViewport(0, 0, width, height)

resize = glfw.set_window_size_callback(winda, winda_resize)

glfw.make_context_current(winda)


vertices = [-0.5, -0.5, 0.0,
            0.5, -0.5, 0.0,
            0.0, 0.5, 0.0]

colors = [1.0, 0.0, 0.0,
          0.0, 1.0, 0.0,
          0.0, 0.0, 1.0]

vertices = np.array(vertices, dtype=np.float32)
colors = np.array(colors, dtype=np.float32)

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT, 0, vertices)

glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, colors)


glClearColor(0, 0.1, 0.4, 1)

while not glfw.window_should_close(winda):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    # glRotate(0.1, 0.1, 2, 5)
    ct = glfw.get_time()
    glLoadIdentity()
    glScale(abs(np.sin(ct)), abs(np.sin(ct)), 1)
    glRotatef(np.sin(ct) * 90, 1, 0, 1)
    glTranslatef(np.sin(ct), np.cos(ct), 0)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glfw.swap_buffers(winda)

glfw.terminate()