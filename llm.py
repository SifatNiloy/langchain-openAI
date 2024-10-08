from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7, # for randomness
    max_tokens=1000, # character number (charged for tokens)
    verbose=True # debug output from model

)

response = llm.stream("Explain quantum mechanics in easy way")   # invoke sends respons and receives text, stream also does that but get response in chunks. batch - can take multiple input prompt
# print(response)

for chunk in response:
    print(chunk.content, end="", flush=True)


