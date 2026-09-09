documents = [
    {
        "title": "Python Basics",
        "content": "Python is a beginner-friendly programming language used for automation, web development, data analysis, and AI.",
    },
    {
        "title": "LLM APIs",
        "content": "Large language models can be accessed through APIs for tasks like summarization, chat, and structured generation.",
    },
    {
        "title": "RAG",
        "content": "Retrieval-Augmented Generation combines search over documents with a language model to answer grounded questions.",
    },
]


def print_documentation():
    for doc in documents:
        print("Title:", doc["title"])
        print("Content:", doc["content"])
        print()

def helloWorld():
    print("Hello, World!")
    word = "Hello, World!"
    word[5]

print_documentation()
helloWorld()