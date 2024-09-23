guests=["deva","dinesh","ragav","vakis"]
print(len(guests))
guests.sort(reverse=True)
print(guests)
guests.reverse()
print(guests)
for i in guests:
    print(f'hello,{i} u r welcome')
    
es="deva"
print(f"\nunfortunately,{es} unable to attend our party")
abc=guests.pop(0)

bcd=guests.append("kharthic")
print("\nsecond set of invitation\n")
for i in guests:
    print(f'hello,{i} u r welcome')
guests.insert(2,"deva")

del guests[1]
guests.remove("vakis")
print(guests)
