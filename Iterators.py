import hashlib
import wikipediaapi
import json

json_file = "countries.json"
country_link = 'country_links.txt'
url = 'https://en.wikipedia.org/wiki/'

class country_url():

    def __init__(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            countries = json.load(file)
            countries_name = (country['name']['common'] for country in countries)
            self.countries_name_iter = iter(countries_name)
            self.wiki = wikipediaapi.Wikipedia('en')

    def __iter__(self):
        return self

    def __next__(self):
        country_name = next(self.countries_name_iter)
        country_page = self.wiki.page(country_name)
        link = country_page.fullurl
        result = f'{country_name} - {link}'
        return result


if __name__=='__main__':
    # for c in country_url(json_file):
    #     print(c)
    with open(country_link, 'w', encoding='utf-8') as file:
        for country in country_url(json_file):
            file.write(f'{country}\n')
            print(hashlib.md5(country.encode()).hexdigest())
        print('Файл country_links.txt записан')




