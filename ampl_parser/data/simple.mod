var xs;

minimize Custo_Total: 20 + 1 * 2^2;
minimize Peso_Total: 20*xs + 1 * 2^2 * x;
minimize Seila_Total: 20.5*xs + 2*ys;

subject to ole: 0.2*xs + 0.3*xv >= 0.5;

end;