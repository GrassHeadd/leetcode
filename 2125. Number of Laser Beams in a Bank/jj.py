class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        # keep track of start and end row, find number of 1s, take to times from, if empty row skip

        i = 0
        j = 1
        if j >= len(bank):
            return 0
        start = bank[i]
        end = bank[j]
        total = 0

        while j < len(bank):
            print("bruh")
            n = 0
            m = 0
            # case of empty row:
            test = ""
            for char in end:
                test += "0"
            if end == test:
                j += 1
                if j >= len(bank):
                    break
                end = bank[j]
                continue
            for char in start:
                if char == "1":
                    n += 1
            for char in end:
                if char == "1":
                    m += 1
            total += m * n

            i = j
            j += 1
            if j >= len(bank):
                break

            start = bank[i]
            end = bank[j]
        return total
