def seat_location(seat_nmbr):
    index = seat_nmbr - 1
    
    i = index // 8
    j = index % 8

    berth = {
        0:"lower" , 1:"middle" , 2:"upper",
        3:"lower" , 4:"middle" , 5:"upper",
        6:"side lower" , 7:"side upper"
    }
    compartment_nmbr = i+1
    berth_type = berth[j]
    return f"seat number {seat_nmbr} is in the compartment {compartment_nmbr}, berth:{berth_type}"

print(seat_location(17))