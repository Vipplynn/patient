from patient import *
from procedure import *

def main():
    pat1 = Patient('John', 'Micheal', 'Smith', '2343 Go Street', 'Vancouver', 'B.C.', 'V37 U43', '(238)-293-2938', 'Julia Smith', '(731)-328-2398')
    pro1 = Procedure('Physical Exam', '2021-10-28', 'Dr. Irvine', 250)
    pro2 = Procedure('X-ray', '2021-10-28', 'Dr. Jamison', 500)
    pro3 = Procedure('Blood Test', '2021-10-28', 'Dr. Smith', 200)


    print("Patient:-----------------------------")
    print()
    print(f'{pat1.get_last()}, {pat1.get_first()} {pat1.get_middle()}')
    print(f'{pat1.get_address()}, {pat1.get_city()}, {pat1.get_state()} | {pat1.get_zip()}')
    print(f'{pat1.get_number()}')

    print()
    print("Emergency Contact:-------------------")
    print()
    print(f'{pat1.name_emer} | {pat1.num_emer}')
    print()
    print("Procedures:--------------------------")
    print()
    print(f'{pro1.get_pro()} | {pro1.get_date()} | {pro1.get_prac()} | {pro1.get_charge()}')
    print(f'{pro2.get_pro()} | {pro2.get_date()} | {pro2.get_prac()} | {pro2.get_charge()}')
    print(f'{pro3.get_pro()} | {pro3.get_date()} | {pro3.get_prac()} | {pro3.get_charge()}')
    print(f"Total Cost: ${pro1.get_charge() + pro2.get_charge() + pro3.get_charge()}")

main()