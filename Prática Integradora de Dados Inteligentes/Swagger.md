# **Documentação da API - Seguradora Auto Aposentado**  
**Versão:** 1.0.0  
**Base URL:** `https://api.seguradoraautoaposentado.com/v1`  

---

## **1. Visão Geral**  
API RESTful desenvolvida para o sistema de seguros de veículos para aposentados. Oferece endpoints para:  
- Simulação de apólices.  
- Cadastro de clientes.  
- Gerenciamento de apólices.  

**Tecnologias:**  
- **Back-end:** Node.js (Express)  
- **Autenticação:** JWT (Bearer Token)  
- **Formato de Dados:** JSON  

---

## **2. Autenticação**  
Todos os endpoints (exceto `/simular` e `/cadastro`) requerem autenticação via token JWT:  
```http
Authorization: Bearer {token}
```

---

## **3. Endpoints**  

### **3.1. Simulação de Apólice**  
#### **POST** `/simular`  
Calcula o valor do seguro com base em idade, valor do veículo e histórico.  

**Request Body:**  
```json
{
  "idade": 65,
  "valorVeiculo": 50000,
  "historico": "limpo" // ou "com_sinistros"
}
```

**Response (Sucesso - 200 OK):**  
```json
{
  "valorSeguro": 2000.00,
  "descontoAposentado": "20%"
}
```

**Response (Erro - 400 Bad Request):**  
```json
{
  "erro": "Dados inválidos. Verifique idade e valor do veículo."
}
```

---

### **3.2. Cadastro de Cliente**  
#### **POST** `/cadastro`  
Registra um novo cliente (aposentado) no sistema.  

**Request Body:**  
```json
{
  "nome": "João Silva",
  "cpf": "123.456.789-00",
  "dataNascimento": "1955-04-10",
  "veiculo": {
    "placa": "ABC1D23",
    "modelo": "Toyota Corolla",
    "ano": 2020
  }
}
```

**Response (Sucesso - 201 Created):**  
```json
{
  "clienteId": "cliente_123",
  "mensagem": "Cadastro realizado com sucesso."
}
```

**Response (Erro - 409 Conflict):**  
```json
{
  "erro": "CPF já cadastrado."
}
```

---

### **3.3. Consulta de Apólices**  
#### **GET** `/apolices?cpf={cpf}`  
Retorna todas as apólices de um cliente.  

**Headers:**  
```http
Authorization: Bearer {token}
```

**Response (200 OK):**  
```json
[
  {
    "apoliceId": "apolice_456",
    "valor": 2000.00,
    "validade": "2024-12-31",
    "status": "ativa"
  }
]
```

---

## **4. Códigos de Status**  
| Código | Descrição |  
|--------|------------|  
| 200 | OK |  
| 201 | Created |  
| 400 | Bad Request |  
| 401 | Unauthorized |  
| 404 | Not Found |  
| 500 | Internal Server Error |  

---

## **5. Exemplo de Uso (cURL)**  
**Simulação:**  
```bash
curl -X POST https://api.seguradoraautoaposentado.com/v1/simular \
  -H "Content-Type: application/json" \
  -d '{"idade": 70, "valorVeiculo": 60000, "historico": "limpo"}'
```

**Cadastro:**  
```bash
curl -X POST https://api.seguradoraautoaposentado.com/v1/cadastro \
  -H "Content-Type: application/json" \
  -d '{"nome": "Maria Souza", "cpf": "987.654.321-00", "dataNascimento": "1958-11-20", "veiculo": {"placa": "XYZ9W87", "modelo": "Honda Civic", "ano": 2019}}'
```

---

## **6. Limitações**  
- **Rate Limiting:** 100 requisições por hora por IP.  
- **Dados obrigatórios:** CPF e placa do veículo devem ser válidos.  

---

## **7. Contato**  
**Equipe de Desenvolvimento:**  
- Email: delean.mafra@gmail.com  
- Slack: `#api-seguros-aposentados`  

---

**Última Atualização:** 21/04/2025  
[Download PDF](#) | [Postman Collection](#)  

--- 

### **Notas:**  
- Esta documentação é fictícia e pode ser adaptada para incluir mais endpoints (ex: `/renovacao`, `/cancelamento`).  
