# Replace numeric strings with English words

"""
    숫자 문자열과 영단어 - 2021 카카오 채용연계형 인턴십

    - 일부 자릿수가 영단어로 표현된 카드를 원래 숫자로 바꾸기
"""

def solution(s):
    num_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    answer = s
    for key, value in num_dict.items():
        answer = answer.replace(key, value)
    return int(answer)