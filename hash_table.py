uidHash = {}

def read_file(filename):
    try:
        f = open(filename, "r")
        # initialize the list
        ls = []
        #lines = f.readlines()
        #print(lines)
        for ln in f.readlines():
            print(ln)
            ls = ln.split(':')
            print(ls)
            print("UID is :%s" %ls[2])
            # now create the hash_table for each UID
            if ls[2] not in uidHash.keys():
                uidHash[ls[2]] = ln
            else:
                print("Duplicate key")
                print(uidHash[ls[2]])
                print(ln)
    except IOError:
        print("Could not open file")
#    except Exception:
#        print(ln)
#        print ("Duplicate UIDs in the passwd file")


if __name__ == "__main__":
    fname = input("Enter the filename")
    read_file(fname)
    print(uidHash)
