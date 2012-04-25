#-- coding: utf-8 --
cars = 100                              #количество машин
space_in_a_car = 4                      #количество мест в машине
drivers = 30                            #количество имеющихся водителей
passengers = 90                         #количество пассажиров
cars_not_driven = cars - drivers        #количество машин без водителя
cars_driven = drivers                   #количество машин с водителем
carpool_capacity = cars_driven * space_in_a_car         #максимальное количество пассажиров
average_passengers_per_car = passengers / cars_driven   #среднее число пассажиров на машину


print "There are", cars, "cars availiable."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
