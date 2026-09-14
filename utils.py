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


def print_documentation(doc_list=None):
    if doc_list is None:
        doc_list = documents
    for doc in doc_list:
        print(f"Title: {doc.get('title', 'Untitled')}")
        print(f"Content: {doc.get('content', '')}")
        print("-" * 40)
