'''
[문제]
이차원 리스트에 값을 입력하는 방법은 여러가지가 있다. 행 우선 입력 방법이나
열 우선 입력 방법들을 일반적으로 생각할 수 있는데, 본 프로그램에서는 행과 열을
가장 바깥쪽에서 안쪽으로 채워나가는 달팽이 모양으로 값을 입력하고자 합니다.
예를들어
3x3 인 구조는
0  1  2
7  8  3
6  5  4

5X5 인 구조는
 0  1  2  3  4
15 16 17 18  5
14 23 24 19  6
13 22 21 20  7
12 11 10  9  8
과 같이 (0,0)부터 시작해서 바깥쪽부터 안쪽으로 값이 채워지는 리스트를 만들고자 합니다.

<실행결과>
Row와Column 입력 (예) 5 5 > 3 3
  0  1  2
  7  8  3
  6  5  4

'''


from snailNumber_sub import snailNumber

if __name__ == "__main__":
   
    r,c = map(int,input("Row와Column 입력 (예) 5 5 > ").split(' '))

    #array는 입력받은 행과 열만큼 0로 초기화된 이차원 리스트
    array = [[0 for x in range(c)] for x in range(r)]

    row,col = r,c   # 나중에 array를 출력할때를 위해 r,c 백업

    snailNumber(array, r, c)

    for i in range(row):       # array 출력
        for j in range(col):
            print('{:3d}'.format(array[i][j]),end="")
        print()
