hours_worked = float(input("Hours worked: "))

ot_hours = hours_worked - 40
straight_pay = 15.00 #this is a constant.
overtime_rate = straight_pay * 1.5
after_tax = 0.75 #35% removed for taxes, etc., conservative result

if ot_hours < 0:
  net_pay = ((straight_pay * 40) + (ot_hours * overtime_rate)) * after_tax
else:
  net_pay = (straight_pay * hours_worked) * after_tax

print('$%.2f' % net_pay )
