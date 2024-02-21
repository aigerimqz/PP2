import json
with open("sample-data.json") as sample:
    data = json.load(sample)

x = json.dumps(data, indent=4)
print("Interface Status")
print("="*75)
print("DN" + " "*49 + "Description" + " "*11 + "Speed" + " "*4 + "MTU")
print("-"*50 + " " + "-"*20 + " "*2 + "-"*6 + " "*2 + "-"*6)
for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    descrp = item["l1PhysIf"]["attributes"]["descr"]
    speed = item["l1PhysIf"]["attributes"]["speed"]
    mtu = item["l1PhysIf"]["attributes"]["mtu"]

    print(dn + " "*29 + descrp, speed, " ", mtu)