# API Receita CPF

### Acessando a API de CPF

Para acessar a API, um CPF no formato de {11} dígitos deve ser fornecido, por exemplo: "01001000110".
Após o CPF, deve ser fornecido o tipo de retorno desejado, que deve ser "*json*" ou "*api*".

#### Exemplo de pesquisa por CPF

api-receita-cpf.herokuapp.com/cpf/01001000110/?format=json

### Formato de Retorno (json)

Veja o exemplo de acesso à API e o tipo de retorno:

```
[
    {
        "NUM_CPF": "01001000110",
        "NOME": "FULANO DE TAL",
        "DATA_NASCIMENTO": "2000-01-01",
        "IND_SEXO": "M",
        "NOME_MAE": "FULANA DE TAL",
        "NUM_TITULO_ELEITOR": "000000000000",
        "TIPO_LOGRADOURO": "RUA",
        "DESCR_LOGRADOURO": "NOME DA RUA",
        "NUM_LOGRADOURO": "00",
        "DESCR_COMPLEMENTO_LOGRADOURO": "COMPLEMENTO",
        "NOME_BAIRRO": "NOME DO BAIRRO",
        "NUM_CEP": "00000000",
        "NOME_MUNICIPIO": "NOME DO MUNICÍPIO",
        "SIGLA_UF": "UF",
        "NUM_DDD": "00",
        "NUM_TELEFONE": "00000000",
        "NUM_FAX": "00000000",
        "SE_ESTRANGEIRO": "N",
        "NOME_PAIS_NACIONALIDADE": "",
        "COD_SITUACAO_CADASTRAL": "0",
        "DESCR_SITUACAO_CADASTRAL": "REGULAR",
        "DATA_SITUACAO_CADASTRAL": "",
        "DATA_INSCRICAO": "21/06/06",
        "ANO_OBITO": "",
        "ANO_ULTIMA_ENTREGA_DECLARACAO": "2018",
        "DATA_BASE": "03/10/19"
    }
]
```