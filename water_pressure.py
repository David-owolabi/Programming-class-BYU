def water_column_height(tower_height, tank_height):
    """
    Calculate the height of the water column in a water tower.
    h = t + 3w/4
    Where:
    h is height of the water column
    t is the height of the tower (tower_height)
    w is the height of the walls of the tank that is on top of the tower (tank_height)

    """
    water_height = tower_height + 3 * tank_height / 4
    return water_height

def pressure_gain_from_water_height(height):
    """
    Calculate the pressure gain from a given height of water column.
    P = ρgh/1000
    Where:
    P is the pressure in kilopascals
    ρ is the density of water 998.2 (kilogram / meter3)
    g is the acceleration from Earths gravity 9.80665 (meter / second2)
    h is the height of the water column inmeters (height)
    """
    pressure_gain = 998.2*9.80665*height/1000
    return pressure_gain

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculate the pressure loss from a pipe using the Darcy-Weisbach equation.
    Where:
    P is the lost pressure in kilopascals
    f is the pipe’s friction factor (friction_factor)
    L is the length of the pipe in meters (pipe_length)
    ρ is the density of water 998.2 (kilogram / meter3)
    v is the velocity of the water flowing through the pipe in meters / second (fluid_velocity)
    d is the diameter of the pipe in meters (pipe_diameter)
    """
    pressure_loss = -friction_factor * pipe_length * 998.2 * fluid_velocity**2 / 2000* pipe_diameter
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculate the pressure loss from pipe fittings.
    P = 
    −0.04*ρ v**2*2000* n/2000
    Where:
    P is the lost pressure in kilopascals
    ρ is the density of water (998.2 kilogram / meter3)
    v is the velocity of the water flowing through the pipe in meters / second (fluid_velocity)
    n is the quantity of fittings (quantity_fittings)
    """
    pressure_loss = -0.04 * 998.2 * fluid_velocity**2 * quantity_fittings / 2000
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculate the Reynolds number for water flowing through a pipe.
    R = ρdv/μ
    Where:
    Re is the Reynolds number
    ρ is the density of water (998.2 kilogram / meter3)
    d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter. (hydraulic_diameter)
    v is the velocity of the water flowing through the pipe in meters / second (fluid_velocity)
    μ is the dynamic viscosity of water  (0.0010016 Pascal seconds)
    """
    reynolds_num = 998.2 * hydraulic_diameter * fluid_velocity / 0.0010016
    return reynolds_num

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculate the pressure loss from a sudden pipe reduction.
    k=(0.1+50/R)*((D/d)**4 -1)
    P = -k*ρ v**2/2000
    Where:
    k is a constant computed by the first formula and used in the second formula
    R is the Reynolds number that corresponds to the pipe with the larger diameter (reynolds_number)
    D is the diameter of the larger pipe in meters (larger_diameter)
    d is the diameter of the smaller pipe in meters (smaller_diameter)
    P is the lost pressure kilopascals
    ρ is the density of water (998.2 kilogram / meter3)
    v is the velocity of the water flowing through the larger diameter pipe in meters / second (fluid_velocity)
    """
    k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    pressure_loss = -k * 998.2 * fluid_velocity**2 / 2000
    return pressure_loss
    

  
    