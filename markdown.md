# 마크다운 학습

## 제목(heading)

제목은 `#`으로 표현한다.

### h3
#### h4
##### h5

## 목록

- 사과
- 배
- 바나나
    - 바나나
    - 바나나

1. 사과
2. 배
3. 바나나
    1. 바나나
    2. 바나나

## 코드블록

```python
print('hello world')
#주석
```
```html
<h1>Hello, world!</h1>
<!--주석-->
```
```sql
-- 주석
select * from HI;
```

## 링크

[구글](https://google.com)

[파이썬 코드](./main.py)

## 이미지
[이미지](./apple.jpg)

![이미지](./apple.jpg)

## 인용문

> 인용

## 테이블

|이름|나이|
|--|--|
|홍길동|60|

## 텍스트 스타일링

*텍스트* **텍스트** ~~텍스트~~

---

## Fenced Code Block

```
{
    "firstName": "John",
    "lastName": "Smith",
    "age": 25
}
```

```json
{
    "firstName": "John",
    "lastName": "Smith",
    "age": 25
}
```

## Footnote

Here's a sentence with a footnote,[^1] and here's a longer one.[^bignote]

[^1]: This is the footnote.
[^bignote]: Here's one with multiple paragraphs and code.

Indent paragraphs to include them in the footnote.

`{my code}`

Add as many paragrphs as you like.




## Heading ID

### My Great Heading {#custom-id}
[Heading IDs](#heading-ids)

## Definition List

First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.

## Strikethrough

~~The world is flat.~~ We know that the world is round.

## Task Lists

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

## Emoji

That is so funny! :joy:

## Highlight

I need to highlight these ==very important words==.

## Subscript

H~2~O

## Superscript

X^2^