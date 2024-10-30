# The chaos game

The chaos game is a simple dynamic  where: <br>

1. You choose 3 points in a 2D space in such a way that they form a triangle it doesn't matter what kind they just have to form one, once we have our vertices A, B and C we can join them to form the boundary of our game board.<br>

2. Once we have our triangle we can choose at random a point contained within it or outside it as our starting value.<br>

3. Now we assign each vertex of our triangle a pair of values from a 6 sided dice where each side has a dot in it (e.g A has the sides with 1 and 2 dots, B 3 dots and 4 dots and C 5 dots and 6 dots) once we do this we can roll our dice.<br>

4. Depending on the face up value of our dice we will choose a point half way between our starting point and the vertex assigned to that value on our dice, now our starting point will be this new location (You don't really need a dice at all, just a tool that gives you a random integer).<br>

5. We run this new position iterative selection algorithm until we can see a pattern arise.<br>

## Consideration

All of the animations shown in this project are the result of changing the distance at which we are choosing our next point in this iterative process.<br>

The normal dynamic fixes this distance at 0.5 (half way) but I think it's more interesting to see it change in time.<br>

## Some questions

1. What happens when the process doesn't have any restrictions?<br>

2. What happens when we don't let vertices repeat?<br>

3. What happens when we use two frames of the same shape with the same rules?<br>

4. What happens when we use two different shapes as the frames to run this process?<br>

## A triangle

The following animation is the result of our dynamic using the distance parameter of 0.5: <br>

![](https://github.com/uli-wizrd/Chaos_Game/blob/main/Graphics/triangle.gif)

We obtain the Sierpinski gasket (audience claps). <br>

And if we look at what happens when we let the distance parameter increase over time we get this: <br>

![](https://github.com/uli-wizrd/Chaos_Game/blob/main/Graphics/dist_var_tri.gif)

If we restrict the way we choose the next vertex we get this: <br>

![](https://github.com/uli-wizrd/Chaos_Game/blob/main/Graphics/dist_var_rest_tri.gif)

## A cuadrilateral

When we use the distance parameter of 0.5, a cuadrilateral frame and we restrict the way we choose our next vertex so it's not the previous one we get this picture:

![](https://github.com/uli-wizrd/Chaos_Game/blob/main/Graphics/Chaos_Game_Cuad_0.5.png)

This highly irregular pattern when we change the distance parameter evolves like this: <br>

![](https://github.com/uli-wizrd/Chaos_Game/blob/main/Graphics/dist_var_cuad.gif)

And the most impressive part I think is that when we don't restrict the way we choose the next vertex highly regular patterns arise:

![](https://github.com/uli-wizrd/Chaos_Game/blob/main/Graphics/dist_var_unrest_cuad.gif)

## A pentagon

Now let's see what happens with a 5 sided frame: <br>

![](https://github.com/uli-wizrd/Chaos_Game/blob/main/Graphics/Chaos_Game_Pent_0.5.png)

We can see weird looking turtles (at least that what I see haha). <br>

Now an animation of the unrestricted process: <br>

![](https://github.com/uli-wizrd/Chaos_Game/blob/main/Graphics/dist_var_unrest_pent.gif)

Now the restricted version:<br>

![](https://github.com/uli-wizrd/Chaos_Game/blob/main/Graphics/dist_var_pent.gif)

## Using two frames

Now I felt it would be interesting to add more frames (more shapes like triangles or squares, etc.) and see what happens. <br>

In the following animation we can see what happens when we run our game using a triangle and a cuadrilateral frame, the animation shows how changing the distance parameter in the game alters the way points are plotted in space: <br>

![](https://github.com/uli-wizrd/Chaos_Game/blob/main/Graphics/dist_var_cuad_tri.gif)

Now using 2 cuadrilaterals:<br>

![](https://github.com/uli-wizrd/Chaos_Game/blob/main/Graphics/dist_var_cuad_cuad.gif)

Now using 2 triangles: <br>

![](https://github.com/uli-wizrd/Chaos_Game/blob/main/Graphics/dist_var_d_tri.gif)

This part oddly enough renders very similar results every time, how ever it must be noted that in every dynamic that was animated the process was restricted (can't choose the previous vertex as the next one), I have yet to animate this process without restrictions, but one can imagine that the types of shapes will change given our previous experience with this condition. <br>

## Conclusions

The conclusions I can make from playing around with this set of rules is that complexity can arise from simple rules, which is just a beautiful thing about our world that we can learn through mathematics, also to answer my own questions starting with the first one is that we get a very ordered fractal that reflects the frame used to generate it, like a triangle, a square or a pentagon, etc. The funny thing happens when we add restrictions which I think add some order to the game, we get a less ordered fractal like when we run the restricted version of the dynamic with the square this answers question 2, and to answer the last two questions I can say that at least if we are just running the restricted version of the process our fractals become very similar, without a lot of distinctive features but they are still fractals which is interesting.<br>

Now if you would like to recreate my results here you can find the files that I used to generate them, I wrote all of the code usign only the rules of the game, thank you for reading this and I hope you have as much fun as I did with this subject.

With kind regards, 

Eng. Ulises O. Rangel Rivera.

## References

In order to make this project I used the following resources, so if you like what you see here please be sure to check them out.

1.- Library <a href="https://www.youtube.com/watch?v=kbKtFN71Lfs&t=450s" target="_blank"> Numberphile video on the subject <a> <br>
2.- Library <a href="https://numpy.org/" target="_blank"> Numpy <a> <br>
4.- Library <a href="https://matplotlib.org/stable/gallery/color/index.html" target="_blank"> Matplotlib <a> <br>
