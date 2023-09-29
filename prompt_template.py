from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate

my_system_message = SystemMessage(content=(
        "You are a Data Scientist working for a big pharma company. "
        "Your job is to complete coding related tasks. "
        "You are working with clinical trial data. "
        "Any code that you write must be working and correct. "
        "When asked to write code, you must write the code in SAS. "
        "You are not allowed to use any other programming language. "
        "You are not allowed to use any other software. "
        "When asked to generate instructions, you must write the clear instructions in English. "
        "Instructions are written to be understood by a human and translated into code by a computer later. "
    ))

PromptTemplateInstructions = ChatPromptTemplate.from_messages([
    my_system_message,
    HumanMessagePromptTemplate.from_template((
        "You are in charge of explaining to a colleague how to collect a particular column from the STDM dataset. "
        "The column is called {column_in_sheet_name} and is located in the file {sheet_name}. "
        "The resulting column is named {col_id}. "
        "To assist your task, a hint is provided: {hint}. "
        "It is important to note that this column is or depend on an ID column. "
    ))
])

PromptTemplateCodeGen1 = ChatPromptTemplate.from_messages([
    my_system_message,
    HumanMessagePromptTemplate.from_template((
        "One of your colleague provided your with instructions to collect a particular column from the STDM dataset. "
        "{instructions} "
        "Your task is to translate these instructions into a working SAS code. "
        "Your code should print the resulting column. "
    ))
])

PromptTemplateCodeGen2 = ChatPromptTemplate.from_messages([
    my_system_message,
    HumanMessagePromptTemplate.from_template((
        "One of your colleague created a list of SAS code to collect particular columns from the STDM dataset. "
        "Your task is to compile all these instructions into a working SAS code. "
        "Your code shoud save the resulting columns in a new dataset named 'ADAM'. "
        "You should not alter the code snippets provided by your colleague. "
    ))
])
