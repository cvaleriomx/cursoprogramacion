import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def multiply_by_scalar(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    def pcross(self, other):
        return Vector3D(self.y *other.z-self.z*self.y,
                        self.z *other.x-self.x*other.z,
                        self.x *other.y-self.y*other.x)
    def norma(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    def angulo_vectores(self,other):
        angulo=math.acos(self*other/(self.norma()*other.norma()))*180/3.1416
        return angulo

    def __repr__(self):
        #return f"V3D({self.x}, {self.y}, {self.z})"
        #return "V3D({}, {}, {})".format(self.x, self.y, self.z)
        return "V3D(%s, %s, %s)" % (self.x, self.y, self.z)

# Ejemplo de uso:
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

# Suma de vectores
sum_result = v1 + v2
print("Suma de vectores:", sum_result)

# Resta de vectores
sub_result = v1 - v2
print("Resta de vectores:", sub_result)

# Multiplicación por escalar
scalar_multiplication = v1.multiply_by_scalar(3)
print("Multiplicación por escalar:", scalar_multiplication)

# Producto punto
#dot_product = dot_product(v1,v2)

#dot_product = v1.dot_product(v2)
dot_product = v1*v2

print("Producto punto:", dot_product)
cruz=v1.pcross(v2)
print("Producto cruz:",cruz)

norma1=v1.norma()
print("norma del vector:",norma1)
v5= Vector3D(0, 1, 0)
v6= Vector3D(1, 1, 0)
ang=v5.angulo_vectores(v6)
print("angulo vec:",ang)
