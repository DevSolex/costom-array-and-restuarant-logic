class Restaurant:
    tables = []
    menu = []
    def __init__(self):
        pass
    # def __init__(self, order:str, table:str):
    #     self.order:str = order
    #     self.table:str = table

    def add_table(table_name:str):
        if len(Restaurant.tables) < 4:
            Restaurant.tables.append(table_name)
            return f'{table_name} added to tables successfully'
        else:
            print("Cannot add more tables.")

    def remove_table(table_name:str):
        if table_name in Restaurant.tables:
            del table_name
            return f'{table_name} removed from tables successfully'
        else:
            return f"table {table_name} no found"
        
    def add_menu(food_name:str):
        if food_name not in Restaurant.menu:
            Restaurant.menu.append(food_name)
            return f'{food_name} added to menu successfully'
        else:
            return f'{food_name} in menu already'
        
    def remove_menu(food_name:str):
        if food_name in Restaurant.menu:
            Restaurant.menu.remove(food_name)
            return f'{food_name} removed from menu successfully'
        else:
            return f'{food_name} not found in menu'

class Order:
    def __init__(self):
        pass
    # def __init__(self, order:str, table:str):
    #     super().__init__(order, table)

    def place_order(self, order:str, table:str='table'):
        print('Welcome to Luckify Restaurant')
        print('Orders...')
        print(Restaurant.menu)
        print(Restaurant.tables)
        if order in Restaurant.menu:
            if table in Restaurant.tables:
                return f'Your order of {order} in {table} is successful'
            else:
                return f'Your ordered table {table} not found'
        else:
            return f'Your ordered food {order} not in menu'



Restaurant.add_table('table1')
Restaurant.add_table('table2')
Restaurant.add_table('table3')
Restaurant.add_table('table4')
Restaurant.add_menu('shawarma')
Restaurant.add_menu('burger')
Restaurant.add_menu('pasta')
Restaurant.add_menu('salad')
order1 = Order()
print(order1.place_order('shawarma', 'table1'))
order2 = Order()
print(order2.place_order('salad', 'table5'))


