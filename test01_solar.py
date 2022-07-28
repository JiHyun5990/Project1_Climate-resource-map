from netCDF4 import Dataset
import matplotlib.pyplot as plt

ncfile = Dataset('KMAPP_solar_FWS_09H_mean.nc')
print(ncfile)

'''
<class 'netCDF4._netCDF4.Dataset'>
root group (NETCDF4 data model, file format HDF5):
    dimensions(sizes): X(6900), Y(6750)
    variables(dimensions): float64 X(X), float64 Y(Y), float32 SWDN_flat_with_shading(Y, X)
    groups: 
'''

solar = ncfile.variables['SWDN_flat_with_shading']

plt.imshow(solar)
plt.gca().invert_yaxis()
plt.title('solar_09H')

plt.savefig('solar_09H.png')
plt.show()