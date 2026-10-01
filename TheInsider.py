print(f"--------------------------------------------------------------------------")
print(f"                         💱THE INSIDER💱                                 ")
print(f"--------------------------------------------------------------------------")
Groceries = int(input("How much have you spent on Groceries: "))
Rent = int(input("How much have you spent on Rent: "))
Crypto = int(input("How much have you spent on Crypto: "))
Fun = int(input("How much have you spent on Fun: "))
print(f"----------------------------💲💲💲💲💲----------------------------------")

Groceries_items = ['Waygu Steak','Lamb Cops','Pack of Ribs','Foreign Spices']
Rent_duties = ['Real Estate','Bonds','Nyc Penthouse','Camps Bay Condo']
Crypto_jobs = ['S&P500','','Nasdaq 100', 'Apple']
Fun_ = ['Alchohol','Entertainment','Congress dinner','Buyer Golf Meetings','Thursday Compulsory Dinners']

if (Groceries > 5000):
    print("---------------------------------------------------------------------------")
    print(f"WARNING⚠️: You are spending too much money on Groceries " "Total: {Groceries}")
    print("---------------------------------------------------------------------------")
    print(f"Cutdown on spending on one of these items: {Groceries_items}")
    print("---------------------------------------------------------------------------")
if (Rent > 5000):
    print("---------------------------------------------------------------------------")
    print(f"WARNING⚠️: You are spending too much money on Rent" "Total: {Rent}")
    print("---------------------------------------------------------------------------")
    print(f"Cutdown on spending on one of these properties: {Rent_duties}")
    print("---------------------------------------------------------------------------")
if (Crypto > 5000):
    print("---------------------------------------------------------------------------")
    print(f"WARNING⚠️: You are spending too much money on Crypto " "Total {Crypto}")
    print("---------------------------------------------------------------------------")
    print(f"Structure spending on one of these investments: {Crypto_jobs}")
    print("---------------------------------------------------------------------------")
if (Fun > 5000):
    print("---------------------------------------------------------------------------")
    print(f"WARNING⚠️: You are spending too much money on Fun " "Total {Fun}")
    print("---------------------------------------------------------------------------")
    print(f"Cutdown on spending on fun in one of these departments: {Fun_}")
    print("---------------------------------------------------------------------------")
    