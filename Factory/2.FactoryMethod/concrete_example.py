from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class Square(Shape):
    def operation(self) -> str:
        return "Product: Operation performed by square!"


class Triangle(Shape):
    def operation(self) -> str:
        return "Product: Operation performed by triangle!"


class ShapeFactory(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def create_shape(self) -> str:

        # Call the factory method to create a Shape object.
        shape = self.factory_method()

        # Now, use the shape instance to do some operation.
        result = f"Creator: The same creator's code has just worked with {shape.operation()}"

        return result


class SquareFactory(ShapeFactory):

    def factory_method(self) -> Shape:
        return Square()


class TriangleFactory(ShapeFactory):

    def factory_method(self) -> Shape:
        return Triangle()


def client_code(creator: ShapeFactory) -> None:

    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.create_shape()}", end="")


if __name__ == "__main__":
    print("App: Launched with the SquareFactory.")
    client_code(SquareFactory())
    print("\n")

    print("App: Launched with the TriangleFactory.")
    client_code(TriangleFactory())


# Out:
# App: Launched with the SquareFactory.
# Client: I'm not aware of the creator's class, but it still works.
# Creator: The same creator's code has just worked with Product: Operation performed by square!
#
# App: Launched with the TriangleFactory.
# Client: I'm not aware of the creator's class, but it still works.
# Creator: The same creator's code has just worked with Product: Operation performed by triangle!
