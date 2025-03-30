from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import config

llm = OpenAI(temperature=0.7, api_key=config.OPENAI_API_KEY)

template = PromptTemplate.from_template("""
You are a helpful assistant. Answer the following question: {question}
""")

chain = template | llm | StrOutputParser()

overall_chain = RunnablePassthrough.assign(
    output=chain,
)

# Run the chain
result = overall_chain.invoke({
    "question": "{input}",
})

question = ''

# Q/A loop
while question != 'exit':
    # Get user input
    question = input("Ask a question (or type 'exit' to quit): ")
    
    # Check if user wants to exit
    if question.lower() != "exit":
        # Run the chain
        result = overall_chain.invoke({
            "question": question,
        })
        # Print the generated response
        print(result["output"])