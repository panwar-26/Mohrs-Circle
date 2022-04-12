import numpy as gt
import matplotlib.pyplot as graph
from math import *
import math

import datetime
now = datetime.datetime.now()



# -------------------------------------------------------------Graphical Method---------------------------------------------------------------------------------------------------
class MohrsCircle:

    def __init__(self, sigma_X, sigma_Y, tau_XY):  # Constructor For The MohrsCircle Class
        self.sigma_X = sigma_X  # Assigning Values corresponding to it.
        self.sigma_Y = sigma_Y
        self.tau_XY = tau_XY

    def center(self):  # Finding Centre Of The Circle
        return (self.sigma_X + self.sigma_Y) / 2

    def radius(self):  # Finding Radius Of The Circle
        x = (self.sigma_X - self.sigma_Y) / 2
        b = self.tau_XY
        d = pow((pow(x, 2) + pow(b, 2)), 0.5)
        return d

    def MaxPrincipalStress(self):  # Finding Maximum Principal Stress
        return self.center() + self.radius()

    def MinPrincipalStress(self):  # Finding Minimum Principal Stress
        return self.center() - self.radius()

    def MaxShearStress(self):  # # Finding Maximum Shear Stress
        return self.radius()

    def plot(self):  # Plotting The Circle
        rad = gt.linspace(0, 360, 361) * (2 * gt.pi / 360)  # Constructing Plane
        X_point = self.center() + self.radius() * gt.cos(rad)  # X coordinate values using x = x' + r cos(theta)
        Y_point = self.radius() * gt.sin(rad)  # Y coordinate values using y = y' + r sin(theta)

        graph.figure(figsize=[6, 5])
        graph.plot(X_point, Y_point, label="Mohr's Circle", color='Black')  # Plotting the Graph
        graph.plot([self.sigma_X, self.sigma_Y], [self.tau_XY, -self.tau_XY],[self.sigma_X,self.sigma_X],[self.tau_XY,0],[self.sigma_Y,self.sigma_Y],[-self.tau_XY,0],[self.center(),self.center()],[self.MaxShearStress(),-self.MaxShearStress()] ,linestyle = '--',color="blue")  # Plotting The coordinates
        graph.plot([self.center()], [0], marker='o', color='black')

        graph.title("Mohr's Circle", fontsize=20)
        graph.xlabel(r'$\sigma$(Normal Stress)', fontsize=15)
        graph.ylabel(r'$\tau$(Shear Stress)', fontsize=15)

        graph.axhline(color='k')
        graph.axvline(color='k')

        graph.fill_between(X_point, Y_point, color='b', alpha=0.1)

        graph.grid()
        X1 = str(self.sigma_X)
        Y1 = str(self.tau_XY)
        X2 = str(self.sigma_Y)
        Y2 = str(-self.tau_XY)
        cen = str(self.center())
        graph.text(self.MaxPrincipalStress(), 0, r'$\sigma_{max}$', va='bottom', ha='right', fontsize=18)
        graph.text(self.MinPrincipalStress(), 0, r'$\sigma_{min}$', ha='left', va='bottom', fontsize=18)
        graph.text(self.center(), self.MaxShearStress(), r'$\tau_{max}$', va='top', ha='center', fontsize=18)
        graph.text(self.center(), 0,'(' + cen + ',' + '0' + ')' , va='bottom', ha='right', fontsize=10, color = "magenta")
        graph.text(self.sigma_X, self.tau_XY, '(' + X1 + ',' + Y1 + ')', va='bottom', ha='right', fontsize=10,
                   color="red")
        graph.text(self.sigma_Y, -self.tau_XY, '(' + X2 + ',' + Y2 + ')', va='bottom', ha='left', fontsize=10,
                   color="red")
        graph.tight_layout()

        graph.show()


# -------------------------------------------------------------------------Analyic Method-----------------------------------------------------------------------------------------


class MohrAnalytic:
    def __init__(self, sigma_X, sigma_Y, tau_XY):  # Constructor For The MohrsCircle Class
        self.sigma_X = sigma_X
        self.sigma_Y = sigma_Y
        self.tau_XY = tau_XY

    def Principal_Plane_Theta(self):
        x = 2 * self.tau_XY / (self.sigma_X - self.sigma_Y)
        theta = math.degrees(math.atan(x)) / 2
        return theta

    def Shear_Stress_Plane_Theta(self):
        x = -(self.sigma_X - self.sigma_Y) / (2 * self.tau_XY)
        theta = math.degrees(math.atan(x)) / 2
        return theta

    def MaximumPrincipalStress(self):
        x = (self.sigma_X + self.sigma_Y) / 2
        y = (self.sigma_X - self.sigma_Y) / 2
        z = self.tau_XY
        m = x + pow(pow(y, 2) + pow(z, 2), 0.5)
        return m

    def MinimumPrincipalStress(self):
        x = (self.sigma_X + self.sigma_Y) / 2
        y = (self.sigma_X - self.sigma_Y) / 2
        z = self.tau_XY
        m = x - pow(pow(y, 2) + pow(z, 2), 0.5)
        return m

    def MaximumShearStress(self):
        x = (self.MaximumPrincipalStress() - self.MinimumPrincipalStress()) / 2
        return x



"----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
# MAIN

print('''\t\t Hello This Is ME212 Project 
    \t\tTopic - Finding Limiting Stresses Using Mohr's Circle
    \t\tMade By - Jitendra Kumar Pandey
    \t\tRoll - 200103055''')

print("\t\tCurrent date and time: ")
print(now.strftime('\t\t%Y-%m-%d %H:%M:%S'))

"----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
print()
print()
print("Enter The Values Of The Required Parameters:")
print("----------------------------------------------------------------------")
print()
Sigma_X = float(input("Enter The Normal Stress(SigmaX in kN/m^2): "))
Sigma_Y = float(input("Enter The Normal Stress(SigmaY in kN/m^2): "))
Tau_XY = float(input("Enter The Normal Stress(TauXY in kN/m^2): "))

x = MohrsCircle(Sigma_X, Sigma_Y, Tau_XY)
y = MohrAnalytic(Sigma_X, Sigma_Y, Tau_XY)
x.plot()
print()

radius = round(x.radius(),3)
center = round(x.center(),3)
center = str(center)
print()
print("------------ Mohr's Circle Values---------------------------------")
print()
print("Mohr's Circle Radius = ", radius)
print("Mohr's Circle Centre = (" + center + "," + "0)")
print("------------------------------------------------------------------")
print()

print("------------ Result Obtained From Mohr's Circle-------------------")
print()
max1 = round(x.MaxPrincipalStress(),3)
min1 = round(x.MinPrincipalStress(),3)
max_tau = round(x.MaxShearStress(),3)
print("Maximum Principal Stress = "+str(max1)+" kN/m^2")
print("Minimum Principal Stress = "+str(min1)+" kN/m^2")
print("Maximum Shear Stress = "+str(max_tau)+" kN/m^2")
print("----------------------------------------------------------------------")
print()

print("------------ Result Obtained From Analytical Method-------------------")
print()
max1 = round(y.MaximumPrincipalStress(),3)
min1 = round(y.MinimumPrincipalStress(),3)
max_tau = round(y.MaximumShearStress(),3)
angle_of_priciple_stress = round(y.Principal_Plane_Theta(),3)
angle_of_shear_stress = round(y.Shear_Stress_Plane_Theta(),3)
print("Maximum Principal Stress = "+str(max1)+" kN/m^2")
print("Minimum Principal Stress = "+str(min1)+" kN/m^2")
print("Maximum Shear Stress = "+str(max_tau)+" kN/m^2")
print("Principal Plane 1 Direction = "+str(angle_of_priciple_stress)+" degree")
print("Principal Plane 2 Direction = "+str(90.0+angle_of_priciple_stress)+" degree")
print("Maximum Shear Stress = "+ str(angle_of_shear_stress) + " degree")
xc = abs(angle_of_priciple_stress - angle_of_shear_stress)
print("----------------------------------------------------------------------")
print("Diffrence btween ShearStress Plane And PrincipalStress Plane = " + str(xc) + " degree")

print()
print("\t\t Hope You Get The Desired Result")
print("\t\t\t Thank You")