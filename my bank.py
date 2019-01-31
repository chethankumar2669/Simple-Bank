#Simulation of a bank administration 
import random,os                                                 #Works beautifully
class Data_base:
	def __init__(self):                                          #{"Name":[amount,password]}
		self.current_users={}
class New_user(Data_base):
	def create_user(self,user_name,initial_deposit):
		self.new_password=random.randint(10000,99999)
		self.initial_deposit=initial_deposit
		self.user_name=user_name
		print(f"Congratulations {self.user_name} your account has been added successfully") 
		print(f"Please remember this password for future use : {self.new_password}")
		print("-------------------------------------------------------")
		self.current_users[self.user_name]=[self.initial_deposit,self.new_password]
class Existing_user(New_user):
	def check_user(self,user_name,user_password,user_choice):
		self.user_name=user_name
		self.user_password=user_password
		self.user_choice=user_choice
		if self.user_name in self.current_users:
			print("User name identified")
			if self.user_password==self.current_users[self.user_name][1]:
				print("User password verified ")
				if self.user_choice==1:
					self.withdraw_amount=int(input("Enter the amount to withdraw : "))
					if self.withdraw_amount>self.current_users[self.user_name][0]:
						print("Sorry insufficient balance")
					else:
						print("Transaction completed !")
						self.current_users[self.user_name][0]-=(self.withdraw_amount)
						print(f"Remaining balance : {self.current_users[self.user_name][0]}")
				elif self.user_choice==2:
					self.deposit_amount=int(input("Enter the amount to be deposited : "))
					print(f"Transaction completed !")
					self.current_users[self.user_name][0]+=+(self.deposit_amount)
					print(f"Remaining balance : {self.current_users[self.user_name][0]}")
				else: 
					print(f"Remaining account balance : {self.current_users[self.user_name][0]}")
			else:
				print("Please verify your password")
		else:
			print(f"user name : {self.user_name} is not identified")
		print("-------------------------------------------------------")
if __name__=="__main__":
	cal=Existing_user()
	print("Simulation of Bank administration \n")
	while True:
		user_input=int(input("Enter 1-New User 2-Existing User 3-Clear Screen 4-Exit : "))
		if user_input == 1:
			new_user_name=input("Enter your name : ")
			new_deposit=int(input("Enter your initial deposit : "))
			cal.create_user(new_user_name,new_deposit)
		elif user_input == 2:
			existing_user_name=input("Enter your name : ")
			password=int(input("Enter your password : "))
			user_choice=int(input("Enter 1-Withdraw amount 2-Deposit amount 3-Check Balance : "))
			if user_choice == 1:
				final=1
			elif user_choice == 2:
				final=2
			elif user_choice == 3:
				final=3
			else:
				print("Invalid Choice")
			cal.check_user(existing_user_name,password,final)
		elif user_input==3:
			os.system("cls")
		elif user_input==4:
			break
		else:
			print("Invalid Choice")