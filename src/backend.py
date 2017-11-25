import sys
import random

category_tree = { "transportation":{"uber":{}, "parking":{}, "MetroCard":{}, "Auto":{"Lease":{}, "Insurance":{}, "Repairs":{}}}, "Housing":{"Rent":{}}, "Groceries":{"FreshDirect":{}, "Supermarket":{}, "Cosco":{}}, "Financial":{"Fees":{}, "Penalties":{}, "Transfers":{}, "ATMWithdrawals":{}}}

def traversal(a_tree):
    if  len(a_tree.keys())>0:
        for x in a_tree:
            yield x
            for y in traversal(a_tree[x]):            
                yield x+"-"+y
        

def load_user(uid,month):
    results=traversal(category_tree)
    new_results=[result.lower()+","+str(random.randint(100,200)) for result in results]
    counter={}
    for result in new_results:
        parts=result.split(",")
        count=int(parts[1])
        for cate in parts[0].split("-"):
            if cate not in counter:
                counter[cate]=0
            counter[cate]+=count
    new_results2=[]
    for result in new_results:
        a=result.split(",")
        new_results2.append(a[0]+"-end"+","+str(counter[a[0].split("-")[-1]]))
        
    return new_results2


def forecast_user(uid,month):
    results=["date\tassets\tliabilities\tnetworth"]
    date=20170101
    assets=3000
    liabilities=200
    for i in range(60):
        results.append(str(date)+"\t"+str(assets)+"\t"+str(liabilities)+"\t"+str(assets-liabilities))
        assets+=random.randint(-100,200)
        liabilities+=random.randint(-100,200)
    return results



def main():
    #print load_user('a','b')
    print forecast_user('a','b')


if __name__== "__main__":
    main()
    
