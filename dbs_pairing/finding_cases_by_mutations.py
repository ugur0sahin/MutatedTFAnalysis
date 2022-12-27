import os
import pandas as pd

"""
# JOB : THIS SCRIPT IS RESPONSIBLE TO PAIR MUTATION W IT'S CASES THAT HAS PRESENT.
#       AFTER RELATED CASES ARE FOUND CODE PAIRS CASES W/ IT'S TRANSCRIPTION PROFILES.
"""
def find_symbol_in_transcription_keys(hugo_symb,expression_keys_dbs):
    try:
        return list(filter(lambda x: hugo_symb in x, expression_keys_dbs))[0]
    except:
        return None

def pair_mutation_w_case(mutation_hugo_symbol,DepMAP_mutation_overall ):
    targeted_hugo_symb_dbs = DepMAP_mutation_overall[DepMAP_mutation_overall["Hugo_Symbol"]==mutation_hugo_symbol]
    cases_have_mutations = targeted_hugo_symb_dbs["DepMap_ID"].to_list()
    return cases_have_mutations


def get_Transcript_value_of_objected_gene_in_given_case(case,expression_key,Transcription_Profiles_Of_Cell_Lines_dbs):
    try:
        return Transcription_Profiles_Of_Cell_Lines_dbs.loc[case][expression_key]
    except:
        return None

"""
if __name__ != '__main__':
    expression_keys = get_proper_keys_Hugo_Symbol()
    print(find_symbol_in_transcription_keys("PIK3CA",expression_keys))
    print(get_Transcript_value_of_objected_gene_in_given_case("ACH-000502","KRAS (3845)"))
    #print(get_Transcript_profiles_of_cases())
"""