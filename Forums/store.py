class MemberStore:
  members = []
  last_id = 1

  def get_all(self):
    return(MemberStore.members)

  def add(self, member):
    member.id = MemberStore.last_id
    MemberStore.members.append(member)
    MemberStore.last_id += 1

  def entity_exist(self, member):
    for e in MemberStore.members:
      if(str(e) == str(member)):
        return True
      else:
         return False
        
  def get_by_id(self, id):
     all_members = self.get_all()
        for member in all_members:
            if member.id ==  id:
                return member

  def delete(self, member):
    if self.entity_exists(member) :
      MemberStore.members.remove(member)
      print (member + " is deleted")
    else :
      print (member + " doesn't exist")

#--------------------------------------
class PostStore:
  posts = []
  last_id = 1

  def get_all(self):
      return(PostStore.posts)

  def add(self, post):
    post.id = PostStore.last_id
    PostStore.posts.append(post)
    MemberStore.last_id += 1

  def entity_exist(self, post):
    for e in PostStore.posts:
      if(str(e) == str(post)):
        return True
      else:
         return False

  def get_by_id(self, id):
    all_posts = self.get_all()
    for post in all_posts:
      if post.id ==  id:
          return post

  def delete(self, member):
    if self.entity_exists(post) :
      PostStore.posts.remove(post)
      print (post + " is deleted")
    else :
      print (post + " doesn't exist")
  
