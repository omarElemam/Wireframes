class MemberStore:
  members = []

  def get_all(self):
      print(MemberStore.members)

  def add(self, member):
      self.member = member.name
      MemberStore.members.append(self.member)

#--------------------------------------
class PostStore:
  posts = []

  def get_all(self):
      print(PostStore.posts)

  def add(self, post):
      self.post = post.title
      PostStore.posts.append(self.post)
