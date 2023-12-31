# 데이터 모델링
## 데이터 모델링의 이해
### 주요 특징
- 추상화: 현실 세계를 간략하게 표현한다.
- 단순화: 누구나 쉽게 이해할 수 있도록 표현한다.
- 명확성: 명확하게 의미가 해석되어야 하고 한 가지 의미를 가져야 한다.

### 데이터 모델링 단계
- 개념적 모델링
    - 전사적 관점
    - 추상화 수준이 가장 높은 수준의 모델링
    - 업무 측면에서 모델링
- 논리적 모델링
    - 재사용성을 높임
- 물리적 모델링
    - 성능, 보안, 가용성 등을 고려하여 데이터베이스를 구축

### 데이터 모델링 관점
- 데이터
- 프로세스
- 데이터와 프로세스

### ERD
엔터티와 엔터티 간의 관계를 정의하는 모델링 방법
중요한 엔터티를 가급적 왼쪽 상단에 배치한다.
ERD는 이해가 쉬워야 하고 너무 복잡하지 않아야 한다.

#### ERD 작성절차
1. 엔터티를 도출하고 그린다
2. 엔터티를 배치한다
3. 엔터티 간의 관계를 설정한다
4. 관계명을 서술한다
5. 관계 참여도를 표현한다
6. 관계의 필수 여부를 표현한다

## 3층 스키마
- 사용자, 설계자, 개발자가 데이터베이스를 보는 관점에 따라 데이터베이스를 기술하고 이들간의 관계를 정의한 ANSI 표준이다.
(ANSI: 데이터베이스와 관련된 표준을 정의한 것.)
- 데이터베이스의 독립성을 확보하기 위한 방법
- 데이터의 독립성을 확보하면 복잡도 감소, 데이터 중복 제거, 사용자 요구사항 변경에 따른 대응력 향상, 관리 및 유지보수 비용 절감
- 3단계 계층으로 분리해서 독립성 확보. 각 계층을 뷰(View)라고도 한다.

### 3층 스키마의 독립성
- 논리적 독립성: 개념 스키마가 변경되더라도 외부 스키마가 영향을 받지 않음.
- 물리적 독립성: 내부 스키마가 변경되더라도 개념 스키마가 영향을 받지 않음.

### 3층 스키마의 구조
- 외부 스키마: 응용 프로그램이 접근하는 데이터베이스
- 개념 스키마: 통합 데이터베이스 구조
- 내부 스키마: 물리적 저장 구조


## 엔터티
엔터티는 업무에서 관리해야 하는 데이터 집합을 의미하며, 저장되고 관리되어야 하는 데이터이다. 엔터티는 개념, 사건, 장소 등의 명사이다.

### 엔터티의 특징
- 식별자: 유일한 식별자가 있어야 한다.
- 인스턴스 집합: 2개 이상의 인스턴스가 있어야 한다.
- 속성: 반드시 속성을 가직 있다.
- 관계: 다른 엔터티와 최소한 한 개 이상 관계가 있어야 한다.
- 업무: 엔터티는 업무에서 관리되어야 하는 집합

### 엔터티 종류
- 유형과 무형에 따른 엔터티 종류
    - 유형 엔터티: 지속적으로 사용되는 엔터티
    - 개념 엔터티: 유형 엔터티는 물리적 형태가 있지만, 개념 엔터티는 물리적 형태가 없다.
    - 사건 엔터티: 비즈니스 프로세스를 실행하면서 생성되는 엔터티이다.

- 발생 시점에 따른 엔터티 종류
    - 기본 엔터티: 키 엔터티. 독립적으로 생성되는 엔터티
    - 중심 엔터티: 기본 엔터티와 행위 엔터티 간의 중간에 있는 것
    - 행위 엔터티: 2개 이상의 엔터티로부터 발생된다.

## 속성
속성이라는 것은 업무에서 필요한 정보인 엔터티가 가지는 항목.

속성은 더 이상 분리되지 않는 단위. 업무에 필요한 데이터를 저장할 수 있다.

인스턴스의 구성요소이고 의미적으로 더 이상 분해되지 않는다.

일반적으로 하나의 값만 가진다.

주식별자에게 함수적으로 종속된다. 기본키가 변경되면 속성의 값도 변경된다.

### 속성의 종류
- 분해 여부에 따른 속성의 종류
    - 단일 속성: 하나의 의미로 구성된 것(회원ID, 이름)
    - 복합 속성: 여러 개의 이미가 있는 것.(주소) 주소는 시, 군, 동 등으로 분해될 수 있다.
    - 다중값 속성: 속성에 여러 개의 값을 가질 수 있는 것.(상품 리스트) 다중값 속성은 엔터티르 분해된다.

- 특성에 따른 속성의 종류
    - 기본 속성: 비즈니스 프로세스에서 도출되는 본래의 속성(회원ID, 이름)
    - 설계 속성: 데이터 모델링 과정에서 발생되는 속성. 유일한 값을 부여(상품코드, 지점 코드)
    - 파생 속성: 다른 속성에 의해서 만들어지는 속성(합계, 평균)

---
**도메인**: 도메인은 속성이 가질 수 있는 값의 범위이다.(성별이라는 속성의 도메인은 남자와 여자이다.)

---


## 관계
엔터티 간의 관련성을 의미하며 존재 관계와 행위 관계로 분류된다.
- 존재 관계: 두 개의 엔터티가 존재 여부의 관계가 있는 것.(고객이 은행에 회원가입을 하면, 관리점이 할당되고, 그 할당된 관리점에서 고객을 관리한다.)

- 행위 관계: 두 개의 엔터티가 어떤 행위에 의한 관련성이 있는 것.(증권회사는 계좌를 개설하고 주문을 발주한다)

### 관계 차수
관계 차수는 두 개의 엔터티 간에 관계에 참여하는 수를 의미한다.
- 1:1 관계: 고객은 하나의 휴대폰번호를 가지거나 없을 수 있다.
- 1:N 관계: 고객은 여러개의 계좌를 가질 수 있다.
- M:N 관계: 학생이 여러 개의 과목을 수강할 수 있다. 과목은 여러 명의 학생이 수강한다. M:N관계의 조인은 카테시안 곱이 발생하므로 1:N, N:1로 해소해야 한다.(수강이라는 엔터티를 추가로 도출하여 해소)

필수적 관계는 | 로 표현되고 선택적 관계는 O로 표현된다.

### 식별 관계와 비식별 관계
- 식별 관계: 고객과 계좌 엔터티에서 고객 엔터티의 기본키인 회원ID를 계좌 엔터티의 기본키의 하나로 공유하는 것
- 비식별 관계: 강한 개체의 기본키를 다른 엔터티의 기본키가 아닌 일반 칼럼으로 관계를 가지는 것

---
**강한 개체**: 누구에게도 지배되지 않는 독립적인 개체

**약한 개체**: 개체의 존재가 다른 개체의 존재에 달려 있는 개체

---

## 엔터티 식별자
### 키의 종류
1. 기본키(주식별자, Primary key): 후보키 중에서 엔터티를 대표할 수 있는 키
    - 최소성: 최소성을 만족
    - 대표성: 엔터티를 대표
    - 유일성: 엔터티의 인스턴스를 유일하게 식별
    - 불변성: 자주 변경되지 않아야 한다
2. 후보키(Candidate key): 유일성과 최소성을 만족하는 키
3. 슈퍼키(Super key): 유일성은 만족하지만 최소성을 만족하지 않는 키
4. 대체키(Alternate key): 여러 개의 후보키 중에서 기본키를 선정하고 남은 키
5. 외래키(Foreign key)
    - 하나 혹은 다수의 다른 테이블의 기본 키 필드를 가리키는 것으로 참조 무결성을 확인하기 위해서 사용되는 키이다.
    - 허용된 데이터 값만 데이터베이스에 저장하기 위해서 사용된다.

### 식별자의 종류
1. 식별자의 대표성
    - 주식별자: 엔터티를 대표하는 식별자. 참조 관계로 연결될 수 있다.
    - 보조 식별자: 대표성을 만족하지 못하는 식별자

2. 생성 여부
    - 내부 식별자: 엔터티 내부에서 스스로 생서오디는 식별자(부서코드, 주문번호)
    - 외부 식별자: 다른 엔터티와의 관계로 인하여 만들어지는 식별자(계좌 엔터티에 회원ID)

3. 속성의 수
    - 단일 식별자: 하나의 속성으로 구성
    - 복합 식별자: 두 개 이상의 속성으로 구성

4. 대체 여부
    - 본질 식별자: 비즈니스 프로세스에서 만들어지는 식별자
    - 인조 식별자: 인위적으로 만들어지는 식별자

---
**인조 식별자**: 
- 후보 식별자 중에서 주식별자로 선정할 것이 없거나 주식별자가 너무 많은 칼럼으로 되어있는 경우에 사용.
- 순서번호(Sequence Number)를 사용해서 식별자를 만드는 것.
---
