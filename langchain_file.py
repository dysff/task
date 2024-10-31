from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def generate_output(prompt_text):
  llm = OpenAI()
  prompt_template = PromptTemplate(
    input_variables=["prompt"], 
    template="{prompt}"
  )
  chain = LLMChain(llm=llm, prompt=prompt_template, output_key='response')
  response = chain({"prompt": prompt_text})

  return response