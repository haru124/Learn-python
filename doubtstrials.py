

"""
def funca(a,d):
    x = [a,d]
    print(x)
    funcb(x,4,5)
    print(x)

def funcb(x,b,c):
    x.append(c)
    x.append(b)
    return x

funca(2,3)
"""
"""
a= {'list':[1,2,3,4,5,6,7,8,9], 'string':"abcdefghij",'words':"I am a psychopath/I always have this thought about killing people/I wish I could kill someone someday/Intro About Me/Hari"}
b = a['words'].split('/')[-3]
c = a['words'][-3]
print(b)
print(c)
print(type(c))

d = {'m':1,'m':2,'n':3}
def add(l,m,n, **kwargs):
    print(l+m+n)

add(**d)

import joblib
import numpy
EMBEDDINGS = joblib.load("embeddings.joblib")
print(type(EMBEDDINGS))
print(EMBEDDINGS.shape)

print(EMBEDDINGS)


text = "Get the desired field (if the key is missing an empty string should be used)"
print(text, type(text))
text = text.strip()
print(text, type(text))

def concatenate_fields(dataset, fields):
    # Initialize the list where the texts will be stored    
    concatenated_data = [] 

    # Iterate over movies
    for data in dataset:
        # Initialize text as an empty string
        text = "" 

        # Iterate over the fields
        for field in fields: 
            # Get the desired field (if the key is missing an empty string should be used)
            context = data.get(field, '')
            print(f"inside 2 loops context = {context}") 

            if context:
                # Add the context to the text (add an extra space so fields are separate)
                text += f"{context} " 
                print(f"inside 2 loops text = {repr(text)}")

        # Strip whitespaces from the text
        # Removes leading and trailing whitespace (spaces, tabs, newline characters)
        text = text.strip()[:493]
        print(f"\n\ninside 1 loop text = {repr(text)}")
        # Append the text with extra context to the list
        concatenated_data.append(text) 
    
    return concatenated_data

dataset = [
    {
        "title": "Inception",
        "description": "A thief who steals corporate secrets through dream-sharing technology.",
        "year": "2010",
        "director": "Christopher Nolan"
    },
    {
        "title": "The Matrix",
        "description": "A computer hacker learns about the true nature of reality and his role in the war against its controllers.",
        "year": "1999",
        # 'director' key missing on purpose to test data.get(field, '')
    },
    {
        "title": "Interstellar",
        "description": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "year": "2014",
        "director": "Christopher Nolan"
    }
]

fields = ["title", "description", "year", "director"]

result = concatenate_fields(dataset, fields)

for r in result:
    print(repr(r))
"""