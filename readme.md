## Test GB - Python

#### Utilizar Python 3.9

### Instalação Linux

- Criar ambiente virtual
    - ```python3.9 -m venv venv```

-  Com ambiente virtual ativado, instalar dependências:
    - ```pip install -r requirements.txt```

- Criar arquivo .env baseado no ```.env.example```
    ```text
    DATABASE_URL=sqlite:///./store.db
    ENVIRONMENT=development
    DEBUG=True
    ```

- rodar projeto:
    - ```python runserver.py```

- rodar testes:
    - ```pytest```

- rodar coverage:
    - ```coverage run -m pytest```
    - ```coverage html```