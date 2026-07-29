from pathlib import Path
import json

# 시리즈 정보가 있는 책들 끼리 묶기
# 아래에 생성형 AI를 활용한 코드 작성
input_dir = Path('./skeleton/data/series_items')
output_path = Path('./skeleton/data/series.json')

if input_dir.exists():
    series_data = []

    for json_path in input_dir.rglob('*.json'):
        with json_path.open('r', encoding='utf-8') as file:
            data = json.load(file)

        series_data.append(data)

    with output_path.open('w', encoding='utf-8') as file:
        json.dump(series_data, file, ensure_ascii=False, indent=4)

    print(f"{output_path} 파일이 생성되었습니다.")
else:
    print(f"디렉토리가 존재하지 않습니다: {input_dir}")
