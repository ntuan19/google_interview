from collections import defaultdict
class SnapShot():
    def __init__(self):
        self.current_snapshot = 0 
        self.dic = defaultdict(int)
        self.snapshotVersion = defaultdict(list)
    
    def put(self,k,v):
        self.dic[k] = v 
        self.snapshotVersion[k].append((self.current_snapshot,v))
    def take_snapshot(self):
        self.current_snapshot +=1
        return self.current_snapshot 

    def get(self,key,snapshotId =None):
        if snapshotId != None:
            if key in self.snapshotVersion:
                for version, val in self.self.snapshotVersion[key][::-1]:
                    if version <= snapshotId:
                        return val  
            else:
                return ""
        else:
            return self.dic.get(key,"")

s = SnapShot()
s.put("a",1)
print(s.get("a"))
s.put("b",2)
s.take_snapshot()
s.put("a",5)
print(s.get("a"),1)
s.put("a",1)
print(s.snapshotVersion)


