import  pyshorteners as pyshort

link_URL = input("Enter the URL: ")
shortener = pyshort.Shortener()
short_URL = shortener.tinyurl.short(link_URL)
print(f'The shortened URL is: {short_URL}')