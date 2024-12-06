def swap_case(s):
   return ''.join(map(lambda c: c.upper() if c.islower() else c.lower(), s))
    

if __name__ == '__main__':
