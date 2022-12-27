import os
import pandas as pd
from dbs_pairing.finding_cases_by_mutations import *


TTRUST_file_defined="../dbs/trrust_rawdata.human.tsv"
def parsing_of_TRRUST_dbs(TTRUST_file = TTRUST_file_defined):
    TTRUST_dbs=pd.read_csv(TTRUST_file,sep="\t")
    return TTRUST_dbs


def calculate_mutation_impact_to_target_gene_expression(MT_protein, target_gene_expression_level):
    all_expression_dbs_keys = get_proper_keys_Hugo_Symbol()
    targeted_case_ls, expression_keys_of_targeted_gene = pair_mutation_w_case(MT_protein),\
                                                         find_symbol_in_transcription_keys(target_gene_expression_level, all_expression_dbs_keys)

    expression_levels_in_cases_ls = [get_Transcript_value_of_objected_gene_in_given_case(case, expression_keys_of_targeted_gene) for case in targeted_case_ls]
    return expression_levels_in_cases_ls


if __name__ == '__main__':
    #calculate_mutation_impact_to_target_gene_expression("KRAS","BRAF")
    collection_ls = list()
    for index,row in parsing_of_TRRUST_dbs().iterrows():
        impact_dict={"MT_Gene":row["Gene1"],"Target_Gene":row["Gene2"]}
        Transcriptional_level_ls_on_targeted_gene = calculate_mutation_impact_to_target_gene_expression(row["Gene1"],row["Gene2"])
        impact_dict["Transcriptional_Level"]=Transcriptional_level_ls_on_targeted_gene
        collection_ls.append(impact_dict)
        print(impact_dict)
