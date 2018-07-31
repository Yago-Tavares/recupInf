# Aplicação simples usando google appengine

## Configurando o ambiente de desenvolvimento

* Faça o download do sdk apropriado para o seu sistema neste link [https://cloud.google.com/sdk/docs](https://cloud.google.com/sdk/docs)
* Abra o terminal e execute os seguintes comandos:
```shell
cd [diretório onde o sdk foi salvo]
tar -zvxf [nome do .tar.gz baixado]
cd google-cloud-sdk…
mv google-cloud-sdk ~/
cd
./google-cloud-sdk/install.sh (siga as dicas que o instalador dará)
bash
```

## Inicializando aplicação
#### Faça um clone deste repositório ou crie uma aplicação
* No terminal, navegue até o diretório do seu projeto onde está localizado o arquivo main.py
* digite o comando ```python main.py```
* A aplicação estará rodando no: http://http://localhost:8081/

> Para mais informações leia a documentação disponível em: [https://cloud.google.com/appengine/docs/standard/python](https://cloud.google.com/appengine/docs/standard/python)
