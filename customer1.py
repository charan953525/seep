class customer:
    def __init__(self,name,email,phone_no,profile_pic):
        self.name = name
        self.email = email
        self.phone_no = phone_no
        self.profile_pic = profile_pic
    def update_profile(self,name=None,email=None,phone_no=None,profile_pic=None):
        if name:
            self.name = name
        if email:
            self.email =email
        if phone_no:
            self.phone_no =phone_no
        if profile_pic :
           self.profile_pic =profile_pic
    def display_profile(self):
        print("name:",self.name)
        print("email:",self.email)
        print("phone_no:",self.phone_no)
        print("profile_pic",self.profile_pic)
customer1=customer("charan","charan14112005@gmail","1234567890","profile_pic.jpg")
customer1.display_profile()
print("\n updating_profile")
customer1.display_profile()