import pulp

x1=pulp.LpVariable("x1",lowBound=0)
x2=pulp.LpVariable("x2",lowBound=0)
x3=pulp.LpVariable("x3",upBound=0)

optimum=pulp.LpProblem("max",pulp.LpMaximize)

optimum+=2*x2-x3+3, "objective function"

optimum+=x1+x2+x3<=3
optimum+=x1+x2+x3>=3
optimum+=x1-x2>=1
optimum+=x2-x3<=1
optimum+=x1+x2>=3

optimum.solve()

print("decision variable values")

for variable in optimum.variables():
    print(variable.name,"=",variable.varValue)

print("\nmax:")
pulp.value(optimum.objective)
