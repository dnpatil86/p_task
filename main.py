from selenium import webdriver
import time
import json

path = "C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(path)


driver.get("https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1")



results = driver.find_elements_by_class_name("product")

mylist = []

for result in results:
    item = {}

    item["price"] = result.find_element_by_class_name("price").text
    item["title"] = result.find_element_by_class_name("catalog-item-name").text
    try:
        result.find_element_by_class_name("out-of-stock")
        item["stock"] = False
    except:
        item["stock"] = True
    item["maftr"] = result.find_element_by_class_name("catalog-item-brand").text

    mylist.append(item)
    ##print(item)

jsondata = json.dumps(mylist)
print (jsondata)

driver.close()
