import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

# GPT-2 modelini yuklab olish
gpt2_url = "https://tfhub.dev/openai/gpt2/2"
gpt2 = hub.load(gpt2_url)

# O'rganish uchun ma'lumotlar
training_data = ["salom"]  # O'rganish ma'lumotlarini shu yerga kiritishingiz kerak
target_data = ["Salom"]    # Natijalar (masalan, so'zlarni davom ettirish uchun) shu yerga kiritishingiz mumkin

# Ma'lumotlarni o'qitish uchun o'zgartirishlar
# Ma'lumotlarni sizning formatlaringizga moslab oling
# Misol uchun, matnlarni tokenlar ro'yxati bo'lib, ma'lumotlar modelga kiritiladi:
input_tokens = ["salom!!"]    # GPT-2 modeliga kiritish uchun matnlar ro'yxati
target_tokens = ["Salom"]   # GPT-2 modelining natijasini tekshirish uchun matnlar ro'yxati

# Ma'lumotlarni TensorFlow datasetga o'girish
dataset = tf.data.Dataset.from_tensor_slices((input_tokens, target_tokens))

# Ma'lumotlarni batchlar (guruhlar) halida qayta tashkil etish va tarqatish
batch_size = 32
dataset = dataset.batch(batch_size)

# Modelni o'qitish uchun funksiya
def train_model(model, dataset, epochs=5):
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    optimizer = tf.keras.optimizers.Adam()

    for epoch in range(epochs):
        total_loss = 0.0
        steps = 0

        for batch_input, batch_target in dataset:
            with tf.GradientTape() as tape:
                # GPT-2 modeliga kirishni va natijani olish
                model_input = dict(input_ids=batch_input, attention_mask=tf.ones_like(batch_input))
                outputs = model(model_input)
                logits = outputs['logits']

                # Loss ni hisoblash
                loss = loss_fn(batch_target, logits)

            # Gradientlarni hisoblash va modelni yangilash
            gradients = tape.gradient(loss, model.trainable_variables)
            optimizer.apply_gradients(zip(gradients, model.trainable_variables))

            total_loss += loss
            steps += 1

        # Har bir epoxada o'rtacha o'chib ketgan loss ni chiqarish
        average_loss = total_loss / steps
        print("Epoch {}, Loss: {}".format(epoch + 1, average_loss))


# GPT-2 modelini o'qitish
train_model(gpt2, dataset, epochs=5)

# GPT-2 modelini saqlash
gpt2.save('trained_gpt2_model')
