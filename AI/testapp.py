# import torch
# from transformers import GPTNeoForCausalLM, GPT2Tokenizer
# # Model va tokenizer nomi
# model_name = "EleutherAI/gpt-neo-2.7B"
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)
# model = GPTNeoForCausalLM.from_pretrained(model_name)
# # Foydalanuvchidan so'rov olish va javob bermoq
# while True:
#     user_input = input("Siz: ")
#     if user_input.lower() == "exit":
#         break
#     # Tokenlash va modelga o'qitish
#     inputs = tokenizer(user_input, return_tensors="pt")
#     outputs = model(**inputs)
#     with torch.no_grad():
#         output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=50256,attention_mask=attention_mask)
#     # Javobni chiqarish
#     response = tokenizer.decode(output[0][len(input_ids[0]):]
#     print("Chatbot:", response)


#
# import torch
# from transformers import GPT2LMHeadModel, GPT2Tokenizer
#
#
# from transformers import GPTNeoForCausalLM, GPT2Tokenizer
#
# # GPT-2 model va tokenizerini yaratish
#
#
#
# def UZAI_Response(request, chat_messages=None):
#
#     # Tokenlar va attention_mask ni o'rganish
#     input_ids = tokenizer.encode(text, return_tensors='pt')
#     attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
#
#     # Modelga ma'lumotni o'tkazib, javobni olish
#     with torch.no_grad():
#         output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=50256,
#                                 attention_mask=attention_mask)
#
#     # Javobni chatga qo'shish
#     response = tokenizer.decode(output[0][len(input_ids[0]):],
#                                 skip_special_tokens=True)  # input_ids[0] dan keyin kelgan qismi ajratib olish
#     chat_messages.append({'sender': 'gpt2', 'text': response})



