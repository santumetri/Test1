class live1():
    def getinput(self):
        print ("Enter the paragraph: , finish by hitting ctl+z")
        content =[]
        while True:
            try:
                line=input()
            except EOFError:
                break
            content.append(line)
        content = " ".join(content)
        return content

    def compare(self,lst):
            lst1 = []
            for i in lst:
                if i not in lst1:
                    lst1.append(i)
            nofound =1
            for i in range(0, len(lst1)):
                if lst.count(lst1[i]) >1:
                    print("word:","\"",lst1[i],"\"", "occurrence: ", lst.count(lst1[i]))
                    nofound = 0

            if nofound:
                print("No words are repeated")

