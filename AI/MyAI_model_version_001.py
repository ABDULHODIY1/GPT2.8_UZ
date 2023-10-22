# import torch
# import torch.nn.functional as F
# import torchvision.transforms as transforms
# import torchvision.models as models
#
# import captum
# from captum.attr import IntegratedGradients, Occlusion, LayerGradCam, LayerAttribution
# from captum.attr import visualization as viz
#
# import os, sys
# import json
#
# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt
# from matplotlib.colors import LinearSegmentedColormap


import socket

def get_ip(domain):
    return socket.gethostbyname(domain)

def is_onion(ip):
    return ip.endswith('.onion')

domain = 'example.com'
ip = get_ip(domain)
is_onion = is_onion(ip)

print(f'The domain {domain} is hosted on the {{"onion" if is_onion else "clearnet"}}.')