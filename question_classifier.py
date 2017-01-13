
from stanfordNER import sfNER

def is_wh_question(parsed_question):
    if parsed_question[0].label()=="SBARQ":
        return True
    return False

from stanfordParser import sfParser

def is_who_question(parsed_question):
    if(parsed_question[0][0].leaves()[0].lower()=="who"):
        return True
    return False

def is_what_question(parsed_question):
    if(parsed_question[0][0].leaves()[0].lower()=="what"):
        return True
    return False

def is_where_question(parsed_question):
    if(parsed_question[0][0].leaves()[0].lower()=="where"):
        return True
    return False

def is_when_question(parsed_question):
    if(parsed_question[0][0].leaves()[0].lower()=="when"):
        return True
    return False

# Now we can specific different kind of questions:
def name_question(parsed_question):

    assert(is_who_question(parsed_question))
    # This part should check correct type of question
    raw_sent=parsed_question[0].leaves()
    ner_parser=sfNER()
    tagged_sent=ner_parser.tag(raw_sent)
    person_entity=[w for w,p in tagged_sent if p =="PERSON"]
    person_entity=" ".join(person_entity)
    def create_query(person_key):
        def filter_query(person_key):
            return "filter regex(?name,\""+person_key+"\",\"i\")."
        query="""
        prefix rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix foaf:<http://xmlns.com/foaf/0.1/>
        prefix rdfs:<http://www.w3.org/2000/01/rdf-schema#>
        select ?comment
        where{
            ?subject rdf:type foaf:Person.
            ?subject foaf:name ?name.
        """+"\t"+\
              filter_query(person_key)+\
        """
            ?subject rdfs:comment ?comment.
        }
        limit 10
        """
        return query
    query=create_query(person_entity)
    return (query,"comment")

def location_question(parsed_question):
    # This part should check correct type of question
    # Problem with type where question is choose the right part that most of object have
    # Example:
    # 1/ .Where is Eiffel Tower?
    #    .Where is Giza?
    #    .Where is Liberty Statue?
    #    .Where is Great Wall?
    #    .Where is Brooklyn Bridge?
    # All of them should have a same unit to return: a country may be the best choice
    # However, not all of them have country attribute: Eiffel Tower, Liberty Statue have location attribute,
    # but Giza, Great Wall have country attribute,...
    # Difficulty here is how to get a mutual query to get information for both of them, or know how to group them into
    # some specific group have similar structure

    # But another elegant solution: UNION operator
    # https://jena.apache.org/tutorials/sparql_union.html

    raw_sent = parsed_question[0].leaves()
    ner_parser = sfNER()
    tagged_sent = ner_parser.tag(raw_sent)
    location_entity = [w for w, p in tagged_sent if p != "O"]
    location_entity = " ".join(location_entity)

    def create_query(location_key):
        def filter_query(location_key):
            return "filter regex(?name,\"" + location_key + "\",\"i\")."

        query = """
            prefix rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            prefix dbo:<http://dbpedia.org/ontology/>
            prefix rdfs:<http://www.w3.org/2000/01/rdf-schema#>
                select ?location
            where
            {
            ?subject rdf:type dbo:Place.

            ?subject rdfs:label ?name.
                {
                ?subject dbo:location ?location_uri.
                ?location_uri rdfs:label ?location.}
                UNION{
                ?subject dbo:country ?country.
                ?country rdfs:label ?location
                }
            """  + \
                filter_query(location_key) + \
                """
            }
            limit 20
            """
        return query

    query = create_query(location_entity)
    return (query, "location")


def quest_cl(parsed_question):
    if(is_who_question(parsed_question)):
        query,key=name_question(parsed_question)
        return (query,key)
    if (is_where_question(parsed_question)):
        query,key=location_question(parsed_question)
        return (query, key)
    return (None,None)
    # You can build more interesting questions, as many as you like, as long
    # as you can understand how to get information by SPARQL :)
