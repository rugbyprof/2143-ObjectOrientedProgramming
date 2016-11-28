## Model View Controller - MVC

### Overview

"Model–View–Controller (MVC)is a software design pattern for implementing user interfaces on computers. It divides a given software application into three interconnected parts, so as to separate internal representations of information from the ways that information is presented to or accepted from the user."
<sup>https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller</sup>

The interacting parts are known as the **Model**, the **View** and the **Controller**. This pattern aims at dividing the application (the Controller part), the business processing logic (the Model part) and the output format logic (the View part) from each other. It's widely used in desktop solutions needing a "GUI" and in web sites.


|             Simple View        |
|:------------------------------:|
| ![](https://upload.wikimedia.org/wikipedia/commons/a/a0/MVC-Process.svg) |



|             More Complex View        |
|:------------------------------:|
| ![](http://www.bogotobogo.com/DesignPatterns/images/mvc/mvc_diagram.png) |

### Model

This typically is known as the "data" compoenent. Another description is "business logic":"In computer software, business logic or domain logic is the part of the program that encodes the real-world business rules that determine how data can be created, displayed, stored, and changed." This fits really well, because the "model" is all about data. 

### View

This is the presentation layer, or what the user sees. It is responsible for formatting and organizing anything the user interacts with. The goal is to keep as much "logic" or code out of this layer, and only attach "events" to actions performed by a user. The "event" would in turn be connected to a **Controller** which would call the appropriate action.


### Controller
This is the middle man between the **View** and the **Model**. 



```
import sqlite3
```
