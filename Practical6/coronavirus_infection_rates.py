#import matpoltlib
import matplotlib.pyplot as plt
#define a function so it's easier to use later
def mkplot_infection_rate(**case):  
    fig, ax = plt.subplots()
    ax.pie(
        case.values(),
        labels = case.keys(),
        autopct = '%1.1f%%',
        shadow = True
        )
    ax.axis('equal')
    plt.show()
#use the function to create to plot
mkplot_infection_rate(
    USA = 29862124,
    India = 11285561,
    Brazil = 11205972,
    Russia = 4360823,
    UK = 4234924
    )

