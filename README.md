# About
This python aplication and library will remove all white or black from an image. It's based on a previous phtoshop plugin I created, call killwhite. 

### How it works
In the case of [127] gray pixel, it finds the amount of white in the pixel (50%), then sets the pixel to black, and adds a 50% alpha. Thus the finnal result apear to not have changed but now has a transparency. 99% black is still 1% white and will have a 1% alpha. 

If it affects a reagon your didnt want, use photoshop or another editor and merge the images togeather preserving the areas you want. 

## The recipe:
```
RGB -> HSV
convert to double 
convert to value scale (0-1)

// make the alpha
alpha = 1.0-(v-s)

// preserve color and values
if (alpha < 1.0)
  v = s/alpha
  S = s/alpha

to origional value scale
HSV -> RGB
```

## Use RemoveWhite()
It can be used to remove the background from a logo

<img width="324" alt="logo" src="logo.png"> <img width="324" alt="logo_alpha" src="logo_alpha.png">

Add alpha to difficult to edit artwork:

<img width="324" alt="logo" src="mushroom_art.png"> <img width="324" alt="logo_alpha" src="mushroom_art_alpha.png">

combine with other images / color to replace the white in an image:

## Use RemoveBlack()

Stock fire images/video is usualy shot on a black background for ease of adding to other imagery. This makes it even better, no compromise in color or value like with "blendmodes".

<img width="324" alt="fire" src="fire.png"> <img width="324" alt="fire_alpha" src="fire_alpha.png">

fire source &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; with alpha from RemoveBlack()

<img width="324" alt="grill" src="grill.png"> <img width="324" alt="mask" src="fire_grill_mask.png">

grill source &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; &emsp; aditional mask

<img width=648 alt="fire_grill" src="fire_grill.png">

# Parameters
### -i, --image

this is the path to the desired image

### -a, --alpha_suffix

Optional, Sperates the alpha and adds suffix to alpha's filename, without this it will write a single file with an alpha if the file type supports it. Use this if you want to write a file type without an alpha channel like JPG. 

### -o, --output

output image path and extension

### -b, --remove_black

Optional, With this flag it will remove black, by default it removes white. 

### --plugin

Advanced, Optional, I use the imageio for increased file type compatablity, imageio has multiple methods to write common file types, use this flag to specify which imageio plugin you want to write with. May require additional installation, see imageio docs for more info. Example plugins: [freeimage, pillow, ITK, GDAL, tifffile]

