class InstagramAccount:
    def __init__(self, account_name, password):
        self.account_name = account_name          
        self._private_reels = []                  
        self.__archived_reels = []                
        self.__password = password                
    
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print(f"Private reel '{reel_name}' added.")

    
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:")
            for reel in self._private_reels:
                print("-", reel)
        else:
            print("Access Denied! Only followers can view private reels")

  
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print(f"Archived reel '{reel_name}' added.")

   
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:")
            for reel in self.__archived_reels:
                print("-", reel)
        else:
            print("Access Denied! Only account holder can view archived reels")

  
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"

    def set_password(self, new_password):
        self.__password = new_password
        print("Password updated successfully!")

account = InstagramAccount("insta", "insta123")


account.add_private_reel("Gym Reel")
account.add_private_reel("Travel Reel")


account.add_archived_reel("Old Dance Reel")
account.add_archived_reel("College Memories")

account.display_private_reels(True)


account.display_private_reels(False)


account.display_archived_reels("wrongpass")

account.display_archived_reels("insta123")

account.set_password("newpass123")


account.display_archived_reels("insta123")


account.display_archived_reels("newpass123")
