from SPARQLWrapper import SPARQLWrapper,JSON
def get_answer(query,extract_part):
    assert(query!=None and extract_part!=None)

    sparql=SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON )
    sparql.setQuery(query)

    results=sparql.query().convert()
    case_flag=True
    for result in results["results"]["bindings"]:
        if result[extract_part]["xml:lang"]=="en":
            case_flag=False
            print(result[extract_part]["value"])
    if case_flag==True:
        print("I don't know")
