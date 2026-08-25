class supplier :
    def __init__(self,supplier_name,city,contact_number):
        self.supplier_name = supplier_name
        self.city = city
        self.contact_number = contact_number
        
        
class product :
    def __init__(self,product_id,product_name,category,price,supplier):
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.__price = price
        self.supplier = supplier
      
    def get_price(self):
        return self.__price
    
    def set_price(self,price):
        if price >= 100 :
            self.__price = price
            return "price updated successfully"
        else:
            return "price be less than RS. 100 "
    
    def calculate_final_price(self):
        return self.__price
    
    def display(self):
        print("Original Price:",self.__price)
        final_price = self.calculate_final_price()
        discount = self.__price - final_price
        print("Discount:",discount)
        print("Final price:",final_price)
        print("Supplier City:",self.supplier.city)
        
    def __str__(self):
        return f"p{self.product_id}-{self.product_name}-{self.category}"
    
    
class Electronics(product):
    
    def __init__(self, product_id, product_name, category, price, supplier,warranty_year):
        super().__init__(product_id, product_name, category, price, supplier)            
        self.warranty_year = warranty_year
        
    def calculate_final_price(self):
        discount = self.get_price() * 10/100
        return self.get_price()-discount
    def display(self):
        super().display()
        print("Warranty:",self.warranty_year,"Year")
        
        
class clothing(product):
    def __init__(self, product_id, product_name, category, price, supplier,size):
        super().__init__(product_id, product_name, category, price, supplier)
        self.size = size
        
    def calculate_final_price(self):
        discount = self.get_price() * 20 / 100
        return self.get_price() - discount
    def display(self):
        super().display()
        print("Size:",self.size)
        
        
class grocery(product):
    def __init__(self, product_id, product_name, category, price, supplier,exipiry_date):
        super().__init__(product_id, product_name, category, price, supplier)            
        self.exipriy_date = exipiry_date
        
    def calculate_final_price(self):
        discount = self.get_price() * 5 / 100
        return self.get_price() - discount
    
    def display(self):
        super().display()
        print("Expiry Date:",self.exipriy_date)
        

                                                   
supplier1 = supplier(
    "Tech word",
    "pune",
    "534572578478"
)
                
p1 = Electronics(
    101,"Loptop","Electronics",50000,supplier1,2
)        
p1.display()