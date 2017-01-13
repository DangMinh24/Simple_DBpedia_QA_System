from nltk.tag.stanford import StanfordNERTagger

STANFORD_NER_CLF="/home/dang/Desktop/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz"
STANFORD_JAR="/home/dang/Desktop/stanford-ner-2015-12-09/stanford-ner.jar"
def sfNER(jar_path=STANFORD_JAR,clf_path=STANFORD_NER_CLF):
    return StanfordNERTagger(STANFORD_NER_CLF,STANFORD_JAR)
