## Command Pattern

### Overview



|             Simple View        |         More Complex View  |
|:------------------------------:|:------------------------------:|
| ![](https://upload.wikimedia.org/wikipedia/commons/a/a0/MVC-Process.svg) | ![](http://www.bogotobogo.com/DesignPatterns/images/mvc/mvc_diagram.png) |



## Workflow  


<sup>Source: [[1]]</sup>

## Definitions


## Key Points


<sup>Source: [[4]]</sup>
## Code Example  

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
<sup>Source: [[3]]</sup>

#### Sources:
- <sup>1. https://realpython.com/blog/python/the-model-view-controller-mvc-paradigm-summarized-with-legos/</sup>
- <sup>2. https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller</sup>
- <sup>3. http://zqpythonic.qiniucdn.com/data/20140929095044/index.html
- <sup>4. https://wiki.wxpython.org/ModelViewController

[1]: https://realpython.com/blog/python/the-model-view-controller-mvc-paradigm-summarized-with-legos/
[2]: https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
[3]: http://zqpythonic.qiniucdn.com/data/20140929095044/index.html
[4]: https://wiki.wxpython.org/ModelViewController

