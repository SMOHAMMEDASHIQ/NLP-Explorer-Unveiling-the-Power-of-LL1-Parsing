class InformationRetrieval:
    def __init__(self, documents):
        self.documents = documents

    def search(self, query):
        results = []
        for doc_id, doc_content in enumerate(self.documents):
            if query.lower() in doc_content.lower():
                results.append(doc_id)
        return results

# Example usage:
def main():
    # Input documents from the user
    num_documents = int(input("Enter the number of documents: "))
    documents = []
    for i in range(num_documents):
        document = input(f"Enter document {i+1}: ")
        documents.append(document)

    # Initialize InformationRetrieval object
    ir_system = InformationRetrieval(documents)

    # Perform search
    query = input("Enter your search query: ")
    search_results = ir_system.search(query)

    # Display search results
    if search_results:
        print("Search Results:")
        for result in search_results:
            print(f"Document {result}: {documents[result]}")
    else:
        print("No matching documents found.")

if __name__ == "__main__":
    main()
