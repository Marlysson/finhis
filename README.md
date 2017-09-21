# Relatório da aplicação

## Questão 1 ( Modelos )

> Como foi implementado

Foi utilizado os modelos do django refletindo um diagrama de classes elaborado. Se valendo pelos relacionamentos de ForeignKey e ManyToManyField, e estão localizados em : [models.py](https://github.com/Marlysson/finhis/blob/master/core/models.py)

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

## Questão 3 ( Autenticação )

> Como foi feito

Foi usado a classe de permissão padrão do DRF chamada ```IsAuthenticated``` e para cada classe que fosse necessário era adicionada à uma tupla de um atributo responsável por mapear atributos de permissões na [view.py](https://github.com/Marlysson/finhis/blob/master/core/views.py).

#### Views autenticadas

- ProfileViewList
- RequestCategoryViewList
- RequestCategoryViewDetail
- MovementViewDetail

#### Views não-autenticadas

- ProfileViewDetail
- CategoryViewList
- CategoryViewDetail
- MovementViewDetail

> Exemplo de código

```
class RequestCategoryViewList(RequestCategoryDataRepeated,generics.ListCreateAPIView):
	name = 'request-category-list'
	permission_classes = (IsAuthenticated,)

```

> Como validar e testar

Há duas formas: acessando via browser e vendo a mensagem solicitando a permissão, ou executar os testes da aplicação, como é dito na questão acima.

## Questão 4 ( Documentação )

> Como foi implementado

Basicamente foi instaldo o drf-docs via pip , adicionado a aplicação no INSTALLED_APPS e depois mapeado a url para ser acessada, que está localizada em : [urls.py](https://github.com/Marlysson/finhis/blob/master/finhis/urls.py)

> Como validar e testar

Basicamente rodando o projeto e acessando a [url da documentação](http://localhost:8000/docs)


## Questão 5 ( Paginação e Throttling)

> Como foi feito

Basicamente foi utilizado os parâmetros default que o próprio DRF provê, e só bastou adicionar eles no arquivo [settings.py](https://github.com/Marlysson/finhis/blob/master/finhis/settings.py)

Código do trecho:

```
PAGINATION_REST = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5
}

THROTTLING_REST = {
    'DEFAULT_THROTTLE_CLASSES': ('rest_framework.throttling.AnonRateThrottle',
                                 'rest_framework.throttling.UserRateThrottle',),

    'DEFAULT_THROTTLE_RATES': {'anon': '10/hour', 'user': '120/hour'}
}

REST_FRAMEWORK = {}
REST_FRAMEWORK.update(PAGINATION_REST)
REST_FRAMEWORK.update(THROTTLING_REST)

```