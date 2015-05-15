__author__ = "Gibran Felix"

import win32com.client as com
import os

Vissim = []

def DefaulValues():
    global Vissim

    random_seed = 42
    Vissim.Simulation.SetAttValue('RandSeed', random_seed)

    # Set maximum speed:
    Vissim.Simulation.SetAttValue('UseMaxSimSpeed', True)

    Vissim.Simulation.SetAttValue('SimSpeed', 100) # 10 => 10 Sim.sec. / s
    # Or run the simulation continuous (it stops at breakpoint or end of simulation)
    end_of_simulation = 8000 # Simulationsecond [s]
    Vissim.Simulation.SetAttValue('SimPeriod', end_of_simulation)

def Load(filename):
    global Vissim
    ## Connecting the COM Server => Open a new Vissim Window:
    Vissim = com.Dispatch("Vissim.Vissim")
    # If you have installed multiple Vissim Versions, you can open a spcific Vissim version adding the bit Version (32 or 64bit) and Version number
    # Vissim = com.Dispatch("Vissim.Vissim-32.600") # Vissim 6 - 32 bit
    # Vissim = com.Dispatch("Vissim.Vissim-64.600") # Vissim 6 - 64 bit
    # Vissim = com.Dispatch("Vissim.Vissim-32.700") # Vissim 7 - 32 bit
    #Vissim = com.Dispatch("Vissim.Vissim-64.700") # Vissim 7 - 64 bit
    Path_of_COM_example_network = os.getcwd()  #'C:\\Users\\Public\\Documents\\PTV Vision\\PTV Vissim 7\\Examples Training\\COM\\Basic Commands\\'

    #Load a Vissim Network:
    Filename = os.path.join(Path_of_COM_example_network, filename + '.inpx')
    flag_read_additionally = False  # you can read network(elements) additionally, in this case set "flag_read_additionally" to true
    Vissim.LoadNet(Filename, flag_read_additionally)
    ## Load a Layout:
    Filename = os.path.join(Path_of_COM_example_network, filename + '.layx')
    Vissim.LoadLayout(Filename)
    DefaulValues()
    return Vissim

def GetAllVehicles():
    # Method #2: Loop over all Vehicles using Object Enumeration
    for Vehicle in Vissim.Net.Vehicles:
        print Vehicle
        veh_number = Vehicle.AttValue('No')
        veh_type = Vehicle.AttValue('VehType')
        veh_speed = Vehicle.AttValue('Speed')
        veh_position = Vehicle.AttValue('Pos')
        veh_linklane = Vehicle.AttValue('Lane')
        print '%s  |  %s  |  %.2f  |  %.2f  |  %s' % (veh_number, veh_type, veh_speed, veh_position, veh_linklane)

def GetVehicles(signal):
    lstVehicle = []

    signalhead = Vissim.Net.SignalHeads.ItemByKey(signal)
    link_no = signalhead.Lane.Link.AttValue("No")

    allVehicles = Vissim.Net.Links.ItemByKey(link_no).Vehs
    for v in allVehicles:
        if(signalhead.AttValue("Pos") > v.AttValue("Pos") and signalhead.AttValue("Pos") - 30 <= v.AttValue("Pos")):
            lstVehicle.append(v)
            print v
    return lstVehicle


def RunSteps(num):
    global Vissim
    for i in range(num):
        Vissim.Simulation.RunSingleStep()
    print Vissim.Simulation.SimulationSecond

def RunSeconds(sec):
    global Vissim
    stoptime = sec + Vissim.Simulation.SimulationSecond
    Vissim.Simulation.SetAttValue('SimBreakAt', stoptime)
    Vissim.Simulation.RunContinuous()
    print Vissim.Simulation.SimulationSecond
