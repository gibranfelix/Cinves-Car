__author__ = 'Gibran Felix'

import cinvescar

if __name__ == '__main__':
    Vissim = cinvescar.Load("COM_example")
    cinvescar.GetSteps(200)
    cinvescar.GetAllVehicles()
