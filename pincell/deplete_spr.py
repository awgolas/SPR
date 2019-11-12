import openmc
import openmc.deplete

geometry = openmc.Geometry().from_xml()
materials = openmc.Materials().from_xml()
settings = openmc.Settings().from_xml()

# lower_left = (-65,-65,-95)
# upper_right = (65,65,75)

# clad = materials[0]
# fuel = materials[1]
# hp_vap = materials[2]
# hp_liq = materials[3]

#vol = openmc.VolumeCalculation([fuel, clad, hp_vap, hp_liq], 100000, lower_left, upper_right).from_hdf5('volume_1.h5')

#geometry.add_volume_information(vol)
#fuel.add_volume_information(vol)
#clad.add_volume_information(vol)
#hp_vap.add_volume_information(vol)
#hp_liq.add_volume_information(vol)


power = 5440
#results = openmc.deplete.ResultsList.from_hdf5('depletion_results.h5')
operator = openmc.deplete.Operator(geometry, settings, "/home/ubuntu/xs_data/chain_endfb71.xml")

time_steps = [1971000]*100
integrator = openmc.deplete.CELIIntegrator(operator, time_steps, power)
integrator.integrate()
