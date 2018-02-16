import models
import store

member1 = models.Member("Ahmed", "23")
member2 = models.Member("Omar", "20")

post1 = models.Post("post1_title", "post1_content")
post2 = models.Post("post2_title", "post2_content")
post3 =	models.Post("post3_title", "post3_content")


#Check ---------------------------
member_store = store.MemberStore()
member_store.add(member1)
member_store.add(member2)

post_store = store.PostStore()
post_store.add(post1)
post_store.add(post2)

member_store.get_all()
post_store.get_all()

membert = store.MemberStore()

print(membert.get_by_id(0).name)

membert.entity_exist(member1)


