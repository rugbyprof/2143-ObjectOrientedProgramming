## Image Processing Filters
<sup>source: http://www.cs.umb.edu/~jreyes/csit114-fall-2007/project4/filters.html#warhol</sup>

### Description of Algorithms

Most of the filters described below can be done using [convolution](https://en.wikipedia.org/wiki/Kernel_(image_processing)) which is a technique of traversing over image data and applying special functions to alter pixel values. 

Each example will be using the original image viewed below:

![](http://www.cs.umb.edu/~jreyes/csit114-fall-2007/images/project4/waterlilies.jpg)

Original, unaltered lilies.

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
Don't forget that dealing with pixels near the border of the image could result in a pixel that is "off" the image itself (`value < 0 or value > image_size`). Pythons `random.choice` function could help with this problem. Here is an example where we don't allow any choices to be below 0:

```python
# assume i is some number between 0 and width of your image.
nums = [x for x in range(i - distance, i + distance) if x >= 0]

choice = random.choice(nums)
```
You could alter the above snippet to ensure that all random choices are ON the current image.

There are other ways to handle the boundary cases. What you decide to do is ultimately up to you. Be sure to include a discussion of what you do decide to do in your analysis.
<center>
![](http://www.cs.umb.edu/~jreyes/csit114-fall-2007/images/project4/glass.jpg)
Lilies through glass. DISTANCE = 5.
</center>
### Vertical Flip

The vertical flip has the same effect viewing the image from mirror placed at the image's bottom (or top, depending on how you look at it.) Alternatively, pretend that the image is printed on a translucent gel and that you're facing it from the front. Now physically flip the picture over its top (or bottom) edge so that you're viewing it from the back. This acheives the same effect as the vertical flip filter.

Choose a rectangular region RECTANGLE in the image.
Let TOP be the y-coordinate that bounds the top of RECTANGLE.

For each pixel CURRENT in RECTANGLE:
	Let DISTANCE be the difference between the y-coordinate of CURRENT and TOP.
	Let MIRROR-RELATIVE be the pixel whose x-coordinate is the same as CURRENT
		and whose y-coordinate is the same distance from BOTTOM as DISTANCE.
		
	Set the color of CURRENT to the color of MIRROR-RELATIVE.
You can easily tweak this algorithm to achieve a horizontal flip. When I initially implemented this filter, I accidentally flipped both vertically and horizontally. How might you do this? How might you reflect across another, oblique axis?

Vertical flip
Lilies flipped upside-down.

### Posterize

Posterization is the result of reducing the number of colors present in an image. The effect therefore resembles a graphic poster. If you try to view a 24-bit color image on an old 16 color CRT monitor, the screen will render a posterized version of the image.

In the algorithm below, we will split up each of the color channels into ranges. All values within each range will get transformed to a specified value for that range. For example, all values between 0 and 64 might get mapped to 0. However, what these values are is entirely up to you. Then all values between 64 and 128 to 64, etc. You may want to implement a method that allows you to specify the number of divisions at run-time.

Choose a rectangular region in the image.
Split the values [0, 255] into N distinct intervals I1, I2, ..., IN.
For each interval Ik, assign a fixed number VALUEk.

For each pixel CURRENT in the region:
	For CHANNEL∈{red, green, blue} values of CURRENT:
		If CHANNEL∈Ik, then set CURRENT to VALUEk.
There are several ways to implement this algorithm. To make the selection of the numbers VALUEk easy, you may want to rely on the modulo operator, x%y, which returns the remainder of x divided by y.

Posterize (16 colors)
Posterized lilies. Colors reduced mod 64.

### Blur

There are many ways to smooth or blur an image. The approach taken here is sometimes called mean filtering. In general, this algorithm as a low-pass filter. That is, it selects the low spatial frequencies present in the image while dispensing with the high ones (which is the opposite of the edge detector we designed in class does). For more on spatial filtering and image processing, you might check out this page on frequency filtering.

Choose a rectangular region RECTANGLE in the image.

For each pixel CURRENT in the region:
	For VALUE∈{red, green, blue} value of a pixel:
		Find the average VALUE of CURRENT and the neighboring pixels 
			immediately to its left, top, right, and bottom.
		Set VALUE to this average.
As in the glass filter, you will need to deal with the boundary pixels. Again, you may choose to wrap the image. It is also customary to set pixels on the boundary to a fixed color, for example, to black. In your analysis, describe the choices you made and the rationale behind them.

Blur filter
Blurry lilies. Each pixel on a full 3×3 grid weighted by 1/9.

### Solarize

Solarization is an effect from chemical photography caused by vast amounts of over-exposure to film. It results in the reversal of some tones in a photograph; that is, it is a partial negation of the image. The same effect can be achieved in digital image processing by negating those pixels whose intensity lies above or below a certain threshold. You may want your implementation to take a parameter that allows you to experiment more easily.

Choose a rectangular region in the image.
Let THRESHOLD be a fixed number.

For each pixel CURRENT in the region:
	If the intensity of CURRENT is less than (greater than) THRESHOLD,
		then negate CURRENT.
You may want to apply some technique other than negate in your method to achieve another effect instead. In your analysis, be sure to explain how you obtained your final threshold value and comparison operator (greater than, less than, e.g.). How does choosing a smaller (larger) value change the result of solarization?

Solarized (Overexposure)
Over-exposed lilies. Solarized with threshold set for those pixels with intensity less than 128.

### Warhol effect

Andy Warhol was an American artist. He began his career as a commercial illustrator and then became a famous painter. His style combined techniques from commercial illustration popular at the time. We will combine filters described above and in class to mimic his work.

Choose a rectangular region RECTANGLE in the image.
Apply grayscale RECTANGLE.
Apply posterize to RECTANGLE.

Split the values [0, 255] into N distinct intervals I1, I2, ..., IN.
For each interval Ik, assign a fixed color COLORk.

For each pixel CURRENT in RECTANGLE:
	Let INTENSITY be the intensity of CURRENT.
	If INTENSITY∈Ik, then set the color of CURRENT to COLORk.
Several strategies that we've already seen are present here, most notably thresholding and code reuse. You may want to review if-then-else statements. Also review the conditional operators AND (&&) and OR (||). They are extremely helpful for this filter.

In your analysis, detail the design process. How did you choose the number of intervals, their ranges, and associated colors?

Warhol effect
Waterlilies à la Warhol. Intervals were taken in multiples of 32.
The colors used were blue, magenta, orange, yellow, and pink.

Last Updated: 18 October 2007
