class Test_Error(BaseException):
        pass

def check_test(l):
    if False in l: 
        raise Test_Error

def compare_knowlage_answers(t1):
    pass

def compare_practical_answers(SHOW_BREAKDOWN,t1,t2,t3,t4,t5,t6,t7):
    import hashlib
    
    try:
        m = hashlib.sha256()
        m.update(str(t1).encode('utf-8'))
        ans_1 = m.hexdigest() == 'b474a99a2705e23cf905a484ec6d14ef58b56bbe62e9292783466ec363b5072d'

        m = hashlib.sha256()
        m.update(str(t2[0]).encode('utf-8'))
        ans_2_1 = m.hexdigest() == '811786ad1ae74adfdd20dd0372abaaebc6246e343aebd01da0bfc4c02bf0106c'

        m = hashlib.sha256()
        m.update(str(t2[1]).encode('utf-8'))
        ans_2_2 = m.hexdigest() == '96061e92f58e4bdcdee73df36183fe3ac64747c81c26f6c83aada8d2aabb1864'

        m = hashlib.sha256()
        m.update(str(t3[0]).encode('utf-8'))
        ans_3_1 = m.hexdigest() == 'dd760309ec23fd4782c4e11a21007becc091144f6d6396cf2ef4a15807a8df52'

        m = hashlib.sha256()
        m.update(str(t3[1]).encode('utf-8'))
        ans_3_2 = m.hexdigest() == '24a52187630fb0624f06b545af4427c28c116b05cfce2280a78de92f3b822fce'

        m = hashlib.sha256()
        m.update(str(t3[2]).encode('utf-8'))
        ans_3_3 = m.hexdigest() == '38d3224a22509f3eb801abe9f7e69b8f5691d6c72c7ff4ab728ed92fb220c394'

        m = hashlib.sha256()
        m.update(str(t3[3]).encode('utf-8'))
        ans_3_4 = m.hexdigest() == 'aebcd62348b2e8eac4040cb11b9e414b9538d2a7ef9a283c47406d9b11adea72'

        m = hashlib.sha256()
        m.update(str(t3[4]).encode('utf-8'))
        ans_3_5 = m.hexdigest() == '1eef934efda846e29fefebb2e55152e864d7df3674307fc1431a41ae98e3131a'
        
        m = hashlib.sha256()
        m.update(str(t4).encode('utf-8'))
        ans_4 = m.hexdigest() == '3e76fd3d8f78cabdf83dd5310a85183e5bc1c72e080d9bc3e951e87792f73af6'

        m = hashlib.sha256()
        m.update(str(t5).encode('utf-8'))
        ans_5 = m.hexdigest() in ['81b637d8fcd2c6da6359e6963113a1170de795e4b725b84d1e0b4cfd9ec58ce9',
        '3a5a2512949399115565867a73a413ec6ba215c8f2df385f78b33238a6639b7c',
        '34b36454cab2e7842c389f7d88ecb7df279e3918cbac07970d4cde496e70f4c8']

        m = hashlib.sha256()
        m.update(str(t6).encode('utf-8'))
        ans_6 = m.hexdigest() in ['1648dec6017d9cf193cfeb8c844de341834b1f972cfbcee5a8973c9ed0c518f1','679f01bc578a23267b03ede7d4862630ec4db73ef7bfc5b18ca85b46d6338f02']

        # if the function returns it passes as errors will be raised
        m = hashlib.sha256()
        m.update(str(t7).encode('utf-8'))
        ans_7 = m.hexdigest() == 'dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91'
    except:
        raise Test_Error('test not completed invalid answer in at least 1 question')

    answers = [ans_1,ans_2_1,ans_2_2,ans_3_1,ans_3_2,ans_3_3,ans_3_4,ans_3_5,ans_4,ans_5,ans_6,ans_7]
    if SHOW_BREAKDOWN: 
        print('<Python Test> results')
        for i,res in enumerate(answers):
            print(f"{i}. {res}")
    check_test(answers)
