# Duct Performance Analysis using Python

## Introduction

Ducts are essential components in HVAC systems, serving as conduits for delivering and removing air to ensure acceptable indoor air quality and thermal comfort. In this analysis, air is considered the fluid flowing through the ducts. Although air is compressible, it is treated as incompressible for engineering calculations, simplifying the analysis without significant errors.

## Problem Statement

The objective is to analyze duct system design using a Python program. This program calculates the total flow rate and pressure drop based on input parameters. Additionally, it performs curve fitting to determine the mathematical relationship between pressure and flow rate, allowing predictions for any flow rate value.

## Duct Design

### Design and Dimensions

The duct design is created using SolidWorks, inspired by a research paper ([source](http://www.casde.iitb.ac.in/store/training/2003/kailash-wt-perf-analysis.pdf)). The specific dimensions used in the analysis are:

- **Curved Radius at Inlet**: 0.125m
- **Length at Inlet**: 1m
- **Breadth at Inlet**: 1m
- **Length at Outlet**: 1.6m
- **Breadth at Outlet**: 2.4m
- **Obstruction Dimension**: 0.5m x 0.01m

## Losses in Duct

### Minor Losses

1. **Inlet Loss**: Calculated using equivalent diameter and a given \( r/D \) profile:
   - Equivalent Diameter = \( \frac{2 \times \text{length} \times \text{breadth}}{(\text{length} + \text{breadth})} \)
   - Loss coefficients (\( K_1 \)) for different \( r/D \) values are provided:
     - \( r/D = 0.03, K_1 = 0.3 \)
     - \( r/D = 0.05, K_1 = 0.2 \)
     - \( r/D = 0.10, K_1 = 0.06 \)
     - \( r/D = 0.15, K_1 = 0.06 \)

2. **Obstruction Loss**: Based on the vena-contracta effect, calculated as:
   - \( K_2 = \left( \frac{a_1}{(a_1 - a) \times 0.9} - 1 \right)^2 \)
   - Here, 0.9 is the assumed coefficient of contraction.

3. **Outlet Loss**: Derived from velocity changes using the continuity equation:
   - \( V_2 = \left( \frac{A_1}{A_2} \right) V_1 = 0.2604 V_1 \)
   - Pressure loss at outlet: \( \Delta P_{\text{outlet}} = \frac{1}{2} K_3 \rho V_2^2 \)
   - Resultant \( K_3 = 0.0678 \)

4. **Duct Diffuser Loss**: Calculated using:
   - Equivalent Diameter (\( D_e \)) and specific loss coefficient (\( K_4 = 1 - C_p \))

### Major Losses

- **Duct Friction Loss**: Calculated using the Colebrook equation, solved via Newton-Raphson method:
  - Friction factor (\( f \)) calculation:
    - \( f = -2 \left( \log_{10} \left( \frac{\epsilon/D}{3.7} + \frac{2.51}{Re \sqrt{f}} \right) \right)^{-2} \)
  - Pressure drop due to friction (\( \Delta P_{\text{friction}} \)) using Darcy-Weisbach equation:
    - \( \Delta P = f \left( \frac{L}{D} \right) \frac{\rho V^2}{2} \)

## Curve Fitting

Curve fitting is performed to establish a relationship between pressure and flow rate. The obtained graph indicates a cubic relationship, and the function defined follows a cubic equation. The optimal parameters (Popt) and their covariance (Pcov) are determined using Python's curve fitting functions. The goodness of fit is evaluated using metrics such as:

- **SSE**: Sum of Squares Due to Error
- **R-Square**: Coefficient of determination
- **Adjusted R-Square**: Adjusted coefficient of determination
- **RMSE**: Root Mean Square Error

A good fit is indicated by an R-Square value greater than 0.7.

## Results

The obtained graph and mathematical function can be used to select the optimal flow rate for a given pressure and to determine the power required for a fan/blower using the equation:

\[ P_{\text{req}} = p \times Q \]

This analysis is applicable to all ventilation systems, providing a practical tool for optimizing duct performance.

## References

1. [Wikipedia: Duct (flow)](https://en.wikipedia.org/wiki/Duct_(flow)#Air_terminals)
2. [Wikipedia: Duct (industrial exhaust)](https://en.wikipedia.org/wiki/Duct_(industrial_exhaust))
3. [Research Paper](http://www.casde.iitb.ac.in/store/training/2003/kailash-wt-perf-analysis.pdf)
4. [IIT Hyderabad Class Notes](http://www.iith.ac.in/~ksahu/class13_FM.pdf)

