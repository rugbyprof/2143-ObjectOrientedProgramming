## Model View Controller - MVC

### Overview

"Model–View–Controller (MVC)is a software design pattern for implementing user interfaces on computers. It divides a given software application into three interconnected parts, so as to separate internal representations of information from the ways that information is presented to or accepted from the user."
<sup>https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller</sup>

The interacting parts are known as the **Model**, the **View** and the **Controller**. This pattern aims at dividing the application (the Controller part), the business processing logic (the Model part) and the output format logic (the View part) from each other. It's widely used in desktop solutions needing a "GUI" and in web sites.


|             Simple View        |             More Complex View        |
|:------------------------------:|:------------------------------:|
| ![](https://upload.wikimedia.org/wikipedia/commons/a/a0/MVC-Process.svg) |![](http://www.bogotobogo.com/DesignPatterns/images/mvc/mvc_diagram.png) |



|             More Complex View        |
|:------------------------------:|
| ![](http://www.bogotobogo.com/DesignPatterns/images/mvc/mvc_diagram.png) |

It all starts with a request…
In the case of the Legos, it was your brother who asked you to build something. In the case of a web app, it’s a user entering a URL, requesting to view a certain page.

So your brother is the user.

The request reaches the controller…
With the Legos, you are the controller.

The controller is responsible for grabbing all of the necessary building blocks and organizing them as necessary.

Those building blocks are known as models…
The different types of Legos are the models. You have all different sizes and shapes, and you grab the ones you need to build the spaceship. In a web app, models help the controller retrieve all of the information it needs from the database.

So the request comes in…
The controller (you) receives the request.

It goes to the models (Legos) to retrieve the necessary items.

And now everything is in place to produce the final product.

The final product is known as the view…
The spaceship is the view. It’s the final product that’s ultimately shown to the person who made the request (your brother).

In a web application, the view is the final page the user sees in their browser.

### Model

This typically is known as the "data" compoenent. Another description is "business logic":"In computer software, business logic or domain logic is the part of the program that encodes the real-world business rules that determine how data can be created, displayed, stored, and changed." This fits really well, because the "model" is all about data. 

### View

This is the presentation layer, or what the user sees. It is responsible for formatting and organizing anything the user interacts with. The goal is to keep as much "logic" or code out of this layer, and only attach "events" to actions performed by a user. The "event" would in turn be connected to a **Controller** which would call the appropriate action.


### Controller
This is the middle man between the **View** and the **Model**. 



```
class Model(object):

    products = {
        'milk': {'price': 1.50, 'quantity': 10},
        'eggs': {'price': 0.20, 'quantity': 100},
        'cheese': {'price': 2.00, 'quantity': 10}
    }


class View(object):

    def product_list(self, product_list):
        print('PRODUCT LIST:')
        for product in product_list:
            print(product)
        print('')

    def product_information(self, product, product_info):
        print('PRODUCT INFORMATION:')
        print('Name: %s, Price: %.2f, Quantity: %d\n' %
              (product.title(), product_info.get('price', 0),
               product_info.get('quantity', 0)))

    def product_not_found(self, product):
        print('That product "%s" does not exist in the records' % product)


class Controller(object):

    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_product_list(self):
        product_list = self.model.products.keys()
        self.view.product_list(product_list)

    def get_product_information(self, product):
        product_info = self.model.products.get(product, None)
        if product_info is not None:
            self.view.product_information(product, product_info)
        else:
            self.view.product_not_found(product)


if __name__ == '__main__':

    controller = Controller()
    controller.get_product_list()
    controller.get_product_information('cheese')
    controller.get_product_information('eggs')
    controller.get_product_information('milk')
    controller.get_product_information('arepas')

### OUTPUT ###
# PRODUCT LIST:
# cheese
# eggs
# milk
#
# PRODUCT INFORMATION:
# Name: Cheese, Price: 2.00, Quantity: 10
#
# PRODUCT INFORMATION:
# Name: Eggs, Price: 0.20, Quantity: 100
#
# PRODUCT INFORMATION:
# Name: Milk, Price: 1.50, Quantity: 10
#
# That product "arepas" does not exist in the records
```
