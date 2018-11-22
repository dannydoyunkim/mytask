# 초기 도서 목록 데이터를 이름순으로 정렬하는 메서드
# @param[in] books	초기화된 도서 목록 데이터
# @return 	이름순으로 정렬된 도서 목록 데이터
def sortBooks(books):
    print(books)
    for i in range(len(books)):
        temporaryVariable = "";
        for j in range(len(books)-1):
            if books[j] > books[j+1]:
                temporaryVariable = books[j]
                books[j] = books[j+1]
                books[j+1] = temporaryVariable;

    return books

# 기준연도에 따라 최신 도서를 추출하는 메서드
# @param[in] sortedBooks	이름순으로 정렬된 도서 목록 데이터
# @param[in] basicPeriod	기준연도
# @return               	기준연도에 따라 추출된 도서 목록 데이터
def extractLatestBook(sortedBooks, basicPeriod):
    extractedBooks = []
    #TODO
    extractedyear = 0

    for i in range(len(sortedBooks)) :
        extractedyear = int(list(sortedBooks[i].split("_"))[1])
        # print(extractedyear)
        if extractedyear == basicPeriod :
            extractedBooks.append(sortedBooks[i])
    
    return extractedBooks