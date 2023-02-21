number = int(input())
third_cypher = number % 10
second_cypher = number // 10 % 10
first_cypher = number // 100
print(first_cypher, second_cypher, third_cypher)