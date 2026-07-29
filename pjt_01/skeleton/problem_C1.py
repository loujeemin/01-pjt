from datetime import datetime  # 날짜와 시간을 처리하기 위한 라이브러리
import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

# 월별 책 정보 모아보고 평균 가격 계산하기
# 아래에 전체 코드 작성
from datetime import datetime
import json
from pathlib import Path

file_path = Path('./skeleton/data/books_2000.json')

if file_path.exists():
    with file_path.open('r', encoding='utf-8') as file:
        books = json.load(file)

    monthly_stats = {}

    for book in books:
        pub_date = datetime.strptime(book["pubDate"], "%Y-%m-%d")
        month = pub_date.month
        price = book["priceSales"]

        if month not in monthly_stats:
            monthly_stats[month] = {
                "count": 0,
                "total": 0
            }

        monthly_stats[month]["count"] += 1
        monthly_stats[month]["total"] += price

    for month, stats in sorted(monthly_stats.items()):
        count = stats["count"]
        total = stats["total"]
        average = total / count

        print(f"{month}월: 평균 가격 {average:.2f}원 (총 {count}권)")

else:
    print(f"파일이 존재하지 않습니다: {file_path}")

