from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

TEMPLATE = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully:\n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

MODEL = OllamaLLM(model="llama3.2")

def parse_with_ollama(dom_chunks: list, parse_description: str) -> str:
    """Parse DOM content chunks with LLM according to the user's description."""
    prompt = ChatPromptTemplate.from_template(TEMPLATE)
    chain = prompt | MODEL
    parsed_result = []
    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})
        print(f"Parsed batch {i} of length {len(dom_chunks)}")
        parsed_result.append(response)
    return "\n".join(parsed_result)