# 개요
Django를 이용해 간단한 웹 사이트를 제작해보자. 접속시 보이는 home 화면의 내용을 구성해보자.
# :star: 목차
[Django를 이용하여 웹페이지를 열어보자.](#file_folder-Django를-이용하여-웹페이지를-열어보자)

<br>

# :file_folder: Django를 이용하여 웹페이지를 열어보자
## 명령프롬프트로 Django 프로젝트 생성

![이미지](./명령프롬프트로%20django프로젝트%20생성.PNG)

만들고자 하는 폴더에서 명령프롬프트를 시작한 후에 `django-admin startproject project_name`을 통해 프로젝트를 생성한다.

<br>

## 구조 설명
Django 프로젝트를 생성한 후에 pycharm을 통해 열어보면 다음과 같은 구조로 구성되어있다.

![이미지](./django%20시작시%20첫%20구조.PNG)

-  `project_name/`: 프로젝트 설정을 담고 있는 디렉토리이다.
-  `manage.py`: Django 프로젝트를 관리하기 위한 스크립트이다. 서버 실행, 데이터베이스 마이그레이션, 앱 관리 등 다양한 작업을 수행할 수 있다.
    - `__init__.py`: Python 패키지로 인식되게 하는 빈 파일이다.
    - `asgi.py`: ASGI(Asynchronous Server Gateway Interface) 설정 파일로, 비동기 웹 서버와의 인터페이스를 정의한다.
    - `settings.py`: 프로젝트의 설정을 관리하는 파일로, 데이터베이스, 앱, 템플릿, 정적 파일, 보안 설정 등을 포함한다.
    - `urls.py`: 최상위 URL 매핑을 정의하는 파일이다. 사용자의 URL 요청을 해당하는 뷰로 연결시킨다.
    - `wsgi.py`: WSGI(Web Server Gateway Interface) 설정 파일로, 웹 서버와의 인터페이스를 정의한다.