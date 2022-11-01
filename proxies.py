from Proxy_List_Scrapper import ALL, Scrapper

scrapper = Scrapper(category=ALL, print_err_trace=True)
data = scrapper.getProxies()

print("Scrapped Proxies:")
for item in data.proxies:
    print(f'{item.ip}:{item.port}')

print("Total Proxies")
print(data.len)

print("Category of the Proxy")
print(data.category)

