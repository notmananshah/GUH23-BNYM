apple = 2.45
cake = 8
milk = 1


def printing_statements():
    print("Hello, welcome to the grocery calculator. The store offers apples, milk, and cake.")
    print("Please enter what you would like. First, write the item you want to buy, then write the amount in grams, ml, or quantity.")


    price = 0
    x = 0
    while x <= 15:
        print(x)
        st2 = input("Enter the item (milk, cake, apple) or type 'done' to finish: ").lower()
        if st2 == "done":
            break
        st3 = int(input("Enter the amount: "))
        if st2 == "milk":
            price += milk * st3
        elif st2 == "cake":
            price += cake * st3
        elif st2 == "apple":
            price += apple * st3
        else:
            print("You have entered something incorrect. Please try again.")
            continue


        x += st3
        num = 15 - x
        print(f"You have {num} items left to buy and your total price so far is ${price:.2f}")


    print("Sorry, your basket is full as you have reached 15 items. The total price for your groceries today is ${:.2f}".format(price))


printing_statements()