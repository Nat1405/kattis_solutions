import sys

class CongaLine:
    def __init__(self):
        self.lineup = []

    def setup(self):
        # Consume first line, tells us how many couples and instructions 
        num_couples, self.num_instructions = \
                map(int, sys.stdin.readline().rstrip('\n').split(' '))

        for i in range(num_couples):
            line = sys.stdin.readline()
            # Obtuse way to clean up line to two names,
            # and construct two dancer objects from those lines.
            dancer_1, dancer_2 = \
                map(Dancer, line.rstrip('\n').split(' '))

            dancer_1.partner = dancer_2
            dancer_2.partner = dancer_1

            self.lineup.append(dancer_1)
            self.lineup.append(dancer_2)
        
        # Hand mic to first person in line
        self.lineup[0].hasMic = True


    def __str__(self):
        output = (f"Dancer       Partner   hasMic\n")
        for d in self.lineup:
            output += str(d) + '\n'

        return output

    def get_line_moving(self):
        # Start processing instructions
        for i in range(self.num_instructions):
            instruction = sys.stdin.read(1)

            # Switch to deal with five instruction types
            if instruction == 'F':
                self.F()
            elif instruction == 'B':
                self.B()
            elif instruction == 'R':
                self.R()
            elif instruction == 'C':
                self.C()
            elif instruction == 'P':
                self.P()
                
                
    # Five instruction types. Modify line in-place ish, and may print output.
    def F(self):
        #print("F")
        self.pass_forward()
        #print(self)


    def B(self):
        #print("B")
        self.pass_back()
        #print(self)

    def R(self):
        #print("R")
        self.move_to_back(
            self.pop_former_mic_holder_off(
                self.pass_back()
            )
        )
        #print(self)

    def C(self):
        #print("C")
        self.move_behind_partner(
            self.pop_former_mic_holder_off(
                self.pass_back()
            )
        )
        #print(self)

    def P(self):
        #print("P")
        self.yell_partners_name()
        #print(self)


    # Now, there are 5 fundamental operations behind the five instructions.
    # Cleaner to implement them here this way.

    def pass_forward(self):
        """passes mic forward and returns reference to former mic holder"""
        #print("Pass forward")
        mic_holder_index = self.mic_holder_index()
        former_mic_holder_index = self.lineup[mic_holder_index]

        # Is mic holder @ front of line? If so pass to back
        if mic_holder_index == 0:
            self.lineup[0].hasMic = False
            self.lineup[-1].hasMic = True
        else:
            self.lineup[mic_holder_index].hasMic = False
            self.lineup[mic_holder_index - 1].hasMic = True

        return former_mic_holder_index

    def pass_back(self):
        """passes mic back and returns reference to former mic holder"""
        #print("Pass backward")
        mic_holder_index = self.mic_holder_index()
        former_mic_holder_index = mic_holder_index

        # Is mic holder @ back of line? If so pass to back
        if mic_holder_index == len(self.lineup) - 1:
            self.lineup[-1].hasMic = False
            self.lineup[0].hasMic = True
        else:
            self.lineup[mic_holder_index].hasMic = False
            self.lineup[mic_holder_index + 1].hasMic = True

        return former_mic_holder_index

    def pop_former_mic_holder_off(self, former_mic_holder_index):
        """pop the former mic holder out of the line"""
        #print("pop mic holder off")
        return self.lineup.pop(former_mic_holder_index)

    def move_to_back(self, former_mic_holder):
        #print("move to back")
        self.lineup.append(former_mic_holder)

    def move_behind_partner(self, former_mic_holder):
        #print("move behind partner")
        partner_index = self.lineup.index(
            former_mic_holder.partner
        )
        self.lineup.insert(partner_index + 1, former_mic_holder)

    def yell_partners_name(self):
        """Get the mic holder to yell partners name"""
        #print("yell partners name")
        print(
            self.lineup[self.mic_holder_index()].partner.name)


    def mic_holder_index(self):
        # Could probably be done more efficient
        for i in range(len(self.lineup)):
            if self.lineup[i].hasMic:
                return i

class Dancer:

    def __init__(self, name):
        self.name = name
        self.partner = None
        self.hasMic = False

    def __str__(self):
        return f"{self.name:7} -- > {self.partner.name:7}" + \
                f"{'   *' if self.hasMic else ''}"


if __name__ == "__main__":
    conga_line = CongaLine()

    conga_line.setup()

    #print(conga_line)

    conga_line.get_line_moving()
    
    print()
    for d in conga_line.lineup:
        print(d.name)

    
