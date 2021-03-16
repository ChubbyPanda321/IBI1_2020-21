#import matpoltlib
import matplotlib.pyplot as plt
#define a function so it's easier to use later
def mkplot_infection_rate(**case):  
    plt.pie(
        case.values(),
        labels = case.keys(),
        autopct = '%1.1f%%',
        shadow = True
        )
    plt.axis('equal')
    plt.title('Infected cases by countries\n')
    plt.show()
    return case
#use the function to create to plot
cases = mkplot_infection_rate(
    USA = 29862124,
    India = 11285561,
    Brazil = 11205972,
    Russia = 4360823,
    UK = 4234924
    )
#print the dict of the infected cases
print(cases)
