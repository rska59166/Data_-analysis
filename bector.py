from elice_utils import EliceUtils
import numpy as np

elice_utils = EliceUtils()

def main():
    data = [1,2,3]
    
    print(calculate_norm(data))
    print(unit_vector(data))
    

def calculate_norm(data):
    '''
    지시사항1: 함수 안에 주어진 데이터 data의 크기(scale) 값을 출력하는 함수를 채우시오.
    '''
    
    
    return np.linalg.norm(data)

def unit_vector(data):
    '''
    지시사항2: 함수 입력으로 주어진 data 벡터를 단위 벡터(unit vector)로 바꾸어 출력하세요.
    '''
    
    return np.array(data) / np.linalg.norm(data)

if __name__ == "__main__":
    main()
