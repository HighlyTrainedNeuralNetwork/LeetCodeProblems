# Solution required more efficient method of trying weights than my initial naive increment.

def shipWithinDays(weights, days):
        l = max(weights)
        r = sum(weights)
        while l < r:
            bound = (l + r) // 2
            packages = 1
            package = 0
            for weight in weights:
                if package + weight > bound:
                    package = 0
                    packages += 1
                package += weight
            if packages > days:
                l = bound + 1
            else:
                r = bound
        return l

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(shipWithinDays(weights, days))

