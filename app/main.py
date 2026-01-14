import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json", "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    shops = [Shop(s) for s in config["shops"]]
    customers = [Customer(c) for c in config["customers"]]

    for person in customers:
        print(f"{person.name} has {person.money} dollars")
        cheapest_shop = None
        min_cost = float("inf")

        for shop in shops:
            cost = person.calculate_trip_cost(shop, fuel_price)
            print(f"{person.name}'s trip to the {shop.name} "
                  f"costs {round(cost, 2)}")

            if cost < min_cost:
                min_cost = cost
                cheapest_shop = shop

        if cheapest_shop and person.money >= min_cost:
            print(f"{person.name} rides to {cheapest_shop.name}\n")

            # Update customer location to shop location upon arrival
            person.location = cheapest_shop.location

            person.print_receipt(cheapest_shop)
            person.money -= min_cost
            print(f"\n{person.name} rides home")
            print(f"{person.name} now has {round(person.money, 2)} dollars\n")
        else:
            print(f"{person.name} doesn't have enough money "
                  f"to make a purchase in any shop\n")
