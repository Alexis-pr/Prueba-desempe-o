# This is where the books are stored.
import datetime
inventory = [
    {
        "title" : "Harry Potter",
        "author" : "J. K. Rowling",
        "category" : "Science fiction",
        "cost": 20000.0,
        "stock" : 30,
    },
    {
        "title" : "lord of the rings",
        "author" : "J.R.R.Tolkien",
        "category" : "Science fiction",
        "cost": 20000.0,
        "stock" : 20,
    },
    {
        "title" : "Percy Jackson",
        "author" : "Rick Riordan",
        "category" : "mitologyc",
        "cost": 15000.0,
        "stock" : 15,
    },
    {
        "title" : "Habitos Atómicos",
        "author" : "James Clear",
        "category" : "Self Help",
        "cost": 10000.0,
        "stock" : 20,
    },
    {
        "title" : "El Jardín De Las Mariposas",
        "author" : "Dot Hutchison",
        "category" : "Thriller",
        "cost": 19000.0,
        "stock" : 19,
    }
]

sales = []

code = "Ahorr025"


#function that allows adding data

def addBooks():

    while True:
        # here validate and add the title books
        while True:       
                namebook = input("Add to names to book: ").lower() # store the name books and convert to lowercase              
                for letra in namebook:
                    if letra in "áéíóú": 
                        print("Accents are not allowed") # Accents are not allowed
                        break 

                    elif not letra.isalnum() and letra != " ":  # validate if the variable is a word or if there is a space
                        print("Special characters are not allowed")
                        break 
                else: # only execute if for continues
                     break # get out of the while
                
        # here validate and add the name autors           
        while True:       
                author = input("Add the author's names: ").lower() # store the name author and convert to lowercase     
                for letra in author:
                    if letra in "áéíóú": 
                        print("No se permiten tildes") # Accents are not allowed
                        break 

                    elif not letra.isalnum() and letra != " ":   # validate if the variable is a word or if there is a space
                        print("No se permiten caracteres especiales")
                        break 
                else: # only execute if for continues
                     break # get out of the while
        
        # here validate and add the category books 
        while True:       
                category = input("Add the book's categories: ").lower()  #store the category books and convert to lowercase   
                for letra in category:
                    if letra in "áéíóú": 
                        print("Accents are not allowed") # Accents are not allowed
                        break 

                    elif not letra.isalnum() and letra != " ":     # validate if the variable is a word or if there is a space
                        print("Special characters are not allowed")
                        break 
                else: # only execute if for continues
                     break # get out of the while
          
       # here validate and add the books price          
        while True:
            try:
                price = float(input("Add the book's price: "))  #store the price books and accept values with decimals          
                if price() > 0: # validate that numer is older than to zero
                    break                  
                else:
                    price = round(price,2) # only accept two decimals after dot 
            except ValueError:
                print("sonly numbers")

        while True:
            stock = input("Add to stock: ") # add to stock the books
            if stock.isdigit():  # verify that the number is an int           
                stock = int(stock) #convert to number to interger
                if stock > 0: # validate that numer is older than to zero                
                    break
                else:
                    print("---- El cantidad no puede ser negativo o 0 -----\n")
            else:
                print("ingresar numeros sin decimal")

        saveBooks(namebook,author,category,price,stock) # send to data to function savebooks 
        break

def saveBooks(namebook,author,category,price,stock): #receive to data and push to inventory
    book = { #data 
        "title" : namebook,
        "author" : author,
        "category" : category,
        "cost": price,
        "stock" : stock,
    }
    inventory.append(book) # save info in inventory
    print("\nbook saved successfully ") # message to successfully

def consultbooks():
    if not inventory: # is when the inventory is empty
          print("The inventory is empty.")
    else:
        #loop to inventory with enumrate for to get data and show in console
        for i,book in enumerate(inventory, start = 1):#enumerate recorre una lista y me devuelve su key-value -- :.2findica que solo muestre 2 valores despues del punto
            print(f"- Book number - {i}\n- the name's book is: {book['title']}\n- the author's book is: {book['author']}\n- the category book is: {book["category"]}\n- The book's price is: {book['cost']:.2f}\n- the book's Stock is: {book['stock'] }\n")
            
    #print("\n")


def updatebooks():
    try:
        # is when the inventory is empty
        if not inventory:
            print(" # * # * The inventory is empty * # * #")
        
        elif inventory: 
            # compares whether the option chosen by the user is equal to the key of the variable
            option= input("¿what do you do update? (¿title?/¿author?/¿category?/cost?/Stock?): ").lower()
            if option == "title":
                id_update = int(input("Choose the ID that you need update: ")) #choose the id variable to change   
                if 1 <= id_update <= len(inventory): # compare de ID to positión in inventory
                    newTitle = input("Add the title of a new book: ").lower()# request a new data
                    inventory[id_update - 1]['title'] = newTitle  # assign the new value
                    print("book saved successfully.")
                else:
                    print("Invalid product ID.") # is shown in case of error
                    
            if option == "author":
                id_update = int(input("Choose the ID that you need update: "))
                if 1 <= id_update <= len(inventory):
                    newAuthor = input("Add the author of a new book: ").lower()
                    inventory[id_update - 1]['author'] = newAuthor
                    print("book saved successfully.")
                else:
                    print("Invalid product ID.")

            if option == "category":
                id_update = int(input("Ingrese el ID del producto a actualizar: "))
                if 1 <= id_update <= len(inventory):
                    newCategory = input("Add the category of a new book: ").lower()
                    inventory[id_update - 1]['category'] = newCategory
                    print("book saved successfully.")
                else:
                    print("Invalid product ID.")
            if option == "cost":
                id_update = int(input("Choose the ID that you need update: "))
                if 1 <= id_update <= len(inventory):
                    newCost = float(input(" add the cost or price of a new book: "))
                    inventory[id_update - 1]['cost'] = newCost
                else:
                    print("Invalid product ID.")
            if option == "stock":
                id_update = int(input("Choose the ID that you need update: "))
                if 1 <= id_update <= len(inventory):
                    newCost = int(input(" add the cost or price of a new book: "))
                    inventory[id_update - 1]['stock'] = newCost
                else:
                    print("Invalid product ID.")

    except ValueError:
        print("Entrada inválida. Por favor ingrese un valor válido.") 


def deletebooks():

    try: 
        if not inventory:
            print(" # * # * The inventory is empty * # * #")
        else:
            consultbooks()

            deleteID = int(input("Choose the ID that you need delete: "))
            if 1 <= deleteID <= len(inventory):
                inventory.pop(deleteID- 1)  #Subtract or minus 1 to adjust to the list index
                print(" The book is deleted successfully.")
    except ValueError:
        print("Invalid ID number. Please enter a valid number.")


def addsales():
  

    try:
        # here validate and add the title books
        while True:       
                customer = input("Add to names to customer: ").lower() # store the name books and convert to lowercase              
                for letra in customer:
                    if letra in "áéíóú": 
                        print("Accents are not allowed") # Accents are not allowed
                        break 

                    elif not letra.isalnum() and letra != " ":  # validate if the variable is a word or if there is a space
                        print("Special characters are not allowed")
                        break 
                else: # only execute if for continues
                     break # get out of the while
                
        # here validate and add the name autors           
           
        while True:
            fecha_str = input("Introduce the date (YYYY-MM-DD): ")
            try:
                fecha_obj = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
                print("add date:", fecha_obj)
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")


        while True:
            quantity = input("Add to stock: ") # add to stock the books
            if quantity.isdigit():  # verify that the number is an int           
                quantity = int(quantity) #convert to number to interger
                if quantity > 0: # validate that numer is older than to zero                
                    break
                else:
                    print("---- El cantidad no puede ser negativo o 0 -----\n")
            else:
                print("ingresar numeros sin decimal")

        while True:
            discount = int(input("Add to discount: ")) # add to stock the books
            # verify that the number is an int           
                #convert to number to interger
            if discount > 0 and discount < 10: # validate that numer is older than to zero                
                 break
            else:
                 print("---- El cantidad no puede ser negativo o 0 -----\n")
           

            if quantity <= 0 or discount < 0:
                print("invalid values. ")
                return 

            if inventory["stock"] < quantity:
                print("Stock insuficiente.")
                return
            break

    
            
   
    # for i in inventory:   
    #     i["stock"] -= quantity

        savesCustomers(customer,quantity,discount,fecha_obj)
    except:
        print("Error: valores numéricos inválidos.")   
        

def savesCustomers(customer,quantity,discount,fecha_obj):


    user= {
      "client": customer,
      "title": inventory["title"].values(),
        "author": inventory["author"].values(),
        "quantity": quantity,
        "cost": inventory["cost"].values(),
        "discount": discount,
        "date" : fecha_obj
    }
    sales.append(user) # save info in inventory
    print("\nsales saved successfully ") # message to successfully


def reports():
    try:
        if not sales:
            print("Aún no hay ventas.")
            return
        counts = {}

        for sal in sales:
            book = sal["title"]
            counts[book] = counts.get(book, 0) + sal["quantity"]

        # for  i, sal in enumerate(sales, start=1):
        #     book = sal["title"]
        #     counts[i] = counts.get(book, 0) + sal["quantity"]

    
        sorted_books = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        for title, more in sorted_books[:3]:
            print(f"{title}: {more} vendidos")
        


     
    except ValueError:
        print("Error al calcular estadísticas. Por favor, verifique los datos del inventario.")
        




