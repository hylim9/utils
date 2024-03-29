

class DictUtils:
    @classmethod
    def get_list_divided_by_specific_number_of_dictionaries(cls, data, number=500):
       
        # 특정 숫자 기준으로 딕셔너리 데이터 나눈 리스트 생성

        share = int(len(data.keys()) / number)  # 몫
        remain = len(data.keys()) % number  # 나머지

        result_list = []  # 결과 리스트
        for idx, _ in enumerate(range(share)):
            result_list.append(dict(list(data.items())[idx * number:(idx + 1) * number]))

        if remain:
            result_list.append(dict(list(data.items())[share * number:]))

        return result_list

    @classmethod
    def get_object_by_specific_key(cls, objs, key):
        # 특정 key 기준으로 object 정보 담은 딕셔너리 반환

        obj_by_specific_key = {}
        for obj in objs:
            obj_by_specific_key[getattr(obj, key)] = obj

        return obj_by_specific_key
