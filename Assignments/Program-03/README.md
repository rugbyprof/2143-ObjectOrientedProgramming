## Image Processing Filters
<sup>source: http://www.cs.umb.edu/~jreyes/csit114-fall-2007/project4/filters.html#warhol</sup>


### Links to help you
<sup>Note: You cannot used any built in functions to apply any of the filters below. You must alter each pixel yourself. In other words, loop over the image to mage all your changes.</sup>

http://effbot.org/imagingbook/introduction.htm

```python
# opens an image using PIL
img = Image.open(file_name)

# resizes an image to a new height
img = img.resize((new_width,new_height), Image.ANTIALIAS)

# one method to get all the pixel data from an image however
# you now have one long list of rgb values and no idea of 
# width and height
pixels = list(img.getdata())

size = img.size 
# size is now a tuple with width and height (e.g. (345,200)) where 345=width and 200=height
```

### Description of Algorithms

Most of the filters described below can be done using [convolution](https://en.wikipedia.org/wiki/Kernel_(image_processing)) which is a technique of traversing over image data and applying special functions to alter pixel values. 

Each example will be using the original image viewed below:

| Original, unaltered lilies |
|:---:|
|![](http://www.cs.umb.edu/~jreyes/csit114-fall-2007/images/project4/waterlilies.jpg)|

### Glass Filter

To create a filter that mimics the effect of viewing the image through antique glass. Here is the general strategy to apply the filter to a particular patch of an image:

```
Choose a DISTANCE value.

For each pixel in the image: 
	Let XPOS = current x-coordinate
	Let YPOS = current y-coordinate

	Randomly select another pixel NEIGHBOR where:  
		x-coordinate is between: XPOS − DISTANCE and XPOS + DISTANCE
		y-coordinate is between: YPOS − DISTANCE and YPOS + DISTANCE

	Set the color of the CURRENT to the color of the NEIGHBOR.
```
Don't forget that dealing with pixels near the border of the image could result in a pixel that is "off" the image itself where:

> (`value < 0 or value > image_size`). 

Pythons `random.choice` function could help with this problem. Here is an example where we don't allow any choices to be below 0:

```python
# assume i is some number between 0 and width of your image.
nums = [x for x in range(i - distance, i + distance) if x >= 0]

choice = random.choice(nums)
```
You could alter the above snippet to ensure that all random choices are ON the current image by changing the `if` statement in the list comprehension.

| Lilies through glass DISTANCE = 5  |
|:---:|
|![](http://www.cs.umb.edu/~jreyes/csit114-fall-2007/images/project4/glass.jpg)|

### Vertical Flip

The vertical flip has the same effect viewing the image from mirror placed at the image's bottom (or top, depending on how you look at it.) 

```
# if flipping horizontal

define opposite:
   opposite = image_height - current_row
Example:
   image_size = (100,200)
   i = 0 , opposite = (image_size[1] - 0) # or 200
   i = 27, opposite = (image_size[1] - 27) # or 173 

start at top of image (y == 0)

loop through entire image one row at a time:
    exchange current row with opposite row 
   
# flipping vertical

Hmmmm. You've got this.

```

| Lilies flipped upside-down |
|:---:|
|![](http://www.cs.umb.edu/~jreyes/csit114-fall-2007/images/project4/flip.jpg)|

### Posterize

Posterization is the result of reducing the number of colors present in an image. The effect therefore resembles a graphic poster. If you try to view a 24-bit color image on an old 16 color CRT monitor, the screen will render a posterized version of the image.

In the algorithm below, we will split up each of the color channels into ranges. All values within each range will get transformed to a specified value for that range. For example, all values between 0 and 64 might get mapped to 0. However, what these values are is entirely up to you. Then all values between 64 and 128 to 64, etc. You may want to implement a method that allows you to specify the number of divisions at run-time.

```
Choose a rectangular region in the image.
Split the values [0, 255] into N distinct intervals I1, I2, ..., IN.
For each interval Ik, assign a fixed number VALUEk.

For each pixel CURRENT in the region:
	For CHANNEL∈{red, green, blue} values of CURRENT:
		If CHANNEL∈Ik, then set CURRENT to VALUEk.
```

There are several ways to implement this algorithm. To make the selection of the numbers VALUEk easy, you may want to rely on the modulo operator, x%y, which returns the remainder of x divided by y.

| Posterized lilies. Colors reduced mod 64 |
|:---:|
|![](http://www.cs.umb.edu/~jreyes/csit114-fall-2007/images/project4/posterize.jpg)|

### Blur

There are many ways to smooth or blur an image. The approach taken here is sometimes called mean filtering. In general, this algorithm as a low-pass filter. That is, it selects the low spatial frequencies present in the image while dispensing with the high ones (which is the opposite of the edge detector we designed in class does). For more on spatial filtering and image processing, you might check out this page on frequency filtering.

```
Choose a rectangular region RECTANGLE in the image.

For each pixel CURRENT in the region:
	For VALUE∈{red, green, blue} value of a pixel:
		Find the average VALUE of CURRENT and the neighboring pixels 
			immediately to its left, top, right, and bottom.
		Set VALUE to this average.
```

As in the glass filter, you will need to deal with the boundary pixels. Again, you may choose to wrap the image. It is also customary to set pixels on the boundary to a fixed color, for example, to black. In your analysis, describe the choices you made and the rationale behind them.

| Blurry lilies. Each pixel on a full 3×3 grid weighted by 1/9 |
|:---:|
|![](http://www.cs.umb.edu/~jreyes/csit114-fall-2007/images/project4/blur.jpg)|

### Solarize

Solarization is an effect from chemical photography caused by vast amounts of over-exposure to film. It results in the reversal of some tones in a photograph; that is, it is a partial negation of the image. The same effect can be achieved in digital image processing by negating those pixels whose intensity lies above or below a certain threshold. You may want your implementation to take a parameter that allows you to experiment more easily.

```
Let THRESHOLD be a fixed number.

For each pixel CURRENT in the region:
	If the intensity of CURRENT is less than (greater than) THRESHOLD,
		then negate CURRENT.
```

You may want to apply some technique other than negate in your method to achieve another effect instead. In your analysis, be sure to explain how you obtained your final threshold value and comparison operator (greater than, less than, e.g.). How does choosing a smaller (larger) value change the result of solarization?


Over-exposed lilies. Solarized with threshold set for those pixels with intensity less than 128.

| Solarized (Overexposure)|
|:---:|
|![](http://www.cs.umb.edu/~jreyes/csit114-fall-2007/images/project4/solarize.jpg)|



### Warhol effect

Andy Warhol was an American artist. He began his career as a commercial illustrator and then became a famous painter. His style combined techniques from commercial illustration popular at the time. We will combine filters described above and in class to mimic his work.

```
Choose a rectangular region RECTANGLE in the image.
Apply grayscale RECTANGLE.
Apply posterize to RECTANGLE.

Split the values [0, 255] into N distinct intervals I1, I2, ..., IN.
For each interval Ik, assign a fixed color COLORk.

For each pixel CURRENT in RECTANGLE:
	Let INTENSITY be the intensity of CURRENT.
	If INTENSITY∈Ik, then set the color of CURRENT to COLORk.
```

Several strategies that we've already seen are present here, most notably thresholding and code reuse. You may want to review if-then-else statements. Also review the conditional operators AND (&&) and OR (||). They are extremely helpful for this filter.

In your analysis, detail the design process. How did you choose the number of intervals, their ranges, and associated colors?


| Warhol effect|
|:---:|
|![](http://www.cs.umb.edu/~jreyes/csit114-fall-2007/images/project4/warhol.jpg)|

Waterlilies à la Warhol. Intervals were taken in multiples of 32.
The colors used were blue, magenta, orange, yellow, and pink.


