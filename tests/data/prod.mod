set P;

param a {j in P};
param b;
param c {j in P};
param u {j in P};

var X {j in P};

maximize profit: sum {j in P} c[j] * X[j];

subject to Time:  sum {j in P} (1/a[j]) * X[j] <= b;

subject to Limit {j in P}:  0 <= X[j] <= u[j];


data;  ############ DATA STARTS HERE ############


set P := bands coils;

param:     a     c     u  :=
  bands   200   25   6000
  coils   140   30   4000 ;

param b := 40;


