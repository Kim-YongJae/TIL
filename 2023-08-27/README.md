## 데이터 베이스의 종류: 계층형, 네트워크형, 관계형
- 계층형 데이터베이스: 1:N 관계
- 네트워크 데이터베이스: 1:N과 함께 M:N 표현도 가능
- 관계형 데이터베이스: 릴레이션과 릴레이션의 조인 연산을 통해서 여러 집합을 만들 수 있다.

## 관계형 데이터베이스
### 집합 연산
- 합집합(Union)
- 차집합(Difference)
- 교집합(Intersection)
- 곱집합(Cartesian product)

### 관계 연산
- 선택 연산(Selection): 릴레이션에서 조건에 맞는 행(튜플)만을 조회
- 투영 연산(Projection): 릴레이션에서 조건에 맞는 속성만 조회
- 결합 연산(Join): 여러 릴레이션의 공통된 속성을 사용해서 새로운 릴레이션을 만든다
- 나누기 연산(Division): 기준 릴레이션에서 나누는 릴레이션이 가지고 있는 속성과 동일한 값을 가지는 행(튜플)을 추출하고 나누는 릴레이션의 속성을 삭제한 후 중복된 행을 제거하는 연산

## SQL(Structured Query Language)
관계형 데이터베이스에 대해서 데이터의 구조를 정의, 데이터 조작, 데이터 제어등을 할 수 있는 절차형+비절차형 언어이다.

### SQL표준
- ANSI/ISO SQL 표준
- ANSI/ISO SQL3 표준

### SQL 종류
1. DDL
    - 관계형 데이터베이스의 구조를 정의하는 언어
    - Create, ALTER, DROP, RENAME, TRUNCATE
2. DML
    - 테이블에서 데이터를 입력, 수정, 삭제, 조회한다
    - INSERT, UPDATE, DELETE, SELECT
3. DCL
    - 데이터베이스 사용자에게 권한을 부여하거나 회수한다
    - GRANT, REVOKE
4. TCL
    - 트랜잭션을 제어하는 명령어이다.
    - COMMIT, ROLLBACK, SAVEPOINT
