import torch
from torchvision import models, transforms
from PIL import Image

# 1 - Carregar modelo pré-treinado
model = models.resnet50(pretrained=True)
model.eval()

# 2 - Carregar a imagem
image_path = "1.jpg"
image = Image.open(image_path)

# 3 - Pré-processar a imagem
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])

input_tensor = preprocess(image)
input_batch = input_tensor.unsqueeze(0)  # Adicionar dimensão de lote


import torch
import json
from urllib import request

# 3 - Fazer a predição
with torch.no_grad():
    output = model(input_batch)

# 4 - Baixar as labels
LABELS_URL = "https://raw.githubusercontent.com/anishathalye/imagenet-simple-labels/master/imagenet-simple-labels.json"
labels_path = "imagenet-simple-labels.json"
request.urlretrieve(LABELS_URL, labels_path)

# 5 - Carregar as labels
with open(labels_path, "r") as f:
    labels = json.load(f)

# 6 - Obter a classe prevista
predicted_idx = torch.max(output, 1)[1]
predicted_label = labels[predicted_idx.item()]

# 7 - Imprimir o objeto na imagem
print(f"O objeto na imagem é: {predicted_label}")
