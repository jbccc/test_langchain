from langchain.prompts import ChatPromptTemplate
from langchain.prompts.chat import SystemMessage, HumanMessagePromptTemplate

template = ChatPromptTemplate.from_messages([
    SystemMessage(content=(
        "You are a helpful assistant that re-writes the user's text to "
        "sound more upbeat."
    )),
    HumanMessagePromptTemplate.from_template(
        "{text}"
    )
])
