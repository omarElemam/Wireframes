class MemberStore:
  members = []

  def get_all(self):
      return(MemberStore.members)

  def add(self, member):
      MemberStore.members.append(member)

#--------------------------------------
class PostStore:
  posts = []

  def get_all(self):
      return(PostStore.posts)

  def add(self, post):
      PostStore.posts.append(post)
