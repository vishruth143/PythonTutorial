class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # No instance exists
            cls._instance = super().__new__(cls)  # Create design_pattern new instance
        return cls._instance  # Return the single instance

# Test the Singleton
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # True: Both are the same instance