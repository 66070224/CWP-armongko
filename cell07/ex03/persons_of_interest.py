#!/usr/bin/env python3

def famous_births(val: dict[str, dict[str,str]]):
    result = [f"{person.get("name")} is a great scientist born in {person.get("date_of_birth")}." for person in val.values()]
    for res in sorted(result, key=lambda x: int(x[-5:-1:])):
        print(res)

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
