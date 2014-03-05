#coding=utf-8
#车辆：100
cars=100
#每车车位：4.0
space_in_a_car=4.0
#司机：30
drivers=30
#旅客：90
passengers=90
#未配司机车辆
cars_not_driven=cars-drivers
#已配司机车辆
cars_driven=drivers
#可发运人数
carpool_capacity=cars_driven*space_in_a_car
#每车需发运人数
average_passengers_per_car=passengers/cars_driven


print "今天有【".decode('utf-8').encode('gb2312'),cars,\
      "】辆车可用；".decode('utf-8').encode('gb2312')

print "但司机只有【".decode('utf-8').encode('gb2312'),drivers,\
      "】位可供配置；".decode('utf-8').encode('gb2312')

print "今天将有【".decode('utf-8').encode('gb2312'),cars_not_driven,\
      "】辆车无司机可配；".decode('utf-8').encode('gb2312')

print "今天我们能发运【".decode('utf-8').encode('gb2312'),carpool_capacity,\
      "】名旅客；".decode('utf-8').encode('gb2312')

print "今天有【".decode('utf-8').encode('gb2312'),passengers,\
      "】名旅客需发运；".decode('utf-8').encode('gb2312')

print "所以,每车需要发运【".decode('utf-8').encode('gb2312'),average_passengers_per_car,\
      "】名旅客".decode('utf-8').encode('gb2312')
