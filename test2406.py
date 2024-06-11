import random

# 1. 메뉴 데이터베이스
menus = [
    {"name": "비빔밥", "type": "한식", "diet": "standard"},
    {"name": "된장찌개", "type": "한식", "diet": "standard"},
    {"name": "김치찌개", "type": "한식", "diet": "standard"},
    {"name": "초밥", "type": "일식", "diet": "standard"},
    {"name": "라멘", "type": "일식", "diet": "standard"},
    {"name": "파스타", "type": "양식", "diet": "standard"},
    {"name": "샐러드", "type": "양식", "diet": "vegetarian"},
    {"name": "채식 비빔밥", "type": "한식", "diet": "vegetarian"},
    {"name": "두부 스테이크", "type": "양식", "diet": "vegetarian"},
    {"name": "야채 라면", "type": "일식", "diet": "vegetarian"}
]

# 2. 사용자 입력 받기
def get_user_preferences():
    print("점심 메뉴를 추천해드립니다.")
    cuisine_type = input("원하는 음식 종류를 선택하세요 (한식, 일식, 양식, 상관없음): ")
    diet_preference = input("식단 제약이 있습니까? (standard, vegetarian, 상관없음): ")
    return cuisine_type, diet_preference

# 3. 메뉴 추천 알고리즘
def recommend_menu(menus, cuisine_type, diet_preference):
    filtered_menus = [menu for menu in menus if 
                      (cuisine_type)]
