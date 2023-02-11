chicken_gom, pizza_gom, burger_gom = map(int, input().split())
chicken_ticket, pizza_ticket, burger_ticket = map(int, input().split())

ate = 0
for i in range(3):
    chicken = min(chicken_gom, chicken_ticket)
    ate += chicken
    chicken_gom -= chicken
    chicken_ticket -= chicken

    pizza = min(pizza_gom, pizza_ticket)
    ate += pizza
    pizza_gom -= pizza
    pizza_ticket -= pizza

    burger = min(burger_gom, burger_ticket)
    ate += burger
    burger_gom -= burger
    burger_ticket -= burger

    new_chicken = burger_ticket // 3
    new_pizza = chicken_ticket // 3
    new_burger = pizza_ticket // 3

    chicken_ticket = new_chicken
    pizza_ticket = new_pizza
    burger_ticket = new_burger

print(ate)
