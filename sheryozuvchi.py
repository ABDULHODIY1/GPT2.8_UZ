# # import numpy as n
# # import matplotlib.pylab as p
# # import numpy as np
# #
# # sx = n.asarray([
# #     [0,1,0,1,0],
# #     [0,0,1,1,0],
# #     [1,1,0,1,0],
# #     [1,1,1,0,1],
# #     [0,0,0,1,0]
# # ])
# #
# #
# # ys=n.asarray([
# #     [0],
# #     [1],
# #     [1],
# #     [1],
# #     [0]
# # ])
# #
# # ins = 5
# # out = 1
# #
# # def W(ins,ou):
# #     ws = n.random.randn(ins,ou)
# #     return ws
# # ws = W(ins,out)
# #
# # ers = []
# #
# # for i in range(5000):
# #     yh = sx @ ws
# #
# #     e= yh - ys
# #     e = np.sum(np.abs(e))
# #     if e < 0.05:
# #         print("test 1")
#
# import numpy as np
#
# # So'zlar
# words = ['salom', 'nima', 'yangiliklar', 'bugun', 'kun', 'qanday', 'siz', 'ishlaringiz', 'qalay', 'yaxshi']
#
# # Mini GPT modeli
# class MiniGPT:
#     def __init__(self, words, max_length=100):
#         self.words = words
#         self.max_length = max_length
#         self.num_words = len(words)
#         self.word_to_index = {word: i for i, word in enumerate(words)}
#         self.index_to_word = {i: word for i, word in enumerate(words)}
#
#         # Neyron tarmoqni yaratish uchun parametrlar
#         self.input_size = len(words)
#         self.hidden_size = 128
#         self.output_size = len(words)
#         self.learning_rate = 0.01
#
#         # Tarmoqni o'zgaruvchilari
#         self.Wxh = np.random.randn(self.input_size, self.hidden_size) * 0.01
#         self.Whh = np.random.randn(self.hidden_size, self.hidden_size) * 0.01
#         self.Why = np.random.randn(self.hidden_size, self.output_size) * 0.01
#         self.bh = np.zeros((1, self.hidden_size))
#         self.by = np.zeros((1, self.output_size))
#
#     def forward(self, inputs, hprev):
#         xs, hs, ys, ps = {}, {}, {}, {}
#         hs[-1] = np.copy(hprev)
#         for t in range(len(inputs)):
#             xs[t] = np.zeros((1, self.input_size))
#             xs[t][0, inputs[t]] = 1  # Input encoding
#             hs[t] = np.tanh(np.dot(xs[t], self.Wxh) + np.dot(hs[t-1], self.Whh) + self.bh)  # Hidden state
#             ys[t] = np.dot(hs[t], self.Why) + self.by  # Unnormalized log probabilities for next words
#             ps[t] = np.exp(ys[t]) / np.sum(np.exp(ys[t]))  # Softmax for probabilities
#         return xs, hs, ps
#
#     def backward(self, inputs, hs, ps, targets):
#         dWxh, dWhh, dWhy = np.zeros_like(self.Wxh), np.zeros_like(self.Whh), np.zeros_like(self.Why)
#         dbh, dby = np.zeros_like(self.bh), np.zeros_like(self.by)
#         dhnext = np.zeros_like(hs[0])
#
#         for t in reversed(range(len(inputs))):
#             dy = np.copy(ps[t])
#             dy[0, targets[t]] -= 1  # Backprop into y
#             dWhy += np.dot(hs[t].T, dy)
#             dby += dy
#             dh = np.dot(dy, self.Why.T) + dhnext  # Backprop into h
#             dhraw = (1 - hs[t] ** 2) * dh  # Backprop through tanh nonlinearity
#             dbh += dhraw
#             dWxh += np.dot(inputs[t].T, dhraw)
#             dWhh += np.dot(hs[t-1].T, dhraw)
#             dhnext = np.dot(dhraw, self.Whh.T)
#
#         for dparam in [dWxh, dWhh, dWhy, dbh, dby]:
#             np.clip(dparam, -5, 5, out=dparam)  # Clip to mitigate exploding gradients
#
#         return dWxh, dWhh, dWhy, dbh, dby
#
#     def train(self, start_word, targets, num_iterations=100):
#         for i in range(num_iterations):
#             # Ma'lumotlarni tayyorlash
#             inputs = [self.word_to_index[word] for word in start_word.split()]
#             hprev = np.zeros((1, self.hidden_size))  # Boshlang'ich o'rnash
#
#             # Forward va backward o'qish
#             xs, hs, ps = self.forward(inputs, hprev)
#             loss = -np.sum(np.log(ps[np.arange(len(inputs)), targets]))  # Cross-entropy loss
#             ers.append(loss)
#             dWxh, dWhh, dWhy, dbh, dby = self.backward(inputs, hs, ps, targets)
#
#             # Parametrlarni yangilash
#             self.Wxh -= self.learning_rate * dWxh
#             self.Whh -= self.learning_rate * dWhh
#             self.Why -= self.learning_rate * dWhy
#             self.bh -= self.learning_rate * dbh
#             self.by -= self.learning_rate * dby
#
#             # Test qilish
#             if i % 100 == 0:
#                 print('Iteration {}, Loss: {}'.format(i, loss))
#
# # Boshlang'ich kodingiz
# sx = np.asarray([
#     [0,1,0,1,0],
#     [0,0,1,1,0],
#     [1,1,0,1,0],
#     [1,1,1,0,1],
#     [0,0,0,1,0]
# ])
#
# ys = np.asarray([
#     [0],
#     [1],
#     [1],
#     [1],
#     [0]
# ])
#
# ers = []
# ins = 5
# out = len(words)  # Chiquq o'lchamini so'zlar soniga moslashtirdik
#
# # Mini GPT obyekti yaratish
# mini_gpt = MiniGPT(words, max_length=100)
#
# # Boshlang'ich so'zni tanlash va suhbatni generatsiya qilish
# start_word = 'salom'
# targets = [mini_gpt.word_to_index[word] for word in start_word.split()]
# mini_gpt.train(start_word, targets, num_iterations=5000)
import torch
import torch.nn as nn
import torch.optim as optim

# So'zlar bazasi
words = ['salom', 'nima', 'yangiliklar', 'bugun', 'kun', 'qanday', 'siz', 'ishlaringiz', 'qalay', 'yaxshi']

# Ma'lumotlarni tayyorlash
word_to_idx = {word: idx for idx, word in enumerate(words)}
idx_to_word = {idx: word for word, idx in word_to_idx.items()}

# Ma'lumotlar va ma'lumotlarni kodlash
data = ['salom nima yangiliklar', 'bugun kun', 'qanday siz', 'ishlaringiz qalay', 'yaxshi salom']
encoded_data = [torch.tensor([word_to_idx[word] for word in sentence.split()], dtype=torch.long) for sentence in data]

# Model tuzilmasi
class GPTMini(nn.Module):
    def __init__(self, vocab_size, d_model, nhead, num_layers):
        super(GPTMini, self).__init__()
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.transformer = nn.Transformer(
            d_model=d_model, nhead=nhead, num_encoder_layers=num_layers
        )
        self.fc = nn.Linear(d_model, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer(x)
        x = self.fc(x)
        return x

# Model yaratish
vocab_size = len(words)
d_model = 128
nhead = 4
num_layers = 2
model = GPTMini(vocab_size, d_model, nhead, num_layers)

# Optimizator va yoksaklik funktsiyasi
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Modelni o'rganish
num_epochs = 1000
for epoch in range(num_epochs):
    for sentence in encoded_data:
        inputs = sentence[:-1].unsqueeze(0)
        targets = sentence[1:].unsqueeze(0)

        # Yutuqlarni qayta hisoblash
        outputs = model(inputs)

        # O'yinchoqlarni hisoblash
        loss = criterion(outputs.view(-1, vocab_size), targets.view(-1))

        # Gradientlarni tozalash va yangilash
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Natijani chiqarish
        if epoch % 100 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

# Sizning so'zingiz bilan gaplashish
start_word = 'salom'
start_idx = word_to_idx[start_word]
input_word = torch.tensor(start_idx, dtype=torch.long).unsqueeze(0)

# Sizning so'zlarizni yaratish
generated_words = []
with torch.no_grad():
    for _ in range(20):  # 20 so'zdan iborat gap
        output = model(input_word)
        _, next_word_idx = torch.max(output[:, -1, :], dim=1)
        input_word = next_word_idx.unsqueeze(0)
        generated_words.append(idx_to_word[next_word_idx.item()])

# Generatsiya qilingan gapni chiqarish
generated_sentence = ' '.join(generated_words)
print('Generatsiya qilingan gap: ', generated_sentence)
