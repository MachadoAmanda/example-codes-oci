# Evento DeepDive Oracle
Para seguir esse laboratório, você precisa estar conectado na sua console Oracle Cloud Infraestruture.

### Passo 1 - Criando e configurando o ambiente

Nesse passo vamos fazer a inicialização dos serviços utilizados, criação de um Autonomous AI Database e de um AI Data Platform diretamente pelo console da OCI. 

#### 1.1 - Criando o Autonomous AI Database

Clicando no menu de hamburguer, parte superior esquerda da tela, você tem acesso ao menu de serviços disponíveis na OCI. Com o menu aberto, busque Oracle AI Database e Autonomous AI Database, abrindo esse serviço.

<img width="1913" height="1030" alt="image" src="https://github.com/user-attachments/assets/15e75f59-ab1a-4395-afc0-f8c75fcd5b44" />

Verifique se você está no compartimento correto, você pode criar em qualquer um, e clique no botão de criar autonomous AI database.

<img width="1890" height="642" alt="image-2" src="https://github.com/user-attachments/assets/d0134d24-bce9-4a46-b195-7db8700381b6" />

Na tela de criação, adicione o nome do seu banco de dados autônomo como `DeepDiveAutonomousDatabase`, nos dois campos. E escolha a opção Transaction Processing para o tipo do seu banco.

<img width="1896" height="972" alt="image-4" src="https://github.com/user-attachments/assets/59a45429-a30c-40ce-8695-a4af0f58eea6" />

Descendo um pouco mais a tela, selecione a versão do banco como `26ai` e storage como 100GB nas configurações.

<img width="1463" height="471" alt="image-5" src="https://github.com/user-attachments/assets/39f0ac5d-5c1f-46c1-8122-98a2bce13c05" />

<img width="1302" height="372" alt="image-6" src="https://github.com/user-attachments/assets/a5ba0ac6-e375-4684-9aba-53884ac32d35" />

Por fim, na parte de credencial da mesma tela, crie uma senha que você consiga lembrar para o usuário administrador do banco `admin`. A senha deve:
- Ser de 12 a 30 caracteres
- Ter pelo menos uma letra maiúscula e um numero
- Não pode conter aspas duplas ou simples, nem o nome do usuário

Quando a senha estiver correta, clique no botão inferior direito para confirmar as informações e seguir para criação do banco.

<img width="1912" height="990" alt="image-7" src="https://github.com/user-attachments/assets/9c9867c2-aa13-47fe-ae44-3a8a37511a40" />

As demais informações da configuração, devem ser deixadas como padrão. Seu banco deve passar para o estado de provisionamento e abrir automaticamente a tela a seguir.

<img width="1878" height="392" alt="image-8" src="https://github.com/user-attachments/assets/0f304048-0c35-408a-adf0-823242352de9" />

Aguarde até que o provisionamento seja efetivado e o banco esteja ativo.

<img width="1883" height="431" alt="image-9" src="https://github.com/user-attachments/assets/0df54478-57a7-4591-bc1c-fc7a4896d838" />

#### 1.2 Criação do AI Data Platform

Assim como a criação do banco de dados, vamos iniciar a criação da plataforma de dados, nela vamos poder criar um catalogo, manipular volumes, manipular os dados e até criar aplicações inteligentes. A plataforma de dados é o centralizador de uma boa estratégia de dados. Para iniciar a criação, acesse o menu lateral e procure `Analytics & AI`, clicando nessa opção, você deve acessar o serviço `AI Data Platform Workbench`.

<img width="1912" height="975" alt="image-10" src="https://github.com/user-attachments/assets/4a8a4382-9635-441b-b0f8-95ca3b210718" />

Avalie se você está no compartimento correto, assim como no autonomous esse serviço pode ser criado em qualquer compartimento da sua escolha. E clique no botão de criação.

<img width="1896" height="392" alt="image-12" src="https://github.com/user-attachments/assets/8d6231f0-e820-4efa-b269-2ca27855da3a" />

Na tela de criação vamos preencher algumas propriedades abaixo. Primeiro vamos adicionar um nome para o AIDP e um nome para o espaço de trabalho que ele criará internamente, chamado de workspace. Vamos colocar `DeepDiveAIDP` e `DeepDiveWorkspace`.

<img width="1892" height="977" alt="image-14" src="https://github.com/user-attachments/assets/db01d12a-662e-4b65-9446-9c2a7f60f388" />

Descendo a tela, selecione a opção ALH de criar um novo, e adicione uma senha para a plataforma, recomendamos colocar a mesma adicionada no Autonomous anteriormente para facilitar.

<img width="1447" height="558" alt="image-15" src="https://github.com/user-attachments/assets/0d92b281-53e8-4f68-88f6-9f353f161077" />

Para finalizar, vamos selecionar a opção Standard de politicas de segurança e clicar no botão de criação para confirmar a configuração selecionada.

<img width="1906" height="885" alt="image-16" src="https://github.com/user-attachments/assets/e11fe0a0-6f83-4f4c-b8de-1a45506f9f9f" />

Nesse momento você será redirecionado para a tela de inicio do serviço, com seu AIDP estando em estado de criação.

<img width="1457" height="328" alt="image-17" src="https://github.com/user-attachments/assets/ece11ab6-2d0d-46e8-a58c-fc60d5402375" />

---
### Passo 2 - Ingestão dos dados
#### 2.1 Fazendo a ingestão de dados via Autonomous

Vamos realizar dois tipos de ingestão nesse laboratório, uma direto no Autonomous e outra no AIDP, sessão 2.2. Acesse a sua instância ativa no Autonomous.

<img width="1913" height="1030" alt="image" src="https://github.com/user-attachments/assets/15e75f59-ab1a-4395-afc0-f8c75fcd5b44" />

Clique no nome do banco.

<img width="1745" height="147" alt="image-18" src="https://github.com/user-attachments/assets/8295a07b-00cf-475a-9d05-5162b971997e" />

Dentro da tela do banco, abra o menu de `database actions` e clique em `SQL`. Essa ação vai abrir a tela de workspace do banco para execução de SQL dentro do banco.

<img width="1907" height="692" alt="image-20" src="https://github.com/user-attachments/assets/6f50ecf6-b81b-4e36-a868-63a40fd25081" />

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

<img width="1910" height="574" alt="image-21" src="https://github.com/user-attachments/assets/acccea84-7850-450b-925f-a1edeb35a516" />

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
<img width="1508" height="568" alt="image-22" src="https://github.com/user-attachments/assets/6915ad7d-d8c7-4c55-8caa-1482bd686712" />

Ou, você pode visualizar na própria console, buscando o nome da tabela na lateral, clicando com o botão direito do mouse e `Open`.

<img width="722" height="523" alt="image-23" src="https://github.com/user-attachments/assets/02ed2fe2-b542-47a3-b849-77c009706b5e" />

Automaticamente vai abrir uma aba lateral com os dados da tabela, colunas, dados, gatilhos e outras propriedades da tabela criada.

<img width="1913" height="1031" alt="image-24" src="https://github.com/user-attachments/assets/e4a22a20-e804-43ea-a52e-52ad7c777d1e" />

#### 2.2 Ingestão dos dados via AIDP

Na sequência, vamos fazer a ingestão do segundo dataset, agora de outra maneira, via AIDP. Para isso, vamos acessar o AIDP criado anteriormente.

<img width="1912" height="975" alt="image-10" src="https://github.com/user-attachments/assets/4a8a4382-9635-441b-b0f8-95ca3b210718" />

Clique no nome da sua plataforma de dados para acessar e faça o login.

<img width="1467" height="392" alt="image-25" src="https://github.com/user-attachments/assets/104dd9c1-8a43-43c9-9ef3-8ebd5229fea8" />

Essa é a pagina principal do AIDP, você já pode ver no menu lateral seu catalogo de dados, workspace, workflows, agentes e demais informações.

<img width="1901" height="550" alt="image-27" src="https://github.com/user-attachments/assets/580b399f-bd3a-4ef3-9233-5f8f95c59be4" />

#### 2.3 Criando um catalogo dentro do AIDP

Vamos primeiro criar um catalogo apontando para o autonomous que criamos anteriormente. Para isso, clique em `create` no menu lateral.

<img width="1547" height="463" alt="image-28" src="https://github.com/user-attachments/assets/1f78b5f4-13cc-434e-a379-fc297cdc8ade" />

O nome do nosso catalogo vai ser `DeepDiveCatalog_Bronze` e vamos colocar como tipo de conexão externa, escolhendo o nosso Autonomous previamente criado. Preencha as demais informações na sequência da tela como na imagem abaixo.

<img width="1905" height="1026" alt="image-30" src="https://github.com/user-attachments/assets/03d7af96-a415-4f3a-80e7-184ae9704bd9" />

Depois da opção de serviço, você deve preencher a mesma senha do autonomous na caixa de texto da wallet e senha, e deixar o usuário como `admin`. Teste a conexão antes de seguir no botão de criar. Se a conexão estiver correta, siga para criação.

<img width="1045" height="548" alt="image-32" src="https://github.com/user-attachments/assets/bf8b6c9a-dd04-41e3-8972-bf173f9f2f06" />

Seu catalogo deve iniciar o processo de criação.

<img width="1234" height="53" alt="image-33" src="https://github.com/user-attachments/assets/40831924-3c9a-449d-a14f-913977ccba9e" />

Quando o catalogo for finalizado, você já conseguirá visualizar as tabelas que existem no Autonomous com seu respectivo schema.

<img width="368" height="175" alt="image-34" src="https://github.com/user-attachments/assets/7e69ac71-f59a-49a9-a180-7dacf528a33a" />

#### 2.5 Importando o notebook do laborátorio dentro do workspace

Para importar o notebook, vamos primeiro acessar o workspace do menu lateral.

<img width="1908" height="552" alt="image-35" src="https://github.com/user-attachments/assets/7d79eb5d-b225-4e3b-ab52-1d16164bc6c8" />

O workspace já vem com uma pasta criada que se chama `Shared` com exemplos. Para importar o notebook do laboratório, você deve primeiro ter realizado o download dele na sua máquina. Depois, clique no botão com o icone de upload, indicado na imagem abaixo.

<img width="1907" height="432" alt="image-37" src="https://github.com/user-attachments/assets/37850300-084e-432b-84d9-7fd5cc83948a" />

Busque seu arquivo no seu repositório, e clique em upload para submeter ele.

<img width="1237" height="1017" alt="image-38" src="https://github.com/user-attachments/assets/c48bb726-67b4-4d90-b247-7292d708466a" />

Seu arquivo vai ser adicionado imediatamente no workspace. E você já pode abrir ele clicando no nome do notebook.

<img width="800" height="88" alt="image-39" src="https://github.com/user-attachments/assets/0a94086a-bf69-4213-ad3f-1a511f3e2702" />

Repare que ao abrir o seu notebook, no centro superior da tela, indica `no cluster attached`. Assim, chegamos ao último passo de configuração para você conseguir realizar todos os laboratórios da sessão 1 e 2, que é a criação do cluster. Clique no canto superior direito no botão de cluster e na sequência em `Create Cluster`.

<img width="1647" height="413" alt="image-40" src="https://github.com/user-attachments/assets/624bb611-e2c6-45b4-96e7-070b9f42e091" />

Uma aba se abrirá imediatamente, basta adicionar o nome e as configurações desejadas. No nosso caso, inserimos o nome como `DeepDiveCluster` e deixamos as configurações padrão, clicando em `Create` para confirmar a criação.

<img width="1323" height="998" alt="image-42" src="https://github.com/user-attachments/assets/5c162ec8-ef44-47b9-b82e-1b834e1f079a" />

Aguarde um momento para que o cluster seja criado, se ele não for automaticamente adereçado ao seu notebook, vá novamente no botão cluster e busque a opção de `attach a cluster`, selecionando o que foi previamente criado. 

<img width="1315" height="301" alt="image-43" src="https://github.com/user-attachments/assets/09977d3e-af1c-49bf-9a81-9ad2ba7431f6" />

Até que o cluster esteja ativo no notebook.

<img width="505" height="74" alt="image-44" src="https://github.com/user-attachments/assets/ac673755-9172-4751-b9db-e974a39baa82" />
<img width="490" height="77" alt="image-45" src="https://github.com/user-attachments/assets/447118ef-acff-4b1c-aa8b-c32c9a213cd4" />

#### 2.6 Importando o notebook para a sessão 2

Repita o mesmo processo de upload para o arquivo jupyter da segunda sessão.

<img width="1238" height="1017" alt="image-46" src="https://github.com/user-attachments/assets/23809cbb-1f90-45de-8fa2-7d45708e4cf1" />

Com isso, você terá todos os notebooks necessários para realizar as sessões práticas direto no seu workspace.

<img width="1646" height="437" alt="image-47" src="https://github.com/user-attachments/assets/c2e2771f-911f-41aa-bf37-1db0d766338a" />

Agora, você tem um ambiente completamente configurado e pode seguir as instruções do próprio jupyter junto com o instrutor para executar os laboratórios. 

