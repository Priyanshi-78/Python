# Clean 10 customer names
customer_names = [
    "  John Doe  ",
    "  Jane Smith  ",
    "  Bob Johnson  ",
    "  Alice Brown  ",
    "  Charlie Davis  ",
    "  Diana Wilson  ",
    "  Edward Taylor  ",
    "  Fiona Anderson  ",
    "  George Thomas  ",
    "  Hannah Martinez  "
]
for name in customer_names:
#strip(): Removes all the Extra spaces
#title() → converts the first letter of each word to uppercase 
    clean_customer = name.strip().title()
    print(clean_customer)