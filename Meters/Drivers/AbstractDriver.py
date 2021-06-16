from abc import ABC, abstractmethod

class AbstractDriver(ABC):
    def Errcheck(self):

        myError = []
        ErrorList = self.Meter.query("SYST:ERR?").split(',')
        Error = ErrorList[0]
        if int(Error) == 0:
            print("+0, No Error!")
        else:
            while int(Error) != 0:
                print("Error #: " + ErrorList[0])
                print("Error Description: " + ErrorList[1])
                myError.append(ErrorList[0])
                myError.append(ErrorList[1])
                ErrorList = self.Meter.query("SYST:ERR?").split(',')
                Error = ErrorList[0]
                myError = list(myError)

        return myError

    def Open(self, mPar):
        data = '*RST'.encode()
        self.Meter.write(data.decode('utf-8'))

    def Close(self):
        self.Meter.write('SYST:PRES')
        self.Meter.clear()
        self.Meter.close()
