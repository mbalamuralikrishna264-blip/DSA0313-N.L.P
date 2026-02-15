from openai import OpenAI

client = OpenAI(api_key="your_api_key_here")

prompt = input("Enter prompt: ")

response = client.responses.create(
    model="gpt-3.5-turbo",
    input=prompt,
    max_output_tokens=50
)

print("Generated Text:")
print(response.output_text)
