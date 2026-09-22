#!/usr/bin/env python3

def find_the_redheads(val: dict[str, str]):
    return [k for k, v in val.items() if v == "red"]

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))
