# A___15__B__15__C__15__D_15__E__15___F
# 5 km --->> 100
# 1 km --->> 10 per km after 5 km
# 6 km --->> 100+10 =110 -- 6/24min
# A to B -->> 60min --- 1km/4min

# input
# customer_ID
# pickup location
# drip location

# output
# travel duration
# total charge


def texi_driving_application(cust_id, pick_up, drop):
    try:
        total_charge = 0
        time = ""
        if pick_up == "A" and drop == "B" or pick_up == "B" and drop == "C" or pick_up == "C" and drop == "D" or pick_up == "D" and drop == "E" or pick_up == "E" and drop == "F":
            time = "1 hour"
            total_charge = 100 + 10 * 10
        elif pick_up == "A" and drop == "C" or pick_up == "B" and drop == "D" or pick_up == "C" and drop == "E" or pick_up == "D" and drop == "F":
            time = "2 hour "
            total_charge = 100 + 10 * 25
        elif pick_up == "A" and drop == "D" or pick_up == "B" and drop == "E" or pick_up == "C" and drop == "F":
            time = "3 hour "
            total_charge = 100 + 10 * 40
        elif pick_up == "A" and drop == "E" or pick_up == "B" and drop == "F":
            time = "4 hour "
            total_charge = 100 + 10 * 55
        elif pick_up == "A" and drop == "F":
            time = "5 hour "
            total_charge = 100 + 10 * 55
        else:
            print("Please Enter The Correct Pick Up And Drop Location")
        return print(
            f"Thank You For Using Our Taxi Service \n\n Your Total Duration of Traveling = {time} \n\n Total Travelling Charge = {total_charge} Rs only"
        )
    except Exception as e:
        print("somthing went wrong", e)


while True:
        
    print("------------------------------Press Any Key To Start Using Our Taxi Service Or Press q For Quit The Service------------------------------")
    q = str(input()).capitalize()
    if q == "Q":
        print("------------------------------Thank You For Using Our Taxi Services------------------------------")
        break
    else:
        cust_id = str(input("Please Enter Your Customer Id \n\n"))
        pick_up = str(input("Please Enter Your Pick Up Location \n\n"))
        drop = str(input("Please Enter Your Drop Location \n\n"))
        texi_driving_application(cust_id, pick_up, drop)
