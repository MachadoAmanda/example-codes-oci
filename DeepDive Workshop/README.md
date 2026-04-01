# Evento DeepDive Oracle
Para seguir esse laboratório, você precisa estar conectado na sua console Oracle Cloud Infraestruture.

### Passo 1 - Criando e configurando o ambiente

Nesse passo vamos fazer a inicialização dos serviços utilizados, criação de um Autonomous AI Database e de um AI Data Platform diretamente pelo console da OCI. 

#### 1.1 - Criando o Autonomous AI Database

Clicando no menu de hamburguer, parte superior esquerda da tela, você tem acesso ao menu de serviços disponíveis na OCI. Com o menu aberto, busque Oracle AI Database e Autonomous AI Database, abrindo esse serviço.

![alt text](image.png)

Verifique se você está no compartimento correto, você pode criar em qualquer um, e clique no botão de criar autonomous AI database.

![alt text](image-2.png)

Na tela de criação, adicione o nome do seu banco de dados autônomo como `DeepDiveAutonomousDatabase`, nos dois campos. E escolha a opção Transaction Processing para o tipo do seu banco.

![alt text](image-4.png)

Descendo um pouco mais a tela, selecione a versão do banco como `26ai` e storage como 100GB nas configurações.

![alt text](image-5.png)

![alt text](image-6.png)

Por fim, na parte de credencial da mesma tela, crie uma senha que você consiga lembrar para o usuário administrador do banco `admin`. A senha deve:
- Ser de 12 a 30 caracteres
- Ter pelo menos uma letra maiúscula e um numero
- Não pode conter aspas duplas ou simples, nem o nome do usuário

Quando a senha estiver correta, clique no botão inferior direito para confirmar as informações e seguir para criação do banco.

![alt text](image-7.png)

As demais informações da configuração, devem ser deixadas como padrão. Seu banco deve passar para o estado de provisionamento e abrir automaticamente a tela a seguir.

![alt text](image-8.png)

Aguarde até que o provisionamento seja efetivado e o banco esteja ativo.

![alt text](image-9.png)

#### 1.2 Criação do AI Data Platform

Assim como a criação do banco de dados, vamos iniciar a criação da plataforma de dados, nela vamos poder criar um catalogo, manipular volumes, manipular os dados e até criar aplicações inteligentes. A plataforma de dados é o centralizador de uma boa estratégia de dados. Para iniciar a criação, acesse o menu lateral e procure `Analytics & AI`, clicando nessa opção, você deve acessar o serviço `AI Data Platform Workbench`.

![alt text](image-10.png)

Avalie se você está no compartimento correto, assim como no autonomous esse serviço pode ser criado em qualquer compartimento da sua escolha. E clique no botão de criação.

![alt text](image-12.png)

Na tela de criação vamos preencher algumas propriedades abaixo. Primeiro vamos adicionar um nome para o AIDP e um nome para o espaço de trabalho que ele criará internamente, chamado de workspace. Vamos colocar `DeepDiveAIDP` e `DeepDiveWorkspace`.

![alt text](image-14.png)

Descendo a tela, selecione a opção ALH de criar um novo, e adicione uma senha para a plataforma, recomendamos colocar a mesma adicionada no Autonomous anteriormente para facilitar.

![alt text](image-15.png)

Para finalizar, vamos selecionar a opção Standard de politicas de segurança e clicar no botão de criação para confirmar a configuração selecionada.

![alt text](image-16.png)

Nesse momento você será redirecionado para a tela de inicio do serviço, com seu AIDP estando em estado de criação.

![alt text](image-17.png)

---
### Passo 2 - Ingestão dos dados
#### 2.1 Fazendo a ingestão de dados via Autonomous

Vamos realizar dois tipos de ingestão nesse laboratório, uma direto no Autonomous e outra no AIDP, sessão 2.2. Acesse a sua instância ativa no Autonomous.

![alt text](image.png)

Clique no nome do banco.

![alt text](image-18.png)

Dentro da tela do banco, abra o menu de `database actions` e clique em `SQL`. Essa ação vai abrir a tela de workspace do banco para execução de SQL dentro do banco.

![alt text](image-20.png)

Abrindo a tela de SQL, vamos submeter o seguinte comando no banco:

```` sql
CREATE TABLE BRONZE_WC_MATCHES (
    key_id NUMBER,
    tournament_id VARCHAR2(50),
    tournament_name VARCHAR2(200),
    match_id VARCHAR2(100),
    match_name VARCHAR2(200),
    stage_name VARCHAR2(100),
    group_name VARCHAR2(100),
    group_stage NUMBER,
    knockout_stage NUMBER,
    replayed NUMBER,
    replay NUMBER,
    match_date VARCHAR2(50),
    match_time VARCHAR2(50),
    stadium_id VARCHAR2(50),
    stadium_name VARCHAR2(200),
    city_name VARCHAR2(100),
    country_name VARCHAR2(100),
    home_team_id VARCHAR2(50),
    home_team_name VARCHAR2(100),
    home_team_code VARCHAR2(10),
    away_team_id VARCHAR2(50),
    away_team_name VARCHAR2(100),
    away_team_code VARCHAR2(10),
    score VARCHAR2(20),
    home_team_score NUMBER,
    away_team_score NUMBER,
    home_team_score_margin NUMBER,
    away_team_score_margin NUMBER,
    extra_time NUMBER,
    penalty_shootout NUMBER,
    score_penalties VARCHAR2(20),
    home_team_score_penalties NUMBER,
    away_team_score_penalties NUMBER,
    result VARCHAR2(50),
    home_team_win NUMBER,
    away_team_win NUMBER,
    draw NUMBER
);
````
Execute o comando no botão verde de `Run Statement`. 

![alt text](image-21.png)

Esse comando vai criar uma tabela com a estrutura requerida, todas as colunas e tipos listados no próprio comando. Após a criação, vamos agora copiar os dados para dentro da tabela, para isso, rode o seguinte comando:

```` sql
BEGIN
  DBMS_CLOUD.COPY_DATA(
    table_name => 'BRONZE_WC_MATCHES',
    credential_name => NULL,
    file_uri_list => 'https://objectstorage.us-chicago-1.oraclecloud.com/n/idajmumkp9ca/b/DeepDiveWorkshopData/o/worldcup_matches.csv',
    format => json_object(
        'type' value 'csv',
        'skipheaders' value '1'
    )
  );
END;
````

Esse comando busca o csv em um repositório publico e copia seus dados para a tabela que foi criada anteriormente. Após executado, você pode visualizar os dados via comando SELECT, adicione esse comando abaixo e clique em executar novamente.

```` sql
SELECT * FROM BRONZE_WC_MATCHES
````
![alt text](image-22.png)

Ou, você pode visualizar na própria console, buscando o nome da tabela na lateral, clicando com o botão direito do mouse e `Open`.

![alt text](image-23.png)

Automaticamente vai abrir uma aba lateral com os dados da tabela, colunas, dados, gatilhos e outras propriedades da tabela criada.

![alt text](image-24.png)

#### 2.2 Ingestão dos dados via AIDP

Na sequência, vamos fazer a ingestão do segundo dataset, agora de outra maneira, via AIDP. Para isso, vamos acessar o AIDP criado anteriormente.

![alt text](image-10.png)

Clique no nome da sua plataforma de dados para acessar e faça o login.

![alt text](image-25.png)

Essa é a pagina principal do AIDP, você já pode ver no menu lateral seu catalogo de dados, workspace, workflows, agentes e demais informações.

![alt text](image-27.png)

#### 2.3 Criando um catalogo dentro do AIDP

Vamos primeiro criar um catalogo apontando para o autonomous que criamos anteriormente. Para isso, clique em `create` no menu lateral.

![alt text](image-28.png)

O nome do nosso catalogo vai ser `DeepDiveCatalog_Bronze` e vamos colocar como tipo de conexão externa, escolhendo o nosso Autonomous previamente criado. Preencha as demais informações na sequência da tela como na imagem abaixo.

![alt text](image-30.png)

Depois da opção de serviço, você deve preencher a mesma senha do autonomous na caixa de texto da wallet e senha, e deixar o usuário como `admin`. Teste a conexão antes de seguir no botão de criar. Se a conexão estiver correta, siga para criação.

![alt text](image-32.png)

Seu catalogo deve iniciar o processo de criação.

![alt text](image-33.png)

Quando o catalogo for finalizado, você já conseguirá visualizar as tabelas que existem no Autonomous com seu respectivo schema.

![alt text](image-34.png)

#### 2.5 Importando o notebook do laborátorio dentro do workspace

Para importar o notebook, vamos primeiro acessar o workspace do menu lateral.

![alt text](image-35.png)

O workspace já vem com uma pasta criada que se chama `Shared` com exemplos. Para importar o notebook do laboratório, você deve primeiro ter realizado o download dele na sua máquina. Depois, clique no botão com o icone de upload, indicado na imagem abaixo.

![alt text](image-37.png)

Busque seu arquivo no seu repositório, e clique em upload para submeter ele.

![alt text](image-38.png)

Seu arquivo vai ser adicionado imediatamente no workspace. E você já pode abrir ele clicando no nome do notebook.

![alt text](image-39.png)

Repare que ao abrir o seu notebook, no centro superior da tela, indica `no cluster attached`. Assim, chegamos ao último passo de configuração para você conseguir realizar todos os laboratórios da sessão 1 e 2, que é a criação do cluster. Clique no canto superior direito no botão de cluster e na sequência em `Create Cluster`.

![alt text](image-40.png)

Uma aba se abrirá imediatamente, basta adicionar o nome e as configurações desejadas. No nosso caso, inserimos o nome como `DeepDiveCluster` e deixamos as configurações padrão, clicando em `Create` para confirmar a criação.

![alt text](image-42.png)

Aguarde um momento para que o cluster seja criado, se ele não for automaticamente adereçado ao seu notebook, vá novamente no botão cluster e busque a opção de `attach a cluster`, selecionando o que foi previamente criado. 

![alt text](image-43.png)

Até que o cluster esteja ativo no notebook.
![alt text](image-44.png)
![alt text](image-45.png)

#### 2.6 Importando o notebook para a sessão 2

Repita o mesmo processo de upload para o arquivo jupyter da segunda sessão.

![alt text](image-46.png)

Com isso, você terá todos os notebooks necessários para realizar as sessões práticas direto no seu workspace.

![alt text](image-47.png)

Agora, você tem um ambiente completamente configurado e pode seguir as instruções do próprio jupyter junto com o instrutor para executar os laboratórios. 

