# :star: 목차
[git의 기본 명령어](#file_folder-git-기본-명령어)

[branch](#file_folder-branch)

[fork](#file_folder-fork)

[기타 명령어](#file_folder-기타-명령어)

<br>

# :file_folder: git 기본 명령어

## 프로젝트 시작할 때

### 로컬에서 처음 시작하기
```bash
git init
```
* git init하면 (main)으로 확인할 수 있음

### 원격 저장소 프로젝트로 시작하기
```bash
git clone 'https://~'
```

<br>

## 버전 기록할 때

```bash
git add .
git commit -m '커밋메시지'
```
* git status로 파일 상태 확인 해보기 
* git log로 커밋 확인하기

<br>

## 원격저장소 최초 설정할 때

```bash
git remote add origin url
```

<br>

## 원격저장소 활용

### push

```bash
git push origin main
```

- `origin` : 원격저장소의 이름

- `main` : 브랜치의 이름

### pull

```bash
git pull origin main
```

<br>

# :file_folder: branch
브랜치는 코드 개발과 관리의 유연성과 안정성을 높여주는 중요한 기능이다. 코드를 분리하고 독립적으로 작업하여 효율적이고 조직적인 개발을 가능하게 해준다.

## branch 관련 명령어

1. 브랜치 생성하기 : 새로운 브랜치를 만든다.
```bash
git branch <branch_name>
```
2. 브랜치 전환하기: 다른 브랜치로 전환한다.
```bash
git checkout <branch_name>
```
3. 새로운 브랜치 생성하고 전환하기: 새로운 브랜치를 생성하고 해당 브랜치로 전환한다.
```bash
git checkout -b <new_branch_name>
```
4. 로컬 브랜치 목록 보기: 현재 로컬 저장소에 있는 모든 브랜치 목록을 확인합니다.
```bash
git branch
```
5. 원격 브랜치 목록 보기: 원격 저장소에 있는 브랜치 목록을 확인합니다.
```bash
git branch -r
```
6. 브랜치 삭제하기: 브랜치를 삭제합니다. (-d 옵션은 안전하게 삭제하고, -D 옵션은 강제로 삭제합니다.)
```bash
git branch -d <branch_name>
```
7. 원격 브랜치 가져오기: 원격 저장소의 최신 브랜치 정보를 가져옵니다.
```bash
git fetch
```
8. 브랜치 병합하기: 다른 브랜치를 현재 브랜치로 병합합니다.
```bash
git merge <branch_name>
```
9. 브랜치 리베이스: 현재 브랜치에 다른 브랜치의 변경사항을 리베이스합니다.
```bash
git rebase <branch_name>
```
10. 현재 브랜치 정보 확인하기: 현재 작업 중인 브랜치를 확인합니다.
```bash
git branch --show-current
```
<br>

## 브랜치 사용과정
1. 브랜치를 생성한다.
```bash
git branch <branch_name>
```
2. 브랜치에서 코딩을 진행한다.
```bash
git add
git commit
...
```
3. 코딩을 완료한 후 생성한 브랜치의 원격저장소에 올린다.
```bash
git push origin <branch_name>
```
4. 생성한 브랜치에서 완료한 코딩을 main 브랜치로 `merge`하기 위해 Pull Request를 요청한다.

5. 작업물이 확인되고 문제가 없다면, Pull Request는 허가되고 생성한 브랜치에서 완료한 코딩은 main 브랜치로 `merge`된다.

<br>

# :file_folder: fork
## fork를 사용하는 이유

1. **원본 프로젝트의 변화와 독립성 유지**: 다른 개발자나 팀이 유지하는 원본 프로젝트를 fork하여 자체적인 작업 영역을 만든다. 이렇게 하면 원본 프로젝트의 변경사항이 자신의 작업에 직접 영향을 주지 않으면서 독립적으로 작업할 수 있다.

2. **개별 개발 브랜치 생성**: fork한 프로젝트에서는 자신만의 브랜치를 만들어 기능 개발이나 버그 수정을 할 수 있다. 이렇게 하면 원본 프로젝트에 영향을 주지 않으면서 여러 기능을 개발하거나 실험할 수 있다.

3. **컨트리뷰션 제공**: 오픈 소스 프로젝트에 기여하고 싶을 때, fork한 프로젝트에서 변경사항을 가진 브랜치를 생성하고 이를 원본 프로젝트로 풀 리퀘스트(Pull Request)를 보내서 변경사항을 제안할 수 있다. 원본 프로젝트 관리자는 이러한 변경사항을 검토하여 통합할 수 있다.

4. **권한과 보안**: fork를 통해 원본 프로젝트의 코드는 자신의 계정으로 분리되며, 다른 개발자와 공유할 수 있는 관리 및 접근 권한을 설정할 수 있다. 그렇기 때문에 보안 및 컨트롤 측면에서 유용하다.

5. **실험 및 테스트**: fork를 통해 원본 프로젝트에 대한 특정 변경사항을 테스트하거나 실험할 수 있다. 이러한 실험을 통해 더 나은 기능을 개발하거나 버그를 수정할 수 있다.

<br>

## fork하는 방법
1. GitHub에서 Fork버튼을 누른다. (원본 내용을 내 github 저장소에 복사하여 저장한다. 내 저장소에 새로운 branch를 만드는 것과 같다.)
2. 바탕화면에서 git bash를 열고 아래의 명령어를 작성한다.
 ```
 git clone `원본을 내 github 저장소에 fork한 주소`
 ``` 
3. 위의 명령어를 통해 바탕화면에 생성된 폴더를 확인하고 열어준다. 
    - 2.에서 git bash를 바탕화면에서 했기 때문에 바탕화면에 폴더가 생성
4. 파일을 만들고 `add`,`commit`을 해준다.
5. `git push origin main`을 실행하면, `git push`를 통해 `commit`한 내용이 *나의 github 저장소*에 올라가게된다.
6. GitHub에서 Pull Request를 통해 *나의 github 저장소*에서 작성한 내용을 원본에 `merge`하는 것을 요청한다.

<br>

# :file_folder: 기타 명령어

## git add를 취소

```bash
git restore --staged 파일명
```

<br>

## 커밋 메시지를 변경

```bash
git commit --amend
```

<br>

## 커밋을 취소 

```bash
git reset --hard 커밋
git reset --soft 커밋
```

```bash
git revert 커밋
```