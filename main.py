from tabulate import tabulate
from math import sqrt

# isi titik - titik di bawah ini

class Membership:
    
    # inisialisasi data
    data = {
            "Sumbul": "Platinum",
            "Ana": "Gold",
            "Cahya": "Platinum"
        }
    
    # inisialisai attribute
    def __init__(self, username: str):
        self.username = username
        
    # method untuk menampilkan benefit membership
    def show_benefit(self) -> None:
        # init headers
        headers = ["Tier Membership", "Discount", "Benefit"]
        
        # init values
        tables = [
            ["Platinum", "15%", "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"],
            ["Gold", "10%", "Benefit Silver + Voucher Ojol"],
            ["Silver", "8%", "Voucher Makanan"]
        ]
        
        print("PacCommerce Benefit Membership")
        print("")
        print(tabulate(tables, headers, tablefmt="presto"))
        
    # method untuk menampilkan requirements membership
    def show_requirements(self) -> None:
        # init headers
        headers = ["Tier Membership", "Monthly Expense (Juta)", "Monthly Income (Juta)"]
        
        # init values
        tables = [
            ["Platinum", 8, 15],
            ["Gold", 6, 10],
            ["Silver", 5, 7]
        ]
        
        print("PacCommerce Requirements Membership")
        print("")
        print(tabulate(tables, headers, tablefmt = "presto"))
        
    # method untuk melakukan prediksi membership
    # menggunakan euclidean distance
    def predict_membership(self, monthly_expense: float, monthly_income: float):
        # init parameter data
        parameter_data = [[8, 15], [6, 10], [5, 7]]
        
        # create empty list to store the value
        result_tmp = []
            
        # iterate for each tier membership
        for idx in range(len(parameter_data)):
            
            # give defense, expense < income
            if monthly_expense < monthly_income:
                
                # implement euclidean distance
                euclidean_dist = round(sqrt((monthly_expense - parameter_data[idx][0])**2 + \
                                      (monthly_income - parameter_data[idx][1])**2), 2)
                
                # store the result to list
                result_tmp.append(euclidean_dist)
                
            else:
                raise Exception("Expense tidak boleh lebih besar dari Income")
    
        # store the values into dictionary
        dict_result = {
            "Platinum": result_tmp[0],
            "Gold": result_tmp[1],
            "Silver": result_tmp[2]
        }
        
        print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {dict_result}")
    
        # get minimum values from list
        get_min_distance = min(result_tmp)
        
        # iterate data to each dictionary
        for key, value in dict_result.items():
            
            # compare with minimum data
            if value == get_min_distance:
                print(key)
                
                # insert membership to dict membership data
                self.data[self.username] = key
            
#             else:
#                 raise Exception("Value minimum tidak ada yang sama")
            
    # method untuk menampilkan membership yang dimiliki
    # dari database yang dimiliki
    def calculate_price(self, username: str, list_harga: list):
        
        try:
            # get membership by given username
            membership = self.data.get(username)
            
            # calculate total list harga
            sum_harga = sum(list_harga)
            
            # create branching for each tier membership
            
            if membership == "Platinum":
                # get discount 15%
                total_price = sum_harga - (sum_harga * 0.15)
                
                return total_price
                
            elif membership == "Gold":
                total_price = sum_harga - (sum_harga * 0.10)
                
                return total_price
            
            elif membership == "Silver":
                total_price = sum_harga - (sum_harga * 0.08)
                
                return total_price
            
            else:
                raise Exception("Membership tidak Valid!!!!!")
            
            
        except:
            raise Exception("Error in Program")
        
        
obj_1 = Membership(username = "Santoso")

# get benefit
obj_1.show_benefit()

# predict membership
obj_1.predict_membership(monthly_expense = 3,
                         monthly_income = 20)

print(obj_1.data)