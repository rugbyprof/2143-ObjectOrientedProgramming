# Program 2
***Due: TBD (To Be Determined)***

### Overview

- Given the [grid.py](./grid.py) file in this directory, turn this module style file into an object called grid.
- The "color_wheel" provided by this module has 18 unique colors. We are going to increase this by a lot. Lets use all the "named" html colors that exist. The file [colors.json](./colors.json) has 148 colors. Of course this doesn't mean that all colors will be rendered perfect or look good next to each other, however it does give us more choices.
- To read this json file in, use the following snippet:
```
with open("colors.json") as file: 
   colors = file.read()

colors = json.loads(colors)

for color in colors:
    print(color)
```

- This will print out:

```
...
{u'rgb': [46, 139, 87], u'html': u'#2e8b57', u'name': u'seagreen'}
{u'rgb': [255, 250, 250], u'html': u'#fffafa', u'name': u'snow'}
{u'rgb': [0, 0, 205], u'html': u'#0000cd', u'name': u'mediumblue'}
{u'rgb': [25, 25, 112], u'html': u'#191970', u'name': u'midnightblue'}
{u'rgb': [175, 238, 238], u'html': u'#afeeee', u'name': u'paleturquoise'}
{u'rgb': [238, 232, 170], u'html': u'#eee8aa', u'name': u'palegoldenrod'}
...
```

- The new `__main__` code for testing should do the following:
    - Ask the user for how many colors (or use argv)
    - Check the input number to ensure it can be displayed in a square grid. For example:
        - 9 = ***`3 x 3`***
        - 16 = ***`4 x 4`***
        - 25 = ***`5 x 5`***
    - Based on this number of colors ***N***, create a grid that is ***N x N***. 
    - For a ***9 x 9*** grid, each color will be in a mini ***3 x 3*** grid:
    
    ![](https://d3vv6lp55qjaqc.cloudfront.net/items/3x0n3t300n1V1C0X2b3u/table9x9_colors.png?X-CloudApp-Visitor-Id=1094421)
