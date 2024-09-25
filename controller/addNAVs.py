from .scrape import getNAVAndGrowth
from model.mutual_fund import getMutualFund
from model.NAV import insertNAV

def addNavs ():
    mutualfunds = getMutualFund()
    for mutualfund in mutualfunds:
        nav, growth = getNAVAndGrowth(mutualfund[1])
        if nav != '' and growth != '':
            nav = nav.replace('₹', '')
            growth = growth.replace('%', '')
            print(nav, growth)
            insertNAV(mutualfund[0], nav, growth)