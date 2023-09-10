class Player:
    def __init__(self, instrument):
        self.instrument = instrument
    
    # 객체의 자율성: 객체의 역할 및 책임을 수행하는 과정을 객체가 자율적으로 졀정하도록 코드를 작성
    # prepare, ing, end, curtain_call 이렇게 4개로 두면 만약 새로운 함수를 추가하고자 할 때 ~Concert.py 모두 다 수정을 해야한다.
    # 하지만 play로 묶어두면 수정할 것이 적어진다.
    # 앞에 __ 붙이는 것은 private으로 설정하는 것이다. 외부에서 호출 할 수 없게 한다. play를 호출 할 수 밖에 없도록 만든다.
    # 이와 같이 외부의 변경에 유연하게 대처, 수정가능할 수 있는 구조가 facard 구조이다.
    
    def play(self):
        self.__prepare()
        self.__ing()
        self.__end()
        self.__curtain_call()
    
    def __prepare(self):
        print(self.instrument + '를 연주할 준비 중입니다.')
        
    def __ing(self):
        print(self.instrument + '를 연주 중입니다.')
        
    def __end(self):
        print(self.instrument + '를 다 연주했습니다.')
        
    def __curtain_call(self):
        print('커튼콜을 진행합니다')