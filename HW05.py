import matplotlib.pyplot as plt
from matplotlib import rc


def get_category(cat_str):
    ages_cat = cat_str.split(',')
    ages_cat = list(map(str.strip, ages_cat))
    return ages_cat


def get_birth_list(birth_str):
    birth_lst = []
    for i in birth_str:
        x = i.split(',')
        birth_lst.append(x)
    return birth_lst


def get_birth_rates(birth_lst):
    birth_dict = {}
    for i in birth_lst:
        birth_dict[i[0]] = list(map(float, i[1:]))
    return birth_dict


def generate_plot(ages, birth_dict):
    # 사용할 한글 폰트 설정
    rc('font', family='AppleGothic')

    plt.title('연령대별 서울시 출산율')  # 그래프의 제목
    plt.xlabel('연령대')  # 그래프의 x축 이름
    plt.ylabel('출산율(인/만명)')  # 그래프의 y축 이름

    plt.bar(ages[1:], birth_dict['서울특별시'][1:], color='blue')
    plt.plot(ages[1:], birth_dict['서울특별시'][1:], 'ro--')

    plt.show()


if __name__ == '__main__':
    category_str = '소계, 15-19세, 20-24세, 25-29세, 30-34세, 35-39세, 40-44세, 45-49세'
    birth_rates_str = ['서울특별시,0.626,0.2,1.8,12.1,57.6,43.9,8.3,0.2',
                       '종로구,0.531,0.0,1.1,9.4,43.3,40.8,10.4,0.2',
                       '중구,0.634,0.0,1.0,10.5,55.8,49.4,10.2,0.2',
                       '용산구,0.664,0.5,1.8,10.8,59.7,47.7,11.1,0.3',
                       '성동구,0.764,0.0,1.3,11.2,74.5,55.6,9.7,0.2',
                       '광진구,0.525,0.3,1.4,9.6,46.1,38.7,7.7,0.3',
                       '동대문구,0.660,0.0,1.4,14.4,61.7,44.0,8.5,0.1',
                       '중랑구,0.650,0.1,3.5,15.2,58.9,42.7,9.4,0.1',
                       '성북구,0.656,0.4,1.5,13.0,62.1,44.7,8.1,0.1',
                       '강북구,0.541,0.0,3.1,14.1,44.4,37.4,7.2,0.2',
                       '도봉구,0.579,0.0,2.8,14.3,50.0,39.4,8.0,0.1',
                       '노원구,0.701,0.1,1.9,16.7,66.9,44.6,7.4,0.1',
                       '은평구,0.604,0.1,2.1,14.6,52.8,42.1,7.6,0.3',
                       '서대문구,0.635,0.7,1.7,11.0,59.6,42.9,9.5,0.1',
                       '마포구,0.587,0.3,0.9,8.4,50.9,46.8,9.3,0.3',
                       '양천구,0.645,0.1,2.1,14.4,62.2,42.6,5.7,0.1',
                       '강서구,0.617,0.2,2.9,12.7,57.5,41.4,8.0,0.1',
                       '구로구,0.737,0.3,2.0,16.4,70.0,47.5,10.0,0.2',
                       '금천구,0.612,0.3,3.0,13.1,53.6,41.4,9.7,0.7',
                       '영등포구,0.713,0.5,1.9,12.1,68.2,50.6,9.1,0.3',
                       '동작구,0.602,0.3,1.2,8.4,56.5,44.3,7.9,0.5',
                       '관악구,0.437,0.3,1.6,6.7,33.7,35.7,7.3,0.1',
                       '서초구,0.666,0.2,0.7,12.3,63.2,48.4,7.3,0.3',
                       '강남구,0.523,0.4,0.6,8.9,47.8,38.5,7.0,0.1',
                       '송파구,0.623,0.1,1.5,12.3,60.1,41.3,8.8,0.1',
                       '강동구,0.797,0.2,2.8,18.5,75.2,51.9,9.5,0.3']

    # category_str을 사용하여 나이대를 나타내는 문자열로 구성된 리스트 생성
    ages_category = get_category(category_str)
    print(ages_category)

    # birth_rates_str을 이용하여 출산율로 구성된 birth_rates_lst 생성
    birth_rates_lst = get_birth_list(birth_rates_str)
    print(birth_rates_lst)

    # birth_rates_lst를 이용하여 구 이름을 키(key), 연령 구간별 출산율 데이터를 아이템으로 가지는 딕셔너리 birth_rates 생성
    birth_rates = get_birth_rates(birth_rates_lst)
    print(birth_rates)

    # 제시된 그래프를 그리기 위한 함수 호출
    generate_plot(ages_category, birth_rates)
