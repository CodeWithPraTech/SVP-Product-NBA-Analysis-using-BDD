from dd.autoref import BDD

def bdd_product(bdds):
    # Start with the true BDD as the base
    product_bdd = bdds[0]
    
    # AND all BDDs together
    for i in range(1, len(bdds)):
        product_bdd &= bdds[i]
    
    return product_bdd 

