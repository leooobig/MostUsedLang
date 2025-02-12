# GitLangAnalyzer

Ola, este projeto tem a funcionalidade de extrair dados de um usuário do GitHub, analisando todos seus repositórios, pegando o nome e linguagem predominante de cada um deles.


Antes de tudo crie seu token de acesso para conseguir utilizar os dados da API: https://docs.github.com/pt/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization


Abaixo vou apresentar um tutorial de como utilizar:

> Clone o repositório a partir deste comando no terminal: ```git clone git@github.com:leooobig/GitLangAnalyzer.git```

Para extrair os dados, você vai precisar do username do perfil que deseja utilizar, entre no perfil desta pessoa ou empresa e copie o nome a partir da barra de pesquisa:

> Copie somente o username: ```https://github.com/**username**```.

Agora no compilador:


> Renomeie o arquivo "env-example.txt" para ".env" e coloque seu token de acesso no **"API_TOKEN"**


> Dentro de "main.py", coloque o username que copiamos anteriormente e depois só rodar o código e será gerado um arquivo .csv com todas as informações requeridas

