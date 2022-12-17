# remove_white
This python aplication will remove all white from an image.

This application is based on a phtoshop plugin I created, call killwhite. 

In the case of (127) gray pixel, it finds the amount of white in the pixel (50%), then sets the pixel to black, and produces a 50% alpha. Thus the finnal result apear to not have changed but now has a transparency. 99% black is still 1% white and will have a 1% alpha, this seams to surprise some people. 

If it affects a reagon your didnt want, use photoshop or another editor and merge the images togeather keeping the areas you want. 

Uses:
It an be used to remove the background from a logo


<img width="324" alt="logo" src="https://user-images.githubusercontent.com/19735729/208267731-866fb6d9-6384-47b9-bba1-d08064a8b2b6.png">

->

![logo_alpha](https://user-images.githubusercontent.com/19735729/208267746-e759bea5-8a53-47c2-86df-054811267a49.png)
