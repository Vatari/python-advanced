from collections import deque

food_qty = int(input())
order_qty = deque([int(s) for s in input().split()])
sum_orders = []
print(max(order_qty))
while order_qty:
    order = order_qty[0]
    if food_qty >= order:
        food_qty -= order_qty.popleft()
    else:
        order_qty = [str(o) for o in order_qty]
        print(f"Orders left: {' '.join(order_qty)}")
        break

if len(order_qty) == 0:
    print("Orders complete")
