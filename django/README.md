# 점프 투 장고

# 가상환경
```bash
mkdir venv

python3 -m venv mysite

# 가상환경 활성
cd venv
. mysite/bin/activate

# 활성상태 종료
deactivate
```

# 장고 install
```bash
python3 -m pip --upgrade pip
pip install django
```

# 프로젝트 생성
```bash
# 프로젝트 폴더 생성
mkdir projects
cd projects

# 가상환경 진입
. ../venv/mysite/bin/activate
mkdir mysite
cd mysite

# 장고 프로젝트 생성
django-admin startproject config . # 현재 티렉토리를 프로젝트로 생성

# 서버 구동
python3 manage.py runserver
```

# Create Super User
```bash
python3 manage.py createsuperuser
```
주소 : localhost:8000/admin