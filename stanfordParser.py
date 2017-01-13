STANFORD_JAR="/home/dang/Desktop/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0.jar"
STANFORD_MODEL="/home/dang/Desktop/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0-models.jar"

from nltk.parse.stanford import StanfordParser

def sfParser(jar_path=STANFORD_JAR,model_path=STANFORD_MODEL):
    return StanfordParser(STANFORD_JAR,STANFORD_MODEL)