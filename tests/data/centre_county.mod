var x1 binary;
var x2 binary;
var x3 binary;
var x4 binary;

maximize Profit: 600 * x1 + 100 * x2 + 300 * x3 + 500 * x4;

subject to Budget: 50 * x1 + 20 * x2 + 150 * x3 + 70 * x4 <= 200;
subject to Space: 8 * x1 + 4 * x3 + 5 * x4 <= 15;
subject to IfBasketballThenPark: x2 <= x1;
end;
