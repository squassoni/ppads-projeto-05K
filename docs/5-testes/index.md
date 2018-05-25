# Plano de testes

Para cada caso de uso, elabore um **procedimento de teste** para testar o cenário principal.

Em cada procedimento de teste, siga o modelo abaixo:

**Nome do caso de uso:** Consultar tarefas

**Preparação:**

* Criar no sistema um usuário com o perfil de **Funcionário**.
* Cadastrar 5 tarefas para o usuário criado.

**Procedimento de teste:**

| Passo | Procedimento | Resultado esperado |
| --- | --- | --- |
| 1 | Executar o navegador Chrome e acesse a URL https://teste.mackenzie.br | Apresentação da tela de login do sistema |
| 2 | Preencher os campos **login** e **password** com os dados de um usuário com perfil de **Funcionário**. | Apresentação do painel do Funcionário |
| 3 | Clicar no link **Listar todas as tarefas**. | Apresentação das 5 tarefas cadastradas para o funcionário. |

****************************************************************************************************************************************

**Nome do caso de uso:** Marcar Consulta

**Preparação:**

* Criar no sistema um usuário com o perfil de **Funcionário** ou **Paciente**.
* Ter Profissionais cadastrados e horários disponíveis

**Procedimento de teste:**

| Passo | Procedimento | Resultado esperado |
| --- | --- | --- |
| 1 | Executar o navegador Chrome e acesse a URL http://ppads-dev2.us-west-2.elasticbeanstalk.com/login | Apresentação da tela de login do sistema |
| 2 | Preencher os campos **login** e **password** com os dados de um usuário com perfil de **Funcionário** ou **Paciente**. | Apresentação do painel do Funcionário |
| 3 | Clicar no link **Criar Consulta**. | Apresentação de formulário de agendamento |

****************************************************************************************************************************************
**Nome do caso de uso:** Realizar Cadastro

**Preparação:**

**Procedimento de teste:**

| Passo | Procedimento | Resultado esperado |
| --- | --- | --- |
| 1 | Executar o navegador Chrome e acesse a URL http://ppads-dev2.us-west-2.elasticbeanstalk.com/login | Apresentação da tela de login do sistema |
| 2 | Clicar em **Cadastrar** | Apresentação do formulário de cadastro de Usuário |

****************************************************************************************************************************************
**Nome do caso de uso:** Alterar Consulta

**Preparação:**

* Ter Agendamentos cadastrados

**Procedimento de teste:**

| Passo | Procedimento | Resultado esperado |
| --- | --- | --- |
| 1 | Executar o navegador Chrome e acesse a URL http://ppads-dev2.us-west-2.elasticbeanstalk.com/login | Apresentação da tela de login do sistema |
| 2 | Preencher os campos **login** e **password** com os dados de um usuário com perfil de **Funcionário** ou **Paciente**. | Apresentação do painel do Funcionário |
| 3 | Clicar no link **Agenda**. | Apresentação de formáliro de agendamento |
| 4 | Selecionar consulta a ser Alterada | Apresentação de formulário de alteração |

****************************************************************************************************************************************
**Nome do caso de uso:** Cancelar Consulta

**Preparação:**

* Ter Agendamentos cadastrados

**Procedimento de teste:**

| Passo | Procedimento | Resultado esperado |
| --- | --- | --- |
| 1 | Executar o navegador Chrome e acesse a URL http://ppads-dev2.us-west-2.elasticbeanstalk.com/login | Apresentação da tela de login do sistema |
| 2 | Preencher os campos **login** e **password** com os dados de um usuário com perfil de **Funcionário** ou **Paciente**. | Apresentação do painel do Funcionário |
| 3 | Clicar no link **Agenda**. | Apresentação de formáliro de agendamento |
| 4 | Selecionar consulta a ser Cancelada | Apresentação de formulário de cancelamento |

****************************************************************************************************************************************
**Nome do caso de uso:** Realizar Consulta

**Preparação:**

* Ter Agendamentos cadastrados

**Procedimento de teste:**

| Passo | Procedimento | Resultado esperado |
| --- | --- | --- |
| 1 | Executar o navegador Chrome e acesse a URL http://ppads-dev2.us-west-2.elasticbeanstalk.com/login | Apresentação da tela de login do sistema |
| 2 | Preencher os campos **login** e **password** com os dados de um usuário com perfil de **Profissional** | Apresentação do painel do Profissional |
| 3 | Clicar no link **Agenda**. | Apresentação de formáliro de agendamento |
| 4 | Selecionar consulta a ser realizada | Apresentação de formulário de consulta |
