import matplotlib.pyplot as plt
predator_population= 15
prey_population= 100
predator_birth_fraction = 0.01
predator_births = (predator_birth_fraction * prey_population) * predator_population
predator_death_proportionality_constant = 1.06
predator_deaths = predator_death_proportionality_constant * predator_population
prey_birth_fraction = 2
prey_births = prey_birth_fraction * prey_population
prey_death_proportionality_constant = 0.02
prey_deaths = (prey_death_proportionality_constant * predator_population)* prey_population
t=0
dt=0.001
simLength=12
numiterations=int(simLength/dt)+1
timeLst=[t]
predatorLst=[predator_population]
preyLst=[prey_population]
for i in range(1,numiterations):
    t=i*dt
    prey_population=prey_population+(prey_births-prey_deaths)*dt
    predator_population=predator_population+(predator_births-predator_deaths)*dt
    predator_births = (predator_birth_fraction * prey_population) * predator_population
    predator_deaths = predator_death_proportionality_constant * predator_population
    prey_births = prey_birth_fraction * prey_population
    prey_deaths = (prey_death_proportionality_constant * predator_population) * prey_population
    timeLst.append(t)
    predatorLst.append(predator_population)
    preyLst.append(prey_population)
print('Months\t\tPrey Population\t\tPredator Population\n')
for i in range(1,13):
    print('%5.1f\t\t%5.2f\t\t%5.2f\n\n' %(timeLst[i*1000],preyLst[i*1000],predatorLst[i*1000]))
plt.plot(timeLst,preyLst, color='blue')
plt.text(2,450,'Prey(squirrel)',color='blue')
plt.plot(timeLst,predatorLst,color='red')
plt.text(2.5,300,'Predator(hawk)',color='red')
plt.xlabel('Months')
plt.title('Prey-Predator Model: Graph of Squirrel and Hawk populations versus time in months')
plt.show()
