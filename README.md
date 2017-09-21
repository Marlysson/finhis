# Relatório da aplicação

## Questão 1 ( Modelos )

> Como foi implementado

Foi utilizado os modelos do django refletindo um diagrama de classes elaborado. Se valendo pelos relacionamentos de ForeignKey e ManyToManyField

> Arquivos trabalhados:

https://github.com/Marlysson/finhis/blob/master/core/models.py

> Como validar e testar

Essa parte dos modelos é mais a base da aplicação, a parte de testar e validar será mostrada mais à frente;

## Questão 2 ( Esquema de autenticação )

> Como foi implementado

**Foram utilizadas 2 formas de autenticação**
 
- TokenAuthentication ( ```rest_framework.authentication.TokenAuthentication``` )
- BasicAuthentication ( ```'rest_framework.authentication.BasicAuthentication``` )

**PASSOS**

- [x] Adicionado a aplicação que faz a obtenção do token no INSTALLED_APPS ( [settings.py](https://github.com/Marlysson/finhis/blob/master/finhis/settings.py) )
- [x] Mapeado a url que fará com que o cliente possa requisitar um token. ( [url.py](https://github.com/Marlysson/finhis/blob/master/finhis/urls.py) )
- [x] No momento da criação de cada usuário é criado um ```Token``` associado à ele passar posteriormente ser feito autenticação. ( [views.py](https://github.com/Marlysson/finhis/tree/master/core/views.py) )

> Como validar e testar

Essa funcionalidade está validada no arquivo de testes localizado em : [testes.py](https://github.com/Marlysson/finhis/blob/master/core/tests.py)

E para executar basta entrar na raiz do projeto e executar o comando:

```
python manage.py test core.tests
```

