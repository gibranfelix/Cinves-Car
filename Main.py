__author__ = 'Usuario'

import Cinvescar

Vissim = Cinvescar.load("Real")

lanes = [(1, 4), (2, 3)]

Vissim.Simulation.RunContinuous()

SC_number = 1

Controller = Vissim.Net.SignalControllers.ItemByKey(SC_number)

PrincipalGroup = Controller.SGs.ItemByKey(1)
SecondaryGroup = Controller.SGs.ItemByKey(2)
PedestrianGroup = Controller.SGs.ItemByKey(3)
time = 15
while Vissim.Simulation.SimulationSecond <= 8000:
    if PrincipalGroup.AttValue("State") == "RED":
        totalcars = len(Cinvescar.getvehicles(lanes[0][0])) + len(Cinvescar.getvehicles(lanes[0][1]))
        if totalcars >= 30:
            time = 60
            Cinvescar.runseconds(time)
            PrincipalGroup.SetAttValue("State", "GREEN")
            SecondaryGroup.SetAttValue("State", "RED")
            PedestrianGroup.SetAttValue("State", "RED")
        elif 0 < totalcars < 30:
            time = totalcars*1.8
            Cinvescar.runseconds(time)
            PrincipalGroup.SetAttValue("State", "GREEN")
            SecondaryGroup.SetAttValue("State", "RED")
            PedestrianGroup.SetAttValue("State", "RED")
        elif totalcars == 0:
            Cinvescar.runseconds(time)
            PedestrianGroup.SetAttValue("State", "GREEN")
            SecondaryGroup.SetAttValue("State", "RED")
            PrincipalGroup.SetAttValue("State", "RED")

    elif SecondaryGroup.AttValue("State") == "RED":
        totalcars = len(Cinvescar.getvehicles(lanes[1][0])) + len(Cinvescar.getvehicles(lanes[1][1]))
        if totalcars >= 30:
            time = 60
            Cinvescar.runseconds(time)
            SecondaryGroup.SetAttValue("State", "GREEN")
            PrincipalGroup.SetAttValue("State", "RED")
            PedestrianGroup.SetAttValue("State", "RED")
        elif 0 < totalcars < 30:
            time = totalcars*1.8
            Cinvescar.runseconds(time)
            SecondaryGroup.SetAttValue("State", "GREEN")
            PrincipalGroup.SetAttValue("State", "RED")
            PedestrianGroup.SetAttValue("State", "RED")
        elif totalcars == 0:
            Cinvescar.runseconds(time)
            PedestrianGroup.SetAttValue("State", "GREEN")
            PrincipalGroup.SetAttValue("State", "RED")
            SecondaryGroup.SetAttValue("State", "RED")



# To stop the simulation:
Vissim.Simulation.Stop()
