cd ../../

python3 manage.py makemigrations main
python3 manage.py migrate

python3 manage.py makemigrations notice
python3 manage.py migrate

python3 manage.py makemigrations people
python3 manage.py migrate

python3 manage.py makemigrations ppr
python3 manage.py migrate

python3 manage.py makemigrations tabs
python3 manage.py migrate

cd initialize/linux/