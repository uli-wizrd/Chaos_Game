import matplotlib.pyplot as plt
import numpy as np
import datetime

# distance parameter

d = 0.5

# our triangle frame

tri = [[65,105,25,65],[120,20,20,120]]

# initial point
i_px = 2
i_py = 5

# we define where we will store stuff

p_x = []
p_y = []

# we store our initial values
p_x.append(i_px)
p_y.append(i_py)

np.random.seed(13)

ct = 0

start_time = datetime.datetime.now()

for i in range(8000):
    
    ct += 1

    dice_r = np.random.randint(1,4,dtype=int)

    if dice_r == 1:
            
            s_x = round(tri[0][0] + i_px, 4)
            s_y = round(tri[1][0] + i_py, 4)

            c_x = round((s_x*d), 4)
            c_y = round((s_y*d), 4)

            p_x.append(c_x)
            p_y.append(c_y)

            i_px = c_x
            i_py = c_y

    elif dice_r == 2:

            s_x = round(tri[0][1] + i_px, 4)
            s_y = round(tri[1][1] + i_py, 4)

            c_x = round((s_x*d), 4)
            c_y = round((s_y*d), 4)

            p_x.append(c_x)
            p_y.append(c_y)

            i_px = c_x
            i_py = c_y

    elif dice_r == 3:

            s_x = round(i_px + tri[0][2], 4)
            s_y = round(i_py + tri[1][2], 4)

            c_x = round((s_x*d), 4)
            c_y = round((s_y*d), 4)

            p_x.append(c_x)
            p_y.append(c_y)

            i_px = c_x
            i_py = c_y

    if ct % 5 == 0:
           
           p1_x = np.array(p_x).reshape(-1,1)
           p1_y = np.array(p_y).reshape(-1,1)
           dots = np.hstack((p1_x,p1_y))
            
           fig, ax = plt.subplots(facecolor = 'black' , figsize=(7,7))
           ax.set_title("Sierpinski Gasket",color = 'white')
           plt.scatter(dots[:,0],dots[:,1],s=1, c = dots[:,1], cmap = plt.get_cmap("plasma"),
                       alpha = 0.6)
           plt.axis('off')
           n_1 = 'CGT_' + str(ct) + '.jpg'
           plt.savefig("C:/Users/uli-8/Documents/Python/Proyectos/Chaos Game/triangle_animations/triangle" + str(n_1))
           plt.close()

           p1_x = []
           p1_y = []
           dot = []

print("Done")
print('Time spent animating: {}'.format(datetime.datetime.now() - start_time))