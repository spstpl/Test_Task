class Product():
    def __init__(self,product):
        self.product = product
        print("Total Amount : $",self.get_product_count())

    def get_product_count(self):
        product_a_amount = self.scan(self.product.count('A'), \
            4, 7, 2)
        print("Product A Total amount : $",format(product_a_amount, '.2f'))
        product_b_amount = self.scan(self.product.count('B'), \
                0, 0, 12)
        print("Product B Total amount : $",format(product_b_amount, '.2f'))

        product_c_amount = self.scan(self.product.count('C'), \
                6, 6, 1.25)
        print("Product C Total amount : $",format(product_c_amount, '.2f'))

        product_d_amount = self.scan(self.product.count('D'), \
                0, 0, 0.15)
        print("Product D Total amount : $",format(product_d_amount, '.2f'))

        total_amount = product_a_amount + product_b_amount + \
            product_c_amount + product_d_amount
        return format(total_amount, '.2f')

    def scan(self, product_count, volume, volume_price, \
         unit_price):
        if volume > 0:
            total_volume_products = int(product_count / volume)
            remaining_unit_products = product_count % volume
            return total_volume_products*volume_price + \
                remaining_unit_products* unit_price
        else:
            return product_count * unit_price


if __name__ == '__main__':
    products  = input("Please enter Items e.g ABCDABAA \n")
    obj = Product(products)