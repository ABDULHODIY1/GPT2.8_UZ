import torch
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
# Load the GPT-Neo model and tokenizer
model = GPTNeoForCausalLM.from_pretrained('EleutherAI/gpt-neo-2.7B')
tokenizer = GPT2Tokenizer.from_pretrained('EleutherAI/gpt-neo-2.7B')

# Function to generate a response using GPT-Neo
def generate_response(input_text):
        input_ids = tokenizer.encode(input_text, return_tensors='pt')
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

        with torch.no_grad():
            output = model.generate(input_ids, max_length=100, num_return_sequences=1,
                                    pad_token_id=70256, attention_mask=attention_mask)

        response = tokenizer.decode(output[0][len(input_ids[0]):], skip_special_tokens=True)
        return response

# Example usage
while True:
    user_input = input("Enter your message: ")  # Get user input
    response = generate_response(user_input)    # Generate response
    print("Response:", response)                # Print the response
