def main():
    total_sales_value = 0
    sales = float(input("Please enter sales: $"))
    while sales >= 0:
        sales = float(input("Please enter sales: $"))
        total_sales_value += sales
    if total_sales_value < 1000:
        sales_bonus = (total_sales_value * 0.1)
    else:
        sales_bonus = (total_sales_value * 0.5)
    print("Your sales bonus is $",sales_bonus)

main()