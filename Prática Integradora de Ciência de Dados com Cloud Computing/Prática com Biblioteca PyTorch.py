import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# 1 - Preparar os dados (MNIST)
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_dataset = torchvision.datasets.MNIST(root='./data', train=True, transform=transform, download=True)
test_dataset = torchvision.datasets.MNIST(root='./data', train=False, transform=transform, download=True)

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=64, shuffle=False)

# 2 - Definir uma rede neural simples
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(-1, 28*28)
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 3 - Função para treinar e avaliar com diferentes losses
def train_and_evaluate(loss_function):
    model = SimpleNet()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    # Treinamento
    for epoch in range(2):  # poucas épocas para teste rápido
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)

            if isinstance(loss_function, nn.MSELoss):
                # Converter labels para one-hot quando usar MSE
                labels_onehot = torch.zeros(labels.size(0), 10)
                labels_onehot.scatter_(1, labels.view(-1,1), 1)
                loss = loss_function(outputs, labels_onehot)
            else:
                loss = loss_function(outputs, labels)

            loss.backward()
            optimizer.step()

    # Avaliação
    correct, total = 0, 0
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = correct / total
    print(f"Acurácia com {loss_function.__class__.__name__}: {accuracy:.2f}")

# 4 - Comparar CrossEntropyLoss vs MSELoss
train_and_evaluate(nn.CrossEntropyLoss())
train_and_evaluate(nn.MSELoss())
