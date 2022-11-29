from minimal_crossing import *
from newick_parse import *


T1 = stringToNewick('(V1980,(V1978,(V1968,(V1965,(V1962,V1963,V1964,(V1967,(V1959,V1960),V1966)))),((V1969,V1970),(V1971,(V1972,V1973))),((V1981,V1982),(V1984,(V1990,(V1989,V1991))),((V1987,V1988),(V1985,V1986,(V1993,V1994))),(V1983,V1992))),(V1999,(V1998,(V2000,V2001),(V1997,(V1995,V1996)))),((V1977,V1979),V1976,(V1974,V1975)))')
m,bt,newT = numberCrossing(T1)
print(m,newickToString(newT)=='(((V1974,V1975),V1976,(V1977,V1979)),((((V1962,V1963,V1964,((V1959,V1960),V1966,V1967)),V1965),V1968),((V1969,V1970),(V1971,(V1972,V1973))),V1978,((V1981,V1982),(V1984,(V1990,(V1989,V1991))),(V1983,V1992),((V1987,V1988),(V1985,V1986,(V1993,V1994))))),V1980,((((V1995,V1996),V1997),V1998,(V2000,V2001)),V1999));')

