from stanfordParser import sfParser
from question_classifier import quest_cl
from answer import get_answer
who_question="Who is Barack Obama?"
def main(question):
    parser=sfParser()
    parsed_iter=parser.raw_parse(question)

    for iter in parsed_iter:
        parsed_question=iter

    print("Q:%s"%question)

    query,key_value=quest_cl(parsed_question)
    if query!=None and key_value!=None:

        print("A:")
        get_answer(query,key_value)
        print("----------------------------")
        print()
    else:
        print("Haven't defined this kind of question. "
              "You can define it now!!!")
        print("----------------------------")
        print()

if __name__ == '__main__':
    print("For simplify problem, I only deal with 2 kind of question")
    print("1/Who-question\t2/Where-question")
    print("Example question: ")
    print("\tWho is Barack Obama?")
    print("\tWhere is Eiffel Tower?")
    print("\tWho is Bill Gate?")
    print("There will be more than 1 answer (may be duplicate) but they use for user selection")
    print("Where-question may not get a good result. Reason is NERtagger to tag LOCATION is not perfect now!")
    while(1):
            question=input()
            main(question)
