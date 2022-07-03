import bisect

def maximumBeauty(items, queries):
    items = sorted(items + [[0,0]])
    prices = [item[0] for item in items]
    min_price = min(prices[1:])
    for i in range(1, len(items)):
        items[i][1] = max(items[i][1], items[i - 1][1])
    output = [items[bisect.bisect_right(prices, query) - 1][1] if query >= min_price else 0 for query in queries]
    return output


items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]
# items = [[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]]
# queries= [885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584]
print(maximumBeauty(items, queries))