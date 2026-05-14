def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="Shubham", age=21, city="Chapra")
# Output:
# name: Shubham
# age: 21
# city: Chapra
