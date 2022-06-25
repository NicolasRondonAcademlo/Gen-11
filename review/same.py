

scores = [
  {
    "name": "Alexandra",
    "score": 1458
  },
    {
    "name": "Alexandra",
    "score": 9785
  },
  {
    "name": "Camilo",
    "score": 8795
  },
  {
    "name": "Felipe",
    "score": 5456
  },
  {
    "name": "Roberto",
    "score": 5549
  },
    {
    "name": "Roberto",
    "score": 5549
  }
]
# {'Alexandra': 11243, 'Camilo': 8795, 'Felipe': 5456, 'Roberto': 11098}


result = {}
for i in scores:
    if i["name"] in result.keys():
        result[i["name"]] += i["score"]
    else:
        result[i["name"]]=i["score"]

print(result)

values = {
    "a": 1,
    "b": 2,
    "c":3
}