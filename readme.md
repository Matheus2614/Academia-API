### Curso Técnico de Desenvolvimento de Sistemas - Senai Itapeva

![Imagem de capa](img/WR%20FIT.gif)  <!-- Substitua pelo caminho correto do seu GIF/imagem de capa do admin -->

**Descrição:**

Esta API fornece a conexão entre o Front-End e o banco de dados (Firebase) que armazena os clientes para o sistema WR FIT, esta API oferece rotas para gerenciar os clientes (adicionar, excluir, editar e vizualizar). Desenvolvido com Python, Flask e Firebase.

## Índice

* [Funcionalidades](#funcionalidades)
* [Tecnologias Utilizadas](#tecnologias-utilizadas)
* [Como Executar](#como-executar)
* [Autores](#autores)
* [Licença](#licença)

## Funcionalidades

*   **`GET /clientes`**: Retorna uma lista (array) de todas os clientes cadastrados em formato JSON. Cada objeto na lista deve conter `id`, `nome`, `cpf` e `status`.
    *   Exemplo de resposta: `[{"id": 1, "nome": "...", "cpf": "...", "status": "..."}]`

* **`GET /clientes/<cpf>`**: Retorna um cliente especificado pelo `cpf`
    *   Exemplo de resposta: `{"id": "...", "nome": "...", "cpf": "(cpf especificado)", "status": "..."}`

*   **`POST /clientes`**: Recebe um corpo JSON com `nome`, `cpf` e `status` para cadastrar um novo cliente. Retorna uma mensagem de sucesso ou erro.
    *   Exemplo de corpo da requisição: `{"nome": "Nome do cliente", "cpf": "CPF do cliente", "status": "ativo/inativo"}`

*   **`PUT /clientes/<id>`**: Recebe um corpo JSON com `nome`, `cpf` e `status` para atualizar o cliente com o `id` especificado na URL. Retorna uma mensagem de sucesso ou erro.
    *   Exemplo de corpo da requisição: `{"nome": "Nome editado", "cpf": "cpf editado", "status": "status editado (ativo/inativo) }`

*   **`DELETE /clientes/<id>`**: Exclui o cliente com o `id` especificado na URL. Mostra uma mensagem de sucesso ou erro. 

*   A API deve ser configurada adequadamente para lidar com solicitações CORS (Cross-Origin Resource Sharing), permitindo requisições vindas da origem onde o front-end de admin está sendo executado.

## Tecnologias Utilizadas
![imagem](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![imagem](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![imagem](https://img.shields.io/badge/firebase-ffca28?style=for-the-badge&logo=firebase&logoColor=black)

## Como executar

-   Abra este link: https://academia-api-xi.vercel.app/

## Autores

-   Matheus - https://github.com/Matheus2614 - matheuss.wincler.senai@gmail.com

-   Richard - https://github.com/Richard15151 - richard.oliveira.senai@gmail.com

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE (se existir no seu repositório) para mais detalhes.