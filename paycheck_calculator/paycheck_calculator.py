hours_worked = float(input("Hours worked: "))

ot_hours = hours_worked - 40
straight_pay = 19.95 #this is a constant.
overtime_rate = straight_pay * 1.5
after_tax = 0.65 #35% removed for taxes, etc., conservative result

net_pay = ((straight_pay * 40) + (ot_hours * overtime_rate)) * after_tax

print('$%.2f' % net_pay )
