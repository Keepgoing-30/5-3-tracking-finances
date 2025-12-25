transactions = []
# TO-DO Calculate gross pay
def calc_gross_pay(wage, hours):
                      """Return gross pay given hourly wage and hours worked."""
                      return wage * hours
# TO-DO Calculate withholding
def calc_withholding(gross_pay):
    """Return total withholding given gross pay and tax rates."""
    federal = gross_pay * 0.10  # Fixed federal tax rate of 10%
    state = gross_pay * 0.05 # Fixed state tax rate of 5%
    social_security = gross_pay * 0.062  # Fixed security tax rate of 6.2%
    return federal, state, social_security
# TO-DO Calculate net pay
def calc_net_pay(gross_pay, federal, state, social_security):
    """Return net pay given gross pay and total withholding."""
    return gross_pay - (federal + state + social_security)
# TO-DO Create your menu and program
def main():
    while True:
        print("\n1-Calculate net pay")
        print("2-Enter revenue or expense")
        print("3-Show discretionary income")
        print("4-Exit")
        
        choice = input("Choice:  ")
        
        # --- OPTION 1 ---
        if choice == '1':
            try:
                w = float(input("What is your hourly wage?  "))
                h = float(input("How many hours did you work?  "))
                
                # Call step 1
                gross = calc_gross_pay(w, h)
                
                # Call step 2 (receive 3 values at once)
                fed, state, ss = calc_withholding(gross)
                
                # Call step 3
                net = calc_net_pay(gross, fed, state, ss)
                
                # Display results
                print(f"Gross Pay: ${gross:.2f}({h} hours @ ${w:.2f}/hr)")
                print(f"Federal tax: ${fed:.2f}")
                print(f"State tax: ${state:.2f}")
                print(f"Social security: ${ss:.2f}")
                print(f"Net pay: ${net:.2f}")
            except ValueError:
                print("Invalid input. Please enter numbers.")

        # --- OPTION 2: Enter revenue or expense (Affect the global variable transactions) ---
        elif choice == '2':
            while True:
                name = input("Enter transaction name:  ")
                try:
                    amount = float(input("Enter amount (use negative sign for expense):  "))
                    # Add dictionary to the global list
                    transactions.append({"name": name, "amount": amount})
                except ValueError:
                    print("Invalid amount.")
                    
                if input("Another? (Y/N):  ").strip().lower() != 'y':
                    break

        # --- OPTION 3: Calculate discretionary income ---
        elif choice == '3':
            total_rev = 0
            total_exp = 0
            # Iterate through the global list to calculate totals
            for item in transactions:
                amt = item['amount']
                if amt >= 0:
                    total_rev += amt
                else:
                    total_exp += amt
            
            discretionary = total_rev + total_exp
            print(f"Revenue:${total_rev:.2f} Expenses: ${total_exp:.2f} Discretionary: ${discretionary:.2f}")

        # --- OPTION 4: Exit ---
        elif choice == '4':
            print("Thanks for using My Finance!")
            break
        else:
            print("Invalid selection.")

# Run the program
if __name__ == "__main__":
    main()