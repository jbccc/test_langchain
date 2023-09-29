import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-3.5-turbo")

# from langchain.llms import HuggingFacePipeline

# llm_model_name = "meta-llama/Llama-2-70b-chat-hf"
# code_model_name = "Phind/Phind-CodeLlama-34B-v2"

# llm = HuggingFacePipeline.from_model_id(
#     model_id=llm_model_name,
#     task="text-generation",
#     model_kwargs={"temperature": 0.1, "max_length": 1024},
# )

# code = HuggingFacePipeline.from_model_id(
#     model_id=code_model_name,
#     task="text-generation",
#     model_kwargs={"temperature": 0.1, "max_length": 2048},
# )
