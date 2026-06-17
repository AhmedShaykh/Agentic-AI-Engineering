from langchain_community.document_loaders import TextLoader;

data = TextLoader("rag/docs/notes.txt");

docs = data.load();

print(docs);

print(docs[0].page_content);

print("Docs Length: ", len(docs)); # List Length Its Always 1