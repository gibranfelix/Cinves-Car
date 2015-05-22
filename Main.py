__author__ = 'Usuario'

import Cinvescar

Vissim = Cinvescar.load("Real")

lanes = [(2, 6), (7, 3)]

Vissim.Simulation.RunContinuous()

SC_number = 1

Controller = Vissim.Net.SignalControllers.ItemByKey(SC_number)

PrincipalGroup = Controller.SGs.ItemByKey(1)
SecondaryGroup = Controller.SGs.ItemByKey(2)
PedestrianGroup = Controller.SGs.ItemByKey(3)
time = 15
index = 0
while Vissim.Simulation.SimulationSecond <= 8000:
    if index == 0:
        totalcars = len(Cinvescar.getvehicles(lanes[0][0])) + len(Cinvescar.getvehicles(lanes[0][1]))
        print "Principal: " + str(totalcars)
        if totalcars >= 30:
            time = 60
            PrincipalGroup.SetAttValue("State", "GREEN")
            SecondaryGroup.SetAttValue("State", "RED")
            PedestrianGroup.SetAttValue("State", "RED")
            Cinvescar.runseconds(time)
            PrincipalGroup.SetAttValue("State", "RED")
        elif 0 < totalcars < 30:
            time = totalcars * 1.8
            PrincipalGroup.SetAttValue("State", "GREEN")
            SecondaryGroup.SetAttValue("State", "RED")
            PedestrianGroup.SetAttValue("State", "RED")
            Cinvescar.runseconds(time)
            PrincipalGroup.SetAttValue("State", "RED")
        index = ((index + 1) % 3)
    elif index == 1:
        totalcars = len(Cinvescar.getvehicles(lanes[1][0])) + len(Cinvescar.getvehicles(lanes[1][1]))
        print "Secundario: "+ str(totalcars)
        if totalcars >= 30:
            time = 60
            SecondaryGroup.SetAttValue("State", "GREEN")
            PrincipalGroup.SetAttValue("State", "RED")
            PedestrianGroup.SetAttValue("State", "RED")
            Cinvescar.runseconds(time)
            SecondaryGroup.SetAttValue("State", "RED")
        elif 0 < totalcars < 30:
            time = totalcars * 1.8
            SecondaryGroup.SetAttValue("State", "GREEN")
            PrincipalGroup.SetAttValue("State", "RED")
            PedestrianGroup.SetAttValue("State", "RED")
            Cinvescar.runseconds(time)
            SecondaryGroup.SetAttValue("State", "RED")
        index = ((index + 1) % 3)
    elif index == 2:
        PedestrianGroup.SetAttValue("State", "GREEN")
        PrincipalGroup.SetAttValue("State", "RED")
        SecondaryGroup.SetAttValue("State", "RED")
        Cinvescar.runseconds(time)
        PedestrianGroup.SetAttValue("State", "RED")
        index = ((index + 1) % 3)




# To stop the simulation:
Vissim.Simulation.Stop()
