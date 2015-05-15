__author__ = 'Gibran Felix'

import cinvescar

if __name__ == '__main__':
    Vissim = cinvescar.Load("COM_example")

    cinvescar.RunSeconds(30)
    cinvescar.GetVehicles(1)

    #for s in Vissim.Net.SignalHeads:
      #  print s.AttValue("No"), s.AttValue("Lane"), s.AttValue("State"), s.AttValue("LabPosRelX"), s.Lane.Link.AttValue("No"), s.Lane.AttValue("Width"), s.AttValue("Pos")

    #cinvescar.GetAllVehicles()
