class MemberStore:
  members = []

  def get_all(self):
      return(MemberStore.members)

  def add(self, member):
      self.member = member
      MemberStore.members.append(self.member)

#--------------------------------------
class PostStore:
  posts = []

  def get_all(self):
      return(PostStore.posts)

  def add(self, post):
      self.post = post
      PostStore.posts.append(self.post)
