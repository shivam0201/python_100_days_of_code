next=True
bidders={}
high=0
winner=""
while next==True:
    next=False
    name=input("Enter the name of bidder\n")
    bid=int(input("Enter the bidding amount\n"))
    if bid>high:
        winner=name
        bid=high
    bidders[name]=bid
    more=input("More bidders?\n")
    if more.lower()=="yes":
       next=True

print(f"The winner is {winner} with a bid of {bidders[winner]}")

