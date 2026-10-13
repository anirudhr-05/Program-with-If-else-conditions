#Condition :
Spent = 500
Has_Coupon = True

#User_1 Info
User1_Spent = int(input("How much Customer_1 Spent :" ))
User1_Coupon_Status = input("Has Customer_1 has Coupon? (True/False):").strip().lower() == "true"

Check = User1_Spent >= Spent and Has_Coupon == User1_Coupon_Status

if Check:
    print("\nCustomer_1 Eligibility for Discount: Eligible")
else:
    print("\nCustomer_1 Eligibility for Discount: Not Eligible")

#User_2 Info
User2_Spent = int(input("\nHow much customer_2 spent :" ))
User2_Coupon_Status = input("Has customer_2 has coupon? (True/False):").strip().lower() == "true"

Check = User2_Spent >= Spent and Has_Coupon == User2_Coupon_Status

if Check:
    print("\nCustomer_2 Eligibility for Discount: Eligible")
else:
    print("\nCustomer_2 Eligibility for Discount: Not Eligible")