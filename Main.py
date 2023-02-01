# import modules
import cash_on_hand, overheads, profit_loss

def main():
    """
    This function will call functions from adder modules
    No parameter is required
    """
    
    filename = 'summary_report.txt'
    overheads.Overhead_Function(filename)
    cash_on_hand.COH_Function(filename)
    profit_loss.Profit_Loss_Function(filename)


main()
