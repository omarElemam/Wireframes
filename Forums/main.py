import models

member1 = models.Member("Ahmed", "23")
member2 = models.Member("Omar", "20")

post1 = models.Post("post1_title", "post1_content")
post2 = models.Post("post2_title", "post2_content")
post3 =	models.Post("post3_title", "post3_content")


#Check ---------------------------
print(member1.name)
print(member1.age)

print(post1.title)
print(post1.content)
