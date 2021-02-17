import requests
from PIL import Image, ImageDraw, ImageFont
# api-endpoint
URL = "https://benbotfn.tk/api/v1/newCosmetics"
r = requests.get(url=URL)
if r.status_code == 200:
    print(r.status_code)
    data = r.json()
    newCosmetics = data['items']
    currentVersion = data['currentVersion']
    print("Version : "+currentVersion)
    shouldFetch = input("fetch data[y/n]")
    if shouldFetch == "yes" or shouldFetch == "y":
        for cosmetic in newCosmetics:
            cosmeticPath = cosmetic['path']
            cosmeticName = cosmetic['id']
            cosmeticFileName = "assets/" + cosmeticName + ".png"
            assetsUrl = f"""https://benbotfn.tk/api/v1/exportAsset?path={cosmeticPath}&lang=en&noVariants=true&rawIcon=false"""
            r = requests.get(assetsUrl, allow_redirects=True)
            open(cosmeticFileName, 'wb').write(r.content)
            print("saved ", cosmeticName)
    elif shouldFetch == "no" or shouldFetch == "n":
        print("error code 0")

    else:
        print("Version : " + currentVersion)
        shouldFetch = input("fetch data?[y/n]")

