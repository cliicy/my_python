class Spring:
    pass


ss=Spring()
print(ss)
print(Spring)
print(hasattr(Spring,'temperature'))
Spring.temperature='20'
print(hasattr(Spring,'temperature'))

sp=Spring
print(sp())
