# unicond é um sistema gerenciador de condomínios
- projeto realizado durante a graduação em Desenvolvimento de sistemas

Steps:
python3 -m venv venv
source venv/bin/activate
Instale as dependências:
pip install -r requirements.txt
Crie um arquivo .env na raiz do projeto e defina as seguintes variáveis de ambiente:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=unicond
DB_USER=postgres
DB_PASSWORD=postgres
Execute as migrações:
python manage.py migrate
Crie um superusuário:
python manage.py createsuperuser
Inicie o servidor web:
python manage.py runserver