def game():
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
    noun3 = input("Enter a noun: ")
    adj = input("Enter an adjective:")
    print(
        f"Once upon a time there were three friends, their names were {noun1}, {noun2} and {noun3}. {noun1} suggested "
        f"to go on a vacation. Everyone was happy and agreed to go to the beach next Sunday. \nThe dress code for the "
        f"vacation was you must wear something {adj}. {noun2} didn't have something {adj} to wear then {noun2} went "
        f"for shopping with {noun3} they got something so {adj}.It was Sunday! They all went to beach wearing "
        f"something {adj}. \nThey enjoyed playing with the ball in the beach. The police came chasing a thief who was "
        f"wearing something {adj}.The thief escaped from the beach while the police was surprised to see three people "
        f"wearing something {adj} and\n started questioning them. Then {noun1} explained to them how they planned "
        f"their vacation with theme {adj}. The police was convinced with {noun1}'s story and let them go and the "
        f"police went ahead finding the thief. The three friends {noun1}, {noun2} and {noun3} laughed at how they got "
        f"caught with the police with their dresscode {adj}.")

    userinput = input("Do you want to play again \n\t 1 for Yes or 2 for No ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
    noun3 = input("Enter a noun: ")
    adj = input("Enter an adjective:")
    if userinput.strip() == "1":
        print()
    else:
        return

    print(
        f"Once upon a time there was {noun1}, {noun2} and {noun3}. They were homeless but one day, they found a "
        f"house. They went in the house, it seemed abandoned."
        f"{noun2} had an idea, his idea was to live in the house. \nThey agreed with his idea. They tried all the "
        f"things the house, they were all perfect but the beds were not. "
        f"{noun1}'s bed was so less {adj}, {noun2}'s bed was too {adj} but {noun3}'s bed was the right {adj}."
        f"\nThen {noun3} agreed to make their beds perfect with things around the house,they accepted. After a while "
        f"their beds were perfect. They lived happily ever after.")


game()
