# Simple_DBpedia_QA_System

# What is DBpedia?

  -If we want to find information about something, we can search on Wikipedia. Wikipedia's structure contains pages, paragraphs, and links. So it simply contains raw text and links.

  -However, people find that there are lots of connections we can get rather than connection between 2 raw linguistic documents. So they try to make information in Wikipedia more speciffic,realistic as possible
  
  -DBpedia is based on that idea, and now has become a valuable resource for many semantic analysis.
  
  -DBpedia is save as RDF(Resource Description Framework) format. It is simply a network with a lot of graphs which connect together by a speciffic relations.(To know more about RDF: https://jena.apache.org/tutorials/rdf_api.html )
  
  -RDF uses SPARQL to query information in network. Like Tables uses SQL to query, RDF uses SPARQL to query.(To know how to use SPARQL: https://jena.apache.org/tutorials/sparql.html)
 
#Idea:
  
  -QA system using raw paragraphs( documents or raw text) has a lot of difficulties:
  
   .Have to make computer understand a question, which means you have to know: question anlysis, represent semantic meaning (semantic parsing, which is now an young field in NLP), extract key values( etc NER,...), extract correct reference to get answer,...
    
   .Have to make computer answer the question: represent semantic meaning of each sentence(or linguistic unit) in reference
Extract correct answer for the question( who-question's answer should be PERSON,etc...)

   ....
    
  -Instead of trying to represent meaning perfectly, we can use DBpedia as knowledge base to represent all that meaning and relations. So that we can make computer can answer lots of different question (wh-question, binary question, and any kind of question you want as long as you know the basic idea how to use DBpedia)

*To run this code :*

  1/ Download [StanfordNER](http://nlp.stanford.edu/software/CRF-NER.html): We use this tagger to express key words to query

  2/ Download [StanfordParser/StanfordCoreNLP](http://stanfordnlp.github.io/CoreNLP/): You can choose any of two. Using this parser
  to parse a syntactic structure of raw sentence. So I can discriminate and analysis different kind of questions

  3/ Change your location of STANFORD_NER, STANFORD_JAR, STANFORD_MODEL in 2 file stanfordNER.py and stanfordParser.py
  [ref](http://textminingonline.com/how-to-use-stanford-named-entity-recognizer-ner-in-python-nltk-and-other-programming-languages)

  4/ You can easily create a new kind of question.

#Advantages and Disadvantages of this method:

   Pros:Once you understand how to save, connect, query data in RDF, you can create a "DBpedia" of your own. And it much
     easier for you to extract knowledge. Easily update. And really friendly with human environment (there are a lot of concept in real world!!)

   Cons:Still use a lot of syntactic structure to create a question and answer. Cost a lot of time to create a knowledge base
   like DBpedia. And it still have lots of difficulties in inference (Who is 1st President of USA?).

#Further:

   Instead of manually creating question structure and answer structure, it's very ideal if you can find a way to represent semantic meaning
