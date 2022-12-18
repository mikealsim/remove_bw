# remove_white
This python aplication will remove all white from an image.

This application is based on a phtoshop plugin I created, call killwhite. 

In the case of (127) gray pixel, it finds the amount of white in the pixel (50%), then sets the pixel to black, and produces a 50% alpha. Thus the finnal result apear to not have changed but now has a transparency. 99% black is still 1% white and will have a 1% alpha, this seams to surprise some people. 

If it affects a reagon your didnt want, use photoshop or another editor and merge the images togeather keeping the areas you want. 

Uses:
It an be used to remove the background from a logo

<img width="324" alt="logo" src="logo.png"> <img width="324" alt="logo_alpha" src="logo_alpha.png">

Add alpha to difficult to edit artwork:

<img width="324" alt="logo" src="mushroom_art.png"> <img width="324" alt="logo_alpha" src="mushroom_art_alpha.png">

combine with other images / color to replace the white in an image:

Use remove black to remove a background

<img width="324" alt="fire" src="fire.png"> <img width="324" alt="fire_alpha" src="fire_alpha.png">
