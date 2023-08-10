DIGITS = set("0123456789")
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        num_logs = []
        let_logs = []
        for lg in logs:
            _id, cont = lg.split(" ", 1)
            if cont[0] in DIGITS:
                num_logs.append(lg)
            else:
                let_logs.append([cont, _id])
        return [ _id+ " " + cnt for cnt, _id in sorted(let_logs)] + num_logs