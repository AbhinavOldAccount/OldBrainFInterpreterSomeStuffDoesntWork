import os as Os
import webbrowser as WebBrowser

class BrainF:
    def __init__(Self, Dummy):
        Self.Version = "0.0.1"

    def Run(Self, Program):
        Self.Parse(Program)

    def Parse(Self, Program):
        Output = ""
        IsError = False
        LoopRunning = False
        LoopStartPosition = None
        Position = -1
        Array = [0]
        PointerIndex = 0

        while Position < len(Program) - 1:
            Position += 1
            CurrentCharacter = Program[Position]

            if CurrentCharacter in " \n": continue
            elif CurrentCharacter == "<":
                if PointerIndex == 0: PointerIndex = len(Array) - 1
                else: PointerIndex -= 1
            elif CurrentCharacter == ">":
                if PointerIndex + 1 >= len(Array): Array.insert(PointerIndex + 1, 0)
                PointerIndex += 1
            elif CurrentCharacter == "+": Array[PointerIndex] += 1
            elif CurrentCharacter == "-": Array[PointerIndex] -= 1
            elif CurrentCharacter == ".": Output += chr(Array[PointerIndex])
            elif CurrentCharacter == "[":
                LoopStartPosition = Position
                LoopRunning = True
            elif CurrentCharacter == "]":
                if LoopRunning:
                    if Array[PointerIndex] == 0: LoopRunning = False
                    else: Position = LoopStartPosition
                else:
                    print('Error: Expected "<", ">", "+" or "-". Got "]"')
                    IsError = True
                    break
            else:
                print(f'Error: Invalid Character "{CurrentCharacter}"')
                IsError = True
                break
        
        if not IsError:
            if Output != "": print(Output)
            print(">", end=" ")
            for Element in Array:
                if Array.index(Element) == PointerIndex: print(f"[{Element}]", end=" ")
                else: print(Element, end=" ")
            print()
        print()

WebBrowser.open(Os.getcwd() + "\Website.html", new=2)

NewBrainF = BrainF("")
while True:
    print("BrainF")
    Text = input(">>> ")
    try:
        if Text[1] == ":":
            try:
                TextFile = open(Text, "r")
                NewBrainF.Run(TextFile.read())
                TextFile.close()
            except: print("Error: File Not Found")
        else: NewBrainF.Run(Text)
    except: NewBrainF.Run(Text)