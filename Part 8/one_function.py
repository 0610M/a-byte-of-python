def make_car(boss, num, **car_info):
    car_info['boss'] = boss
    car_info['num'] = num
    for k, v in car_info.items():
        car_info[k] = v

    print(car_info)


