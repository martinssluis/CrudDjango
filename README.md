# 🌟 **Projeto CRUD de Clientes com Django** 🌟

🎉 Quero compartilhar um projeto de gerenciamento de clientes que desenvolvi usando o framework Django. Esse sistema oferece um CRUD completo (Create, Read, Update, Delete), permitindo a gestão eficiente de dados de clientes.

## 🛠️ **Tecnologias Utilizadas**

- **Django**: Framework web poderoso e simples de usar, utilizado para o desenvolvimento rápido da aplicação.
- **SQLite**: Banco de dados embutido, leve e eficiente, perfeito para projetos pequenos.
- **HTML e CSS**: Utilizados para personalizar a interface, deixando-a mais atraente e funcional.

## ✨ **Funcionalidades**

### 📋 1. **Cadastro de Clientes**
**Como foi implementado:**  
A funcionalidade de cadastro utiliza um formulário criado com a classe `forms.ModelForm` do Django, que é baseado diretamente no modelo `Client`. Isso permite validação automática dos dados antes de serem salvos no banco. Após o envio do formulário, os dados são processados pela view responsável e, se válidos, são adicionados ao banco de dados.

**Para que serve:**  
Permite adicionar novos clientes preenchendo informações como nome, e-mail, sexo e data de nascimento.

### 📜 2. **Listagem de Clientes**
**Como foi implementado:**  
A listagem é feita através de uma query no banco de dados usando o ORM do Django. Os dados são recuperados e enviados para o template HTML por meio de uma view baseada em função (function-based view). No template, eles são exibidos em uma tabela organizada utilizando a linguagem de template do Django.

**Para que serve:**  
Exibe uma tabela com todos os clientes cadastrados, mostrando informações como ID, nome, e-mail, sexo e data de nascimento. Inclui botões para editar e excluir clientes.

### ✏️ 3. **Atualização de Clientes**
**Como foi implementado:**  
A funcionalidade de edição também utiliza o `ModelForm`. Quando o botão de edição é clicado, o sistema busca os dados atuais do cliente pelo ID e os pré-preenche no formulário. Após a edição, os dados atualizados são validados e salvos no banco de dados.

**Para que serve:**  
Permite editar as informações dos clientes, mantendo os dados atualizados e corrigidos.

### ❌ 4. **Exclusão de Clientes**
**Como foi implementado:**  
A exclusão é realizada através de uma view que recebe o ID do cliente como parâmetro. O Django utiliza seu ORM para localizar e excluir o registro correspondente. Antes da exclusão, uma mensagem de confirmação é apresentada para evitar exclusões acidentais.

**Para que serve:**  
Remove clientes desnecessários ou incorretos, ajudando a manter a base de dados limpa e organizada.

## 🗂️ **Organização do Projeto**

O projeto segue as melhores práticas do Django:

- **Modelos**: O modelo `Client` define os campos essenciais como `name`, `email`, `sex` e `dt_birth`. O campo `sex` tem escolhas pré-definidas e o `dt_birth` utiliza o formato de data nativo do Django.
- **Views**: Cada operação do CRUD é gerenciada por uma view específica, processando as requisições HTTP e retornando a resposta correspondente.
- **Templates**: Os templates HTML são organizados para reutilizar blocos comuns, como tabelas e formulários, oferecendo uma interface clara e eficiente.
- **URLs**: As rotas são configuradas no arquivo `urls.py`, direcionando as requisições para as views correspondentes.

## 📁 **Estrutura de Diretórios**

- `app_forms/`: Aplicação Django responsável por gerenciar as operações relacionadas aos clientes.
- `models.py`: Define o modelo de dados do cliente.
- `views.py`: Controla a lógica do CRUD.
- `forms.py`: Define os formulários utilizados no cadastro e edição.
- `templates/`: Contém os arquivos HTML para renderizar a interface do sistema.
- `db.sqlite3`: Banco de dados utilizado para armazenar os registros dos clientes.
- `manage.py`: Ferramenta para gerenciamento do projeto Django.
