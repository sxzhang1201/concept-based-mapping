from rdflib.graph import Graph
import os


def execute():

    # Load the synthetic data to be queried
    g = Graph().parse(os.getcwd() + '/proof-of-concept/dummy_case.ttl')

    dict_sparql = {
        'sex': os.getcwd() + '/proof-of-concept/sparql/get_sex.txt',
        'gender': os.getcwd() + '/proof-of-concept/sparql/get_gender.txt',
        'male': os.getcwd() + '/proof-of-concept/sparql/get_male.txt',
        'sex_male': os.getcwd() + '/proof-of-concept/sparql/get_sex_male.txt',
        'sex_female': os.getcwd() + '/proof-of-concept/sparql/get_sex_female.txt',
        'biological_sex': os.getcwd() + '/proof-of-concept/sparql/get_biological_Sex.txt',
        'distribution': os.getcwd() + '/proof-of-concept/sparql/get_distribution.txt'
    }

    use_cases = ['distribution']

    # use_cases = [
    #     'sex', 'gender', 'male', 'sex_male', 'sex_female', 'biological_sex'
    # ]

    for use_case in use_cases:
        print("\nUse case: {}".format(use_case))

        with open(dict_sparql[use_case], 'r') as file:
            use_case_query = file.read()

        q_res = g.query(use_case_query)

        print("Query results - {} rows: ".format(len(q_res)))

        for row in q_res:
            
            for element in row:
                print(element, end=' ')
            print('')


if __name__ == '__main__':
    execute()
