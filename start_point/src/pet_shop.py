# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, amount):
    cc_pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(cc_pet_shop, sold):
    cc_pet_shop["admin"]["pets_sold"] += sold    

def get_stock_count(cc_pet_shop):
    return len(cc_pet_shop["pets"])

def get_pets_by_breed(cc_pet_shop, breed):
    dog = []
    for pet in cc_pet_shop["pets"]:
        if pet["breed"] == breed:
            dog.append(pet)
    return dog

def find_pet_by_name(cc_pet_shop, pets_name):
  for pet in cc_pet_shop["pets"]:
    if pet["name"] == pets_name:
        return pet

def remove_pet_by_name(cc_pet_shop, pets_name):
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == pets_name:
            cc_pet_shop["pets"].remove(pet)


def add_pet_to_stock(cc_pet_shop, new_pet):
    cc_pet_shop["pets"].append(new_pet)
    
def get_customer_cash(customers):
    return customers["cash"]    

def remove_customer_cash(customers, total):
    customers["cash"] -= total

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, pet):
    customers["pets"].append(pet)
    
def customer_can_afford_pet(customer, new_pet):
#     # for total in customer["cash"]:
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

def sell_pet_to_customer(cc_pet_shop, pet, customer):
    if pet == None or customer_can_afford_pet(customer, pet) == False:
        return
    customer["pets"].append(pet)
    increase_pets_sold(cc_pet_shop, 1)
    remove_customer_cash(customer, pet["price"])
    add_or_remove_cash(cc_pet_shop, pet["price"])
    remove_pet_by_name(cc_pet_shop, pet["name"])



            
        


            

            
              







    




    

    


    
   



        

 
    


    
          
        

    




    

    
        


