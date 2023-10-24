from lxml import html
import requests
 
url=f'https://ebank.mbbank.com.vn/cp/pl/login?returnUrl=%2F'

resp= requests.get(url)

print(resp)
 
tree = html.fromstring(resp.content)

print(tree)
 
elements = tree.xpath('//*[@id="main-content"]/mbb-welcome/div/div/div[2]/div[2]/div/mbb-login/form/div/div[2]/mbb-word-captcha/div/div[2]/div/div/img')

print(elements)
 
# base_url = “https://en.wikipedia.org"
 
links = [element.attrib['src'] for element in elements]
 
print(links)