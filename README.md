##### Code is Shit, because:
Isso é um prototipo ainda, ta tudo hardcoded porquê é um prototipo, só queria provar pra mim mesmo que funciona, provavelmente não
será usado python mas alguma outra linguagem caso eu detecte problemas de perfomance. Qualquer dia que eu parar pra mexer nisso eu posto os requisitos de forma menos amadora. 


##### Projeto
```
Interface Web --- > API_CLIENT ----> Host Docker
```

Serviços distintos, supondo que a interface web e a API_CLIENT fiquem no mesmo host, deve existir comunicação com o host docker que estará num servidor remoto, o programa contido nesse arquivo seria o serviço que estaria rodando no host docker por solicitações da api_client.

A ideia é que na interface web exista uma espécie de CGI/Client da API que irá comunicar com a API que estará no HOST DOCKER.

Formato de payload que a API_CLIENT deve utilizar para comunicar com o Host Docker:
**[ACTION+TARGET]**

###### Exemplo:
```
run container_name
stop container_name
kill container_name
restart container_name
```

##### Todo 
- Montar uma página web que irá interagir com o api-client 
- Implementar e Testar o start,restart,stop de containers
- Implementar o TTL para 60 minutos de cada container
- Restringir o acesso do container ao IP de origem do start atráves de regras de firewall e porta.
- Criar um daemon, daemonitizar o programa. hue

##### RTFM STUFF
- https://www.programmableweb.com/api/docker
- https://docs.docker.com/develop/sdk/#sdk-and-api-quickstart
- https://docs.docker.com/engine/api/v1.39/#operation/ContainerCreate
- https://docker-py.readthedocs.io/en/stable/containers.html
