from constants import *
from function import *
import json

def login_user(username,password,admin_flag):
    flag = False
    data = read_json_details(user_list_json)
    for item in data:
        if item["username"] == username and item["password"] == password and item["flag"] == admin_flag:
            flag=True
    return flag

def welcome_page_func(choice):
    match choice:
        case '1':
            username = input(enter_username)
            password = input(enter_password)
            if login_user(username,password,"False"):
                while True:
                    print(welcome_user_page)
                    user_choice= input(enter_choice)
                    if welcome_user_page_function(user_choice):
                        break 
            else : 
                print(user_login_failed)

        case '2':
            username = input(enter_admin_username)
            password = input(enter_admin_password)
            if login_user(username,password,"True"):
                while True:
                    print(welcome_admin_page)
                    user_choice= input(enter_choice)
                    if welcome_admin_page_function(user_choice):
                        break 
            else: 
                print(admin_login_failed)
        case '3':
            print(thank_message)
            exit()
        case _:
            print(invalid_choice)

def welcome_user_page_function(choice):
    flag=False
    match choice:
        case '1':
            show_category_list_json()
            show_product_list_json()
        case '2':
            show_cart_list_json()
        case '3':
            show_product_list_json()
            id = int(input(add_cart))
            add_item_cart(id)
        case '4':
            show_cart_list_json()
            id = int(input(delete_cart))
            remove_item_cart(id)
        case '5':
            empty_cart()
        case '6':
            data = read_json_details(cart_list_json)
            if len(data) > 0:
                show_cart_list_json()
                make_payment(data)
            else:
                show_cart_list_json()
        case '7':
            print(thank_message)
            flag=True
        case _:
            print(invalid_choice)
    return flag

def welcome_admin_page_function(choice):
    flag=False
    match choice:
        case '1':
            show_category_list_json()
            show_product_list_json()
        case '2':
            show_product_list_json()
            add_product()
        case '3':
            show_product_list_json()
            id=int(input(enter_product_id_remove))
            remove_product(id)
        case '4':
            show_category_list_json()
            add_category()
        case '5':
            show_category_list_json()
            id=int(input(enter_category_id_remove))
            remove_category(id)
        case '6':
            print(thank_message)
            flag=True
        case _:
            print(invalid_choice)
    return flag

def show_category_list_json():
    print('\n',category_list,'\n')
    data = read_json_details(category_list_json)
    for item in data:
        print(f'{item["category_id"]}. {item["category_name"]}')

def show_product_list_json():
    print('\n',product_list,'\n')
    data = read_json_details(product_list_json)
    for item in data:
        print(f'{item["product_id"]}. {item["product_name"]} => Category Id : {item["category_id"]} => Price : Rs. {item["product_price"]}')

def show_cart_list_json():
    data = read_json_details(cart_list_json)
    if len(data) == 0:
        print(empty_cart_message)
    else :
        for x in data:
            print(x)

def read_json_details(file_name):
    input_file_name=file_name
    with open(input_file_name, 'r') as file:
        data = json.load(file)
    return data

def write_json_details(data,file_name):
    with open(file_name, 'w') as file:
         json.dump(data, file, indent=4)

def get_product_list_json():
    print('\n',product_list,'\n')
    data = read_json_details(product_list_json)
    return data

def add_item_cart(id):
    data = get_product_list_json()
    cart = read_json_details(cart_list_json)
    for temp in data:
        if temp["product_id"]==id:
            cart.append(temp)
            break
    write_json_details(cart,cart_list_json)
    print(add_product_to_cart)
    show_cart_list_json()

def remove_item_cart(id):
    data = show_cart_list_json()
    cart=read_json_details(cart_list_json)
    for temp in cart:
        if temp["product_id"]==id:
            cart.remove(temp)
            break
    write_json_details(cart,cart_list_json)
    print(remove_product_from_cart)
    show_cart_list_json()

def add_product():
    product = read_json_details(product_list_json)
    id=len(product)+1
    name=input(enter_product_name)
    category=int(input(enter_category_id))
    price=int(input(enter_product_price))
    product_disct={
        "product_id":id,
        "product_name":name,
        "category_id":category,
        "product_price":price
        }
    product.append(product_disct)
    write_json_details(product,product_list_json)
    print(add_product_message)
    show_product_list_json()

def remove_product(id):
    data = get_product_list_json()
    for item in data:
        if item["product_id"]==id:
            data.remove(item)
            break
    write_json_details(data,product_list_json)
    print(remove_product_message)
    show_product_list_json()

def empty_cart():
    data = get_product_list_json()
    cart = read_json_details(cart_list_json)
    cart.clear()
    write_json_details(cart,cart_list_json)
    show_cart_list_json()

def pay_cart():
    data = get_product_list_json()
    cart = read_json_details(cart_list_json)
    cart.clear()
    write_json_details(cart,cart_list_json)

def get_category_list_json():
    print('\n',category_list,'\n')
    data = read_json_details(category_list_json)
    return data

def add_category():
    category = read_json_details(category_list_json)
    id=len(category)+1
    name=input(enter_category_name)
    category_disct={
        "category_id":id,
        "category_name":name
        }
    category.append(category_disct)
    write_json_details(category,category_list_json)
    print(add_category_message)
    show_category_list_json()

def remove_category(id):
    data = get_category_list_json()
    for item in data:
        if item["category_id"]==id:
            data.remove(item)
            break
    write_json_details(data,category_list_json)
    print(remove_category_message)
    show_category_list_json()

def make_payment(data):
    total=0
    for temp in data:
        total+=temp["product_price"]
    print(total_amount_cart,total)
    print(payment_options)
    choice = input(payment_input_message)
    match choice:
        case "1":
            card_number=input(card_no)
            valid_till_month=input(valid_till_month)
            valid_till_year=input(valid_till_year)
            cvv=input(cvv_no)
            print(payment_inprogress)
            print(card_payment,f"{card_number[-3:]}")
            print(payed_amount,total)
            pay_cart()
            print(payment_success)
        case "2":
            name=input(bank_username)
            password=input(bank_password)
            print(payment_inprogress)
            print(net_banking_payment,name)
            print(payed_amount,total)
            pay_cart()
            print(payment_success)
        case "3":
            upi_id=input(upi_id)
            print(payment_inprogress)
            print(upi_payment,upi_id)
            print(payed_amount,total)
            pay_cart()
            print(payment_success)
        case "4":
            ppl_username=input(ppl_username)
            ppl_password=input(ppl_password)
            print(payment_inprogress)
            print(paypal_payment,ppl_username)
            print(payed_amount,total)
            pay_cart()
            print(payment_success)
        case "5":
            print(payment_cancelled)
        case "_":
            print(invalid_choice)
