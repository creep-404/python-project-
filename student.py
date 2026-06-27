# student management system program 

# storing all the students here using roll number as key 

stud_data = {
    1:{"name": "shahid ahmad khan", "marks": [95, 89, 94, 96, 97]},
    2:{"name": "rabiyan khan", "marks": [92, 93 , 98 , 95 , 90]},
    3:{"name": "sumeet goregaonkar", "marks": [90 , 93 , 89 , 96 , 87]},
    4:{"name": "harshit walokar", "marks": [91, 89 , 93 , 95 , 97]},
    5:{"name": "aryan sharma", "marks": [90 , 85 , 89 , 94 , 97]}

} 


# calculating the average of 5 subujects marks 

def get_pct(marks):
    total = sum(marks)
    pct = total / 5 
    return pct


# checking percentage range to assign the grade 

def get_grade(pct):
    if pct >= 90:
        return 'O'
    elif pct >= 80:
        return 'A+'
    elif pct >= 70:
        return 'A'
    elif pct >= 60:
        return 'B+'
    elif pct >= 50:
        return 'B'
    else:
        return 'F'


def add_student():
    print("add student:")
    try:
        r = int(input("roll number:"))
    except:
        print("enter number only:") 
        return
    
    n = input("name:")

    # taking marks of the student one by one 
    m = []
    for i in range(1, 6):
        while True:
            try:
                x = float(input(f"sub {i} marks:"))
                if x < 0 or x > 100:
                    print("marks should be 0 to 100 only:")
                    continue
                m.append(x)
                break
            except:
                print("invalid , enter number:")

    stud_data[r] = {"name": n, "marks": m}
    print("done the student is added:")


def view_students():
    if len(stud_data) == 0:
        print("no records found:")
        return
    

    print()
    print("-"*70)
    print(f"{'roll':<10} {'name':<22} {'percentage':<14} grade")
    print("-"*70)

    for r , d in stud_data.items():
       p = get_pct(d["marks"])
       g = get_grade(p)

       # rounding off two decimal numbers 
       print(f"{r:<10} {d['name']:<22} {round(p,2):<14} {g}")
    
    print("-"*70)


def search_student():
    print("search:")
    try:
        r = int(input("enter the roll number:"))
    except:
        print("only numbers please:")
        return
    

    if r not in stud_data:
        print("student not found:")
        return
    
    d = stud_data[r]
    p = get_pct(d["marks"])
    g = get_grade(p)

    print(f"\nroll    :{r}")
    print(f"name    :{d['name']}")
    print(f"marks   :{d['marks']}")
    print(f"pct     :{round(p,2)}%")
    print(f"grade   :{g}")


def update_student():
    print("update:")
    try:
        r = int(input ("roll number to update:"))
    except:
        print("invalid:")
        return

    if r not in stud_data:
        print("not found:")
        return

    print(f"updating records for {stud_data[r]['name']}:")

    n = input("new name (press enter to skip):")
    if n != "":
        stud_data[r]["name"] = n

    ch = input("update marks also? y/n:")
    if ch == 'y':
        new_marks = []
        for i in range(1, 6):
            while True:
                try:
                    x = float(input(f"sub{i}:"))
                    if 0 <= x <= 100:
                        new_marks.append(x)
                        break
                    else:
                        print("0 and 100 only:")
                except:
                    print("enter valid number:")
        stud_data[r]["marks"] = new_marks
        print("updated:")


def delete_student():
    print("delete:")
    try:
        r = int(input("roll number to delete:"))
    except:
        print("invalid input:")
        return
    
    if r not in stud_data:
        print("student  not found:")
        return
    
    # confirming before deleting 
    sure = input(f"delete {stud_data[r]['name']}? yes/no:")
    if sure == 'y':
        del stud_data[r]
        print("deleted:")
    else:
        print("cancelled:")


def class_report():
    if not stud_data:
        print("no data:")
        return

    all_pct =[]
    p_count =0
    f_count =0
    top_name =""
    top_pct =0

    for r , d in stud_data.items():
        p = get_pct(d["marks"])
        all_pct.append(p)


        if p>=50:
            p_count +=1
        else:
            f_count +=1

        if p> top_pct:
            top_pct = p
            top_name =d["name"]

    avg =sum(all_pct) /len (all_pct)


    print("====CLASS REPORT====")
    print("total students:",len(stud_data))
    print("average%:",round(avg,2))
    print("pass:",p_count)
    print("fail:",f_count)
    print("topper:",top_name,"with",round(top_pct,2),"%")


def rank_list():  # putting everyone in the list with their percentage then sorting them 
    temp =[]
    for r , d in stud_data.items():
        p = get_pct(d["marks"])
        temp.append([p,r,d["name"]])  # using list to store temp data 

    temp.sort(reverse=True)


    print("====RANK LIST====")
    rank = 1 
    for item in temp:
        print(f"rank{rank}->{item[2]}(roll:{item[1]})={round(item[0],2)}%")
        rank+=1




def show_menu():
    print("====STUDENT MANAGEMENT SYSTEM====")
    print("1 add students:")
    print("2 view all:")
    print("3 search:")
    print("4 update:")
    print("5 delete:")
    print("6 class report:")
    print("7 rank list:")
    print("8 exit:")
    print("============================")



# program execution starts from here 

while True:
    show_menu()
    ch = input("choices:")


    if ch == '1':
        add_student()
    elif ch == '2':
        view_students()
    elif ch == '3':
        search_student()
    elif ch == '4':
        update_student()
    elif ch == '5':
        delete_student()
    elif ch == '6':
        class_report()
    elif ch == '7':
        rank_list()
    elif ch == '8':
        exit()
        break
    else:
        print("wrong choice try again")
