class File:
    def __init__(self, path, separator='\t'):
        self.deletions = 0
        self.insertions = 0
        self.substitutions = 0
        self.exon = 0
        self.splice = 0
        self.nonsense = 0
        self.content = []
        self.data = []
        self.headers = []
        self.openFile(path, separator)
        self.countMutations()
        self.mutationLocation()

    def openFile(self, path, separator):
        with open(path, 'r') as file:
            content = file.readlines()
            for i in range(len(content)):
                temp = content[i].split(separator)
                if temp[0] == '':
                    break
                elif temp[0] != '':
                    self.content.append(temp)
        self.headers = self.content[0]
        self.data = self.content[1:]

    def findHeader(self, header):
        for i in range(len(self.headers)):
            if self.headers[i] == header:
                return i
        return -1

    def countEntries(self):
        return len(self.data)

    def countMutations(self):
        insertions = 0
        deletions = 0
        substitutions = 0
        header = self.findHeader('Abberation')
        for i in range(len(self.data)):
            if self.data[i][header] == 'insertion':
                insertions += 1
            elif self.data[i][header] == 'deletion':
                deletions += 1
            elif self.data[i][header] == 'substitution':
                substitutions += 1
        self.insertions = insertions
        self.deletions = deletions
        self.substitutions = substitutions

    def mutationLocation(self):
        header = self.findHeader('Gene component')
        exon = 0
        splice = 0

        for i in range(len(self.data)):
            if self.data[i][header] == 'EXON_REGION':
                exon += 1
            elif self.data[i][header] == 'SD_SITE_CANONICAL':
                splice += 1

        self.exon = exon
        self.splice = splice

    def nonsense(self):
        header = self.findHeader('Mutation Amino Acid')
        count = 0
        for i in range(len(self.data)):
            if self.data[i][header] == '*':
                count += 1
        self.nonsense = count

    def omimFilter(self, omim):
        header = self.findHeader('OMIM_DISEASE')
        omimlist = []
        for i in range(len(self.data)):
            if omim in self.data[i][header]:
                omimlist.append(self.data[i])
        self.data = omimlist

    def names(self):
        header = self.findHeader('Gene name')
        names = []
        for i in range(len(self.data)):
            names.append(self.data[i][header])
        return names

    def aminoacids(self):
        header = self.findHeader('AminoAcid changes')
        aminoacids = []
        for i in range(len(self.data)):
            if self.data[i][header] != '':
                aminoacids.append(self.data[i][header])
            else:
                aminoacids.append('null')
        return aminoacids

    def filterPathogene(self):
        header = self.findHeader('SNP state')
        header2 = self.findHeader('Causative - Projects')
        pathogene = []
        for i in range(len(self.data)):
            if self.data[i][header] == '' or self.data[i][header2] == 'HGMD':
                pathogene.append(self.data[i])
        self.data = pathogene

    def purify(self):
        header = self.findHeader('% variation')
        header2 = self.findHeader('variation reads')
        purify = []
        for i in range(len(self.data)):
            if self.data[i][header] != '' and float(
                    self.data[i][header]) >= 20 and int(
                    self.data[i][header2]) >= 5:
                purify.append(self.data[i])
        self.data = purify

    def removeIntron(self):
        header = self.findHeader('Gene component')
        intron = []
        for i in range(len(self.data)):
            if self.data[i][header] != 'INTRON_REGION':
                intron.append(self.data[i])
        self.data = intron

    def proteinCheck(self):
        header = self.findHeader('Protein domain')
        newdata = []
        for i in range(len(self.data)):
            if self.data[i][header] != 'No protein':
                newdata.append(self.data[i])
        self.data = newdata

    def filter(self, omim):
        self.omimFilter(omim)
        self.proteinCheck()
        self.filterPathogene()
        self.purify()
        self.removeIntron()
