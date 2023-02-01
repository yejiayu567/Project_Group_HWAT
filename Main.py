# import modules
import cash_on_hand
import overheads
import profit_loss


# call function from adder module
def main():
    filename = 'summary_report.txt'
    overheads.overhead_function(filename)
    cash_on_hand.coh_function(filename)
    profit_loss.profit_loss_function(filename)


main()
