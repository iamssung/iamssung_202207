# demo 3번째 파일
# demodict.py
# 사전식 구조
color = {"apple":"red", "banana":"yellow"}
print(color)
print(len(color))
print(color["apple"])
color["cherry"] = "red"
print(color)

type(color)


del color["apple"]
print(color)

for item in color.items():
    print(item)

print("-----key----")

for k in color.keys():
    print(k)

print("-----value------")
for v in color.values():
    print(v)

#장비를 관리
device = {"아이폰":5,"아이패트":10,"윈도우":20}
print(device)
print(device["아이폰"])

#입력
device["안드로이드"] = 30
#삭제
del device["아이폰"]
#수정
device["아이패드"] = 29
print(device)

#파이썬 참조
device2 = device
device2["맥북"] = 100
print(device)
print(device2)

