#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 BookManagement파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from BookManagement import *

basicPeriod = 2013

def main():
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    books = loadData()
    printInitialBookList(books)
    # 초기 도서 목록 데이터를 이름순으로 정렬하는 메서드
    sortedBooks = sortBooks(books)
    # 정렬된 도서 목록 출력 메서드
    printSortedBookList(sortedBooks)
    # 기준연도에 따라 최신 도서를 추출하는 메서드
    extractedBooks = extractLatestBook(sortedBooks, basicPeriod)
    # 추출된 도서 목록 출력 메서드
    printExtractBookList(extractedBooks)


'''
    도서 목록 데이터를 초기화하는 메서드 
    @param[out] books	초기화된 도서 목록 데이터
    @return basicPeriod	기준연도
'''
def loadData():
    ######################
    # 제공 데이터 세트 1
    ######################
    '''
    initialBooksData = [
        "Deep Learning_2018",
        "Weapons of Math Destruction_2011",
        "Computer Systems_2018",
        "Bitcoin and Cryptocurrency Technologies_2016",
        "Code Complete_2017"
    ]
    '''
    ######################
    # 제공 데이터 세트 2
    ######################

    initialBooksData = [
          "A Week in Winter_2016",
         "Sapiens : A Brief History of Humankind_2015",
         "The Millionaire Fastlane_2011",
         "Cosmos_2013",
         "Call Me by Your Name_2018"
    ]

    return initialBooksData


def printInitialBookList(books):
    print("---------------- 초기 입력 데이터 ---------------")
    for rowIndex in range(0, len(books)):
        print((rowIndex + 1),".",books[rowIndex])
    print("---------------------------------------------")

def printSortedBookList(sortedBooks):
    print("---------------- 도서명 순 정렬 결과 ---------------")
    for rowIndex in range(0, len(sortedBooks)):
        print((rowIndex + 1),".",sortedBooks[rowIndex])
    print("--------------------------------------------")

def printExtractBookList(extractedBooks):
    print("-------------- {}년 기준 도서 추출 기능 -------------".format(basicPeriod))
    extractedBooksCount = 0
    for rowIndex in range(len(extractedBooks)):
        print((extractedBooksCount + 1), ".", extractedBooks[rowIndex])
        extractedBooksCount += 1
    print("--------------------------------------------")


## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()