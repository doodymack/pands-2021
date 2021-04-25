# messingWithCorrelations.py
#Author: PaulMcGrath
# trialling scatter and correlations

import matplotlib
import matplotlib.pyplot as plt

plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])

plt.xlabel('Months')
plt.ylabel('Books Read')

plt.show()
plt.savefig('books_read.png', dpi=300, bbox_inches='tight')