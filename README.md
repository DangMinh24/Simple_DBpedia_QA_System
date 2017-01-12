# Simple_DBpedia_QA_System

What is DBpedia?

  -If we want to find information about something, we can search on Wikipedia. Wikipedia's structure contains pages, paragraphs, and links. So it simply contains raw text and links.

  -However, people find that there are lots of connections we can get rather than connection between 2 raw linguistic documents. So they try to make information in Wikipedia more speciffic,realistic as possible
  
  -DBpedia is based on that idea, and now has become a valuable resource for many semantic analysis.
  
  -DBpedia is save as RDF(Resource Description Framework) format. It is simply a network with a lot of graphs which connect together by a speciffic relations.(To know more about RDF: https://jena.apache.org/tutorials/rdf_api.html )
  
  -RDF uses SPARQL to query information in network. Like Tables uses SQL to query, RDF uses SPARQL to query.(To know how to use SPARQL: https://jena.apache.org/tutorials/sparql.html)
 
Idea:
  
  -QA system using raw paragraphs( documents or raw text) has a lot of difficulties:
  
    .Have to make computer understand a question, which means you have to know: question anlysis, represent semantic meaning (semantic parsing, which is now an young field in NLP), extract key values( etc NER,...), extract correct reference to get answer,...
    
    .Have to make computer answer the question: represent semantic meaning of each sentence(or linguistic unit) in reference
Extract correct answer for the question( who-question's answer should be PERSON,etc...)
    
    ....
    
  -Instead of trying to represent meaning perfectly, we can use DBpedia as knowledge base to represent all that meaning and relations. So that we can make computer can answer lots of different question (wh-question, binary question, and any kind of question you want as long as you know the basic idea how to use DBpedia)

In this 
