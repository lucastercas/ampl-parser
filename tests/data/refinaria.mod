var xs >= 0 <= 9;
var xv >= 0 <= 6;

minimize Custo: 20*xs + 15*xv;

subject to gas: 0.3*xs + 0.4*xv >= 2;
subject to que: 0.4*xs + 0.2*xv >= 1.5;
subject to ole: 0.2*xs + 0.3*xv >= 0.5;
end;
