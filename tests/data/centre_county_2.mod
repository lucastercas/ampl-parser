set PROJECTS;

param usage {PROJECTS};
param cost {PROJECTS};
param space {PROJECTS};

var Select {PROJECTS} binary;

maximize TotalUsage: sum {j in PROJECTS} usage[j] * Select[j];

subject to Budget: sum {j in PROJECTS} cost[j] * Select[j] <= 200;
subject to LandAvailable: sum {j in PROJECTS} space[j] * Select[j] <= 15;
end;