def get_context(vectorstore, query, k=3):
    matches = vectorstore.similarity_search(query, k=k)
    return "\n".join(doc.page_content for doc in matches)
