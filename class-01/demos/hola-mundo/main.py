def hello(subject="world", query=None):

    print('value of query', query)

    query = "How are you?"

    print(f"hello {subject}, {query}")


hello(query = "What's the story morning glory")
