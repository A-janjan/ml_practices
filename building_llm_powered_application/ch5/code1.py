import os
from dotenv import load_dotenv
from langchain import HuggingFaceHub

# Load environment variables from a .env file
load_dotenv()

# Get the Hugging Face Hub API token from environment variables
api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

if not api_token:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment variables.")

# Set up the Hugging Face Hub repository ID
repo_id = "tiiuae/falcon-7b-instruct"

# Initialize the HuggingFaceHub language model with specified parameters
llm = HuggingFaceHub(
    repo_id=repo_id, 
    model_kwargs={"temperature": 0.5, "max_length": 1000},
    huggingfacehub_api_token=api_token
)

# Define the prompt
prompt = "What was the first Disney movie?"

# Generate a response from the model using the invoke method
try:
    response = llm.invoke(prompt)
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")
