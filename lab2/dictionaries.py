#task1
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#task2
car["year"] = 2020
print(car)

#task3
car["color"] = "red"
print(car)

#task4
car.pop("model")
print(car)

#task5
car.clear()
print(car)
