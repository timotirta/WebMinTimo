import whoosh.index as index
from whoosh.qparser import QueryParser

ix = index.open_dir("index")

with ix.searcher() as searcher:
    q = QueryParser("content", schema=ix.schema).parse("csharp")
    results = searcher.search(q)
    for x in results:
        print(x["title"])

