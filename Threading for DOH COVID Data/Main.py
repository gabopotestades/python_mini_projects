import os
import time
import linecache

if __name__ == '__main__':
    
    #Set initial values
    mode = ''
    command = 'cls' if os.name == 'nt' else 'clear'

    casesFileName = 'Case_Summary.txt'
    hospitalFileName = 'Hospital_Summary.txt'
    inventoryFileName = 'Inventory_Summary.txt'

    #Choose S for serial and P for parallel
    while mode not in ['S', 'P', 'T']:
        os.system(command)
        mode = input('Select mode (S/T/P): ').upper()

    start_time = time.time()

    if mode == 'S':
        import SerialProcessing
    elif mode == 'T':
        
        import ThreadProcessing
        casesInformationThread = ThreadProcessing.caseThread(1, casesFileName)
        hospitalsInformationThread = ThreadProcessing.hospitalsThread(2, hospitalFileName)
        inventoryInformationThread = ThreadProcessing.inventoryThread(3, inventoryFileName)

        casesInformationThread.start()
        hospitalsInformationThread.start()
        inventoryInformationThread.start()

        casesInformationThread.join()
        hospitalsInformationThread.join()
        inventoryInformationThread.join()

    elif mode == 'P':

        import ParallelProcessing
        casesInformationProcess = ParallelProcessing.caseProcess(1, casesFileName)
        hospitalsInformationProcess = ParallelProcessing.hospitalsProcess(2, hospitalFileName)
        inventoryInformationProcess = ParallelProcessing.inventoryProcess(3, inventoryFileName)

        casesInformationProcess.start()
        hospitalsInformationProcess.start()
        inventoryInformationProcess.start()

        casesInformationProcess.join()
        hospitalsInformationProcess.join()
        inventoryInformationProcess.join()

    print('\n Time processed:')
    end_time = time.time() - start_time
    print("--- %s seconds ---" % end_time)
