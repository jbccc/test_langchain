import pandas as pd
from .model import llm 
from .prompt_template import PromptTemplateInstructions, PromptTemplateCodeGen1, PromptTemplateCodeGen2

def read_metadata(csv_file):
    df = pd.read_csv(csv_file)
    # creates list from rows
    metadata = df.values.tolist()
    return metadata



def main():
    metadata = read_metadata('metadata.csv')
    instructions = []
    for row in metadata:
        instructions.append(PromptTemplateInstructions(row))

    codes = []
    for instruction in instructions:
        codes.append(PromptTemplateCodeGen1(instruction))

    final_code = PromptTemplateCodeGen2(codes)

    print(final_code)
