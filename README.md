# WWTP Project

하수처리장 시계열 데이터의 결측치 복원을 위한 프로젝트

## 폴더 구조
- notebooks/: Colab 실행용 노트북
- src/: 데이터 로딩, 특징공학, 모델 코드
- data/: CSV 원본 (gitignore 권장)
- artifacts/: 결과물 (gitignore 권장)

## 실행 방법
1. Colab에서 `notebooks/00_main.ipynb` 열기
2. 데이터 병합 → 단기 결측 복원 → 장기 결측 복원 → 리포트 순으로 실행
