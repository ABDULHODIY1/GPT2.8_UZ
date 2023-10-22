# from transformers import GPT3Tokenizer, GPT3LMHeadModel
#
# # GPT-3 uchun model va tokenizer'ni yaratish
# tokenizer = GPT3Tokenizer.from_pretrained("gpt3")
# model = GPT3LMHeadModel.from_pretrained("gpt3")
import pydot
from PIL import Image

# Grafikni yaratish
graph = pydot.Dot(graph_type='graph')

# Uzlubni yaratish
node_a = pydot.Node("Node A")
node_b = pydot.Node("Node B")

# Uzlublarni qo'shish
graph.add_node(node_a)
graph.add_node(node_b)

# Uzlublar orasiga aloqani yaratish
graph.add_edge(pydot.Edge(node_a, node_b))

# Grafikni vizualizatsiya qilish
graph.write_png('example_graph.png')

# Ekranga chiqarish
img = Image.open('example_graph.png')
img.show()
