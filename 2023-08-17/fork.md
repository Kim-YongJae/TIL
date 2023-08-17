# Git Fork하는 방법
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