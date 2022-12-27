import os
import pandas as pd
from dbs_pairing.finding_cases_by_mutations import *

DepMAP_mutation_overall = pd.read_csv("../dbs/CCLE_mutations.csv")
Transcription_Profiles_Of_Cell_Lines_dbs = pd.read_csv("../dbs/CCLE_expression-2.csv",index_col=0)
TTRUST_file_defined="../dbs/trrust_rawdata.human.tsv"
def parsing_of_TRRUST_dbs(TTRUST_file = TTRUST_file_defined):
    TTRUST_dbs=pd.read_csv(TTRUST_file,sep="\t")
    return TTRUST_dbs

def calculate_mutation_impact_to_target_gene_expression(MT_protein, target_gene_expression_level, all_expression_dbs_keys):
    targeted_case_ls, expression_keys_of_targeted_gene = pair_mutation_w_case(MT_protein,DepMAP_mutation_overall),\
                                                         find_symbol_in_transcription_keys(target_gene_expression_level, all_expression_dbs_keys)

    expression_levels_in_cases_ls = [get_Transcript_value_of_objected_gene_in_given_case(case, expression_keys_of_targeted_gene,Transcription_Profiles_Of_Cell_Lines_dbs) for case in targeted_case_ls]
    return expression_levels_in_cases_ls

def get_reference_transcription_levels(Transcription_Profiles_Of_Cell_Lines_dbs):
    column_ls_Transcription=Transcription_Profiles_Of_Cell_Lines_dbs.columns.to_list()
    average_transcription_dict=dict()
    for gene_key in column_ls_Transcription:
        average_transcription_dict[gene_key] = Transcription_Profiles_Of_Cell_Lines_dbs[gene_key].mean()
    return average_transcription_dict

if __name__ == '__main__':
    #calculate_mutation_impact_to_target_gene_expression("KRAS","BRAF")
    collection_ls,all_expression_dbs_keys, control_transcription_levels= list(),pd.read_csv("../dbs/CCLE_expression-2.csv", index_col=0).columns.to_list(),get_reference_transcription_levels(Transcription_Profiles_Of_Cell_Lines_dbs)


    for index,row in parsing_of_TRRUST_dbs().iterrows():
        impact_dict={"MT_Gene":row["Gene1"],"Target_Gene":row["Gene2"]}
        expression_keys_of_targeted_gene=find_symbol_in_transcription_keys(row["Gene2"], all_expression_dbs_keys)
        Transcriptional_level_ls_on_targeted_gene = calculate_mutation_impact_to_target_gene_expression(row["Gene1"],row["Gene2"],all_expression_dbs_keys)
        impact_dict["Control"] = control_transcription_levels[expression_keys_of_targeted_gene]
        impact_dict["Transcriptional_Level"]=Transcriptional_level_ls_on_targeted_gene
        collection_ls.append(impact_dict)
        print(impact_dict)
