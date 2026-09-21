buts = {}
buts["Giroud"] = 53
buts["Benzema"] = 37
buts["Henry"] = 51
buts["Griezmann"] = 43
buts["Mbappé"] = 38
print(buts.items())
print(len(buts.keys()))
print(buts["Griezmann"])
if "kanté" in buts.keys():
    print("ok")

buts["Mbappé"] += 1
print(buts.values())
buts.pop["Henry"]
buts["babouche"] = 0