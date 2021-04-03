import matplotlib.pyplot as plt
import numpy as np
import pyoeis

c = pyoeis.OEISClient()
i = [int(i) for i in input().split()]
l = c.lookup_by_terms(i)
plt.plot(l[0].unsigned(10000), color="black" , marker='o', linestyle='dashed', linewidth=1 , markerfacecolor='tab:green' , markersize=6)
'rebeccapurple'
print(l[0].name)
plt.title(l[0].unsigned(10))
plt.show()
