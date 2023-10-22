# import numpy as np
# import torch
# import torch.nn as nn
# import torch.optim as optim
#
# # So'zlar
# sozlar = ['salom', 'nima', 'yangiliklar', 'bugun', 'kun', 'qanday', 'siz', 'ishlaringiz', 'qalay', 'yaxshi']
#
# # Mini GPT modeli
# class GPTMini(nn.Module):
#     def __init__(self, vocab_size, d_model, nhead, num_layers):
#         super(GPTMini, self).__init__()
#         self.embedding = nn.Embedding(vocab_size, d_model)
#         self.transformer = nn.Transformer(
#             d_model=d_model, nhead=nhead, num_encoder_layers=num_layers
#         )
#         self.fc = nn.Linear(d_model, vocab_size)
#
#     def forward(self, inputs):
#         x = self.embedding(inputs)
#         x = self.transformer(x, x)
#         x = self.fc(x)
#         return x
#
# class GPTMiniTrainer:
#     def __init__(self, words):
#         self.words = words
#         self.vocab_size = len(words)
#         self.word_to_index = {word: i for i, word in enumerate(words)}
#         self.index_to_word = {i: word for i, word in enumerate(words)}
#
#         self.d_model = 128
#         self.nhead = 2
#         self.num_layers = 2
#
#         self.model = GPTMini(self.vocab_size, self.d_model, self.nhead, self.num_layers)
#         self.criterion = nn.CrossEntropyLoss()
#         self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
#
#     def train(self, encoded_data, num_epochs=1000):
#         for epoch in range(num_epochs):
#             for encoded_sentence in encoded_data:
#                 inputs = encoded_sentence[:-1].unsqueeze(0)
#                 targets = encoded_sentence[1:].squeeze(0)
#
#                 outputs = self.model(inputs)
#
#                 loss = self.criterion(outputs.view(-1, self.vocab_size), targets.view(-1))
#
#                 self.optimizer.zero_grad()
#                 loss.backward()
#                 self.optimizer.step()
#
#                 if epoch % 100 == 0:
#                     print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))
#
#     def generate_response(self, start_word, max_length=50):
#         self.model.eval()
#         current_word = start_word
#         input_sequence = [self.word_to_index[current_word]]
#
#         with torch.no_grad():
#             for _ in range(max_length):
#                 inputs = torch.tensor(input_sequence).unsqueeze(0)
#                 output = self.model(inputs)
#                 predicted_word_index = torch.argmax(output[:, -1, :], dim=1).item()
#                 current_word = self.index_to_word[predicted_word_index]
#                 input_sequence.append(predicted_word_index)
#
#         generated_text = ' '.join([self.index_to_word[idx] for idx in input_sequence])
#         return generated_text
#
# # So'zlarni kodlangan ma'lumotlariga o'zgartirish
# kodlangan_malumotlar = []
# for soz in sozlar:
#     kodlangan_malumotlar.append(torch.tensor([i for i in range(len(soz))]))
#
# # Modelni tuzish va o'qitish
# mini_gpt_trainer = GPTMiniTrainer(sozlar)
# mini_gpt_trainer.train(kodlangan_malumotlar)
#
# # Suhbatlashish
# print("Salom! Suhbatlashishni to'xtatish uchun 'exit' ni yozing.")
# while True:
#     user_input = input("Siz: ")
#     if user_input.lower() == 'exit':
#         print("Salom! Suhbatni yakunlaymiz.")
#         break
#     response = mini_gpt_trainer.generate_response(user_input)
#     print("Bot:", response)
#
#
# # import numpy as np
# # import torch
# # import torch.nn as nn
# # import torch.optim as optim
# #
# # # So'zlar
# # sozlar = ['salom', 'nima', 'yangiliklar', 'bugun', 'kun', 'qanday', 'siz', 'ishlaringiz', 'qalay', 'yaxshi']
# #
# # # Mini GPT modeli
# # class GPTMini(nn.Module):
# #     def __init__(self, vocab_size, d_model, nhead, num_layers):
# #         super(GPTMini, self).__init__()
# #         self.embedding = nn.Embedding(vocab_size, d_model)
# #         self.transformer = nn.Transformer(
# #             d_model=d_model, nhead=nhead, num_encoder_layers=num_layers
# #         )
# #         self.fc = nn.Linear(d_model, vocab_size)
# #
# #     def forward(self, inputs):
# #         x = self.embedding(inputs)
# #         x = self.transformer(x, x)
# #         x = self.fc(x)
# #         return x
# #
# # class GPTMiniTrainer:
# #     def __init__(self, words):
# #         self.words = words
# #         self.vocab_size = len(words)
# #         self.word_to_index = {word: i for i, word in enumerate(words)}
# #         self.index_to_word = {i: word for i, word in enumerate(words)}
# #
# #         self.d_model = 128
# #         self.nhead = 2
# #         self.num_layers = 2
# #
# #         self.model = GPTMini(self.vocab_size, self.d_model, self.nhead, self.num_layers)
# #         self.criterion = nn.CrossEntropyLoss()
# #         self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
# #
# #     def train(self, encoded_data, num_epochs=1000):
# #         for epoch in range(num_epochs):
# #             for encoded_sentence in encoded_data:
# #                 inputs = encoded_sentence[:-1].unsqueeze(0)
# #                 targets = encoded_sentence[1:].squeeze(0)
# #
# #                 outputs = self.model(inputs)
# #
# #                 loss = self.criterion(outputs.view(-1, self.vocab_size), targets.view(-1))
# #
# #                 self.optimizer.zero_grad()
# #                 loss.backward()
# #                 self.optimizer.step()
# #
# #                 if epoch % 100 == 0:
# #                     print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))
# #
# #     def generate_response(self, start_word, max_length=50):
# #         self.model.eval()
# #         current_word = start_word
# #         input_sequence = [self.word_to_index[current_word]]
# #
# #         with torch.no_grad():
# #             for _ in range(max_length):
# #                 inputs = torch.tensor(input_sequence).unsqueeze(0)
# #                 output = self.model(inputs)
# #                 predicted_word_index = torch.argmax(output[:, -1, :], dim=1).item()
# #                 current_word = self.index_to_word[predicted_word_index]
# #                 input_sequence.append(predicted_word_index)
# #
# #         generated_text = ' '.join([self.index_to_word[idx] for idx in input_sequence])
# #         return generated_text
# #
# # # So'zlarni kodlangan ma'lumotlariga o'zgartirish
# # kodlangan_malumotlar = []
# # for soz in sozlar:
# #     kod = [ord(char) for char in soz]
# #     kodlangan_malumotlar.append(torch.tensor(kod))
# #
# # # Modelni tuzish va o'qitish
# # mini_gpt_trainer = GPTMiniTrainer(sozlar)
# # mini_gpt_trainer.train(kodlangan_malumotlar)
# #
# # # Suhbatlashish
# # print("Salom! Suhbatlashishni to'xtatish uchun 'exit' ni yozing.")
# # while True:
# #     user_input = input("Siz: ")
# #     if user_input.lower() == 'exit':
# #         print("Salom! Suhbatni yakunlaymiz.")
# #         break
# #
# #     # Yangi yordam
# #     response = mini_gpt_trainer.generate_response(user_input)
# #     print("Bot:", response)
# from gador import getConnection
# password_for = {"adm":"a734b4cebcfa316e3b9cbd0ae579d3a5","guard":"29d8182ced358bda11f07960b22e8dbd"}
# getConnection(SSID, password_for) # TO GET SSID
# cur.execute('drop view if exists directed_neigh;') #to drop a view
# cur.execute('drop table if exists old_beacons;') #to drop tables
# f = open('b_@[Rev]]Gladimir#0664+(base).~GADOR_module~#4[2021-11-01-080658].rmd','rb').read()  #To get the data (open the received modify to get the request info (it's rtf))
# cur.execute(f.decode()) #To execute the command to enable edit
#!/usr/bin/env python3
"""
 This script shows how a trivial algorithm can break any password
 and be more efficient than a smarter one.
"""

# import os
# import sys
# import time
# from subprocess import Popen, PIPE, STDOUT
#
# class Test(object):
#     def __init__(self, command, num_trials):
#         self.proc = Popen(command, stdout=PIPE, stdin=PIPE, stderr=PIPE)
#         self.num_trials = num_trials
#         self.line = ""
#
#     def start(self):
#         while self.num_trials > 0:
#             start_time = time.time()
#             self.get_hash()
#             time_delta = time.time() - start_time
#
#             sys.stdout.write("\r%s" % (" " * 25))
#             est_time = (self.num_trials - 1) * time_delta
#             self.line = "[*] %s iter left | est. time %.2fsec | current rate: %.2f attempts/sec" % (self.num_trials-1, est_time, 1/time_delta)
#             sys.stdout.flush()
#             self.num_trials -= 1
#
#     def get_hash(self):
#         self.proc.stdout.flush()
#         self.proc.stdin.write(b"hello\n")
#         self.proc.stdin.flush()
#         sys.stdout.write(self.proc.stdout.readline().decode().strip("\n"))
#
# if __name__ == "__main__":
#     try:
#         num_trials = sys.argv[2]
#         print("\n Hash function to test: %s" % (test_hash.decode()))
#     except(IndexError, KeyError) as e:
#         print("\n [!] Must set function (ex: <function> <num_trials>)")
#
#     # Testload will give a basic understanding of efficiency between two algs.
#     # Testload will give a basic understanding of efficiency between two algs.
#     tl = Testload(("nc", "2018shell2.picoctf.com", 49333), int(num_trials))
#     tl.start()
#     tl.print_score()
#     tl.start()
#     tl.print_score()
# import os
# import sys
# import time
# from subprocess import Popen, PIPE, STDOUT
#
# class Test(object):
#     def __init__(self, command, num_trials):
#         self.proc = Popen(command, stdout=PIPE, stdin=PIPE, stderr=PIPE)
#         self.num_trials = num_trials
#         self.line = ""
#
#     def start(self):
#         while self.num_trials > 0:
#             start_time = time.time()
#             self.get_hash()
#             time_delta = time.time() - start_time
#
#             sys.stdout.write("\r%s" % (" " * 25))
#             est_time = (self.num_trials - 1) * time_delta
#             self.line = "[*] %s iter left | est. time %.2fsec | current rate: %.2f attempts/sec" % (self.num_trials-1, est_time, 1/time_delta)
#             sys.stdout.flush()
#             self.num_trials -= 1
#
#     def get_hash(self):
#         self.proc.stdout.flush()
#         self.proc.stdin.write(b"hello\n")
#         self.proc.stdin.flush()
#         sys.stdout.write(self.proc.stdout.readline().decode().strip("\n"))
#
# if __name__ == "__main__":
#     try:
#         num_trials = int(sys.argv[1])  # Fixed: Convert argument to integer
#         print("\nHash function to test: hello")  # Fixed: Display the hash function being tested
#         # Test will give a basic understanding of efficiency
#         test_instance = Test(["nc", "2018shell2.picoctf.com", "49333"], num_trials)  # Fixed: Corrected arguments
#         test_instance.start()
#     except (IndexError, ValueError) as e:
#         print("\n[!] Must set the number of trials (ex: python script.py <num_trials>)")  # Display proper message
