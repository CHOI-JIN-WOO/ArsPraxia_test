"""

0. 출력 방벙
    1) print("", "", val)
        - ,로 자료형 불문 사용 가능

    2) print(""+ ""+ str(val))
        - +로 string 자료형 사용 가능

    3) print("%s %d" %("", val))
        - printf 처럼

    4) print(""" """)
        - 여러 줄 가능

1. 파이썬 기본 자료 구조
    1) 리스트(List)                               : ['value1', 'value2', ]
        - Array와 유사하지만 서로 다른 자료형 가능

        * 함수
            - example[start:end:step]           : start 이상 end 미만 step 개씩
            - example[index] = 'value'
            - del example[index]
            - example.insert(index, 'value')
            - example.append('value')
            - example.sort()                    : 사전 순 정렬
            - example.reverse()                 : 사전 역순 정렬

    2) 튜플(Tuple)                               : ('value1', 'value2', )
        - 리스트와 비슷
        - 저장된 원소를 변경/삭제 불가

    3) 집합(Set)
        - 수학의 집합과 비슷
        - 원소 간 중복 안됨
        - 원소 간 순서 없음

    4) 사전(Dictionary)                          : {'key1':'value1', 'key2':'value2', }
        - Key와 Value의 쌍으로 구성된 원소

        * 함수
            - example['key'] = 'value'
            - del example['key']


    [결론]
        List        : 각 원소에 접근하기 위해 Index를 사용함
        Dictionary  : 각 원소에 접근하기 위해 Key를 사용함


2. 파이썬 자료형 성질
    1) Mutable : 값 수정 가능
        - List, Dictionary, Set
        
    2) Immuatble : 값 수정 불가능
        - Tuple, Int, Float, String
        
        
3. 파이썬 변수 스코프
        1) global

        2) local


"""

