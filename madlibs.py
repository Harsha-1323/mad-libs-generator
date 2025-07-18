import random

TEMPLATES = [
    "Once upon a time in {place}, there was a {adjective} {noun} who loved to {verb} with {person}.",
    "{person} always said that the best way to {verb} a {noun} is in {place} while being {adjective}.",
    "In the middle of {place}, a {adjective} {noun} was trying to {verb} with help from {person}."
]

def generate_story(words):
    template = random.choice(TEMPLATES)
    return template.format(**words)

