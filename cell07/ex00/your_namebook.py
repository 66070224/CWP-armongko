#!/usr/bin/env python3

def array_of_names(val: dict[str, str]):
    return [f"{k[0].upper()}{k[1::]} {v[0].upper()}{v[1::]}" for k, v in val.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
