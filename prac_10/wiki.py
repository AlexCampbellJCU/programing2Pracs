import wikipedia
search_request = input("What would you like to search?")
while search_request != " ":
    sr = wikipedia.page(search_request)
    print(sr.title)
    print(sr)
    print(sr.summary)
    print(sr.url)
    search_request = input("What would you like to search?")

