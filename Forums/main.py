from models import Member
from models import Post

member1 = Member("Ahmed", "23")
member2 = Member("Omar", "20")

post1 = Post("post1_title", "post1_content")
post2 = Post("post2_title", "post2_content")
post3 =	Post("post3_title", "post3_content")


#Check ---------------------------
print(member1.name)
print(member1.age)

print(post1.title)
print(post1.content)
