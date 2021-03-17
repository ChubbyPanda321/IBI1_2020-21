#import packages
import numpy as np
import matplotlib.pyplot as plt
#use ndarray to calculate the average length
gene_lengths = [9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts = [51,1142,42,216,25,650,32533,57,1,523]
gl_array = np.array(gene_lengths)
ec_array = np.array(exon_counts)
average_exon_length = sorted(gl_array/ec_array)
#print the sorted list
print(average_exon_length)
#make the plot
plt.boxplot(
    average_exon_length,
    notch=False,
    )
plt.ylabel('Length / bp')
plt.xticks([])
plt.grid(True)
plt.title('The average exon length')
plt.show()
#how to change the color of the plot?pls