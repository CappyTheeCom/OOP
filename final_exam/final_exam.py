#Question 1 
class solution:
    def __init__(self, item, price,quanity):
        self.item = item 
        self.price = price 
        self.quanity = quanity

    def print_order(orders):
        print(f'{"ITEM":<11}{"COUNT":^16}{"COST":>10}{"TOTAL":>15}')
        sub_total = 0
        for order in orders:
            total = order.quanity * order.price
            sub_total += total
            tax = sub_total * 0.11
            print(f'{order.item:<11}{order.quanity:^16}{order.price:>10.2f}{+total:>15.2f}')

        print(f"${sub_total} {tax:.2f}")
        


user_order = [solution("Notebook",3,2.65),
              solution("Pen",5,1.20),
              solution("Eraser",4,0.59),
              solution("Highlighter",2,1.75)]

solution.print_order(user_order)

