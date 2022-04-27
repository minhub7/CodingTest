# At least most of the multiple
if __name__ == '__main__':
    nList = list(map(int, input().split()))
    nList.sort()
    minNum = nList[0]

    while True:
        cnt = 0
        for n in nList: # minNum이 nList의 수 중 3개 이상과 매치 되는지 확인
            if minNum % n == 0:
                cnt += 1
        if cnt >= 3:    # nList의 수 중 3개 이상과 매치되면 minNum 출력 후 종료
            print(minNum)
            break
        minNum += 1