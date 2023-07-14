## Teste: 

Criar uma Aplicação Web usando Python e Flask com integração com duas APIs públicas e gratuitas. 

  

## Passo a passo: 

- [x] Crie uma aplicação web utilizando Flask e Python, sem regras de login, logout e usuários.

- [x] Crie uma rota “/busca” usando Blueprints e carregue uma página html onde possua um sistema de abas, sendo duas abas fixas e o restante dinâmicas.

- [x] Em uma das abas fixas, carregue um formulário usando o Flask_WTF, para buscar o CEP na api https://viacep.com.br/. Ao clicar em Buscar, o javascript deve fazer uma requisição para outra rota no flask que vai fazer requisição para a API usando a biblioteca request e renderize a página html com os dados usando o Jinja.

- [x] O retorno da busca do CEP deve ser renderizado na mesma tela sem recarregar a página, trazendo o resultado em uma nova aba no sistema de abas, que deve retornar um outro template html dentro da aba com uma tabela usando o Datatable. Essa tabela deve conter apenas os campos “cep” e “logradouro” da api https://viacep.com.br/ e o restante dos campos devem retornar em uma subtabela dentro da mesma tabela, que deve ter um botão “+”, que ao ser clicado deve aparecer a subtabela na respectiva linha e deve ser omitida ao clicar no botão “-”.

- [x] Na outra aba fixa, carregue um formulário usando o Flask_WTF, para buscar pelo IP na api https://ipapi.co/api/#complete-location. Ao clicar em Buscar, o javascript deve fazer uma requisição para outra rota no flask que vai renderizar a página html em outra aba.

- [x] No retorno da busca do IP , deve renderizar um html de resultado com uma tabela usando o Datatable, porém os dados da tabela devem ser preenchidos via requisição no Javascript ao carregar a aba. Onde também deve ser mostrado apenas os campos “city” e “country_code” e o restante dos campos devem retornar em uma subtabela dentro da mesma tabela, que deve ter um botão “+”, que ao ser clicado deve aparecer a subtabela na respectiva linha e deve ser omitida ao clicar no botão “-”.
 
- [x] Os Datatables devem ter paginação na tabela principal.

- [x] Crie um arquivo Dockfile e docker-compose.yaml para rodar o container da aplicação WEB. 

- [x] Suba o projeto no seu Github e nos envie o link do projeto.
 

## Observações:

- Todas as lógicas no front-end deve ser utilizando Javascript Puro, podendo utilizar somente as libs JQuery, Datatable, Bootstrap e FormValidation.
- Os formulários devem possuir validações.
- Capriche no visual, pois será levado em conta na escolha do candidato.

## APIs para consumo:
- https://viacep.com.br/
- https://ipapi.co/api/#complete-location