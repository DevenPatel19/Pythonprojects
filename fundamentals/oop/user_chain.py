# Create a file with the User class, including the __init__ with all the attributes, parameters and default values.

class user:
    def __init__(self, first_name, last_name, email, age,is_rewards_member = False, gold_card_point = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_point = 0

# Add the display_info(self) method to the User class

    def display_info(self):
        print(f"First Name is {self.first_name}")
        print(f"Last Name is {self.last_name}")
        print(f"Email is {self.email}")
        print(f"Age is {self.age}")
        print(f"Current status of Rewards Membership = {self.is_rewards_member}")
        print(f"Gold Card Points balance = {self.gold_card_point}")

    # Add the enroll method to the User class, implement and test by calling the method on the user in the outer scope.

    def enroll(self):
        if self.is_rewards_member == True:
            print("User is already a member")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_point = 200


    # Implement the spend_points(self, amount) method

    def spend_points(self, amount):
        if amount < int(self.gold_card_point):
            self.gold_card_point = self.gold_card_point - amount
        else:
            shortage_amount = amount - self.gold_card_point
            print(f"You have a shortage of points in the amount of {shortage_amount}")

# In the outer scope, create a user instance and call the display_info method to test.

primary_user = user("Deven", "Patel", "j@gmail.com", 40)
# primary_user.display_info()
# primary_user.enroll()
# primary_user.display_info()

# Make 2 more instances of the User class.

second_user = user("Kris", "Koe", "k@gmail.com", 40)
third_user = user("Peter", "Pat", "p@gmail.com", 43)

# Have the first user spend 50 points

# primary_user.spend_points(50)

# Have the second user enroll.
# Have the second user spend 80 points

# second_user.enroll()
# second_user.display_info()
# second_user.spend_points(80)

# Call the display method on all the users.

# primary_user.display_info()
# second_user.display_info()
third_user.display_info()

# BONUS: Implement the logic for testing if already a member and try to re-enroll the first user.
primary_user.enroll()

primary_user.display_info().enroll().spend_points(50).display_info()
second_user.enroll().spend_points(80).display_info()
