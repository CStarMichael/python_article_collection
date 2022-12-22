from faker import Faker
import pandas as pd

fake = Faker(["zh_CN"])
Faker.seed(0)


def get_data():
    key_list = ["姓名","性别", "详细地址", "所在省份", "手机号", "身份证号", "出生年月", "邮箱","语文","数学","英文","时间"]
    name = fake.name()
    sex = fake.simple_profile()['sex']
    address = fake.address()
    province = address[:3]
    number = fake.phone_number()
    id_card = fake.ssn()
    birth_date = id_card[6:14]
    email = fake.email()
    chinaese = fake.random_int(50,100)
    mathfake = fake.random_int(50,100)
    englishfake = fake.random_int(50,100)
    time = fake.date() + ' ' + fake.time()
    info_list = [name,sex, address, province, number, id_card, birth_date, email,chinaese,mathfake,englishfake, time]
    person_info = dict(zip(key_list, info_list))
    return person_info


df = pd.DataFrame(columns=["姓名", "性别","详细地址", "所在省份", "手机号", "身份证号", "出生年月", "邮箱","语文","数学","英文","时间"])
for i in range(1000):
    person_info = [get_data()]
    df1 = pd.DataFrame(person_info)
    df = pd.concat([df, df1])
df.to_excel("模拟数据.xlsx", index=None)
# df.to_csv("模拟数据.csv", index=None)