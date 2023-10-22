import torch
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
from googletrans import Translator

# GPT-Neo-2.7B modelini yaratish
model = GPTNeoForCausalLM.from_pretrained('EleutherAI/gpt-neo-2.7B')

# Tokenizer ni yaratish
tokenizer = GPT2Tokenizer.from_pretrained('EleutherAI/gpt-neo-2.7B')

# Tarjimon yaratish
translator = Translator()

def generate_uzbek_response(input_text):
    # Kiruvchi matnni tokenizatsiya qilish
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    attention_mask = torch.ones(input_ids.shape, dtype=torch.long)

    # GPT-Neo modeliga matnni bermaslik va javobni olish;
    with torch.no_grad():
        output = model.generate(input_ids, max_length=100, num_return_sequences=1,
                                pad_token_id=70256, attention_mask=attention_mask)

    response = tokenizer.decode(output[0][len(input_ids[0]):], skip_special_tokens=True)

    # Javobni o'zbek tiliga tarjima qilish
    translated_response = translator.translate(response, dest='uz').text
    return translated_response

# Foydalanuvchi kiruvchi xabarini olish
user_input = input("Izohingizni kiriting: ")

# GPT-Neo modeli orqali javobni olish
response = generate_uzbek_response(user_input)

# Javobni konsolga chiqarish
print("GPT-Neo javobi (O'zbekcha):", response)
